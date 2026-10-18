#!/usr/bin/env python3
"""
Converts the GitLab wiki repository of FSang18's Heroes Addon into a
MkDocs (Material) project that can be hosted on GitHub Pages.

Usage:  python3 tools/convert.py <path-to-gitlab-wiki-clone> <output-project-dir>

It is safe to run again whenever you want to re-import from GitLab.
"""
import os, re, sys, shutil, urllib.parse, collections
import yaml

SRC = os.path.abspath(sys.argv[1])
OUT = os.path.abspath(sys.argv[2])
DOCS = os.path.join(OUT, "docs")

WIKI_URL = re.compile(r"https?://gitlab\.com/FSang18/fsang18s-heroes-addon/-/wikis/", re.I)

# --------------------------------------------------------------------------
# 1. Collect pages
# --------------------------------------------------------------------------
pages = {}          # original key ("home/Items/Compound-V") -> info dict
for root, dirs, files in os.walk(SRC):
    dirs[:] = [d for d in dirs if d not in (".git", "uploads", ".gitlab")]
    for f in files:
        if not f.endswith(".md"):
            continue
        full = os.path.join(root, f)
        key = os.path.relpath(full, SRC)[:-3].replace(os.sep, "/")
        pages[key] = {"src": full}

def slug(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"['’(),]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "page"

def humanize(name):
    return name.replace("-", " ").replace("_", " ").strip()

# Which page keys also have a folder of children?  (Items.md + Items/)
all_keys = set(pages)
def has_children(key):
    p = key + "/"
    return any(k.startswith(p) for k in all_keys)

def new_rel(key):
    """Original wiki key -> path inside docs/ (with .md)."""
    if key == "home":
        return "index.md"
    parts = key.split("/")
    if parts[0] == "home":
        parts = parts[1:]
    parts = [slug(p) for p in parts]
    if has_children(key):
        return "/".join(parts) + "/index.md"
    return "/".join(parts) + ".md"

public = {k: v for k, v in pages.items() if k == "home" or k.startswith("home/")}
templates = {k: v for k, v in pages.items() if k.startswith("templates/")}

# collision check
seen = {}
for k in public:
    n = new_rel(k)
    if n in seen:
        print("COLLISION:", k, seen[n], n)
    seen[n] = k
for k, v in public.items():
    v["new"] = new_rel(k)

# --------------------------------------------------------------------------
# 2. Read titles / front matter
# --------------------------------------------------------------------------
FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)

def read(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    return t.replace("\r\n", "\n").replace("\r", "\n")

for k, v in public.items():
    t = read(v["src"])
    title = None
    m = FM.match(t)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
            title = meta.get("title")
        except Exception:
            mm = re.search(r"^title:\s*(.+)$", m.group(1), re.M)
            title = mm.group(1).strip() if mm else None
        t = t[m.end():]
    if not title:
        title = "Heroes Addon Wiki" if k == "home" else humanize(k.split("/")[-1])
    v["title"] = str(title).strip().strip('"')
    v["body"] = t

# --------------------------------------------------------------------------
# 3. Link resolution
# --------------------------------------------------------------------------
redirects = {}
rp = os.path.join(SRC, ".gitlab", "redirects.yml")
if os.path.exists(rp):
    try:
        redirects = yaml.safe_load(read(rp)) or {}
    except Exception:
        redirects = {}

lower_index = collections.defaultdict(list)
for k in public:
    lower_index[k.lower()].append(k)
base_index = collections.defaultdict(list)
for k in public:
    base_index[k.split("/")[-1].lower()].append(k)

unresolved = collections.Counter()

def resolve(path):
    """gitlab wiki path (no domain) -> original key or None"""
    p = urllib.parse.unquote(path)
    p = p.split("?")[0].strip("/")
    p = p.replace("\\(", "(").replace("\\)", ")")
    p = "/".join(seg.lstrip("_") for seg in p.split("/"))
    for _ in range(5):
        if p in public:
            return p
        if p.lower() in lower_index:
            return lower_index[p.lower()][0]
        if p in redirects:
            p = str(redirects[p])
            continue
        break
    if p.lower() in lower_index:
        return lower_index[p.lower()][0]
    if p == "home":
        return "home"
    # singular/plural + basename fallbacks
    for cand in (p + "s", p.rstrip("s")):
        if cand.lower() in lower_index:
            return lower_index[cand.lower()][0]
    b = p.split("/")[-1].lower()
    for cand in (b, b + "s", b.rstrip("s")):
        if len(base_index.get(cand, [])) == 1:
            return base_index[cand][0]
    return None

def rel_link(from_key, to_key, frag=""):
    a = os.path.dirname(public[from_key]["new"])
    b = public[to_key]["new"]
    r = os.path.relpath(b, a or ".").replace(os.sep, "/")
    return r + frag

# ---- scan for a markdown link target that may contain balanced / escaped ()
def find_links(text):
    """yield (start, end, label, url) for every [label](url) (not images)."""
    out = []
    i = 0
    while True:
        j = text.find("](", i)
        if j < 0:
            break
        # find start of label
        k = text.rfind("[", 0, j)
        if k < 0 or "\n\n" in text[k:j]:
            i = j + 2
            continue
        # parse url with balanced parens
        depth, p = 1, j + 2
        while p < len(text) and depth:
            c = text[p]
            if c == "\\":
                p += 2
                continue
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            elif c == "\n":
                break
            p += 1
        if depth:
            i = j + 2
            continue
        url = text[j + 2:p - 1]
        is_img = k > 0 and text[k - 1] == "!"
        out.append((k - (1 if is_img else 0), p, text[k + 1:j], url, is_img))
        i = p
    return out

def fix_body(key, v):
    text = v["body"]
    depth_prefix = os.path.dirname(v["new"])

    # ----- links & images (processed right to left so offsets stay valid)
    for start, end, label, url, is_img in reversed(find_links(text)):
        repl = None
        raw = url.strip()
        m_attr = None
        if is_img:
            # url may be "path" or 'path "title"'
            u = raw.split(' "')[0]
            um = re.match(r"(?:https?://gitlab\.com)?(?:/FSang18/fsang18s-heroes-addon/-/wikis/)?(uploads/[^\s]+)$", u)
            if um:
                target = os.path.join(DOCS, um.group(1))
                rel = os.path.relpath(target, os.path.join(DOCS, depth_prefix) if depth_prefix else DOCS)
                rel = urllib.parse.quote(rel.replace(os.sep, "/"))
                # pick up trailing {attr list}
                tail = text[end:]
                am = re.match(r"\{([^}\n]*)\}", tail)
                attrs = ""
                if am:
                    attrs = am.group(1).strip()
                    end2 = end + am.end()
                else:
                    end2 = end
                alt = label if label and not re.match(r"^image\.png$", label) else v["title"]
                alt = alt.replace("[", "").replace("]", "")
                new = f"![{alt}]({rel}){{ {attrs} loading=lazy }}"
                text = text[:start] + new + text[end2:]
            continue
        wm = re.match(r"(?:https?://gitlab\.com)?(?:/FSang18/fsang18s-heroes-addon/-/wikis/)(.*)$", raw, re.I)
        if raw.lower().startswith("http") and not WIKI_URL.match(raw):
            continue
        if wm:
            path, frag = wm.group(1), ""
            if "#" in path:
                path, frag = path.split("#", 1)
                frag = "#" + frag
            if path.startswith("uploads/"):
                # link to an uploaded file (zip etc.)
                target = os.path.join(DOCS, path)
                rel = os.path.relpath(target, os.path.join(DOCS, depth_prefix) if depth_prefix else DOCS)
                repl = f"[{label}]({urllib.parse.quote(rel.replace(os.sep, '/'))})"
            else:
                tk = resolve(path)
                if tk:
                    repl = f"[{label}]({rel_link(key, tk, frag)})"
                else:
                    unresolved[(key, urllib.parse.unquote(path))] += 1
                    repl = f"{label}"          # keep the text, drop the dead link
            text = text[:start] + repl + text[end:]

    # ----- bare gitlab URLs on their own (autolinks)
    def bare(m):
        path = m.group(1)
        trail = ""
        while path and path[-1] in ".,;:!?\\":
            trail = path[-1] + trail
            path = path[:-1]
        tk = resolve(path)
        if not tk:
            unresolved[(key, urllib.parse.unquote(path))] += 1
            return urllib.parse.unquote(path.split("/")[-1]).replace("-", " ") + trail
        return f"[{public[tk]['title']}]({rel_link(key, tk)})" + trail
    text = re.sub(r"(?<![(\[<\"'])https?://gitlab\.com/FSang18/fsang18s-heroes-addon/-/wikis/([^\s)<>]+)", bare, text)

    # relative upload images that were not caught (no alt etc.) - safety net
    # raw HTML <img src="uploads/..."> if any
    text = re.sub(r'(<img[^>]+src=")(uploads/[^"]+)(")',
                  lambda m: m.group(1) + os.path.relpath(os.path.join(DOCS, m.group(2)),
                            os.path.join(DOCS, depth_prefix) if depth_prefix else DOCS).replace(os.sep, "/") + m.group(3), text)

    # GitLab turns \\< and \\> into literal < >; Python-Markdown does not
    text = text.replace("\\<", "&lt;").replace("\\>", "&gt;")

    # raw HTML tables: GitLab renders **bold** inside cells, MkDocs does not
    def fix_table(m):
        blk = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", m.group(0))
        blk = re.sub(r"(<t[hd][^>]*>)\s+", r"\1", blk)
        blk = re.sub(r"\s+(</t[hd]>)", r"\1", blk)
        return blk
    text = re.sub(r"<table.*?</table>", fix_table, text, flags=re.S)

    # GitLab TOC marker -> nothing (Material has its own table of contents)
    text = text.replace("[[_TOC_]]", "")

    # first line image "{width=..}" with spaces: normalise "){width" -> ")" handled above
    text = text.strip("\n") + "\n"
    # add H1 if page has none at the top
    first = next((l for l in text.split("\n") if l.strip()), "")
    if not first.startswith("# "):
        text = f"# {v['title']}\n\n" + text
    v["out"] = text

# --------------------------------------------------------------------------
# 4. Write docs
# --------------------------------------------------------------------------
if os.path.exists(DOCS):
    shutil.rmtree(DOCS)
os.makedirs(DOCS)

for k, v in public.items():
    fix_body(k, v)

for k, v in public.items():
    dest = os.path.join(DOCS, v["new"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    safe_title = v["title"].replace('"', '\\"')
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f'---\ntitle: "{safe_title}"\n---\n\n{v["out"]}')

# hand-made landing page + theme files (CSS) live outside docs/ so they survive re-imports
hp = os.path.join(OUT, "home-page.md")
if os.path.exists(hp):
    shutil.copy(hp, os.path.join(DOCS, "index.md"))
tf = os.path.join(OUT, "theme-files")
if os.path.isdir(tf):
    shutil.copytree(tf, DOCS, dirs_exist_ok=True)

# images
shutil.copytree(os.path.join(SRC, "uploads"), os.path.join(DOCS, "uploads"))

# templates stay out of the public site -> keep them for the editors
tdir = os.path.join(OUT, "templates")
if os.path.exists(tdir):
    shutil.rmtree(tdir)
os.makedirs(tdir)
for k, v in templates.items():
    name = os.path.basename(k) + ".md"
    name = name.replace("&", "and")
    shutil.copy(v["src"], os.path.join(tdir, name))

# --------------------------------------------------------------------------
# 5. Navigation (built from the files, see make_nav.py)
# --------------------------------------------------------------------------
import subprocess
subprocess.run([sys.executable, os.path.join(OUT, "tools", "make_nav.py")], check=True)

# --------------------------------------------------------------------------
# 6. Report
# --------------------------------------------------------------------------
with open(os.path.join(OUT, "conversion-report.txt"), "w", encoding="utf-8") as fh:
    fh.write(f"Pages converted: {len(public)}\n")
    fh.write(f"Template pages moved to /templates: {len(templates)}\n")
    fh.write(f"Links that pointed at pages that do not exist (text kept, link removed): {sum(unresolved.values())}\n\n")
    for (k, p), n in sorted(unresolved.items()):
        fh.write(f"  in {k}  ->  {p}\n")
print("pages", len(public), "unresolved links", sum(unresolved.values()))

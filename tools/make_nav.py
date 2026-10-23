#!/usr/bin/env python3
"""
Builds the sidebar menu automatically from the files in docs/ and writes mkdocs.yml.

 - A page's menu title = "title:" at the top of the file, else its first "# Heading", else its file name.
 - A folder that contains an index.md becomes a clickable section (title taken from that index.md).
 - Add  unlisted: true  to a page's front matter to keep it out of the menu (it still opens by its link).
 - Add  nav_first: true  to a page's front matter (or a section's index.md) to list it first in its folder.
 - Menu order = alphabetical (numbers sorted naturally), except the top level, which follows TOP_ORDER below.

So to add a page you only add a .md file. You never edit the menu by hand.
Runs automatically on every deploy; you can also run it locally:  python3 tools/make_nav.py
"""
import os, re, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

# order of the top-level menu entries (anything not listed goes after these, alphabetically)
TOP_ORDER = ["Installation", "FAQs", "Commands", "Powers", "Karma", "Skill Point System",
             "Accessory Support", "Blocks", "Items", "Suitsets", "Structures", "Villagers"]

FM = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)

def natkey(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]

def humanize(name):
    return re.sub(r"[-_]+", " ", name).strip().title()

def page_title(path, fallback):
    try:
        t = open(path, encoding="utf-8").read()
    except Exception:
        return fallback
    m = FM.match(t)
    if m:
        try:
            title = (yaml.safe_load(m.group(1)) or {}).get("title")
            if title:
                return str(title)
        except Exception:
            pass
        t = t[m.end():]
    h = re.search(r"^#\s+(.+)$", t, re.M)
    return h.group(1).strip() if h else fallback

def is_unlisted(path):
    """A page with  unlisted: true  in its front matter is left out of the menu (it still opens by link)."""
    try:
        t = open(path, encoding="utf-8").read()
    except Exception:
        return False
    m = FM.match(t)
    if not m:
        return False
    try:
        return bool((yaml.safe_load(m.group(1)) or {}).get("unlisted"))
    except Exception:
        return False

def has_flag(path, key):
    """True if the file's front matter contains  key: true  (used for nav_first)."""
    try:
        t = open(path, encoding="utf-8").read()
    except Exception:
        return False
    m = FM.match(t)
    if not m:
        return False
    try:
        return bool((yaml.safe_load(m.group(1)) or {}).get(key))
    except Exception:
        return False

def build(folder, prefix=""):
    entries = []
    index = None
    for name in os.listdir(folder):
        full = os.path.join(folder, name)
        if name in ("uploads", "stylesheets", "assets", "javascripts", "overrides") and prefix == "":
            continue
        if os.path.isdir(full):
            sub = build(full, prefix + name + "/")
            if sub:
                idx = os.path.join(full, "index.md")
                title = page_title(idx, humanize(name)) if os.path.exists(idx) else humanize(name)
                first = os.path.exists(idx) and has_flag(idx, "nav_first")
                entries.append((title, {title: sub}, first))
        elif name.endswith(".md"):
            if name == "index.md":
                index = prefix + name
                continue
            if is_unlisted(full):
                continue
            title = page_title(full, humanize(name[:-3]))
            entries.append((title, {title: prefix + name}, has_flag(full, "nav_first")))
    entries.sort(key=lambda e: (not e[2], natkey(e[0])))
    items = [e[1] for e in entries]
    if index:
        items.insert(0, index)
    return items

nav = build(DOCS)
home = nav.pop(0) if nav and nav[0] == "index.md" else None

def top_key(item):
    t = next(iter(item))
    return (TOP_ORDER.index(t) if t in TOP_ORDER else 99, natkey(t))
nav.sort(key=top_key)
nav = [{"Home": "index.md"}] + nav

base = open(os.path.join(ROOT, "mkdocs.base.yml"), encoding="utf-8").read().rstrip("\n")
out = base + "\n\n" + yaml.safe_dump({"nav": nav}, allow_unicode=True, sort_keys=False, width=1000)
open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8").write(out)
print("mkdocs.yml written")

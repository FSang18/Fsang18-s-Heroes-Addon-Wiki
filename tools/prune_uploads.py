"""Remove picture files in docs/uploads that no page, stylesheet or config uses.

Usage:  python tools/prune_uploads.py          (dry run: only lists what it would delete)
        python tools/prune_uploads.py --apply  (really deletes)

Rules:
- Only pictures inside the random-named subfolders are ever deleted.
- Loose files directly in docs/uploads (the power icons) are never deleted.
- Non-picture files (.zip, .gpl ...) are listed but never deleted.
- A file counts as used if its "folder/name.png" path appears in any page,
  stylesheet, template or config file.
"""
import os, sys, urllib.parse

UPLOADS = "docs/uploads"
PICTURES = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")
TEXT = (".md", ".css", ".html", ".js", ".yml", ".yaml")
SCAN_DIRS = ["docs", "templates", "theme-files"]
SCAN_FILES = ["mkdocs.base.yml", "mkdocs.yml", "home-page.md"]

def text_files():
    for d in SCAN_DIRS:
        for root, _, names in os.walk(d):
            if root.replace("\\", "/").startswith(UPLOADS):
                continue
            for n in names:
                if n.endswith(TEXT):
                    yield os.path.join(root, n)
    for f in SCAN_FILES:
        if os.path.exists(f):
            yield f

def main():
    apply = "--apply" in sys.argv
    corpus = []
    scanned = 0
    for p in text_files():
        with open(p, encoding="utf-8", errors="ignore") as fh:
            corpus.append(fh.read())
        scanned += 1
    text = urllib.parse.unquote("\n".join(corpus)).lower()

    files = []
    for root, _, names in os.walk(UPLOADS):
        for n in names:
            files.append(os.path.relpath(os.path.join(root, n), UPLOADS).replace("\\", "/"))

    used = [f for f in files if f.lower() in text]
    unused = [f for f in files if f.lower() not in text]
    loose = [f for f in unused if "/" not in f]
    other = [f for f in unused if "/" in f and not f.lower().endswith(PICTURES)]
    doomed = [f for f in unused if "/" in f and f.lower().endswith(PICTURES)]

    size = lambda L: sum(os.path.getsize(os.path.join(UPLOADS, f)) for f in L) / 1e6
    print(f"Text files scanned: {scanned}")
    print(f"Files in uploads:   {len(files)}  ({size(files):.1f} MB)")
    print(f"Used by a page:     {len(used)}  ({size(used):.1f} MB)")
    print(f"Unused pictures:    {len(doomed)}  ({size(doomed):.1f} MB)  <- would be deleted")
    print(f"Kept (loose icons): {len(loose)}  {loose}")
    print(f"Kept (not pictures): {len(other)}")
    for f in other:
        print("   ", f)

    # Safety stop: if the scan found almost nothing in use, something is wrong.
    if scanned < 20 or len(used) < 50:
        print("STOP: the scan looks wrong (too few pages or used files). Nothing deleted.")
        sys.exit(1)

    if not apply:
        print("\nDRY RUN. Nothing was deleted. First 40 files that would go:")
        for f in sorted(doomed)[:40]:
            print("   ", f)
        return
    for f in doomed:
        os.remove(os.path.join(UPLOADS, f))
    for root, dirs, names in os.walk(UPLOADS, topdown=False):
        if root != UPLOADS and not os.listdir(root):
            os.rmdir(root)
    print(f"\nDeleted {len(doomed)} files.")

if __name__ == "__main__":
    main()

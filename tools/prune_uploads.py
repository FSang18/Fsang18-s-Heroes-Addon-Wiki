"""Remove pictures in docs/uploads that no page, stylesheet or setting uses.

Only the random-named folders (32 letters/numbers) are touched.
docs/uploads/power-images and everything else is never deleted.
Run without --apply to only list what would be deleted.
"""
import os, re, sys

APPLY = "--apply" in sys.argv
UP = "docs/uploads"
SKIP_DIRS = {".git", "site", "node_modules", UP}
TEXT = (".md", ".css", ".yml", ".yaml", ".html", ".js", ".py", ".json", ".txt")
PAT = re.compile(r"uploads/([0-9a-f]{32})/([^)\s\"'<>?#]+)")

used = set()
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if os.path.normpath(os.path.join(root, d)) not in SKIP_DIRS and d not in {".git", "site", "node_modules"}]
    for f in files:
        if f.endswith(TEXT):
            try:
                text = open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for h, name in PAT.findall(text):
                used.add((h, name))

keep, drop = [], []
for h in sorted(os.listdir(UP)):
    folder = os.path.join(UP, h)
    if not (re.fullmatch(r"[0-9a-f]{32}", h) and os.path.isdir(folder)):
        continue
    for f in sorted(os.listdir(folder)):
        (keep if (h, f) in used else drop).append(os.path.join(folder, f))

print(f"Keeping {len(keep)} file(s):")
for p in keep: print("  keep ", p)
print(f"\n{'Deleting' if APPLY else 'Would delete'} {len(drop)} file(s).")
if APPLY:
    for p in drop:
        os.remove(p)
        d = os.path.dirname(p)
        if not os.listdir(d): os.rmdir(d)
else:
    for p in drop[:15]: print("  drop ", p)
    if len(drop) > 15: print(f"  ... and {len(drop)-15} more")

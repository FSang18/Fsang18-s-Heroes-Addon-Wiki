"""
Clickable classification pills (runs after the site is built).

What it does
------------
Every power page has a row of classification pills:

    <b class="pc-types"><i class="c-fighter">Fighter</i> ... </b>

This hook wraps each pill in a link to its card on the Power Classifications
page, and stores that card's one-line definition on the link so the CSS can
show it as a tooltip on hover / keyboard focus.

Safety
------
* No .md file is touched. Only the built .html files in site_dir change.
* Definitions are read from the built Power Classifications page, so that
  page stays the single place where a definition is written.
* Running it twice changes nothing (already-linked rows are skipped).
* A pill with no matching card is left exactly as it was (a warning is logged).
* If anything goes wrong, it logs a warning and leaves the pages alone.
  It never fails the build.
"""
import html
import logging
import os
import re
from pathlib import Path

log = logging.getLogger("mkdocs.hooks.pill_links")

# where the classifications page lives inside the built site
CLASS_PAGE = "systems/power-classifications/index.html"

# <h4 id="fighter">Fighter</h4> <p>definition</p>
_CARD = re.compile(r'<h4\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h4>\s*<p>(.*?)</p>', re.S)
_TAG = re.compile(r"<[^>]+>")
# the pills row, and one pill inside it
_ROW = re.compile(r'(<b\b[^>]*\bclass="[^"]*\bpc-types\b[^"]*"[^>]*>)(.*?)(</b>)', re.S)
_PILL = re.compile(r'<i\b[^>]*\bclass="c-([a-z0-9-]+)"[^>]*>(.*?)</i>', re.S)


def _text(fragment):
    """Plain text of an HTML fragment (tags, permalink marks and extra spaces removed)."""
    return " ".join(html.unescape(_TAG.sub("", fragment)).replace("\u00b6", "").split())


def _definitions(page_html):
    """{card id: (name, definition)} read from the classifications page."""
    defs = {}
    for ident, name, body in _CARD.findall(page_html):
        text = _text(body)
        if text:
            defs[ident] = (_text(name), text)
    return defs


def _rewrite(page_html, defs, rel):
    """Return (new html, set of pill classes that had no card)."""
    missing = set()

    def row(m):
        if "pc-link" in m.group(2):  # already done on an earlier build
            return m.group(0)

        def pill(p):
            slug = p.group(1)
            if slug not in defs:
                missing.add(slug)
                return p.group(0)
            name, text = defs[slug]
            tip = html.escape(text, quote=True)
            label = html.escape(name + ": " + text, quote=True)
            return (
                '<a class="pc-link c-%s" href="%s#%s" data-tip="%s" aria-label="%s">%s</a>'
                % (slug, rel, slug, tip, label, p.group(0))
            )

        return m.group(1) + _PILL.sub(pill, m.group(2)) + m.group(3)

    return _ROW.sub(row, page_html), missing


def _run(site):
    class_pages = sorted(site.rglob(CLASS_PAGE))
    if not class_pages:
        log.warning("pill_links: %s not found in %s; pills left as they are", CLASS_PAGE, site)
        return

    done = set()
    for class_page in class_pages:
        class_dir = class_page.parent
        root = class_dir.parent.parent  # the site (or the version folder) this page belongs to
        defs = _definitions(class_page.read_text(encoding="utf-8"))
        if not defs:
            log.warning("pill_links: no definitions found on %s; pills left as they are", class_page)
            continue

        changed, missing = 0, set()
        for page in sorted(root.rglob("index.html")):
            if page in done:
                continue
            done.add(page)
            src = page.read_text(encoding="utf-8")
            if "pc-types" not in src:
                continue
            rel = os.path.relpath(str(class_dir), str(page.parent)).replace(os.sep, "/") + "/"
            out, miss = _rewrite(src, defs, rel)
            missing |= miss
            if out != src:
                page.write_text(out, encoding="utf-8")
                changed += 1

        log.info("pill_links: linked pills on %d page(s) under %s", changed, root)
        if missing:
            log.warning(
                "pill_links: no card on the classifications page for: %s", ", ".join(sorted(missing))
            )


def on_post_build(config, **kwargs):
    try:
        _run(Path(config["site_dir"]))
    except Exception as exc:  # never break the build over a tooltip
        log.warning("pill_links: skipped (%s)", exc)

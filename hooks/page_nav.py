"""
Previous / Next buttons at the end of every page (runs while the site is built).

What it does
------------
Adds two buttons to the end of each page's content, right under the last
section (for example under "Relevant Information"):

    <- Previous page title                       Next page title ->

The order is the menu order, so it always matches the sidebar.

Safety
------
* No .md file is touched; the buttons are added to the built HTML only.
* A page with `no_page_nav: true` in its front matter gets no buttons.
* Pages with no previous and no next page get nothing.
* If anything goes wrong, it logs a warning and leaves that page alone.
  It never fails the build.
"""
import html
import logging

from mkdocs.utils import get_relative_url

log = logging.getLogger("mkdocs.hooks.page_nav")


def _button(kind, target, page):
    href = html.escape(get_relative_url(target.url, page.url), quote=True)
    full = (target.meta or {}).get("title") or target.title
    title = html.escape(str(full or "").strip() or "Untitled", quote=True)
    if kind == "prev":
        label, arrow, rel = "Previous", "\u2190", "prev"
        inner = '<span class="pn-arrow">%s</span><span class="pn-text"><small>%s</small><b>%s</b></span>'
    else:
        label, arrow, rel = "Next", "\u2192", "next"
        inner = '<span class="pn-text"><small>%s</small><b>%s</b></span><span class="pn-arrow">%s</span>'
    if kind == "prev":
        body = inner % (arrow, label, title)
    else:
        body = inner % (label, title, arrow)
    return '<a class="pn pn-%s" href="%s" rel="%s">%s</a>' % (kind, href, rel, body)


def on_post_page(output, page, config, **kwargs):
    try:
        if (page.meta or {}).get("no_page_nav"):
            return output
        prev_page, next_page = page.previous_page, page.next_page
        if not prev_page and not next_page:
            return output
        end = output.rfind("</article>")
        if end == -1:
            return output
        buttons = ""
        if prev_page:
            buttons += _button("prev", prev_page, page)
        if next_page:
            buttons += _button("next", next_page, page)
        nav = '<nav class="page-nav" aria-label="Previous and next page">%s</nav>' % buttons
        return output[:end] + nav + output[end:]
    except Exception as exc:  # never break the build over a button
        log.warning("page_nav: skipped %s (%s)", getattr(page, "file", page), exc)
        return output

"""On power pages, the right-hand contents list shows only the ability categories
(the ### headings), not every single ability (the #### headings)."""


def _prune(items):
    for item in items:
        item.children = [c for c in item.children if getattr(c, "level", 0) < 4]
        _prune(item.children)


def on_page_content(html, page, config, files):
    if 'class="power-card"' in html:
        _prune(page.toc.items)
    return html

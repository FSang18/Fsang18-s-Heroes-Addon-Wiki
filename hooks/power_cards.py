"""
Power cards on hub pages (runs while the site is built).

What it does
------------
Put this one line on a hub page (for example Arachnids), where the bullet list was:

    <!-- power-cards -->

and the page shows one card for every power page in the same folder:
round icon, name, tier badge and classification pills, in that power's colour.
Everything is read from the power's own page, so editing a power page updates its
card by itself. A page that is not a finished power card yet (just a placeholder)
still gets a plain card with its name, so nothing disappears from the hub.

Safety
------
* No page is rewritten on disk; the cards exist only in the built site.
* If anything goes wrong on a hub page, it logs a warning and leaves the marker out.
  It never fails the build.
"""
import html
import logging
import os
import posixpath
import re

import yaml

log = logging.getLogger("mkdocs.hooks.power_cards")

MARKER = "<!-- power-cards -->"
FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
PILL = re.compile(r'<i\b[^>]*\bclass="c-([a-z0-9-]+)"[^>]*>(.*?)</i>', re.S)
BOX = re.compile(r'<b\b[^>]*\bclass="[^"]*\bpc-types\b[^"]*"[^>]*>(.*?)</b>', re.S)


def _read(path):
    text = open(path, encoding="utf-8").read()
    meta = {}
    m = FRONT.match(text)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except Exception:
            meta = {}
        text = text[m.end():]
    return meta, text


def _info(path):
    meta, text = _read(path)
    title = str(meta.get("menu_title") or meta.get("title") or os.path.basename(path)[:-3].replace("-", " ").title())
    card = re.search(r'<div class="power-card"([^>]*)>', text)
    if not card:
        return {"name": title, "power": False}
    style = re.search(r'style="([^"]*)"', card.group(1))
    name = re.search(r'<span class="pc-name">(.*?)</span>', text, re.S)
    tier = re.search(r'data-tier="([SABCDEF])"', text)
    icon = re.search(r'!\[[^\]]*\]\(([^)]+)\)\s*\{[^}]*\.pc-icon[^}]*\}', text)
    box = BOX.search(text)
    return {
        "power": True,
        "name": html.unescape(name.group(1).strip()) if name else title,
        "style": style.group(1) if style else "",
        "tier": tier.group(1) if tier else "",
        "icon": icon.group(1).strip() if icon else "",
        "pills": PILL.findall(box.group(1)) if box else [],
    }


def _cards(page, config):
    docs = config["docs_dir"]
    here = posixpath.dirname(page.file.src_path.replace("\\", "/"))
    base = os.path.join(docs, here)
    root = "../" * len([p for p in page.url.split("/") if p])
    items = []
    for name in sorted(os.listdir(base)):
        full = os.path.join(base, name)
        if not name.endswith(".md") or name == "index.md" or not os.path.isfile(full):
            continue
        meta, _ = _read(full)
        if meta.get("unlisted"):
            continue
        p = _info(full)
        href = name[:-3] + "/"
        rank = (0 if meta.get("nav_first") else 1 if p["power"] else 2)
        if not p["power"]:
            items.append((rank, name, f'<a class="pcard pcard-plain" href="{href}"><span class="pcard-body">'
                       f'<b class="pcard-name">{html.escape(p["name"])}</b>'
                       f'<span class="pcard-soon">Page coming soon</span></span></a>'))
            continue
        icon = ""
        if p["icon"]:
            target = posixpath.normpath(posixpath.join(here, p["icon"]))
            icon = f'<img class="pcard-icon" src="{root}{target}" alt="">'
        else:
            icon = '<span class="pcard-icon"></span>'
        pills = "".join(f'<i class="c-{s}">{l}</i>' for s, l in p["pills"])
        tier = (f'<span class="pcard-tier" data-tier="{p["tier"]}" title="Power ranking: {p["tier"]} Tier">'
                f'<b>{p["tier"]}</b></span>') if p["tier"] else ""
        items.append((rank, name, f'<a class="pcard" href="{href}" style="{html.escape(p["style"], quote=True)}">{icon}'
                   f'<span class="pcard-body"><b class="pcard-name">{html.escape(p["name"])}</b>'
                   f'<b class="pcard-types">{pills}</b></span>{tier}</a>'))
    out = [h for _, _, h in sorted(items)]
    return '<div class="pcards">' + "".join(out) + "</div>\n" if out else ""


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown
    try:
        return markdown.replace(MARKER, _cards(page, config))
    except Exception as exc:
        log.warning("power_cards: skipped %s (%s)", page.file.src_path, exc)
        return markdown.replace(MARKER, "")


# ---------------------------------------------------------------------------
# Page colour: a power page passes the colour of its power card to the whole page
# (headings, lines, stat numbers, the soft glow in the background).
# Pages without a power card keep the normal yellow.
# ---------------------------------------------------------------------------
_CARD_STYLE = re.compile(r'<div class="power-card" style="([^"]*)"')


def on_post_page(output, page, config):
    try:
        m = _CARD_STYLE.search(output)
        if not m:
            return output
        parts = [f"--{k}:{v}" for k, v in re.findall(r'--(hue|sat|lit)\s*:\s*([^;"]+)', m.group(1))]
        if not parts:
            return output
        style = ";".join(parts)
        return output.replace('<div class="md-content" data-md-component="content">',
                              f'<div class="md-content power-page" data-md-component="content" style="{style}">', 1)
    except Exception as exc:  # never fail the build over a colour
        log.warning("power_cards: page colour skipped for %s (%s)", page.file.src_path, exc)
        return output

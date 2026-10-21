---
title: "Power Colors"
unlisted: true
hide:
  - navigation
  - toc
search:
  exclude: true
robots: noindex
---

# Power Colors

Every power's overview card has its own theme color, set with three numbers: **hue** (0 to 360), **saturation** and **lightness**. This page lists the colors already taken so new powers can pick a clearly different one.

<style>
.pk { display: grid; gap: .6rem; max-width: 34rem; margin: 1rem 0 1.4rem; }
.pk label { display: grid; grid-template-columns: 6.5rem 1fr 3rem; align-items: center; gap: .8rem; font-size: .85rem; font-weight: 600; }
.pk output { font-family: var(--md-code-font-family); font-size: .8rem; text-align: right; }
.pk input[type=range] { width: 100%; accent-color: var(--md-accent-fg-color); }
.pk-msg { margin: .2rem 0 0; padding: .55rem .8rem; border-radius: .4rem; font-size: .85rem; border-left: 4px solid; }
.pk-msg.ok { border-color: #4ade80; background: rgba(74, 222, 128, .12); }
.pk-msg.warn { border-color: #fb923c; background: rgba(251, 146, 60, .14); }
.pk-row { display: flex; flex-wrap: wrap; gap: .6rem; align-items: center; }
.pk-row code { padding: .3rem .6rem; }
.pk-btn { cursor: pointer; padding: .3rem .8rem; border: 1px solid var(--md-default-fg-color--lighter); border-radius: .35rem; background: transparent; color: var(--md-default-fg-color); font-weight: 600; font-size: .8rem; }
.pk-btn:hover { border-color: var(--md-accent-fg-color); color: var(--md-accent-fg-color); }
.pcol-strip i { cursor: help; }
</style>

## Hue map

The dots show where each power sits on the color wheel. The dashed dot is the color you are trying below. Pick new hues from the empty stretches.

<div class="pcol-strip" id="pcol-strip"></div>

## Try a color

Move the sliders to preview a color. The page tells you if it is too close to one that is already taken.

<div class="pk">
<label>Hue <input type="range" id="pk-h" min="0" max="360" value="120"><output id="pk-ho"></output></label>
<label>Saturation <input type="range" id="pk-s" min="20" max="100" value="90"><output id="pk-so"></output></label>
<label>Lightness <input type="range" id="pk-l" min="40" max="75" value="62"><output id="pk-lo"></output></label>
<div class="pk-msg ok" id="pk-msg"></div>
<div class="pk-row"><code id="pk-code"></code><button class="pk-btn" id="pk-copy" type="button">Copy</button><button class="pk-btn" id="pk-free" type="button">Suggest a free hue</button></div>
</div>

<div class="pcol-grid"><div class="pcol" id="pk-card"><div class="pcol-swatch"><span>DARK</span><span>LIGHT</span></div><div class="pcol-info"><b>Your color</b><small id="pk-card-text"></small></div></div></div>

## Colors in use

<div class="pcol-grid" id="pcol-grid"></div>

## Adding a power

1. Pick a hue with the tool above. For a power in the same color family as another (two fire powers, say), change the saturation or lightness as well, not just the hue.
2. Put the numbers on the card: `<div class="power-card" style="--hue:12; --sat:95%; --lit:58%" markdown>`.
3. Add one line to the `POWERS` list at the bottom of this page's source file. The dot and the color card appear on their own.

<script>
(function () {
  /* ===== EDIT HERE: one line per power ===== */
  var POWERS = [
    { name: "Reality Warping", hue: 215, sat: 90, lit: 62 },
    { name: "Peter Parker",    hue: 355, sat: 90, lit: 62 },
    { name: "Miles Morales",   hue: 0,   sat: 100, lit: 46 }
  ];
  /* hues closer than this many degrees get a warning */
  var CLOSE = 25;
  var $ = function (id) { return document.getElementById(id); };
  var strip = $("pcol-strip"), grid = $("pcol-grid");
  var hsl = function (h, s, l) { return "hsl(" + h + " " + s + "% " + l + "%)"; };
  var dist = function (a, b) { var d = Math.abs(a - b) % 360; return d > 180 ? 360 - d : d; };
  var nums = function (h, s, l) { return "--hue:" + h + "; --sat:" + s + "%; --lit:" + l + "%"; };
  POWERS.forEach(function (p) {
    var dot = document.createElement("i");
    dot.title = p.name + " (hue " + p.hue + ")";
    dot.style.setProperty("--hue", p.hue);
    dot.style.setProperty("--pcd", hsl(p.hue, p.sat, p.lit));
    strip.appendChild(dot);
    var card = document.createElement("div");
    card.className = "pcol";
    card.style.cssText = nums(p.hue, p.sat, p.lit);
    card.innerHTML = '<div class="pcol-swatch"><span>DARK</span><span>LIGHT</span></div><div class="pcol-info"><b></b><small></small></div>';
    card.querySelector("b").textContent = p.name;
    card.querySelector("small").textContent = nums(p.hue, p.sat, p.lit);
    grid.appendChild(card);
  });
  var ghost = document.createElement("i");
  ghost.title = "Your color";
  ghost.style.border = "2px dashed #fff";
  strip.appendChild(ghost);
  var H = $("pk-h"), S = $("pk-s"), L = $("pk-l");
  function update() {
    var h = +H.value, s = +S.value, l = +L.value;
    $("pk-ho").textContent = h;
    $("pk-so").textContent = s + "%";
    $("pk-lo").textContent = l + "%";
    ghost.style.setProperty("--hue", h);
    ghost.style.setProperty("--pcd", hsl(h, s, l));
    var card = $("pk-card");
    card.style.cssText = nums(h, s, l);
    $("pk-card-text").textContent = nums(h, s, l);
    $("pk-code").textContent = 'style="' + nums(h, s, l) + '"';
    var near = null, nd = 999;
    POWERS.forEach(function (p) {
      var d = dist(h, p.hue);
      if (d < nd) { nd = d; near = p; }
    });
    var msg = $("pk-msg");
    if (!near) {
      msg.className = "pk-msg ok";
      msg.textContent = "No powers listed yet, so any color is free.";
    } else if (nd < CLOSE) {
      msg.className = "pk-msg warn";
      msg.textContent = "Too close to " + near.name + " (only " + nd + "\u00B0 apart). Pick another hue, or change saturation and lightness a lot if it is the same color family.";
    } else {
      msg.className = "pk-msg ok";
      msg.textContent = "Free. Nearest is " + near.name + ", " + nd + "\u00B0 away.";
    }
  }
  function freeHue() {
    var hs = POWERS.map(function (p) { return p.hue; }).sort(function (a, b) { return a - b; });
    if (!hs.length) return 0;
    var best = 0, mid = 0;
    for (var i = 0; i < hs.length; i++) {
      var a = hs[i], b = i + 1 < hs.length ? hs[i + 1] : hs[0] + 360;
      if (b - a > best) { best = b - a; mid = (a + b) / 2; }
    }
    return Math.round(mid) % 360;
  }
  [H, S, L].forEach(function (el) { el.addEventListener("input", update); });
  $("pk-free").addEventListener("click", function () { H.value = freeHue(); update(); });
  $("pk-copy").addEventListener("click", function () {
    var btn = $("pk-copy");
    var text = $("pk-code").textContent;
    var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = "Copy"; }, 1200); };
    if (navigator.clipboard) { navigator.clipboard.writeText(text).then(done); }
  });
  H.value = freeHue();
  update();
})();
</script>

(function () {
  var CSS =
    ".md-header__inner > .md-version{" +
    "order:98 !important;" +
    "margin-left:auto !important;" +
    "margin-right:.6rem !important;" +
    "align-self:center !important;" +
    "display:flex !important;" +
    "align-items:center !important;" +
    "position:relative;" +
    "}" +
    ".md-header__inner > .md-version .md-version__current{margin:0 .4rem !important;}" +
    ".md-header__inner > .md-version .md-version__list{left:auto !important;right:0 !important;}" +
    '.md-header__inner > [data-md-component="palette"]{' +
    "order:99 !important;" +
    "margin-left:0 !important;" +
    "}";

  // the style must survive page changes, so it is re-added whenever it is missing
  function ensureStyle() {
    if (document.getElementById("version-move-style")) return;
    var style = document.createElement("style");
    style.id = "version-move-style";
    style.textContent = CSS;
    document.head.appendChild(style);
  }

  function place() {
    ensureStyle();
    var inner = document.querySelector(".md-header__inner");
    var all = Array.prototype.slice.call(
      document.querySelectorAll(".md-header .md-version")
    );
    if (!inner || !all.length) return;

    var fresh = all[0];
    all.slice(1).forEach(function (extra) {
      extra.remove();
    });

    var palette = inner.querySelector('[data-md-component="palette"]');
    var inPlace =
      fresh.parentNode === inner &&
      (palette
        ? fresh.nextElementSibling === palette
        : fresh === inner.lastElementChild);
    if (inPlace) return;

    if (palette) palette.before(fresh);
    else inner.appendChild(fresh);
  }

  // run on first load, on every in-page navigation, and whenever the header changes
  if (window.document$) window.document$.subscribe(place);
  new MutationObserver(place).observe(document.body, {
    childList: true,
    subtree: true,
  });
  new MutationObserver(ensureStyle).observe(document.head, { childList: true });
  place();
})();

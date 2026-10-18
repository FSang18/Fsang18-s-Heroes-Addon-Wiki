(function () {
  var style = document.createElement("style");
  style.textContent =
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
  document.head.appendChild(style);

  function place() {
    var inner = document.querySelector(".md-header__inner");
    var fresh = document.querySelector(".md-header .md-version");
    if (!inner || !fresh || fresh.parentNode === inner) return;
    inner.querySelectorAll(":scope > .md-version").forEach(function (old) {
      old.remove();
    });
    var palette = inner.querySelector('[data-md-component="palette"]');
    if (palette) palette.before(fresh);
    else inner.appendChild(fresh);
  }

  new MutationObserver(place).observe(document.body, {
    childList: true,
    subtree: true,
  });
  place();
})();

(function () {
  // small style tweaks so the dropdown still looks right in its new spot
  var style = document.createElement("style");
  style.textContent =
    ".md-header__inner > .md-version{position:relative;}" +
    ".md-header__inner > .md-version .md-version__current{margin:0 .4rem;}" +
    ".md-header__inner > .md-version .md-version__list{right:0;}";
  document.head.appendChild(style);

  // move the version selector next to the theme switcher
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

  // the selector is created after the page loads, and again on page changes
  new MutationObserver(place).observe(document.body, {
    childList: true,
    subtree: true,
  });
  place();
})();

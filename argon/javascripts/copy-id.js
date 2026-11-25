document.addEventListener("click", function (event) {
  var target = event.target.closest("code.argon-id");
  if (!target || !navigator.clipboard) return;
  navigator.clipboard.writeText(target.textContent.trim()).then(function () {
    target.classList.add("copied");
    setTimeout(function () {
      target.classList.remove("copied");
    }, 1500);
  });
});

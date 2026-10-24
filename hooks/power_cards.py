/* ===== Power cards on hub pages =====
   Made by hooks/power_cards.py from the line  <!-- power-cards -->  on a hub page. */
.md-typeset .pcards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 19rem), 1fr));
  gap: 1rem;
  margin: 1.4rem 0 1.8rem;
}
.md-typeset a.pcard {
  --pc: hsl(var(--hue, 215) var(--sat, 90%) var(--lit, 62%));
  --t: #ff3b30;
  position: relative;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.1rem;
  border: 1px solid color-mix(in srgb, var(--pc) 45%, transparent);
  border-radius: .9rem;
  overflow: hidden;
  color: var(--md-default-fg-color);
  background:
    radial-gradient(circle at 0% 0%, color-mix(in srgb, var(--pc) 22%, transparent), transparent 60%),
    rgba(127, 127, 127, .06);
  transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
}
[data-md-color-scheme="default"] .md-typeset a.pcard {
  --pc: hsl(var(--hue, 215) calc(var(--sat, 90%) - 15%) max(28%, calc(var(--lit, 62%) - 22%)));
}
.md-typeset a.pcard:hover {
  transform: translateY(-3px);
  border-color: var(--pc);
  box-shadow: 0 .6rem 1.4rem -.6rem color-mix(in srgb, var(--pc) 70%, transparent);
}
.md-typeset .pcard-icon {
  flex: none;
  width: 4.2rem;
  height: 4.2rem;
  border-radius: 50%;
  object-fit: cover;
  background: var(--medal-bg, #0b1020);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--pc) 80%, #000), 0 0 1rem color-mix(in srgb, var(--pc) 45%, transparent);
}
.md-typeset .pcard-body { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: .5rem; }
.md-typeset .pcard-name { font-size: 1.05rem; line-height: 1.2; color: var(--pc); padding-right: 2.6rem; }
.md-typeset .pcard-types { display: flex; flex-wrap: wrap; gap: .3rem; font-weight: 400; }
.md-typeset .pcard-types i[class^="c-"] {
  display: inline-flex; align-items: center; gap: .3rem;
  font-style: normal; font-weight: 700; font-size: .66rem;
  padding: .08rem .5rem .08rem .38rem;
  border: 1px solid color-mix(in srgb, var(--k) 55%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, var(--k) 14%, transparent);
  color: color-mix(in srgb, var(--k) 60%, var(--md-default-fg-color));
}
.md-typeset .pcard-types i[class^="c-"]::before {
  content: ""; width: 1em; height: 1em; background-color: var(--k);
  -webkit-mask: var(--ic) center / contain no-repeat; mask: var(--ic) center / contain no-repeat;
}
.md-typeset .pcard-tier {
  position: absolute;
  top: .7rem;
  right: .8rem;
  width: 2.3rem;
  height: 2.55rem;
  display: grid;
  place-items: center;
  background: var(--t);
  clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%);
  color: #15120a;
  font-size: 1.15rem;
}
.md-typeset .pcard-tier b { line-height: 1; }
.md-typeset .pcard-tier[data-tier="A"] { --t: #ff9500; }
.md-typeset .pcard-tier[data-tier="B"] { --t: #ffd60a; }
.md-typeset .pcard-tier[data-tier="C"] { --t: #34d84f; }
.md-typeset .pcard-tier[data-tier="D"] { --t: #19d3f0; }
.md-typeset .pcard-tier[data-tier="E"] { --t: #4f6bff; color: #fff; }
.md-typeset .pcard-tier[data-tier="F"] { --t: #d946ef; }
.md-typeset a.pcard-plain { --pc: var(--md-default-fg-color--light); border-style: dashed; }
.md-typeset .pcard-plain .pcard-name { color: var(--md-default-fg-color); padding-right: 0; }
.md-typeset .pcard-soon { font-size: .75rem; color: var(--md-default-fg-color--light); }

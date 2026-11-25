---
title: UI Widgets
---

# UI Widgets

<p class="argon-intro">Widgets are the building blocks of power screens and HUD layouts. These are the widgets Argon adds.</p>

<p class="argon-count">2 listed &middot; Argon 1.0.0</p>

### Ability Bar {#argonability_bar}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_bar</code></div>

<div class="argon-desc">Draws the slots of an argon:ability_bar while it is enabled. Left-click picks an ability, right-click picks the crouch variant. Arrows and dots switch presets, the floppy icon saves.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability_bar</code></td><td>String</td><td>The argon:ability_bar ability to draw, e.g. "fsang:marvel/mutant/reality_warping#my_bar".</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>properties</code></td><td>UI Properties</td><td>Shared widget properties like position, size, tooltip and visibility.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{}</td></tr></tbody></table></div>

---

### Karma Icon {#argonkarma_icon}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:karma_icon</code></div>

<div class="argon-desc">The Yin-Yang karma icon, tinted by the viewing player's karma. Hovering it opens a panel with the alignment, progress and the chat title toggle. Karma is private, so it always shows the player's own.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>properties</code></td><td>UI Properties</td><td>Shared widget properties like position, size, tooltip and visibility.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{}</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:karma_icon"
    }
    ```

---


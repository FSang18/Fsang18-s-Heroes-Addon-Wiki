---
title: Dynamic Textures
---

# Dynamic Textures

<p class="argon-intro">Dynamic textures change while the game runs. These are the ones Argon adds.</p>

<p class="argon-count">4 listed &middot; Argon 1.0.0</p>

### Armor Or Skin Texture {#argonarmor_or_skin}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:armor_or_skin</code></div>

<div class="argon-desc">For models on the body, like claws. Uses the worn suit's texture where an active layer from "model_layers" draws over the given region, otherwise the skin. Match the region to the model's UVs.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>regions</code></td><td>Integer[][]</td><td>The areas of the texture sheet to check, each as [u, v, width, height] in pixels (a 64x64 sheet). Should cover the pixels your model samples. Defaults to the bottom of the left arm: [[40, 48, 4, 4]].</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ [ 40, 48, 4, 4 ] ]</td></tr><tr><td><code>min_coverage</code></td><td>Float</td><td>How much of the region must be drawn (0 to 1) for the suit to count as covering it. 1 means every pixel.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>model_layers</code></td><td>string[]</td><td>The model layer names that count as a suit, like "suit_chestplate" in "palladium:player#suit_chestplate".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;suit_chestplate&quot; ]</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:armor_or_skin"
    }
    ```

---

### Chest Armor Texture {#argonchest_armor}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:chest_armor</code></div>

<div class="argon-desc">Uses the texture of the player's active "suit_chestplate" render layer, so an overlay like argon:female_chest always matches the worn suit. Shows the missing texture if no such layer is active.</div>

=== "Example"

    ```json
    {
      "type": "argon:chest_armor"
    }
    ```

---

### Mouth Selection Texture {#argonmouth_selection}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:mouth_selection</code></div>

<div class="argon-desc">Like palladium:eye_selection, but for the pixels picked on the eye screen's "Mouth" tab. A pixel is an eye or a mouth, never both. Needs the argon:customization/mouth_selection flag.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color the mouth pixels are drawn in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:mouth_selection",
      "color": "#ff8080"
    }
    ```

---

### Secondary Eye Selection Texture {#argoneye_selection_secondary}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:eye_selection_secondary</code></div>

<div class="argon-desc">Like palladium:eye_selection, but for the pixels picked on the eye screen's "Secondary" tab, so a pack can color a second set on its own. Needs the argon:customization/secondary_eye_selection flag.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color the secondary pixels are drawn in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:eye_selection_secondary",
      "color": "#00ffff"
    }
    ```

---


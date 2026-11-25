---
title: Beams
---

# Beams

<p class="argon-intro">Beam renderers decide how a beam looks. Use their ID as the <code>beam_renderer</code> of an ability that shoots a beam.</p>

<p class="argon-count">5 listed &middot; Argon 0.3.31</p>

### Boxed Textured {#argonboxed_textured}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:boxed_textured</code></div>

<div class="argon-desc">Renders a beam as a stack of textured boxes like palladium's "textured" renderer, but each face has its own lighting normal. That fixes wrong or flickering brightness on side and bottom faces.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>texture</code></td><td>Texture Reference</td><td>The texture applied to each box segment.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size</code></td><td>Float (&gt;= 0.0),<br>Vector 2D</td><td>The cross-section size of each box segment, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0625</td></tr><tr><td><code>texture_length</code></td><td>Float</td><td>How many blocks of beam one full copy of the texture covers, separate from "size". Keeps the arm's thickness fixed while you control how dense the texture is. Defaults to the average of "size"'s width and height.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rotation</code></td><td>Float</td><td>A fixed rotation, in degrees, around the beam's own axis.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>rotation_speed</code></td><td>Float</td><td>Degrees per tick to continuously spin the boxes around the beam's own axis.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>render_type</code></td><td><code>minecraft:entity_translucent</code><br><code>minecraft:entity_cutout</code><br><code>minecraft:entity_cutout_cull</code><br><code>palladium:entity_translucent_cull</code><br><code>palladium:glow</code><br><code>palladium:glow_cull</code><br><code>argon:glow</code><br><code>argon:additive</code><br><code>argon:glow_no_depth_write</code><br><code>argon:glow_emission</code><br><code>argon:additive_emission</code></td><td>The render type to render the beam with.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">minecraft:entity_cutout</td></tr><tr><td><code>light_emission</code></td><td>Integer</td><td>The light emission of the beam, from 0 to 15.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:boxed_textured",
      "texture": "namespace:textures/beams/example_beam.png",
      "size": 3
    }
    ```

---

### Cone {#argoncone}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:cone</code></div>

<div class="argon-desc">Draws a beam as a cone from "start_size" to "end_size" blocks wide, with a soft glow, a brighter core and an optional scrolling texture. Pair it with the "cone" setting of argon:energy_beam.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>start_size</code></td><td>Float</td><td>How wide the cone is where it starts, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.15</td></tr><tr><td><code>end_size</code></td><td>Float</td><td>How wide the cone is where it ends, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>end_distance</code></td><td>Float</td><td>If set, "end_size" is reached this many blocks from the start and the cone keeps that angle however long the beam is, so a beam stopped by a wall is narrower. Set it to the ability's max_distance. Without it, "end_size" is the width wherever the beam ends.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>glow</code></td><td><em>Cone Layer</em></td><td>The soft outer glow: its colour (hex), its opacity (0 turns it off) and its width compared with the whole cone's. Drawn as "glow_layers" nested cones.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{ &quot;color&quot;: &quot;#FFFFFF&quot;, &quot;opacity&quot;: 0.35, &quot;scale&quot;: 1.0 }</td></tr><tr><td><code>core</code></td><td><em>Cone Layer</em></td><td>The brighter core inside the glow, set the same way.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{ &quot;color&quot;: &quot;#FFFFFF&quot;, &quot;opacity&quot;: 0.5, &quot;scale&quot;: 0.45 }</td></tr><tr><td><code>glow_layers</code></td><td>Integer</td><td>How many nested cones the glow is made of (1-8): more is softer and thicker toward the middle.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3</td></tr><tr><td><code>texture</code></td><td><em>Cone Texture</em></td><td>A texture over the cone's surface. Keys: texture*, color, opacity (0.6), scale (1), texture_length (2), around (2), scroll_speed (0.03), rotation_speed (0).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blend</code></td><td><code>additive</code><br><code>translucent</code></td><td>How the cone is blended into the scene: additive glows brighter where layers overlap, translucent is a plain see-through surface.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">ADDITIVE</td></tr><tr><td><code>end_fade</code></td><td>Float</td><td>How opaque the far end of the cone is compared to the start, 0 to 1. Lower fades the cone out along its length.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.2</td></tr><tr><td><code>segments</code></td><td>Integer</td><td>How many flat sides the cone is drawn with (6-64): more is rounder.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">16</td></tr></tbody></table></div>

    <p class="argon-nested"><code>glow</code> (Cone Layer)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color of the layer.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>opacity</code></td><td>Float (0.0 ~ 1.0)</td><td>How opaque the layer is.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>scale</code></td><td>Float (0.01 ~ 4.0)</td><td>The size of the layer relative to the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>texture</code> (Cone Texture)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>texture</code></td><td>Identifier</td><td>The texture drawn on the cone.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>color</code></td><td>Color</td><td>The tint of the texture.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>opacity</code></td><td>Float (0.0 ~ 1.0)</td><td>How opaque the texture is.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>scale</code></td><td>Float (0.01 ~ 4.0)</td><td>The size of the texture relative to the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>texture_length</code></td><td>Float (0.05 ~ 64.0)</td><td>How many blocks one repeat of the texture covers.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>around</code></td><td>Integer (1 ~ 16)</td><td>How many times the texture repeats around the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>scroll_speed</code></td><td>Float</td><td>How fast the texture scrolls along the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rotation_speed</code></td><td>Float</td><td>How fast the texture turns around the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:cone",
      "end_distance": 20
    }
    ```

---

### Glow Laser {#argonglow_laser}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:glow_laser</code></div>

<div class="argon-desc">Palladium's laser beam with brightness settings for its glow and core. Below 1 fades the part, above 1 stacks extra draws for a stronger glow (up to 8). Both are values, so molang can animate them.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>render_settings</code></td><td>Laser Renderer Settings</td><td>The render settings for the laser, exactly as for palladium:laser.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>glow_intensity</code></td><td>(Dynamic) Value</td><td>How bright the glow is. 1 is the laser as Palladium draws it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>core_intensity</code></td><td>(Dynamic) Value</td><td>How bright the core is. 1 is the laser as Palladium draws it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:glow_laser",
      "render_settings": {
        "bloom": 0
      },
      "glow_intensity": 2,
      "core_intensity": 1
    }
    ```

---

### Ring {#argonring}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ring</code></div>

<div class="argon-desc">Draws a flat textured disc around the start of the beam, as wide as the beam is long, with bands that travel outward like shockwave rings. Only the beam's length matters, so it suits argon:anchored_beam, whose animation_timer fades it in and out.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>texture</code></td><td>Identifier</td><td>The ring texture. Its U axis runs around the ring and its V axis outward.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>color</code></td><td>Color</td><td>A color multiplied with the texture.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FFFFFF</td></tr><tr><td><code>opacity</code></td><td>Float</td><td>How opaque the ring is, 0 to 1.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.8</td></tr><tr><td><code>inner_radius</code></td><td>Float</td><td>Radius of the empty hole in the middle, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>texture_length</code></td><td>Float</td><td>How many blocks outward one repeat of the texture covers.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr><tr><td><code>around</code></td><td>Integer</td><td>How many times the texture repeats around the ring.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3</td></tr><tr><td><code>scroll_speed</code></td><td>Float</td><td>How many texture repeats the bands travel outward per tick; negative pulls them inward.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>rotation_speed</code></td><td>Float</td><td>How many degrees per tick the ring spins.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>twist</code></td><td>Float</td><td>How many degrees the ring is twisted between its inner and outer edge, which curves the bands into spirals.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>end_fade</code></td><td>Float</td><td>How opaque the outer edge is compared with the inner one, 0 to 1.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>height</code></td><td>Float</td><td>How far above the start of the beam the ring is drawn, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.05</td></tr><tr><td><code>blend</code></td><td><code>additive</code><br><code>translucent</code></td><td>How the ring is blended into the scene.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">TRANSLUCENT</td></tr><tr><td><code>segments</code></td><td>Integer</td><td>How many flat sides the ring is drawn with (8-96).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">48</td></tr><tr><td><code>face_beam</code></td><td>Boolean</td><td>If true, the ring faces along the beam instead of lying flat, so it works as a circle in front of a hand.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ring",
      "texture": "example:textures/beams/ring.png"
    }
    ```

---

### Segmented Textured {#argonsegmented_textured}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:segmented_textured</code></div>

<div class="argon-desc">Renders a beam as flat textured layers around one axis that can tile, spin and scroll. Can sag near the origin and tighten over "sag_duration". Good for drill or corkscrew beams.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>textures</code></td><td><em>Beam Texture Layer</em>[]</td><td>The texture layers to render simultaneously around the beam axis, each either a sweeping ribbon ("facing": "radial", default) or a stack of flat cards facing down the beam ("along_beam").</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>render_type</code></td><td><code>minecraft:entity_translucent</code><br><code>minecraft:entity_cutout</code><br><code>minecraft:entity_cutout_cull</code><br><code>palladium:entity_translucent_cull</code><br><code>palladium:glow</code><br><code>palladium:glow_cull</code><br><code>argon:glow</code><br><code>argon:additive</code><br><code>argon:glow_no_depth_write</code><br><code>argon:glow_emission</code><br><code>argon:additive_emission</code></td><td>The render type to render the beam with.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">minecraft:entity_translucent</td></tr><tr><td><code>light_emission</code></td><td>Integer</td><td>The light emission of the beam, from 0 to 15.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>sag_amplitude</code></td><td>Float</td><td>How far, in blocks, the beam bows sideways from a straight line when loose, at its most bowed point near the origin. Both ends always stay pinned to their anchors. 0 (default) keeps the beam perfectly straight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>sag_waves</code></td><td>Float</td><td>How many full side-to-side wave cycles the sag has along the beam, fading from full strength at the origin to none at the target. Only matters when "sag_amplitude" is above 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>sag_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Ticks for the beam to go from loose to taut after it starts being drawn for an entity. It starts loose again after a fresh attach (e.g. a new swing or grapple). Only matters when "sag_amplitude" is above 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>tint</code></td><td><em>Item Tint</em></td><td>Tints every texture layer by the color a registered source reads off an item in "slot" (first match wins). "source" is an id an addon registered; with no match it stays white. Omit for no tint.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>textures[]</code> (Beam Texture Layer)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>texture</code></td><td>Texture Reference,<br>Dynamic Texture</td><td>The texture of the layer.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size</code></td><td>Float (&gt;= 0.0),<br>Vector 2D</td><td>The size of the layer, as one number or width and height.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spacing</code></td><td>Float (&gt;= 0.0)</td><td>The gap between repeats along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rotation</code></td><td>Float (0.0 ~ 360.0)</td><td>The starting rotation in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rotation_speed</code></td><td>Float (&gt;= 0.0)</td><td>How fast the layer rotates.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>motion_speed</code></td><td>Float</td><td>How fast the layer moves along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>facing</code></td><td><code>radial</code><br><code>along_beam</code></td><td>Whether the layer faces outward from the beam or along it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pulse</code></td><td>Pulse</td><td>Makes the layer pulse in size.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>tint</code> (Item Tint)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slot of the item that is tinted.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>source</code></td><td>Identifier</td><td>The tint source used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:segmented_textured",
      "textures": [
        {
          "texture": "namespace:textures/beams/example_beam.png",
          "size": 2,
          "spacing": 1,
          "rotation_speed": 20,
          "pulse": {
            "scale": 0.1,
            "frequency": 2
          }
        },
        {
          "texture": "namespace:textures/beams/example_beam.png",
          "size": 2,
          "spacing": 4,
          "rotation_speed": 10,
          "motion_speed": 8,
          "facing": "along_beam"
        }
      ],
      "sag_amplitude": 0.35
    }
    ```

---


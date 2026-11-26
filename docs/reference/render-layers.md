---
title: Render Layers
---

# Render Layers

<p class="argon-intro">Render layers draw extra models or effects on top of an entity. These are the render layers Argon adds.</p>

<p class="argon-count">3 listed &middot; Argon 1.0.1</p>

### Anchored Lightning Sparks {#argonanchored_lightning_sparks}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:anchored_lightning_sparks</code></div>

<div class="argon-desc">Like Palladium's Lightning Sparks, but the sparks can be tied to named body part bones using the same "anchors" as the Thrusters layer.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>frequency</code></td><td>Float</td><td>The frequency of the sparks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>amount</code></td><td>Integer</td><td>How many sparks spawn each time, per anchor (or for the whole entity if "anchors" is empty).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5</td></tr><tr><td><code>render_settings</code></td><td>Laser Renderer Settings</td><td>The render settings for the sparks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchors</code></td><td>string[]</td><td>Bones to spawn sparks at, e.g. "head" or "right_arm". Each gets its own spark cycle. Empty spawns them anywhere on the entity, like palladium:lightning_sparks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>anchor_size</code></td><td>Float</td><td>Only relevant when "anchors" isn't empty: how far, in blocks, sparks jitter from the anchor point.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>[x, y, z] offset from the anchor (or the entity if "anchors" is empty), so sparks can sit off the bone's pivot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ 0, 0, 0 ]</td></tr><tr><td><code>transformation</code></td><td>Identifier,<br>Identifier[]</td><td>Transformation ID(s). The layer only shows while one of these transformations is shown, on the transformed model. Without this field the layer is hidden while a transformation model is shown. Layers inside a compound layer without their own value use the one of the compound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>shrink_player_parts</code></td><td><code>cape</code><br><code>jacket</code><br><code>left_sleeve</code><br><code>right_sleeve</code><br><code>left_pants_leg</code><br><code>right_pants_leg</code><br><code>hat</code></td><td>Skin overlay part(s) that are scaled down slightly while this layer is visible, so they don't stick out of the layer's model. "cape" has no effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:anchored_lightning_sparks",
      "frequency": 0.2,
      "amount": 10,
      "render_settings": {
        "glow": "#0000ff",
        "bloom": 2,
        "size": 2
      },
      "anchors": [
        "head",
        "right_arm"
      ],
      "anchor_size": 0.25,
      "offset": [
        0,
        0.1,
        0
      ]
    }
    ```

---

### Cloth Render Layer {#argoncloth}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:cloth</code></div>

<div class="argon-desc">Renders a simulated cloth grid (a cape by default) that flows, bends and trails behind the wearer instead of turning as one flat plane.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attachment</code></td><td><code>back</code><br><code>left_arm</code><br><code>right_arm</code><br><code>waist</code></td><td>Which part of the cloth grid is pinned to the wearer: "back" (cape), "left_arm" or "right_arm" (draped along an arm), or "waist" (skirt or kilt, a box-shaped loop around the hips).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">back</td></tr><tr><td><code>material</code></td><td>Identifier,<br>Inline Material Object</td><td>A registered material id (e.g. "argon:heavy") or an inline object overriding individual physics properties.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">argon:standard</td></tr><tr><td><code>size</code></td><td>Vector 2D</td><td>[length, width] of the cloth at rest, in blocks. For a "waist" attachment, "width" is the half-width of the left and right sides of the box. "depth" sets the front and back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ 1.8, 1 ]</td></tr><tr><td><code>segments</code></td><td>Vector 2D</td><td>[segments_x, segments_y]: simulation columns/rows. More = smoother bending at a performance cost.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ 4, 8 ]</td></tr><tr><td><code>wrap</code></td><td>Float</td><td>"back" attachment only. Curves the pinned edge forward so it hugs the wearer's sides, turning a flat cape into a wrap-around cloak. 0 is flat.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>depth</code></td><td>Float</td><td>"waist" attachment only. Half-depth of the front and back sides, in blocks. Usually smaller than "width", since players are thinner front to back. Defaults to "width".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch_influence</code></td><td>Float</td><td>"waist" attachment only. While crouching, the garment follows the body's pitch as one piece. This scales how much, 0 ignores it and 1 follows fully.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>hem_pitch_fraction</code></td><td>Float</td><td>Currently unused. Kept so existing configs that set it still load.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>attach</code></td><td>Vector 3D</td><td>[x, y, z] offset of the attach point from the neck, in wearer space. Y=0 is neck height and higher Y goes down. A cape needs a positive Z to sit behind. For "waist" use X=0, Z=0 and Y about 0.75-0.9.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ 0, 0.1, 0.4 ]</td></tr><tr><td><code>taper</code></td><td>Float</td><td>"back" attachment only. Width at the shoulders as a fraction of the width at the hem, 0.05 to 1. Below 1 the cloth is a trapezoid that flares out to "width" at the hem. 1 is a plain rectangle.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>aerodynamics</code></td><td><em>Cloth Aerodynamics</em></td><td>How the cloth reacts to the wearer's real speed, not the selected flight level. Each part is documented in the tables below.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{}</td></tr><tr><td><code>texture</code></td><td>Texture Reference,<br>Dynamic Texture</td><td>The texture for the cloth. UVs stay stable across the grid however the cloth deforms.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>render_type</code></td><td><code>minecraft:entity_translucent</code><br><code>minecraft:entity_cutout</code><br><code>minecraft:entity_cutout_cull</code><br><code>palladium:entity_translucent_cull</code><br><code>palladium:glow</code><br><code>palladium:glow_cull</code><br><code>argon:glow</code><br><code>argon:additive</code><br><code>argon:glow_no_depth_write</code><br><code>argon:glow_emission</code><br><code>argon:additive_emission</code></td><td>The render type to draw the cloth with.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">minecraft:entity_translucent</td></tr><tr><td><code>transformation</code></td><td>Identifier,<br>Identifier[]</td><td>Transformation ID(s). The layer only shows while one of these transformations is shown, on the transformed model. Without this field the layer is hidden while a transformation model is shown. Layers inside a compound layer without their own value use the one of the compound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>shrink_player_parts</code></td><td><code>cape</code><br><code>jacket</code><br><code>left_sleeve</code><br><code>right_sleeve</code><br><code>left_pants_leg</code><br><code>right_pants_leg</code><br><code>hat</code></td><td>Skin overlay part(s) that are scaled down slightly while this layer is visible, so they don't stick out of the layer's model. "cape" has no effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics</code> (Cloth Aerodynamics)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>airflow_strength</code></td><td>Float (0.0 ~ 4.0)</td><td>How strongly the wearer's speed blows the cloth back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>turn_inertia</code></td><td>Float (0.0 ~ 4.0)</td><td>How much the cloth lags behind when the wearer turns.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>flight_stabilization</code></td><td>Float (0.0 ~ 1.0)</td><td>Calms the swinging of the cloth at speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>flight_stiffness_multiplier</code></td><td>Float (1.0 ~ 3.0)</td><td>Multiplies the stiffness of the cloth during flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.15</td></tr><tr><td><code>stiffness_response</code></td><td>Float (0.01 ~ 1.0)</td><td>How quickly the stiffness follows the speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.1</td></tr><tr><td><code>body_hug</code></td><td>Float (0.0 ~ 1.0)</td><td>How tightly a back cape is pulled against the body near top speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.75</td></tr><tr><td><code>hug_start</code></td><td>Float (0.0 ~ 0.99)</td><td>How far through the speed range the hugging begins.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>limb_collision</code></td><td><em>Cloth Limb Collision</em></td><td>Keeps the cloth out of the wearer's body. Back capes only.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>narrowing</code></td><td><em>Cloth Narrowing</em></td><td>Narrows the cloth as the wearer speeds up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>flutter</code></td><td><em>Cloth Flutter</em></td><td>Makes the cloth flutter at speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.limb_collision</code> (Cloth Limb Collision)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether the cloth is kept out of the body shapes. Back capes only.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>torso</code></td><td><em>Cloth Torso Shape</em></td><td>The torso shape the cloth stays out of.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>head</code></td><td><em>Cloth Head Shape</em></td><td>The head shape the cloth stays out of.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arms</code></td><td><em>Cloth Arm Shape</em></td><td>The arm shape the cloth stays out of.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>legs</code></td><td><em>Cloth Leg Shape</em></td><td>The leg shape the cloth stays out of.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.limb_collision.torso</code> (Cloth Torso Shape)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>width</code></td><td>Float (0.1 ~ 2.0)</td><td>The width of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>depth</code></td><td>Float (0.05 ~ 1.0)</td><td>The depth of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>length</code></td><td>Float (0.1 ~ 2.0)</td><td>The length of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.1</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 0.6)</td><td>How rounded the corners are, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.1</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.limb_collision.head</code> (Cloth Head Shape)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>width</code></td><td>Float (0.1 ~ 2.0)</td><td>The width of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>depth</code></td><td>Float (0.05 ~ 1.0)</td><td>The depth of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>length</code></td><td>Float (0.1 ~ 2.0)</td><td>The length of the shape in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 0.6)</td><td>How rounded the corners are, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.1</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.limb_collision.arms</code> (Cloth Arm Shape)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>Float (0.05 ~ 1.0)</td><td>The radius of the limb in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>length</code></td><td>Float (0.1 ~ 1.5)</td><td>The length of the limb in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.8</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.limb_collision.legs</code> (Cloth Leg Shape)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>Float (0.05 ~ 1.0)</td><td>The radius of the limb in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>length</code></td><td>Float (0.1 ~ 1.5)</td><td>The length of the limb in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.8</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.narrowing</code> (Cloth Narrowing)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether the cloth narrows at speed. Not used by waist cloth.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>start_speed</code></td><td>Float (0.0 ~ 1000.0)</td><td>The speed in blocks per second where narrowing starts when there is no flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10.0</td></tr><tr><td><code>full_speed</code></td><td>Float (0.0 ~ 1000.0)</td><td>The speed in blocks per second where narrowing is full when there is no flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">40.0</td></tr><tr><td><code>start_fraction</code></td><td>Float (0.0 ~ 2.0)</td><td>The fraction of the wearer's top flight speed where narrowing starts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>full_fraction</code></td><td>Float (0.0 ~ 2.0)</td><td>The fraction of the wearer's top flight speed where narrowing is full.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.85</td></tr><tr><td><code>maximum</code></td><td>Float (0.0 ~ 0.9)</td><td>The most the cloth narrows. The default is 0.35 when wrap is above 0 or for arms.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>response</code></td><td>Float (0.001 ~ 1.0)</td><td>How quickly the cloth narrows.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.06</td></tr><tr><td><code>recovery</code></td><td>Float (0.001 ~ 1.0)</td><td>How quickly the cloth widens again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.04</td></tr><tr><td><code>distribution</code></td><td>Float (0.1 ~ 6.0)</td><td>Higher values keep the top of the cloth wider.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>fold</code></td><td>Float (0.0 ~ 1.5)</td><td>How much the cloth folds into pleats. 0 turns the pleats off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>compression</code></td><td>Float (0.0 ~ 0.9)</td><td>How much of the narrowing squeezes the cloth itself instead of folding it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr></tbody></table></div>

    <p class="argon-nested"><code>aerodynamics.flutter</code> (Cloth Flutter)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>intensity</code></td><td>Float (0.0 ~ 5.0)</td><td>How strong the fluttering is.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>frequency</code></td><td>Float (0.1 ~ 5.0)</td><td>How fast the cloth flutters.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>speed_influence</code></td><td>Float (0.0 ~ 4.0)</td><td>How much the wearer's speed adds to the fluttering.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>damping</code></td><td>Float (0.0 ~ 1.0)</td><td>How quickly the fluttering dies down.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>edge_multiplier</code></td><td>Float (1.0 ~ 5.0)</td><td>How much stronger the fluttering is at the free edge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:cloth",
      "texture": "example:textures/models/capes/red_cape.png"
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:cloth",
      "material": "argon:heavy",
      "size": [
        2.4,
        1.6
      ],
      "segments": [
        5,
        10
      ],
      "wrap": 0.6,
      "texture": "example:textures/models/cloaks/heavy_cloak.png"
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:cloth",
      "size": [
        2.5,
        1.4
      ],
      "segments": [
        6,
        10
      ],
      "taper": 0.4,
      "aerodynamics": {
        "airflow_strength": 1.2,
        "narrowing": {
          "maximum": 0.6
        }
      },
      "texture": "example:textures/models/capes/streamlined_cape.png"
    }
    ```

=== "Example 4"

    ```json
    {
      "type": "argon:cloth",
      "attachment": "left_arm",
      "material": "argon:lightweight",
      "size": [
        1.2,
        0.5
      ],
      "segments": [
        3,
        6
      ],
      "attach": [
        -0.3,
        0.2,
        0
      ],
      "texture": "example:textures/models/arm_cloth.png"
    }
    ```

=== "Example 5"

    ```json
    {
      "type": "argon:cloth",
      "attachment": "waist",
      "material": "argon:leather",
      "size": [
        0.32,
        0.28
      ],
      "segments": [
        16,
        6
      ],
      "depth": 0.15999999642372131,
      "pitch_influence": 0.5,
      "attach": [
        0,
        0.64,
        0
      ],
      "texture": "example:textures/models/skirts/skirt.png"
    }
    ```

---

### Fade Render Layer {#argonfade}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:fade</code></div>

<div class="argon-desc">Wraps another render layer and draws it at a changing opacity so it can fade in and out. Put the wrapped layer's conditions inside "layer". Nothing is drawn at opacity 0.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>opacity</code></td><td>Float / Value</td><td>(Dynamic) 0 to 1, how opaque the wrapped layer is. Usually an ability's eased animation timer, e.g. palladium.get_animation_timer_eased('namespace:power#ability'), which already runs 0 to 1.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>layer</code></td><td>Render Layers</td><td>The render layer to draw, written exactly as it would be on its own, including its "conditions".</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:fade",
      "opacity": {
        "type": "palladium:molang_float",
        "molang": "palladium.get_animation_timer_eased('example:power#some_ability')"
      },
      "layer": {
        "texture": {
          "type": "palladium:eye_selection",
          "color": "#6b6b6b"
        }
      }
    }
    ```

---


---
title: Abilities
---

# Abilities

<p class="argon-intro">Abilities are what a power actually does. They go into the <code>abilities</code> field of a Palladium power, and their state decides when they are unlocked and enabled. Every ability that comes with Argon is listed below.</p>

<p class="argon-count">127 listed &middot; Argon 0.3.31</p>

### Ability Bar {#argonability_bar}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_bar</code></div>

<div class="argon-desc">Holds the data for an ability bar widget. Players fill its slots from an ability pool, with optional presets and crouch variants. Does nothing on its own.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>abilities</code></td><td>String</td><td>List of ability pool entries the player can choose from for each slot.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slots</code></td><td>Integer (&gt; 0)</td><td>How many ability bar slots to offer.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5</td></tr><tr><td><code>presets</code></td><td>Integer (&gt; 0)</td><td>How many switchable sets of slot assignments to offer, where 1 disables the preset-switching arrows.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>crouch_variants</code></td><td>Boolean</td><td>Whether each slot also accepts a separate, crouch-only ability assignment.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>hide_unavailable</code></td><td>Boolean</td><td>Hides pool abilities the player can't get yet in the slot picker. Ignores ability_bar_active checks when deciding that.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:ability_bar",
      "abilities": [
        "argon:example#ability_1",
        "argon:example#ability_2"
      ]
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:ability_bar",
      "abilities": [
        {
          "ability": "argon:example#ability_1",
          "slot": 0
        },
        {
          "ability": "argon:example#ability_2",
          "list_index_slot": 0
        }
      ],
      "presets": 3,
      "crouch_variants": true
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "ability_bar": {
          "type": "argon:ability_bar",
          "abilities": [
            "argon:example#ability_1",
            "argon:example#ability_2"
          ]
        }
      }
    }
    ```

---

### Ability Data Attachment Modifier {#argonability_data_attachment_modifier}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_data_attachment_modifier</code></div>

<div class="argon-desc">While enabled, watches a list of other abilities. For each enabled one it adds to, subtracts from or sets a shared number data attachment, at its own rate and timer.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attachment</code></td><td>Data Attachment ID</td><td>The id of the number-valued data attachment to modify, shared by every entry.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>abilities</code></td><td><em>Attachment Modifier</em>,<br><em>Attachment Modifier</em>[]</td><td>Each entry references one of the entity's own abilities (e.g. "fsang:marvel/mutant/cosmic_herald#some_ability"), an operation* ("add" default, "subtract", or "set"), a value used by that operation, and a rate* (default 20 ticks) - the referenced ability's own enabled state is checked every tick, and the modification fires every "rate" ticks it stays enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>abilities</code> (Attachment Modifier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The ability whose value is changed.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>operation</code></td><td><code>add</code><br><code>subtract</code><br><code>set</code></td><td>How the value is applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The amount to add, subtract or set.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rate</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How often the change is applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_data_attachment_modifier",
      "attachment": "example:my_attachment",
      "abilities": [
        {
          "ability": "example:my_power#some_ability",
          "value": 1
        },
        {
          "ability": "example:my_power#other_ability",
          "operation": "subtract",
          "value": 2,
          "rate": 40
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "ability_data_attachment_modifier": {
          "type": "argon:ability_data_attachment_modifier",
          "attachment": "example:my_attachment",
          "abilities": [
            {
              "ability": "example:my_power#some_ability",
              "value": 1
            },
            {
              "ability": "example:my_power#other_ability",
              "operation": "subtract",
              "value": 2,
              "rate": 40
            }
          ]
        }
      }
    }
    ```

---

### Anchored Beam {#argonanchored_beam}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:anchored_beam</code></div>

<div class="argon-desc">While enabled, draws the beam_renderer from a body part, "length" blocks long. Visual only, no aiming or damage. With an animation_timer the beam grows and shrinks.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The id of the beam renderer whose segments to render in place.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>length</code></td><td>Float</td><td>How far, in blocks, each segment reaches past its body_part/offset anchor, in the same direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>rotation</code></td><td>Vector 3D</td><td>Euler rotation in degrees (applied X then Y then Z) that tilts which way each segment extends, relative to its own body part's local space - independent of the offset's own direction. E.g. [90, 0, 0] to swing a segment that otherwise hangs straight down (the default with no offset) so it points forward instead, like an upright held tool.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">( 0.000E+0  0.000E+0  0.000E+0)</td></tr><tr><td><code>yaw_only</code></td><td>Boolean</td><td>If true, the beam only turns with the body's facing and ignores lean, pitch and roll, so it stays level. The start point still follows the body part.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:anchored_beam",
      "beam_renderer": "example:beam_renderer_id",
      "rotation": [
        90,
        0,
        0
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "anchored_beam": {
          "type": "argon:anchored_beam",
          "beam_renderer": "example:beam_renderer_id",
          "rotation": [
            90,
            0,
            0
          ]
        }
      }
    }
    ```

---

### Area Burst {#argonarea_burst}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:area_burst</code></div>

<div class="argon-desc">On its first enabled tick, hits every living entity in a sphere or cone around the user once with damage, armor penetration, knockback and effects. Can deflect or destroy projectiles. Skips the user, pets, teammates and armor stands.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>sphere</code><br><code>cone</code></td><td>"sphere" hits everything within the radius. "cone" only hits what is inside cone_angle of where the user looks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">sphere</td></tr><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>How far the burst reaches, in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>cone_angle</code></td><td>Float</td><td>The full opening angle of the cone, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60.0</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>The damage dealt to each entity hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used; the user's normal attack when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>armor_penetration</code></td><td>Float</td><td>The fraction from 0 to 1 of a hit entity's armor that is ignored.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>falloff</code></td><td>Float</td><td>From 0 to 1, how much damage and knockback are reduced for entities at the very edge of the burst.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>knockback_distance</code></td><td>(Dynamic) Value</td><td>How far, in blocks, hit entities are pushed away from the user. Weakened by knockback resistance.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lift</code></td><td>(Dynamic) Value</td><td>Upward launch speed added to the knockback.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>movement_limit</code></td><td><em>Movement Limit</em></td><td>Scales knockback and lift down for wide entities, as on energy beams.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Mob effects applied to every entity hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>projectiles</code></td><td><code>none</code><br><code>deflect</code><br><code>destroy</code></td><td>"deflect" sends projectiles in range away from the user. "destroy" removes them. The user's own projectiles are left alone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">none</td></tr><tr><td><code>hostile_only</code></td><td>Boolean</td><td>If true, only hostile mobs are affected.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>dispel</code></td><td><em>Dispel</em></td><td>Removes up to count effects of the given category ("beneficial" or "harmful") from every entity hit, longest first. Bosses are skipped unless skip_bosses is false.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>look_target_range</code></td><td>Double</td><td>If set, the burst is centered where the user looks, up to this many blocks away, instead of on the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>push</code></td><td><code>radial</code><br><code>path_side</code></td><td>"radial" pushes hit entities straight away from the user. "path_side" pushes them sideways, off the line the user is travelling along, towards the side they are already on.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">radial</td></tr><tr><td><code>visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle visuals spawned at the centre of the burst, in the same format as the visuals of argon:energy_beam, for example a ring.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>movement_limit</code> (Movement Limit)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>full_below_width</code></td><td>Float (0.0 ~ 64.0)</td><td>Targets up to this wide, in blocks, are pushed with full strength.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>none_above_width</code></td><td>Float (0.0 ~ 64.0)</td><td>Targets at least this wide, in blocks, are not pushed at all. In between, the push fades out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>immovable</code></td><td>Entity Type Tag</td><td>Entities in this tag are never pushed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>dispel</code> (Dispel)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>category</code></td><td><code>beneficial</code><br><code>harmful</code></td><td>Which category of effects is removed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 64)</td><td>How many effects are removed at most.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>skip_bosses</code></td><td>Boolean</td><td>If true, boss mobs are not dispelled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>visuals[]</code> (Beam Visual)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>streak</code><br><code>helix</code><br><code>ring</code><br><code>sphere</code><br><code>burst</code><br><code>crescent</code></td><td>The particle pattern to draw.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor</code></td><td><code>end</code><br><code>caster</code></td><td>Whether the pattern is drawn at the end of the beam or around the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>orientation</code></td><td><code>horizontal</code><br><code>vertical</code></td><td>How ring and crescent patterns are turned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>The particle used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 512)</td><td>How many particles the pattern uses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 64.0)</td><td>The radius of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>step</code></td><td>Float (0.05 ~ 16.0)</td><td>The spacing between particles along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch</code></td><td>Float (0.1 ~ 64.0)</td><td>The length of one full twist for helixes, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strands</code></td><td>Integer (1 ~ 8)</td><td>How many strands a helix has.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arc</code></td><td>Float (1.0 ~ 360.0)</td><td>How much of a circle is drawn, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float</td><td>The height of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rings</code></td><td>Integer (1 ~ 16)</td><td>How many rings are drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Float (0.0 ~ 8.0)</td><td>How far the particles scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:area_burst",
      "radius": 6,
      "damage": 8
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "area_burst": {
          "type": "argon:area_burst",
          "radius": 6,
          "damage": 8
        }
      }
    }
    ```

---

### Armor Slots (Retrieve) {#argonrestore_equipment}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:restore_equipment</code></div>

<div class="argon-desc">Puts items stored under an ID by the store_equipment ability back into their original slots, then forgets that ID.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>id</code></td><td>String</td><td>The ID to restore, matching the one used by the store_equipment ability that stored them.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:restore_equipment",
      "id": "civilian_clothes"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "restore_equipment": {
          "type": "argon:restore_equipment",
          "id": "civilian_clothes"
        }
      }
    }
    ```

---

### Armor Slots (Store) {#argonstore_equipment}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:store_equipment</code></div>

<div class="argon-desc">Stores the items in the given slots under an ID and empties those slots. A matching restore_equipment ability puts them back later.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>id</code></td><td>String</td><td>The ID the stored items are saved under.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slots</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slots whose items should be stored and cleared.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:store_equipment",
      "id": "civilian_clothes",
      "slots": [
        "head",
        "chest",
        "legs",
        "feet"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "store_equipment": {
          "type": "argon:store_equipment",
          "id": "civilian_clothes",
          "slots": [
            "head",
            "chest",
            "legs",
            "feet"
          ]
        }
      }
    }
    ```

---

### Auto Attack {#argonauto_attack}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:auto_attack</code></div>

<div class="argon-desc">While enabled, walks toward the nearest mob in range, jumping over obstacles, and hits it with the held item once it is close enough.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far from the player a mob can be to be selected as a target and chased.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attack_range</code></td><td>Double</td><td>How close the target needs to be before the player stops moving and attacks it instead.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The player's movement speed, in blocks per tick, while chasing a target outside attack range.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:auto_attack",
      "range": 8,
      "attack_range": 2.5,
      "speed": 0.3
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "auto_attack": {
          "type": "argon:auto_attack",
          "range": 8,
          "attack_range": 2.5,
          "speed": 0.3
        }
      }
    }
    ```

---

### Biome Swap {#argonbiome_swap}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:biome_swap</code></div>

<div class="argon-desc">While enabled, replaces the terrain within "radius" of where it started with fresh "biome" terrain (optionally in a black concrete shell). Every changed block is restored on disable.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>Double</td><td>How far from the entity's position (1-64) the swap reaches.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>biome</code></td><td>Identifier</td><td>The biome(s) to generate, vanilla or modded. A single ID, a list of IDs, or a list that mixes IDs with objects that also give a status effect to entities in the area (see the second example).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height_below</code></td><td>Integer</td><td>How many blocks below the entity's feet are included when sphere is false.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>height_above</code></td><td>Integer</td><td>How many blocks above the entity's feet are included when sphere is false.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>sphere</code></td><td>Boolean</td><td>If true, the area is a full sphere inside a solid black concrete shell instead of a column limited by radius.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>unbreakable</code></td><td>Boolean</td><td>If true, none of the newly added blocks can be broken while the ability is enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>build_animation</code></td><td>Boolean</td><td>If true, the area grows in and shrinks out over a couple of seconds instead of popping in and out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:biome_swap",
      "radius": 10,
      "biome": "minecraft:desert"
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:biome_swap",
      "radius": 16,
      "biome": [
        {
          "biome": "minecraft:crimson_forest",
          "effect": "minecraft:fire_resistance",
          "amplifier": 1,
          "affect_self": false
        },
        "minecraft:deep_dark"
      ],
      "height_below": 6,
      "height_above": 8,
      "sphere": true,
      "unbreakable": false,
      "build_animation": false
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "biome_swap": {
          "type": "argon:biome_swap",
          "radius": 10,
          "biome": "minecraft:desert"
        }
      }
    }
    ```

---

### Blast Chain {#argonblast_chain}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:blast_chain</code></div>

<div class="argon-desc">Fires a beam that only damages on reaching its target. If it hits a living entity it fires on to the nearest other visible living entity, up to "chain_count" more times.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The id of the beam renderer to use for every segment of the chain.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>Float</td><td>The damage dealt to the entity hit by the initial shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>damage_falloff</code></td><td>Float</td><td>Multiplier on "damage" for each jump already taken (0.85 means the 2nd hit deals 85%, the 3rd 72.25%). 1 means no falloff. Effects keep their full strength.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>max_distance</code></td><td>Float</td><td>The maximum distance the initial shot can travel before giving up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">30.0</td></tr><tr><td><code>speed</code></td><td>Float</td><td>The blocks every beam piece (initial shot and every chain jump) travels per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>length</code></td><td>Float</td><td>The length of the traveling beam piece, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr><tr><td><code>set_on_fire_ticks</code></td><td>Integer</td><td>How many ticks each hit entity is set on fire for.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>cause_fire</code></td><td>Boolean</td><td>If the initial shot should ignite flammable blocks it hits instead of a living entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>smelt_blocks</code></td><td>Boolean</td><td>If the initial shot should smelt the block it hits instead of a living entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>chain_count</code></td><td>Integer (&gt;= 0)</td><td>The maximum number of additional jumps after the initial hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3</td></tr><tr><td><code>chain_range</code></td><td>Float</td><td>How far, in blocks, from each impact point to search for the next chain target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8.0</td></tr><tr><td><code>can_hit_caster</code></td><td>Boolean</td><td>Whether a jump can pick the caster as its next target. The first shot never hits the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effects</code></td><td><em>Potion Hit Effect</em>,<br><em>Potion Hit Effect</em>[]</td><td>Applied, at full configured strength, to every entity hit by the chain (the initial hit and every jump). Same entry format as "potion_hit"'s "effects": effect, duration, amplifier*, max_amplifier* and particles*.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>A damage type ID such as "minecraft:magic" or one from a pack. Left unset, it is a player attack when a player uses this and a mob attack otherwise. Unknown types fall back to that.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects</code> (Potion Hit Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_amplifier</code></td><td>Integer</td><td>The highest level repeated hits can stack the effect up to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:blast_chain",
      "beam_renderer": "example:beam_renderer_id",
      "damage": 6,
      "damage_falloff": 0.85,
      "max_distance": 25,
      "speed": 2.5,
      "effects": {
        "effect": "minecraft:poison",
        "duration": 60,
        "max_amplifier": 3
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "blast_chain": {
          "type": "argon:blast_chain",
          "beam_renderer": "example:beam_renderer_id",
          "damage": 6,
          "damage_falloff": 0.85,
          "max_distance": 25,
          "speed": 2.5,
          "effects": {
            "effect": "minecraft:poison",
            "duration": 60,
            "max_amplifier": 3
          }
        }
      }
    }
    ```

---

### Blink {#argonblink}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:blink</code></div>

<div class="argon-desc">On activation, teleports you up to "distance" blocks along your look direction. Stops before solid blocks, and can pass through see-through ones like glass ("allow_see_through").</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>distance</code></td><td>(Dynamic) Value</td><td>The maximum distance, in blocks, the user is teleported.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>allow_see_through</code></td><td>Boolean</td><td>Whether see-through solid blocks (glass etc.) are passed through instead of stopping the teleport.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>safe</code></td><td>Boolean</td><td>If true, the blink fails (nothing happens) when the destination is inside blocks, in or over lava, fire or magma, cactus, or over the void.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>respect_protection</code></td><td>Boolean</td><td>If true, the blink fails when a player user could not interact with the destination blocks (spawn protection, claim mods).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>particles</code></td><td><em>Particle Effect</em>[]</td><td>Optional particle effects played at the user's start and end positions in list order, skipped if the user doesn't actually move, where each entry is a full particle options object with an optional world-space offset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>particles[]</code> (Particle Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>particle</code></td><td>Particle</td><td>The particle to spawn.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (&gt;= 0)</td><td>How many particles spawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Double</td><td>How far the particles spread from the origin.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>Offset from the origin in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:blink",
      "distance": 20,
      "properties": {
        "title": "Blink"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:blink",
      "distance": 10,
      "allow_see_through": false,
      "particles": [
        {
          "particle": {
            "type": "minecraft:portal"
          },
          "count": 30
        },
        {
          "particle": {
            "type": "minecraft:cloud"
          },
          "count": 30,
          "offset": [
            0,
            1,
            0
          ]
        }
      ],
      "properties": {
        "title": "Blink"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "blink": {
          "type": "argon:blink",
          "distance": 20,
          "properties": {
            "title": "Blink"
          }
        }
      }
    }
    ```

---

### Block Energy {#argonblock_energy}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:block_energy</code></div>

<div class="argon-desc">While enabled, drains RF from or adds RF to the block you look at, every tick, as long as it is within range and exposes an energy storage. With an energy_bar the drained RF fills that bar and added RF is taken from it, otherwise the RF is simply removed from or created in the block.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td>String</td><td>"drain" pulls RF out of the block, "add" pushes RF into it, "toggle" adds while the user is sneaking and drains otherwise.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">drain</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far away, in blocks, the block can be.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8</td></tr><tr><td><code>rate</code></td><td>(Dynamic) Value</td><td>The most RF moved per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>energy_bar</code></td><td>String</td><td>An energy bar, as "power#bar_name". Drained RF fills it and added RF is spent from it. Left unset, no bar is used and the energy is unlimited.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:block_energy",
      "mode": "drain",
      "range": 8,
      "rate": 200,
      "energy_bar": "example:power#energy"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "block_energy": {
          "type": "argon:block_energy",
          "mode": "drain",
          "range": 8,
          "rate": 200,
          "energy_bar": "example:power#energy"
        }
      }
    }
    ```

---

### Block Scan {#argonblock_scan}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:block_scan</code></div>

<div class="argon-desc">While enabled, shows a panel next to the crosshair for the block you look at: active or powered, energy, fluids, items, connections, damage and readable text. Only what the game exposes is shown.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far away, in blocks, a block can be read from.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8</td></tr><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>Limit the scan to these blocks, given as explicit block IDs, a tag ("#namespace:tag"), or a mix of both. Left unset, any block that has something to read is scanned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>show_status</code></td><td>Boolean</td><td>Show whether the block is active (lit / enabled / powered) and the redstone signal it receives.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_energy</code></td><td>Boolean</td><td>Show stored energy and capacity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_fluids</code></td><td>Boolean</td><td>Show the fluids stored in the block's tanks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_items</code></td><td>Boolean</td><td>Show how full the block's inventory is and the main items in it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_connections</code></td><td>Boolean</td><td>Show which neighbouring blocks it connects to (they have energy, fluid or item storage facing it).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_damage</code></td><td>Boolean</td><td>Show damage the block's state reports (chipped / damaged anvils, cracked blocks).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_info</code></td><td>Boolean</td><td>Show readable information the block carries (a sign's text, a command block's command).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:block_scan",
      "range": 8,
      "blocks": [
        "#c:machines"
      ],
      "show_items": false
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "block_scan": {
          "type": "argon:block_scan",
          "range": 8,
          "blocks": [
            "#c:machines"
          ],
          "show_items": false
        }
      }
    }
    ```

---

### Body Glow {#argonbody_glow}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:body_glow</code></div>

<div class="argon-desc">While enabled, the whole entity (skin, worn armor and layers) gets a glowing tint everyone can see. With an animation_timer the glow fades in and out.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The glow color.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>opacity</code></td><td>Float</td><td>How strong the glow is at its peak, from 0 to 1.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:body_glow",
      "color": "#ffd24a"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "body_glow": {
          "type": "argon:body_glow",
          "color": "#ffd24a"
        }
      }
    }
    ```

---

### Calm {#argoncalm}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:calm</code></div>

<div class="argon-desc">While enabled, looking at an eligible mob long enough calms it. It gets a calm effect and a lockout effect that stops it being calmed again for a while. Owned, already calmed or locked out mobs are skipped.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far away the mob can be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6.0</td></tr><tr><td><code>hold_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the user has to keep looking at the same mob.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60</td></tr><tr><td><code>entity_tag</code></td><td>Entity Type ID(s) / Tag</td><td>Only mobs in this tag can be calmed. Leave it out to allow every mob.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>excluded_tags</code></td><td>Entity Type ID(s) / Tag</td><td>Mobs in any of these tags can never be calmed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>calm_effect</code></td><td>Mob Effect ID</td><td>The effect that calms the mob.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">argon:calmed</td></tr><tr><td><code>calm_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the calm effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">400</td></tr><tr><td><code>lockout_effect</code></td><td>Mob Effect ID</td><td>The effect that stops the mob from being calmed again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">argon:calm_lockout</td></tr><tr><td><code>lockout_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the lockout lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1200</td></tr></tbody></table></div>

---

### Carry {#argoncarry}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:carry</code></div>

<div class="argon-desc">While enabled, grabs the living entity you look at and holds it on a damped spring at an attachment point. It lags and swings as you move but never goes past "maximum_distance". Disabling lets go.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far away, in blocks, a target can be grabbed from.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attachment</code></td><td>Vector 3D,<br><code>right_shoulder</code><br><code>left_shoulder</code><br><code>right_hand</code><br><code>left_hand</code><br><code>chest</code><br><code>above_head</code><br><code>main_hand</code><br><code>off_hand</code><br><code>main_shoulder</code><br><code>off_shoulder</code></td><td>Where the carried entity is drawn toward, in the wearer's frame (x right, y up from the feet, z forward): an [x, y, z] offset, or right_shoulder, left_shoulder, right_hand, left_hand, chest, above_head, or main/off_hand and main/off_shoulder by the wearer's main arm.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">right_shoulder</td></tr><tr><td><code>preferred_distance</code></td><td>Double</td><td>Radius around the attachment point inside which the target is held only loosely.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>maximum_distance</code></td><td>Double</td><td>Radius around the attachment point the target can never leave (a wall can still push it past this).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>stiffness</code></td><td>Double</td><td>Spring strength pulling the target to the attachment point.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.2</td></tr><tr><td><code>damping</code></td><td>Double</td><td>How strongly the target's motion relative to you is resisted. Higher settles faster, lower swings longer.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>gravity_influence</code></td><td>Double</td><td>How much normal gravity acts on the target, so it hangs below you when not pulled up. 0 is none, 1 is full.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>inertia</code></td><td>Double</td><td>The target's mass. Spring and damping are divided by it, so higher means more lag and swing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>follow_strength</code></td><td>Double</td><td>How much of each change in your velocity is passed straight to the target. 0 means only the spring moves it, 1 means it follows exactly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.35</td></tr><tr><td><code>acquire_ticks</code></td><td>Integer</td><td>Most ticks the initial pull-in lasts before normal carry physics takes over.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>target_collision</code></td><td>Boolean</td><td>Whether the carried entity is kept out of walls. If a block is in the way it is pulled back along the line from you instead of going through it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>preserve_release_velocity</code></td><td>Boolean</td><td>Whether the target keeps its velocity when let go, rather than stopping dead.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>allow_mobs</code></td><td>Boolean</td><td>Whether non-player entities can be grabbed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>allow_players</code></td><td>Boolean</td><td>Whether players can be grabbed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>visual_tilt</code></td><td>Double</td><td>How much the carried entity pitches and rolls with the sway when drawn. 0 keeps it upright, 1 is as calculated, higher exaggerates, negative tilts the other way.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>arm_pose</code></td><td>Boolean</td><td>Whether your arm on the attachment side aims at the carried entity automatically (both arms for a centered attachment). Turn it off to animate the arms yourself with the argon.carry_* queries.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>safe_release</code></td><td>Boolean</td><td>Whether the released entity takes no fall damage from its next fall.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>excluded_tags</code></td><td>Entity Type ID(s) / Tag</td><td>Entity types in any of these tags can never be grabbed, for example #c:bosses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_width</code></td><td>Double</td><td>Entities wider than this many blocks can't be grabbed. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max_height</code></td><td>Double</td><td>Entities taller than this many blocks can't be grabbed. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max_health</code></td><td>Double</td><td>Entities with more max health than this can't be grabbed. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max_duration</code></td><td>Integer</td><td>The carry lets go on its own after this many ticks. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>player_duration_multiplier</code></td><td>Double</td><td>Multiplies max_duration when the carried entity is a player, so players can be held for a shorter time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:carry",
      "range": 3
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "carry": {
          "type": "argon:carry",
          "range": 3
        }
      }
    }
    ```

---

### Chat Color {#argonchat_color}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:chat_color</code></div>

<div class="argon-desc">While enabled, recolors every chat message the user sends to one fixed color.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color of the user's chat text, as a hex string (e.g. "#FF0000") or a named color (e.g. "red").</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:chat_color",
      "color": "#ff0000",
      "properties": {
        "title": "Chat Color"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "chat_color": {
          "type": "argon:chat_color",
          "color": "#ff0000",
          "properties": {
            "title": "Chat Color"
          }
        }
      }
    }
    ```

---

### Clone {#argonclone}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:clone</code></div>

<div class="argon-desc">Summons clones of the user that copy their look and gear and fight beside them. At max_active, activating dismisses the oldest clone instead.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>summon_count</code></td><td>(Dynamic) Value</td><td>How many clones to summon per activation.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>max_active</code></td><td>(Dynamic) Value</td><td>How many clones can exist at once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>max_total</code></td><td>(Dynamic) Value</td><td>Lifetime cap on clones summoned, ignoring dismissed ones. Unlimited if unset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>clone_modifiers</code></td><td><em>Clone Modifier</em>[]</td><td>Applied in order to every clone. Clones start with the user's max health, attack damage and movement speed. Each stat is a value (multiplier) or {"amount": value, "operation": "multiply" / "add" / "set"}. "powers" lists power ids to give the clone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>show_name</code></td><td>Boolean</td><td>Whether clones get the user's name as a floating name tag. When false they have no name at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

    <p class="argon-nested"><code>clone_modifiers[]</code> (Clone Modifier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>health</code></td><td>(Dynamic) Value,<br><em>Stat Modifier</em></td><td>Changes the clone's maximum health.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attack_damage</code></td><td>(Dynamic) Value,<br><em>Stat Modifier</em></td><td>Changes the clone's attack damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>movement_speed</code></td><td>(Dynamic) Value,<br><em>Stat Modifier</em></td><td>Changes the clone's movement speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>powers</code></td><td>Power ID(s) / Tag</td><td>The powers the clone gets.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>clone_modifiers[].health</code> (Stat Modifier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>amount</code></td><td>(Dynamic) Value</td><td>The amount to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>operation</code></td><td><code>multiply</code><br><code>add</code><br><code>set</code></td><td>How the amount is applied to the stat of the original.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:clone",
      "summon_count": 1,
      "max_active": 1,
      "properties": {
        "title": "Clone"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:clone",
      "summon_count": 2,
      "max_active": 4,
      "max_total": 10,
      "show_name": false,
      "clone_modifiers": [
        {
          "health": 0.5,
          "attack_damage": {
            "amount": 2,
            "operation": "add"
          },
          "movement_speed": 2.5,
          "powers": [
            "example:clone_power"
          ]
        }
      ]
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:clone",
      "summon_count": {
        "type": "palladium:integer_data_attachment",
        "attachment": "example:clone_level",
        "fallback": 1
      },
      "max_active": 6,
      "clone_modifiers": [
        {
          "health": {
            "amount": {
              "type": "palladium:integer_data_attachment",
              "attachment": "example:clone_level",
              "fallback": 1
            },
            "operation": "multiply"
          }
        },
        {
          "attack_damage": {
            "amount": 6,
            "operation": "set"
          }
        },
        {
          "powers": [
            "example:clone_power_a",
            "example:clone_power_b"
          ]
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "clone": {
          "type": "argon:clone",
          "summon_count": 1,
          "max_active": 1,
          "properties": {
            "title": "Clone"
          }
        }
      }
    }
    ```

---

### Clone Remove {#argonclone_remove}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:clone_remove</code></div>

<div class="argon-desc">Dismisses some of the user's active clones. Doesn't refund the total clone limit.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>order</code></td><td><code>sequential</code><br><code>nearest</code><br><code>furthest</code></td><td>Which clones go first: oldest summoned, closest to the user, or furthest from the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SEQUENTIAL</td></tr><tr><td><code>count</code></td><td>(Dynamic) Value</td><td>How many clones to dismiss per activation.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:clone_remove",
      "count": 1,
      "properties": {
        "title": "Clone Remove"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:clone_remove",
      "order": "nearest",
      "count": 2
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:clone_remove",
      "order": "furthest",
      "count": {
        "type": "palladium:integer_data_attachment",
        "attachment": "example:clones_per_dismiss",
        "fallback": 1
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "clone_remove": {
          "type": "argon:clone_remove",
          "count": 1,
          "properties": {
            "title": "Clone Remove"
          }
        }
      }
    }
    ```

---

### Collision Attack {#argoncollision_attack}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:collision_attack</code></div>

<div class="argon-desc">While enabled and moving faster than "min_speed", every living entity the user runs into takes damage and is knocked away along the user's direction of travel. Damage and knockback grow with how far the speed is above "min_speed". Each target can only be hit again after "hit_cooldown" ticks. Allied entities, the user's vehicle and passengers are skipped.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min_speed</code></td><td>Double</td><td>Horizontal speed in blocks per second the user has to exceed before anything is hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20.0</td></tr><tr><td><code>damage</code></td><td>Double</td><td>Damage dealt at exactly min_speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr><tr><td><code>damage_per_speed</code></td><td>Double</td><td>Extra damage for every block per second above min_speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>knockback</code></td><td>Double</td><td>Knockback strength at exactly min_speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.8</td></tr><tr><td><code>knockback_per_speed</code></td><td>Double</td><td>Extra knockback strength for every block per second above min_speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.03</td></tr><tr><td><code>upward_knockback</code></td><td>Double</td><td>Upward velocity added to the target when it is hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>inflation</code></td><td>Double</td><td>How much the user's hitbox is grown, in blocks, when looking for entities to hit. The box is also stretched along the distance moved this tick so fast runs cannot skip over targets.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>hit_cooldown</code></td><td>Integer</td><td>Ticks before the same target can be hit again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>affect_players</code></td><td>Boolean</td><td>If false, other players are never hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>excluded_entities</code></td><td>Identifier[]</td><td>Entity types that are never hit, so the run passes straight through them. Defaults to minecraft:armor_stand and palladium:suit_stand.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hit_effects</code></td><td><em>Potion Hit Effect</em>,<br><em>Potion Hit Effect</em>[]</td><td>Effects applied to every target that is hit, for example bleeding.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>effects_min_speed</code></td><td>Double</td><td>Horizontal speed in blocks per second the user has to reach before hit_effects, hit_visuals and hit_sound are used. Slower hits only do damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>hit_visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle visuals spawned at every target that is hit, in the same format as the visuals of argon:energy_beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>visuals_require_blood</code></td><td>Boolean</td><td>If true, hit_visuals are skipped for entities in the argon:bloodless tag, so blood particles do not appear on things that cannot bleed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>hit_sound</code></td><td>Identifier</td><td>A sound event played at every target that is hit, instead of the default hit sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hit_sound_volume</code></td><td>Float</td><td>Volume of hit_sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>hit_sound_pitch</code></td><td>Float</td><td>Pitch of hit_sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.9</td></tr></tbody></table></div>

    <p class="argon-nested"><code>hit_effects</code> (Potion Hit Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_amplifier</code></td><td>Integer</td><td>The highest level repeated hits can stack the effect up to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>hit_visuals[]</code> (Beam Visual)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>streak</code><br><code>helix</code><br><code>ring</code><br><code>sphere</code><br><code>burst</code><br><code>crescent</code></td><td>The particle pattern to draw.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor</code></td><td><code>end</code><br><code>caster</code></td><td>Whether the pattern is drawn at the end of the beam or around the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>orientation</code></td><td><code>horizontal</code><br><code>vertical</code></td><td>How ring and crescent patterns are turned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>The particle used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 512)</td><td>How many particles the pattern uses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 64.0)</td><td>The radius of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>step</code></td><td>Float (0.05 ~ 16.0)</td><td>The spacing between particles along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch</code></td><td>Float (0.1 ~ 64.0)</td><td>The length of one full twist for helixes, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strands</code></td><td>Integer (1 ~ 8)</td><td>How many strands a helix has.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arc</code></td><td>Float (1.0 ~ 360.0)</td><td>How much of a circle is drawn, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float</td><td>The height of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rings</code></td><td>Integer (1 ~ 16)</td><td>How many rings are drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Float (0.0 ~ 8.0)</td><td>How far the particles scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:collision_attack",
      "properties": {
        "title": "Collision Attack"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "collision_attack": {
          "type": "argon:collision_attack",
          "properties": {
            "title": "Collision Attack"
          }
        }
      }
    }
    ```

---

### Color Cycle Glow {#argoncolor_cycle_glow}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:color_cycle_glow</code></div>

<div class="argon-desc">While enabled, gives the entity an outline that cycles through "colors" in order. It follows world time so everyone sees the same color. Independent of entity_glow and the Glowing effect. By default it is visible through walls, and the outline is a solid colour, so "intensity" dims it towards black.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>colors</code></td><td>Color[]</td><td>The ordered list of colors to cycle through and fade between; must contain at least one color.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rate</code></td><td>Integer (&gt; 0)</td><td>How many ticks (20 per second) each fade from one color to the next takes.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>intensity</code></td><td>Float / Value</td><td>(Dynamic) 0 to 1, how strong the outline is. The outline is always opaque, so this mixes the colour from faded_color (at 0) to the cycling colour (at 1), for example from an argon:power_age value.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>faded_color</code></td><td>Color</td><td>The colour the outline mixes towards as intensity drops to 0, black by default.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#000000</td></tr><tr><td><code>through_walls</code></td><td>Boolean</td><td>If false, the outline is only shown to viewers who have a clear line of sight to the entity, so it disappears behind blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:color_cycle_glow",
      "colors": [
        "#ff0000",
        "#00ff00",
        "#0000ff"
      ],
      "rate": 10,
      "intensity": 1
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "color_cycle_glow": {
          "type": "argon:color_cycle_glow",
          "colors": [
            "#ff0000",
            "#00ff00",
            "#0000ff"
          ],
          "rate": 10,
          "intensity": 1
        }
      }
    }
    ```

---

### Cooldown Control {#argoncooldown_control}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:cooldown_control</code></div>

<div class="argon-desc">While enabled, makes the listed key bind abilities recharge faster. It can also take time off the longest remaining cooldown whenever the user kills a qualifying entity.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>abilities</code></td><td>Ability Reference[]</td><td>The key bind abilities whose cooldowns are affected.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>recharge_multiplier</code></td><td>(Dynamic) Value</td><td>How fast cooldowns count down while enabled. 1 is normal, 1.5 is half again as fast.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>on_kill</code></td><td><em>Cooldown Kill</em></td><td>On a kill, takes reduce ticks off the longest remaining cooldown among the listed abilities. The victim must be hostile (unless hostile_only is false) and, if any of entity_tag, beneficial_effect (it has a beneficial effect) or power (it owns a matching power) is given, match at least one of them.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>on_kill</code> (Cooldown Kill)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>reduce</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How much cooldown a kill removes.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hostile_only</code></td><td>Boolean</td><td>Only hostile mobs count.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entity_tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag count.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>beneficial_effect</code></td><td>Boolean</td><td>Only entities with a beneficial effect count.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>power</code></td><td><em>Power Requirement</em></td><td>Only entities that match this power requirement count.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>on_kill.power</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:cooldown_control",
      "abilities": [],
      "recharge_multiplier": 1.4
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "cooldown_control": {
          "type": "argon:cooldown_control",
          "abilities": [],
          "recharge_multiplier": 1.4
        }
      }
    }
    ```

---

### Damage {#argondamage}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:damage</code></div>

<div class="argon-desc">When activated, raycasts forward and deals a fixed amount of damage of a given damage type to the first living entity hit within range.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far forward the hit raycast reaches.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>Float</td><td>Damage dealt to the target, plus the user's attack damage attribute if apply_user_damage is true.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type the damage is dealt as.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>apply_user_damage</code></td><td>Boolean</td><td>If true, adds the user's current attack damage attribute (with equipment and effects) on top of "damage".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:damage",
      "range": 6,
      "damage": 5,
      "damage_type": "minecraft:generic"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "damage": {
          "type": "argon:damage",
          "range": 6,
          "damage": 5,
          "damage_type": "minecraft:generic"
        }
      }
    }
    ```

---

### Damage Field {#argondamage_field}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:damage_field</code></div>

<div class="argon-desc">While enabled, constantly deals damage of a given damage type to every living entity touching the user's hitbox (optionally inflated).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>inflation</code></td><td>(Dynamic) Value</td><td>How much to inflate the user's hitbox, in blocks, when looking for entities to hit. 0 is the exact hitbox.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>Damage dealt each tick to entities touching the field, plus the user's attack damage attribute if apply_user_damage is true.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type the damage is dealt as.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>apply_user_damage</code></td><td>Boolean</td><td>If true, adds the user's current attack damage attribute (with equipment and effects) on top of "damage" each tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:damage_field",
      "inflation": 0.5,
      "damage": 2,
      "damage_type": "minecraft:generic"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "damage_field": {
          "type": "argon:damage_field",
          "inflation": 0.5,
          "damage": 2,
          "damage_type": "minecraft:generic"
        }
      }
    }
    ```

---

### Damage Reaction {#argondamage_reaction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:damage_reaction</code></div>

<div class="argon-desc">While enabled, the first reaction matching an incoming hit changes it. It can scale or cancel damage, cancel knockback, hit the attacker back, give effects, and cut another ability's cooldown. argon:reacted can check the last reaction.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>reactions</code></td><td><em>Damage Reaction</em>[]</td><td>Checked in order, the first match wins. kind is "any", "melee" or "projectile"; min_damage is the smallest hit it applies to; damage_multiplier is how much of the damage still goes through (0 cancels the hit); counter_damage is a Value dealt back to a living attacker; attacker_effects and self_effects are lists of { effect*, duration, amplifier, particles }; cooldown_cap is { ability*, cap* } and lowers that key bind ability's remaining cooldown to at most cap.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reactions[]</code> (Damage Reaction)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>id</code></td><td>String</td><td>A name for the reaction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>kind</code></td><td><code>any</code><br><code>melee</code><br><code>projectile</code></td><td>Which kind of damage triggers the reaction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_damage</code></td><td>Float (&gt;= 0.0)</td><td>The damage has to be at least this much.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>damage_multiplier</code></td><td>Float (0.0 ~ 1.0)</td><td>Multiplies the damage taken.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>cancel_knockback</code></td><td>Boolean</td><td>Whether the knockback is cancelled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>counter_damage</code></td><td>(Dynamic) Value</td><td>Damage dealt back to the attacker.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attacker_effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to the attacker.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>self_effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>cooldown_cap</code></td><td><em>Cooldown Cap</em></td><td>Cuts down the cooldown of another ability.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reactions[].attacker_effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reactions[].attacker_effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reactions[].cooldown_cap</code> (Cooldown Cap)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The ability whose cooldown is capped.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>cap</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The cooldown is cut down to at most this long.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:damage_reaction",
      "reactions": []
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "damage_reaction": {
          "type": "argon:damage_reaction",
          "reactions": []
        }
      }
    }
    ```

---

### Damage Reduction {#argondamage_reduction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:damage_reduction</code></div>

<div class="argon-desc">While enabled, multiplies incoming damage (optionally only the given damage_types) by a percentage of the original. 0 blocks all damage, 100 leaves it unchanged.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>percentage</code></td><td>(Dynamic) Value</td><td>The percentage of the original damage the entity takes, e.g. 0 for none or 150 for 50% more. A Value, so it can scale with power age or other data.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_types</code></td><td>Damage Type ID(s) / Tag</td><td>Damage types (or tags) the percentage is limited to. Otherwise it applies to all incoming damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:damage_reduction",
      "percentage": 150,
      "damage_types": [
        "minecraft:on_fire",
        "minecraft:in_fire",
        "minecraft:lava"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "damage_reduction": {
          "type": "argon:damage_reduction",
          "percentage": 150,
          "damage_types": [
            "minecraft:on_fire",
            "minecraft:in_fire",
            "minecraft:lava"
          ]
        }
      }
    }
    ```

---

### Damage Scaling {#argondamage_scaling}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:damage_scaling</code></div>

<div class="argon-desc">While enabled, multiplies the damage the user deals (optionally only the given damage types). It can also make that damage ignore part of the victim's damage reduction.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>damage_types</code></td><td>Damage Type ID(s) / Tag</td><td>Damage types (or tags) the scaling is limited to. Otherwise it applies to all damage the user deals.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>multiplier</code></td><td>(Dynamic) Value</td><td>What outgoing damage is multiplied by, e.g. 1.15 for 15% more.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>resistance_ignore</code></td><td>Float</td><td>The fraction from 0 to 1 of the victim's damage reduction that is ignored for matching damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:damage_scaling",
      "multiplier": 1.2,
      "resistance_ignore": 0.1
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "damage_scaling": {
          "type": "argon:damage_scaling",
          "multiplier": 1.2,
          "resistance_ignore": 0.1
        }
      }
    }
    ```

---

### Danger Sense {#argondanger_sense}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:danger_sense</code></div>

<div class="argon-desc">While enabled, detects hostile mobs (and neutral ones targeting you) within "hostile_range" and players who recently damaged you. Can light the screen border toward each danger.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>hostile_range</code></td><td>(Dynamic) Value</td><td>How far to search for hostile mobs, checked fresh every scan. Also the glow's fade-in distance. A danger's glow eases from invisible at this range to full strength as it gets closer.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attacker_memory_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long after being damaged a player who dealt that damage still counts as a detected danger.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blacklist_powers</code></td><td>Power ID[]</td><td>Entities holding any of these powers never trigger danger sense, whether they're a nearby hostile mob or a recent attacker.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>show_visual</code></td><td>Boolean</td><td>If true, lights up the screen's border in the direction of each detected danger.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>glow_color</code></td><td>Color</td><td>The color of the screen-border glow, when "show_visual" is true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FF3333</td></tr><tr><td><code>glow_opacity</code></td><td>Float</td><td>The glow's peak opacity at its brightest point, from 0 (invisible) to 1 (fully opaque).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>glow_thickness</code></td><td>Float</td><td>How far the glow reaches inward from the screen's edge, in pixels.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">28.0</td></tr><tr><td><code>glow_spread</code></td><td>Float</td><td>How far, in pixels along the screen border, the glow spreads from its brightest point before fading out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">220.0</td></tr><tr><td><code>warn_projectiles</code></td><td>Boolean</td><td>If true, projectiles flying toward the holder (arrows, fireballs, tridents and the like, never the holder's own) count as dangers too and light the screen border like a mob would. Needs "show_visual" to be seen.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>projectile_range</code></td><td>(Dynamic) Value</td><td>How far to look for incoming projectiles when "warn_projectiles" is on.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">24.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:danger_sense",
      "hostile_range": 16,
      "attacker_memory_time": 100,
      "show_visual": true,
      "projectile_range": 24,
      "properties": {
        "title": "Danger Sense"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "danger_sense": {
          "type": "argon:danger_sense",
          "hostile_range": 16,
          "attacker_memory_time": 100,
          "show_visual": true,
          "projectile_range": 24,
          "properties": {
            "title": "Danger Sense"
          }
        }
      }
    }
    ```

---

### Dispel {#argondispel}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dispel</code></div>

<div class="argon-desc">On its first enabled tick, picks the ally or enemy the user looks at within range and removes effects from it, optionally healing it. With ally_or_self, the user is cleansed when no ally is targeted.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>target</code></td><td><code>ally</code><br><code>enemy</code><br><code>ally_or_self</code></td><td>Who can be targeted: "ally" (teammates, pets), "enemy", or "ally_or_self".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">ally</td></tr><tr><td><code>range</code></td><td>Double</td><td>How far away the target can be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>dispel</code></td><td><em>Dispel</em></td><td>Which effects are removed: category is "beneficial" or "harmful", count is how many (longest first), skip_bosses protects bosses.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>heal</code></td><td>(Dynamic) Value</td><td>Health restored to the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>dispel</code> (Dispel)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>category</code></td><td><code>beneficial</code><br><code>harmful</code></td><td>Which category of effects is removed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 64)</td><td>How many effects are removed at most.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>skip_bosses</code></td><td>Boolean</td><td>If true, boss mobs are not dispelled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dispel",
      "dispel": {
        "category": "harmful"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "dispel": {
          "type": "argon:dispel",
          "dispel": {
            "category": "harmful"
          }
        }
      }
    }
    ```

---

### Dive {#argondive}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dive</code></div>

<div class="argon-desc">While enabled, every tick sets the entity's downward speed to "speed" and keeps only part of its sideways speed, so it plunges toward the ground. Flight has to be ended by other conditions for this to take effect, and the landing impact and fall damage are handled by other abilities.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>speed</code></td><td>(Dynamic) Value</td><td>The downward speed, in blocks per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>horizontal_keep</code></td><td>Double</td><td>The fraction (0 to 1) of the sideways speed that is kept every tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dive",
      "speed": 2,
      "properties": {
        "title": "Dive"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "dive": {
          "type": "argon:dive",
          "speed": 2,
          "properties": {
            "title": "Dive"
          }
        }
      }
    }
    ```

---

### Dodge {#argondodge}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dodge</code></div>

<div class="argon-desc">On activation, launches the entity sideways toward its WASD input, or straight backward if no movement key is held.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>velocity_modifier</code></td><td>Float</td><td>The multiplier applied to the dodge direction when this ability activates.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>animation_ticks</code></td><td>Integer</td><td>How many ticks the dodge pose is held after activating, for animation purposes.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>flying_velocity_modifier</code></td><td>Float</td><td>The multiplier used instead of velocity_modifier while flying. Unset, it matches velocity_modifier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>flying_follow_look</code></td><td>Boolean</td><td>Whether a dodge while flying follows where the entity looks, including up and down, so it can be used to maneuver in the air. Otherwise it stays horizontal.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>ticks</code></td><td>Integer</td><td>If above 1, the dodge is a sustained burst: for this many ticks the sideways speed is set to velocity_modifier blocks per tick towards the chosen direction, so it covers about ticks times velocity_modifier blocks on the ground or in the air. It stops early on hitting a wall and afterwards the entity keeps its earlier speed. Not used while flying.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>idle_forward</code></td><td>Boolean</td><td>If true, the direction used when no movement key is held is straight forward instead of backward.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle visuals spawned around the entity when the dodge starts, in the same format as the visuals of argon:energy_beam. Use anchor caster to centre a ring on the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>visuals[]</code> (Beam Visual)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>streak</code><br><code>helix</code><br><code>ring</code><br><code>sphere</code><br><code>burst</code><br><code>crescent</code></td><td>The particle pattern to draw.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor</code></td><td><code>end</code><br><code>caster</code></td><td>Whether the pattern is drawn at the end of the beam or around the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>orientation</code></td><td><code>horizontal</code><br><code>vertical</code></td><td>How ring and crescent patterns are turned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>The particle used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 512)</td><td>How many particles the pattern uses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 64.0)</td><td>The radius of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>step</code></td><td>Float (0.05 ~ 16.0)</td><td>The spacing between particles along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch</code></td><td>Float (0.1 ~ 64.0)</td><td>The length of one full twist for helixes, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strands</code></td><td>Integer (1 ~ 8)</td><td>How many strands a helix has.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arc</code></td><td>Float (1.0 ~ 360.0)</td><td>How much of a circle is drawn, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float</td><td>The height of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rings</code></td><td>Integer (1 ~ 16)</td><td>How many rings are drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Float (0.0 ~ 8.0)</td><td>How far the particles scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dodge",
      "velocity_modifier": 1.5
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "dodge": {
          "type": "argon:dodge",
          "velocity_modifier": 1.5
        }
      }
    }
    ```

---

### Dome {#argondome}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dome</code></div>

<div class="argon-desc">When enabled, creates a dome of air around the user. While it lasts, the user, their team and pets inside take less physical damage and projectiles from anyone else bounce off. Hostile mobs inside are pushed out.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>The radius of the dome in blocks, read once when it is created, so it can scale with power age.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the dome lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">200</td></tr><tr><td><code>damage_reduction</code></td><td>Float</td><td>The fraction from 0 to 1 of melee and projectile damage removed for those protected inside.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>deflect_projectiles</code></td><td>Boolean</td><td>Whether projectiles that are not from the user's allies bounce off the dome.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>protect_all_players</code></td><td>Boolean</td><td>Whether every player inside is protected instead of only the user's team.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>repel</code></td><td>Float</td><td>How hard hostile mobs inside the dome are pushed out each tick. 0 disables it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.25</td></tr><tr><td><code>color</code></td><td>Color</td><td>The colour of the dome.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#cfeeff</td></tr><tr><td><code>follow_user</code></td><td>Boolean</td><td>If true, the dome moves with the user while it lasts instead of staying where it was cast. It ends early if the user is gone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>end_with_ability</code></td><td>Boolean</td><td>If true, the dome ends as soon as this ability is no longer enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>quiet</code></td><td>Boolean</td><td>If true, the dome makes no sound and spawns no gust or poof particles, so it is only the shell. Combine with damage_reduction 0, deflect_projectiles false and repel 0 for a purely visual dome.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dome",
      "radius": 6
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "dome": {
          "type": "argon:dome",
          "radius": 6
        }
      }
    }
    ```

---

### Dragon Rays {#argondragon_rays}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dragon_rays</code></div>

<div class="argon-desc">While enabled, renders the light rays the ender dragon flashes as it dies, anchored to the entity, in a hex color of your choice instead of vanilla's magenta.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color of the rays, as a hex string (e.g. "#6dffff"). Defaults to vanilla's magenta.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">16711935</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dragon_rays",
      "color": "#6dffff"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "dragon_rays": {
          "type": "argon:dragon_rays",
          "color": "#6dffff"
        }
      }
    }
    ```

---

### Drown {#argondrown}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:drown</code></div>

<div class="argon-desc">Makes each configured target, the user or every entity within range, lose oxygen as if drowning.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>targets</code></td><td><em>Drown Target</em>,<br><em>Drown Target</em>[]</td><td>Who this ability forces to drown, each entry either {"type": "self"} or {"type": "range", "range": <value>}. A single entry may be given without the list, and an entry with no range may be just its type ("self").</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;Target[mode=SELF, range=net.threetag.palladium.logic.value.StaticValue@6b37cadf]&quot; ]</td></tr><tr><td><code>drain_percentage</code></td><td>Double</td><td>How fast targets lose breath as a percentage of vanilla drowning. 100 is unchanged, 200 is twice as fast. The highest value wins if several Drown abilities hit one entity. Match palladium:breath's "max_air_percentage" to keep the vanilla time with a bigger breath.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr><tr><td><code>bubbles</code></td><td>Boolean</td><td>Whether bubbles rise round the head of each target while they are drowned. Set it to false for a drain that should not show. If several Drown abilities target the same entity, the bubbles show if any of them has this on.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

    <p class="argon-nested"><code>targets</code> (Drown Target)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>type</code></td><td><code>self</code><br><code>range</code></td><td>Whether the user or entities in range drown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The range in blocks when the type is range.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:drown",
      "properties": {
        "title": "Drown"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:drown",
      "targets": [
        {
          "type": "range",
          "range": 16
        }
      ],
      "properties": {
        "title": "Drown"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "drown": {
          "type": "argon:drown",
          "properties": {
            "title": "Drown"
          }
        }
      }
    }
    ```

---

### Earthquake {#argonearthquake}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:earthquake</code></div>

<div class="argon-desc">On activation, launches nearby ground blocks up and outward as falling blocks in a staggered ripple from the user. Never touches the block directly beneath them.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The horizontal radius, in blocks, around the user that can be affected.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strength</code></td><td>(Dynamic) Value</td><td>The launch velocity (blocks/tick) of each affected block, both up and outward from the user.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ticks_per_block</code></td><td>Double</td><td>Ticks of delay added per block of distance from the user. Higher spreads the ripple out more slowly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>vertical_search</code></td><td>Integer</td><td>How many blocks above and below the user's feet to search, per column, for the first block to launch.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2</td></tr><tr><td><code>disable_movement</code></td><td>Boolean</td><td>If true, sets the user's movement_speed and jump_strength to zero while the ripple is still playing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:earthquake",
      "range": 8,
      "strength": 0.6
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "earthquake": {
          "type": "argon:earthquake",
          "range": 8,
          "strength": 0.6
        }
      }
    }
    ```

---

### Effect {#argoneffect}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:effect</code></div>

<div class="argon-desc">While enabled, applies status effects from a list of applications. Each one hits either every living entity in a radius ("area") or the one you look at ("target"), optionally filtered by powers.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>applications</code></td><td><em>Effect Application</em>[]</td><td>Each entry configures its own effect, duration, amplifier*, particles*, mode* ("area" or "target", default "area"), range, affect_self* (area only, default true), powers* (a list of {power, mode} entries - "include" requires that power, "exclude" forbids it), and targets* ("all", "players" or "mobs", default "all") - all entries are applied every tick the ability is enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>applications[]</code> (Effect Application)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>area</code><br><code>target</code></td><td>Whether the effect hits everything in range (area) or only the looked-at target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>Double</td><td>The range in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>affect_self</code></td><td>Boolean</td><td>Whether the user gets the effect too.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>powers</code></td><td><em>Power Requirement</em>,<br><em>Power Requirement</em>[]</td><td>Only entities that match these power requirements get the effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>targets</code></td><td><code>all</code><br><code>players</code><br><code>mobs</code></td><td>Which kinds of entities can be affected.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>applications[].powers</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:effect",
      "applications": [
        {
          "effect": "minecraft:regeneration",
          "duration": 100,
          "amplifier": 1,
          "particles": false,
          "range": 6
        },
        {
          "mode": "target",
          "effect": "minecraft:weakness",
          "duration": 100,
          "range": 10
        }
      ]
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:effect",
      "applications": [
        {
          "mode": "area",
          "effect": "minecraft:regeneration",
          "duration": "5s",
          "amplifier": 1,
          "range": 6,
          "powers": [
            {
              "power": "example:ally_power",
              "mode": "include"
            },
            {
              "power": "example:hostile_power",
              "mode": "exclude"
            }
          ]
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "effect": {
          "type": "argon:effect",
          "applications": [
            {
              "effect": "minecraft:regeneration",
              "duration": 100,
              "amplifier": 1,
              "particles": false,
              "range": 6
            },
            {
              "mode": "target",
              "effect": "minecraft:weakness",
              "duration": 100,
              "range": 10
            }
          ]
        }
      }
    }
    ```

---

### Energy Bar Color {#argonenergy_bar_color}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:energy_bar_color</code></div>

<div class="argon-desc">While enabled, draws one of the power's energy bars in a different color, easing in and out. Put the conditions in the ability's state. Only changes the wearer's own screen.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>energy_bar</code></td><td>String</td><td>The energy bar to recolor, as "power#bar_name".</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>color</code></td><td>Color</td><td>The color to draw the bar in while this ability is enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>priority</code></td><td>Integer</td><td>When several of these are enabled for one bar, the highest priority is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>blend</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the bar takes to slide to this color (and, once this stops applying, back).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:energy_bar_color",
      "energy_bar": "example:power#bar",
      "color": "#00ff00"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "energy_bar_color": {
          "type": "argon:energy_bar_color",
          "energy_bar": "example:power#bar",
          "color": "#00ff00"
        }
      }
    }
    ```

---

### Energy Beam {#argonenergy_beam}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:energy_beam</code></div>

<div class="argon-desc">Shoots a beam that can bounce off blocks. On hitting a matching entity it can redirect onward or spread into several beams once. Applies damage, fire and smelting along its path.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The id of the beam renderer to use.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>Damage dealt to every entity the beam hits. A value, so it can follow a data attachment to scale with a level.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>max_distance</code></td><td>(Dynamic) Value</td><td>Total distance the beam can travel across all its bounces. A value, so it can follow a data attachment to scale with a level.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">30</td></tr><tr><td><code>max_bounces</code></td><td>Integer (&gt;= 0)</td><td>Most times the beam can bounce off blocks or entities (a spread counts as one) before stopping at its next hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>set_on_fire_ticks</code></td><td>Integer</td><td>How many ticks the beam sets a hit entity on fire for.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>cause_fire</code></td><td>Boolean</td><td>Whether the beam ignites flammable blocks it touches.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>smelt_blocks</code></td><td>Boolean</td><td>Whether the beam smelts every block it touches.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>redirect_off_blocks</code></td><td>Boolean</td><td>Whether the beam bounces off blocks instead of stopping at them. When false, only 'entity_reaction' can redirect it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>entity_reaction</code></td><td><code>none</code><br><code>redirect</code><br><code>spread</code></td><td>What happens when the beam hits an entity matching 'entity_bounce_condition': continue, redirect, or spread into multiple beams.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">NONE</td></tr><tr><td><code>entity_bounce_condition</code></td><td>Condition,<br>Condition[]</td><td>A condition limiting which hit entities can redirect or spread the beam. Ignored when 'entity_reaction' is 'none', otherwise defaults to all entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread_count</code></td><td>Integer (&gt; 0)</td><td>Number of beams the spread effect bursts into when 'entity_reaction' is 'spread'.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5</td></tr><tr><td><code>spread_angle</code></td><td>Float</td><td>Angle in degrees the spread beams fan out from the central reflected direction when 'entity_reaction' is 'spread'.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">25.0</td></tr><tr><td><code>cone</code></td><td><em>Cone</em></td><td>Makes damage, fire, smelting and block mode reach across a cone instead of a line. Widths in blocks at the eyes ("start_size", 0.1) and at "end_distance" (default "max_distance"); "rays" (1-128, default 24) finds blocks. Pair with the argon:cone renderer.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>knockback</code></td><td>(Dynamic) Value</td><td>How hard the beam pushes living entities away from the caster. 1 is firm, 5 is a gale, 0 is none. Knockback resistance weakens it. A value, so it can follow a data attachment to scale with a level.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>knockback_ignores_resistance</code></td><td>Boolean</td><td>Whether "knockback" ignores the target's knockback resistance.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>block_mode</code></td><td><em>Block Mode</em></td><td>What the beam does to blocks it hits: "type" is "melt" or "freeze", with "time" (default 60 ticks), "auto_time", "speed_multiplier", "modifiers", "conversions" and "particle"; freeze adds "frozen_time", "slippery", "friction" and "snow_layers". See the examples.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>charge</code></td><td><em>Beam Charge</em></td><td>Turns the beam into a charged shot: hold the ability to charge and release to fire. Releasing before "min_time" (default 10) fires nothing and the charge is full at "max_time" (default 40), eased by "curve" (linear, ease_in, ease_out, ease_in_out). The beam then shows for "fire_time" (default 8), and with a "taper" from 0 to 1 it appears at full length and narrows to nothing over that fraction of the end of that time instead of retracting, and "grow" (default 0.15) is the fraction of the start over which it widens from nothing to full size. "shots" (default 1) fires that many shots "shot_interval" ticks apart (default 4), each aimed where you look at that moment, and "ignore_hit_immunity" lets every shot damage the same target. Each of the other settings is a { min, max } range used for damage, range, knockback and the amplifier and duration of the entity effects, from no charge to full charge. See the charged beam example.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pierce</code></td><td>Boolean</td><td>Whether the beam passes through every entity in its way and hits all of them, stopping only at a block or its max_distance.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>pierce_limit</code></td><td>Integer (&gt;= 0)</td><td>With pierce, the most entities the beam passes through: it ends at the last one. 0 is no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>pierce_full_charge_only</code></td><td>Boolean</td><td>With pierce and a charge, only a fully charged shot passes through entities; weaker shots stop at the first one.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>pierce_size</code></td><td><em>Pierce Size</em></td><td>With pierce, how far in blocks the beam's reach extends sideways (width) and up and down (height) around the line, so a wide flat or tall thin slash can hit entities beside its path. Default 0.3 for both.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>knockback_distance</code></td><td>(Dynamic) Value</td><td>How far, in blocks, hit living entities are launched away from the caster (or the impact point), instead of the "knockback" strength. Knockback resistance weakens it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lift</code></td><td>(Dynamic) Value</td><td>Upward launch speed added by "knockback_distance" (0.4 is roughly a block and a half).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>airborne_lift</code></td><td>(Dynamic) Value</td><td>Upward launch speed used instead of "lift" while the caster is not on the ground.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lateral_pull</code></td><td>(Dynamic) Value</td><td>How far, in blocks, hit living entities are pulled sideways across the look direction toward the aim line, on top of any knockback. Knockback resistance weakens it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>armor_penetration</code></td><td>Float</td><td>The fraction from 0 to 1 of a hit entity's armor ignored by the damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>heavy_armor</code></td><td><em>Heavy Armor</em></td><td>Adds "bonus" damage to hit entities whose armor value is at least "threshold".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>impact</code></td><td><em>Impact</em></td><td>Makes the beam burst where it ends: every living entity within "radius" blocks of that point is hit instead of the entities on the line, launched away from the point, with damage reduced by up to "falloff" (0 to 1) at the edge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle effects spawned when the beam fires, for beams that should look like air or smoke instead of a laser. "shape" is "streak" (particles along the beam every "step" blocks with "spread" jitter), "helix" ("strands" spirals of "radius" and "pitch" along the beam), "ring" ("rings" rings up to "radius" with "count" particles each, only "arc" degrees facing forward if under 360), "sphere" ("count" particles on a sphere of "radius") or "burst" (the same, filled). "crescent" draws crescent-shaped arcs of "count" particles along the beam every "step" blocks, spanning "arc" degrees (150 by default), sideways or up and down by "orientation" ("horizontal" or "vertical"). "anchor" is "end" (where the beam ends, default) or "caster" for rings, "height" raises them, and "speed" sends the particles along the beam or outward.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entity_effects</code></td><td><em>Beam Effect</em>[]</td><td>Mob effects given to every living entity the beam hits. Duration is ticks or a time like "5s" (default 5s), amplifier 0 is level one, particles defaults to false.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>Damage type ID the damage is dealt as. Unset, it is a player attack for players and a mob attack otherwise.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type_overrides</code></td><td><em>Damage Type Override</em>[]</td><td>Damage types used instead of "damage_type" while their condition is true. Checked in order, first match wins. See the damage type overrides example.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>cone</code> (Cone)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>start_size</code></td><td>Float (0.0 ~ 64.0)</td><td>The width of the cone at the origin, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>end_size</code></td><td>Float (0.0 ~ 64.0)</td><td>The width of the cone at its far end, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>end_distance</code></td><td>Float (0.01 ~ 512.0)</td><td>The distance in blocks at which the cone reaches its end size.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rays</code></td><td>Integer (1 ~ 128)</td><td>How many rays are cast to cover the cone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_mode</code> (Block Mode)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>type</code></td><td><code>melt</code><br><code>freeze</code></td><td>Whether blocks hit by the beam melt or freeze.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long a block takes to change.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60</td></tr><tr><td><code>auto_time</code></td><td>Boolean</td><td>If true, the time is worked out from the block instead of using a fixed value.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>auto_min_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The shortest automatic time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>auto_max_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The longest automatic time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">200</td></tr><tr><td><code>speed_multiplier</code></td><td>(Dynamic) Value</td><td>Multiplies how fast blocks change.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>modifiers</code></td><td><em>Time Modifier</em>[]</td><td>Changes the time for specific blocks or limits the effect to them.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>conversions</code></td><td><em>Block Conversion</em>[]</td><td>Converts specific blocks into other blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td><em>Particle Effect</em></td><td>Particles shown on the changed blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>frozen_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long frozen blocks stay frozen (freeze only).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">200</td></tr><tr><td><code>frozen_time_multiplier</code></td><td>(Dynamic) Value</td><td>Multiplies the frozen time (freeze only).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slippery</code></td><td>Boolean</td><td>Whether frozen blocks are slippery (freeze only).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>friction</code></td><td>Float (0.0 ~ 1.0)</td><td>The slipperiness of frozen blocks (freeze only).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.989</td></tr><tr><td><code>snow_layers</code></td><td><em>Snow Layers</em></td><td>Snow that builds up on frozen blocks (freeze only).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_mode.modifiers[]</code> (Time Modifier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>type</code></td><td><code>whitelist</code><br><code>blacklist</code></td><td>A whitelist only affects the listed blocks, a blacklist leaves them out.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The blocks this entry covers.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Overrides the time for these blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_mode.conversions[]</code> (Block Conversion)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The blocks that are converted.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>result</code></td><td>Identifier</td><td>The block they turn into.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>revert</code></td><td>Boolean</td><td>Whether the block changes back afterwards.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_mode.particle</code> (Particle Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>particle</code></td><td>Particle</td><td>The particle to spawn.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (&gt;= 0)</td><td>How many particles spawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Double</td><td>How far the particles spread from the origin.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>Offset from the origin in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_mode.snow_layers</code> (Snow Layers)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>max</code></td><td>Integer (0 ~ 8)</td><td>The most snow layers that can build up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>time_per_layer</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long one layer stays.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The delay between new layers.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr></tbody></table></div>

    <p class="argon-nested"><code>charge</code> (Beam Charge)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The shortest charge that still fires.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The charge time at which the beam is at full power.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fire_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the beam keeps firing after the charge is released.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8</td></tr><tr><td><code>taper</code></td><td>Float (0.0 ~ 1.0)</td><td>How much the beam thins out over its firing time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>grow</code></td><td>Float (0.0 ~ 1.0)</td><td>How much the beam swells at the start of firing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.15</td></tr><tr><td><code>shots</code></td><td>Integer (1 ~ 64)</td><td>How many shots a single charge releases.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>shot_interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The delay between shots.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ignore_hit_immunity</code></td><td>Boolean</td><td>If true, every shot can hurt even while the target is invulnerable from a previous hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>curve</code></td><td><code>linear</code><br><code>ease_in</code><br><code>ease_out</code><br><code>ease_in_out</code></td><td>How the charge amount maps onto the ranges below.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td><em>Charge Range</em></td><td>Scales the damage with the charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_distance</code></td><td><em>Charge Range</em></td><td>Scales the beam length with the charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>knockback</code></td><td><em>Charge Range</em></td><td>Scales the knockback with the charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effect_amplifier</code></td><td><em>Charge Range</em></td><td>Scales the effect level with the charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effect_duration</code></td><td><em>Charge Time Range</em></td><td>Scales the effect duration with the charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>charge.damage</code> (Charge Range)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Float</td><td>The value at the shortest charge.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max</code></td><td>Float</td><td>The value at a full charge.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>charge.effect_duration</code> (Charge Time Range)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The duration at the shortest charge.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The duration at a full charge.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>pierce_size</code> (Pierce Size)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>width</code></td><td>Float (0.0 ~ 16.0)</td><td>The width of the piercing area in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float (0.0 ~ 16.0)</td><td>The height of the piercing area in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>heavy_armor</code> (Heavy Armor)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>threshold</code></td><td>Float (0.0 ~ 1000.0)</td><td>The armor value of a target above which it counts as heavily armored.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>bonus</code></td><td>Float (0.0 ~ 1000.0)</td><td>The extra amount added against heavily armored targets.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>impact</code> (Impact)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>Float (0.1 ~ 64.0)</td><td>The radius of the impact in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>falloff</code></td><td>Float (0.0 ~ 1.0)</td><td>How much the strength drops towards the edge of the radius.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>visuals[]</code> (Beam Visual)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>streak</code><br><code>helix</code><br><code>ring</code><br><code>sphere</code><br><code>burst</code><br><code>crescent</code></td><td>The particle pattern to draw.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor</code></td><td><code>end</code><br><code>caster</code></td><td>Whether the pattern is drawn at the end of the beam or around the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>orientation</code></td><td><code>horizontal</code><br><code>vertical</code></td><td>How ring and crescent patterns are turned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>The particle used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 512)</td><td>How many particles the pattern uses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 64.0)</td><td>The radius of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>step</code></td><td>Float (0.05 ~ 16.0)</td><td>The spacing between particles along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch</code></td><td>Float (0.1 ~ 64.0)</td><td>The length of one full twist for helixes, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strands</code></td><td>Integer (1 ~ 8)</td><td>How many strands a helix has.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arc</code></td><td>Float (1.0 ~ 360.0)</td><td>How much of a circle is drawn, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float</td><td>The height of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rings</code></td><td>Integer (1 ~ 16)</td><td>How many rings are drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Float (0.0 ~ 8.0)</td><td>How far the particles scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>entity_effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>entity_effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>damage_type_overrides[]</code> (Damage Type Override)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>condition</code></td><td>Condition,<br>Condition[]</td><td>The conditions under which the override is used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used instead.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:energy_beam",
      "beam_renderer": "example:venom_blast",
      "max_bounces": 0,
      "redirect_off_blocks": false,
      "entity_effects": [
        {
          "effect": "argon:shock",
          "duration": "3s"
        }
      ],
      "charge": {
        "min_time": "0.5s",
        "max_time": "2s",
        "fire_time": 8,
        "damage": {
          "min": 3,
          "max": 12
        },
        "max_distance": {
          "min": 5,
          "max": 15
        },
        "effect_amplifier": {
          "min": 0,
          "max": 2
        },
        "effect_duration": {
          "min": "3s",
          "max": "6s"
        }
      },
      "state": {
        "enabling": {
          "type": "palladium:key_bind",
          "behaviour": "held"
        }
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:energy_beam",
      "beam_renderer": "example:heat_vision",
      "damage": 6,
      "damage_type": "minecraft:on_fire",
      "max_distance": 25,
      "entity_effects": [
        {
          "effect": "argon:burning",
          "duration": "5s"
        }
      ],
      "block_mode": {
        "type": "melt",
        "time": "2s",
        "auto_time": true,
        "speed_multiplier": 2,
        "modifiers": [
          {
            "type": "blacklist",
            "blocks": [
              "minecraft:obsidian",
              "minecraft:netherite_block"
            ]
          },
          {
            "type": "blacklist",
            "blocks": "#minecraft:infiniburn_overworld"
          }
        ],
        "conversions": [
          {
            "blocks": [
              "minecraft:ice",
              "minecraft:snow_block"
            ],
            "result": "minecraft:water"
          }
        ],
        "particle": {
          "particle": {
            "type": "minecraft:lava"
          },
          "count": 10,
          "spread": 0.35
        }
      }
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:energy_beam",
      "beam_renderer": "example:frost_breath",
      "damage_type": "minecraft:freeze",
      "max_distance": 20,
      "entity_effects": [
        {
          "effect": "argon:freezing",
          "duration": "5s"
        }
      ],
      "knockback": 2,
      "cone": {
        "start_size": 0.3,
        "end_size": 6,
        "end_distance": 20,
        "rays": 32
      },
      "block_mode": {
        "type": "freeze",
        "time": "2s",
        "auto_time": true,
        "auto_min_time": "0.5s",
        "auto_max_time": "5s",
        "frozen_time": "10s",
        "slippery": true,
        "friction": 0.995,
        "snow_layers": {
          "max": 4,
          "time_per_layer": "5s",
          "interval": "1s"
        },
        "conversions": [
          {
            "blocks": [
              "minecraft:water"
            ],
            "result": "minecraft:ice",
            "revert": true
          },
          {
            "blocks": [
              "minecraft:lava"
            ],
            "result": "minecraft:obsidian",
            "revert": false
          }
        ],
        "particle": {
          "particle": {
            "type": "minecraft:snowflake"
          },
          "count": 8,
          "spread": 0.35
        }
      }
    }
    ```

=== "Example 4"

    ```json
    {
      "type": "argon:energy_beam",
      "beam_renderer": "example:heat_vision",
      "damage": {
        "type": "palladium:integer_data_attachment",
        "attachment": "example:heat_vision_damage"
      },
      "damage_type": "minecraft:on_fire",
      "damage_type_overrides": [
        {
          "condition": {
            "type": "palladium:number_data_attachment",
            "attachment": "example:heat_vision_damage",
            "min": 15,
            "max": 15
          },
          "damage_type": "minecraft:lava"
        }
      ]
    }
    ```

=== "Example 5"

    ```json
    {
      "type": "argon:energy_beam",
      "beam_renderer": "example:beam_renderer_id",
      "damage": 5,
      "max_distance": 25,
      "set_on_fire_ticks": 20,
      "entity_reaction": "spread",
      "entity_bounce_condition": {
        "type": "palladium:or",
        "conditions": [
          {
            "ability": "example:power#reflect_shield",
            "type": "palladium:ability_unlocked"
          },
          {
            "item": "minecraft:shield",
            "slot": "any",
            "type": "palladium:item_in_slot"
          }
        ]
      },
      "knockback": 0
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "energy_beam": {
          "type": "argon:energy_beam",
          "beam_renderer": "example:venom_blast",
          "max_bounces": 0,
          "redirect_off_blocks": false,
          "entity_effects": [
            {
              "effect": "argon:shock",
              "duration": "3s"
            }
          ],
          "charge": {
            "min_time": "0.5s",
            "max_time": "2s",
            "fire_time": 8,
            "damage": {
              "min": 3,
              "max": 12
            },
            "max_distance": {
              "min": 5,
              "max": 15
            },
            "effect_amplifier": {
              "min": 0,
              "max": 2
            },
            "effect_duration": {
              "min": "3s",
              "max": "6s"
            }
          },
          "state": {
            "enabling": {
              "type": "palladium:key_bind",
              "behaviour": "held"
            }
          }
        }
      }
    }
    ```

---

### Energy Modifier {#argonenergy_modifier}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:energy_modifier</code></div>

<div class="argon-desc">While enabled, changes the stored energy on the item in the given slot every "rate" ticks. Never goes below 0 and has no effect on infinite or creative energy items.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to modify the energy-storing item in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">curios:hands</td></tr><tr><td><code>operation</code></td><td><code>add</code><br><code>subtract</code><br><code>set</code></td><td>Whether "value" is added to the item's energy, subtracted from it, or set as its new energy outright.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SUBTRACT</td></tr><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The amount used by "operation", evaluated fresh every time the ability modifies the item.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rate</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long to wait between modifications.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:energy_modifier",
      "value": 50
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:energy_modifier",
      "operation": "add",
      "value": 25
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:energy_modifier",
      "operation": "set",
      "value": 0
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "energy_modifier": {
          "type": "argon:energy_modifier",
          "value": 50
        }
      }
    }
    ```

---

### Equip Armor {#argonequip_armor}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:equip_armor</code></div>

<div class="argon-desc">On activation, equips each item into the matching slot by list index, replacing whatever was worn without storing it.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>items</code></td><td>Item ID</td><td>The items to equip as plain item IDs (count always 1, no custom components), matched by order to 'slots'.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slots</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slots to equip into, matched by order to 'items'.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:equip_armor",
      "items": [
        "minecraft:iron_helmet",
        "minecraft:iron_chestplate",
        "minecraft:iron_leggings",
        "minecraft:iron_boots"
      ],
      "slots": [
        "head",
        "chest",
        "legs",
        "feet"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "equip_armor": {
          "type": "argon:equip_armor",
          "items": [
            "minecraft:iron_helmet",
            "minecraft:iron_chestplate",
            "minecraft:iron_leggings",
            "minecraft:iron_boots"
          ],
          "slots": [
            "head",
            "chest",
            "legs",
            "feet"
          ]
        }
      }
    }
    ```

---

### EXP Gain {#argonexp_gain}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:exp_gain</code></div>

<div class="argon-desc">While enabled, regularly grants EXP for this power. Usually a hidden, always-on background ability.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>interval</code></td><td>Integer (&gt; 0)</td><td>How many ticks between each EXP grant (20 ticks per second, so 1200 = one minute).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1200</td></tr><tr><td><code>amount</code></td><td>Integer (&gt; 0)</td><td>How much EXP to grant each interval.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:exp_gain"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "exp_gain": {
          "type": "argon:exp_gain"
        }
      }
    }
    ```

---

### Explosion {#argonexplosion}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:explosion</code></div>

<div class="argon-desc">On activation, creates an explosion centered on the user that damages and knocks back nearby entities.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>Float</td><td>The explosion's power and radius (for reference, TNT is 4).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr><tr><td><code>destroy_environment</code></td><td>Boolean</td><td>Whether the explosion breaks blocks in range like real TNT. When false it only affects entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>damage_self</code></td><td>Boolean</td><td>Whether the user takes damage and knockback from their own explosion. When false they are left out and others still take full damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:explosion",
      "properties": {
        "title": "Explosion"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "explosion": {
          "type": "argon:explosion",
          "properties": {
            "title": "Explosion"
          }
        }
      }
    }
    ```

---

### Flight Speed Adjuster {#argonflight_speed_adjuster}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:flight_speed_adjuster</code></div>

<div class="argon-desc">A saved flight speed dial from "min_value" to "max_value" (starting at "default_value"), changed by a dependent mod's adjust(entity, steps). Read it with argon:flight_speed or argon:flight_speed_percent.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>division_amount</code></td><td>Double</td><td>current_value is divided by this to get the speed added to the flight type's base speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr><tr><td><code>min_value</code></td><td>Integer</td><td>The lowest the dial can be adjusted to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>max_value</code></td><td>Integer</td><td>The highest the dial can be adjusted to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>default_value</code></td><td>Integer</td><td>The dial's starting value when this ability is first granted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:flight_speed_adjuster",
      "properties": {
        "title": "Flight Speed Adjuster"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "flight_speed_adjuster": {
          "type": "argon:flight_speed_adjuster",
          "properties": {
            "title": "Flight Speed Adjuster"
          }
        }
      }
    }
    ```

---

### Fluid Modifier {#argonfluid_modifier}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:fluid_modifier</code></div>

<div class="argon-desc">While enabled, changes the stored fluid amount on the fluid item in the given slot every "rate" ticks, kept between 0 and the item's capacity.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to modify the fluid-storing item in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">curios:hands</td></tr><tr><td><code>operation</code></td><td><code>add</code><br><code>subtract</code><br><code>set</code></td><td>Whether "value" is added to the item's stored fluid amount, subtracted from it, or set as its new amount outright.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SUBTRACT</td></tr><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The amount used by "operation", evaluated fresh every time the ability modifies the item.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rate</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long to wait between modifications.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:fluid_modifier",
      "value": 50
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:fluid_modifier",
      "operation": "add",
      "value": 25
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:fluid_modifier",
      "operation": "set",
      "value": 0
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "fluid_modifier": {
          "type": "argon:fluid_modifier",
          "value": 50
        }
      }
    }
    ```

---

### Fluid Transfer {#argonfluid_transfer}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:fluid_transfer</code></div>

<div class="argon-desc">While enabled, moves "value" of the given fluid every "rate" ticks from the fluid item in "from_slot" to the one in "to_slot". Limited by the source's fluid and the destination's room.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>from_slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to take the fluid-storing item to draw from.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>to_slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to take the fluid-storing item to fill.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fluid</code></td><td>Fluid ID</td><td>The fluid that must be stored on both the "from_slot" and "to_slot" items for the transfer to happen.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The amount to move per transfer, evaluated fresh every time the ability transfers fluid.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rate</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long to wait between transfers.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:fluid_transfer",
      "from_slot": "curios:hands",
      "to_slot": "curios:back",
      "fluid": "minecraft:water",
      "value": 50
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "fluid_transfer": {
          "type": "argon:fluid_transfer",
          "from_slot": "curios:hands",
          "to_slot": "curios:back",
          "fluid": "minecraft:water",
          "value": 50
        }
      }
    }
    ```

---

### Fluid Transfer (All) {#argonfluid_transfer_all}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:fluid_transfer_all</code></div>

<div class="argon-desc">When enabled, moves as much fluid as fits from the fluid item in "from_slot" to the one in "to_slot" at once. What doesn't fit stays in the source.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>from_slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to take the fluid-storing item to draw from.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>to_slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to take the fluid-storing item to fill.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fluid</code></td><td>Fluid ID</td><td>The fluid that must be stored on both the "from_slot" and "to_slot" items for the transfer to happen.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:fluid_transfer_all",
      "from_slot": "curios:hands",
      "to_slot": "curios:back",
      "fluid": "minecraft:water"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "fluid_transfer_all": {
          "type": "argon:fluid_transfer_all",
          "from_slot": "curios:hands",
          "to_slot": "curios:back",
          "fluid": "minecraft:water"
        }
      }
    }
    ```

---

### Force Start Flight {#argonforce_start_flight}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:force_start_flight</code></div>

<div class="argon-desc">On activation, starts flying right away instead of waiting for the double-jump or fly key, but only while a palladium:flight ability is already enabled.</div>

=== "Example"

    ```json
    {
      "type": "argon:force_start_flight"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "force_start_flight": {
          "type": "argon:force_start_flight"
        }
      }
    }
    ```

---

### Grapple {#argongrapple}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:grapple</code></div>

<div class="argon-desc">Shoots a rope-like beam out to a range and reels in what it hits. A hit living entity is pulled toward the caster, a hit block pulls the caster toward it.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>The maximum distance the grapple can reach.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attach_to_entity</code></td><td>Boolean</td><td>If true, hitting a living entity within range pulls it toward the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>attach_to_block</code></td><td>Boolean</td><td>If true, hitting a block within range pulls the caster toward it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The velocity, in blocks/tick, that the pulled entity (or the caster) moves at.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The beam renderer id used to draw the rope (e.g. a custom one under data/<namespace>/palladium/beams/).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Mob effects applied to a living entity when the grapple hits it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:grapple",
      "range": 20,
      "speed": 1.2,
      "beam_renderer": "example:beam_renderer_id"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "grapple": {
          "type": "argon:grapple",
          "range": 20,
          "speed": 1.2,
          "beam_renderer": "example:beam_renderer_id"
        }
      }
    }
    ```

---

### Ground Beam {#argonground_beam}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ground_beam</code></div>

<div class="argon-desc">While enabled, draws damaging ground beams under entities with solid ground within "max_ground_depth" blocks. "mode" "area" (default) hits every other living entity within "range", "target" only the one you look at.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The id of the beam renderer to use for each ground-to-target beam.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>Double</td><td>In "area" mode, how far from the user, in blocks, to search for targets. In "target" mode, the farthest a target can be while you look at it.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>area</code><br><code>target</code></td><td>Whether this affects every qualifying entity within "range" of the user ("area") or only the single qualifying entity the user is currently looking at ("target").</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">area</td></tr><tr><td><code>max_ground_depth</code></td><td>Double</td><td>How far, in blocks, to search straight down from a target for solid ground. A target with no ground in that depth gets no beam and takes no damage that tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">64.0</td></tr><tr><td><code>damage</code></td><td>Float</td><td>Damage dealt to every beamed entity every "damage_rate" ticks. Leave at 0 for a cosmetic beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>damage_rate</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long, in ticks, to wait between damage applications.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>no_knockback</code></td><td>Boolean</td><td>If true, damaged entities are not knocked back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>powers</code></td><td><em>Power Requirement</em>,<br><em>Power Requirement</em>[]</td><td>Restricts which entities can be targeted based on the powers they hold. Each entry lists a "power" (an explicit power id, a power tag ("#namespace:tag"), or a mix of both) and an optional "mode" - "include" (default) requires at least one matching power to be present, "exclude" requires all of them to be absent; an entity only counts if it satisfies every entry. Leave unset (the default) to target all living entities in range.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>A damage type ID such as "minecraft:magic" or one from a pack. Left unset, it is a player attack when a player uses this and a mob attack otherwise. Unknown types fall back to that.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>powers</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:ground_beam",
      "beam_renderer": "example:beam_renderer_id",
      "range": 10,
      "damage": 2,
      "no_knockback": true
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:ground_beam",
      "beam_renderer": "example:beam_renderer_id",
      "range": 10,
      "damage": 2,
      "powers": [
        {
          "power": "example:ally_power",
          "mode": "exclude"
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "ground_beam": {
          "type": "argon:ground_beam",
          "beam_renderer": "example:beam_renderer_id",
          "range": 10,
          "damage": 2,
          "no_knockback": true
        }
      }
    }
    ```

---

### Hearing {#argonhearing}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:hearing</code></div>

<div class="argon-desc">Client only. Labels each sound you hear with its subtitle and pins it in the world until it fades. Sounds beyond their normal range are forwarded up to "range" blocks as silent markers.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The farthest a sound can be from the holder, in blocks, and still show. Includes sounds the server forwards from beyond their normal distance. Capped at 512 for forwarded sounds.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32.0</td></tr><tr><td><code>duration</code></td><td>Integer (1 ~ 12000)</td><td>How long a sound's marker lasts before it is gone. It stays fully visible for the first 60% and fades over the rest.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>max_markers</code></td><td>Integer (1 ~ 512)</td><td>The most markers shown at once; the oldest are dropped first.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">64</td></tr><tr><td><code>include_unlabeled</code></td><td>Boolean</td><td>Whether sounds with no subtitle in the game's sound definitions are shown too, labeled with the sound's own id.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>see_through</code></td><td>Boolean</td><td>Whether markers are visible through blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>ignore_own</code></td><td>Boolean</td><td>Whether sounds made at the holder's own position (their footsteps, their hurt sound) are skipped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>scale</code></td><td>Float (0.1 ~ 8.0)</td><td>Size multiplier for the marker text.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>color</code></td><td>Color</td><td>The text color, white by default.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>exclude_sources</code></td><td>string[]</td><td>Sound categories that are never shown: any of master, music, record, weather, block, hostile, neutral, player, ambient, voice, ui. Sounds not placed in the world (interface sounds) are always skipped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;master&quot;, &quot;music&quot;, &quot;record&quot;, &quot;ui&quot; ]</td></tr><tr><td><code>muffle_footsteps</code></td><td>Boolean</td><td>Whether footsteps on a soft surface can't be heard. A step is skipped when the block the walker stands in or on is one of the "muffling_blocks". The server applies the same rule to sounds it forwards from far away.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>muffling_blocks</code></td><td>Block ID(s) / Tag</td><td>The blocks that muffle footsteps when "muffle_footsteps" is on, given as explicit block IDs, a tag ("#namespace:tag"), or a mix of both. Left unset, it is vanilla's "#minecraft:dampens_vibrations" tag, which is wool and carpets.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hostile_color</code></td><td>Color</td><td>Text color for sounds made by hostile mobs, instead of "color".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>player_color</code></td><td>Color</td><td>Text color for sounds made by players, instead of "color".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>neutral_color</code></td><td>Color</td><td>Text color for sounds made by neutral and passive mobs, instead of "color".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>prioritize</code></td><td>Boolean</td><td>When more sounds are heard than "max_markers" allows, drop the least significant (ambient and block sounds first, then far-away ones) instead of the oldest. Hostile and player sounds rank highest.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>edge_arrows</code></td><td>Boolean</td><td>Shows a small pointer on the edge of the screen for every marker that is outside your view, pointing the way to the sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:hearing",
      "range": 48,
      "duration": 120,
      "color": "#FFFFFF",
      "exclude_sources": [
        "master",
        "music",
        "record",
        "ui"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "hearing": {
          "type": "argon:hearing",
          "range": 48,
          "duration": 120,
          "color": "#FFFFFF",
          "exclude_sources": [
            "master",
            "music",
            "record",
            "ui"
          ]
        }
      }
    }
    ```

---

### Held Target {#argonheld_target}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:held_target</code></div>

<div class="argon-desc">Deals damage, applies effects and knocks back the entity the user holds with argon:carry (or let go of in the last few ticks). Each entry runs on the first tick, every tick, or the last tick. Does nothing when nothing is held.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>applications</code></td><td><em>Held Application</em>[]</td><td>What to do to the held target. timing is "first_tick", "tick" or "last_tick"; interval is how often a "tick" entry runs; damage is a Value; armor_penetration is the fraction from 0 to 1 of the target's armor ignored by the damage; damage_type is a damage type ID (unset, a player attack); effects is a list of { effect*, duration, amplifier, particles }; knockback_distance (Value, blocks, away from the user) and lift (Value, upward speed) are weakened by knockback resistance; reset_invulnerability (default false) clears the target's hit immunity just before the damage so several quick hits all land.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>release_window</code></td><td>Integer</td><td>How many ticks after the target was let go it still counts as held, so an entry can run on the tick the carry ends.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr></tbody></table></div>

    <p class="argon-nested"><code>applications[]</code> (Held Application)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>timing</code></td><td><code>first_tick</code><br><code>tick</code><br><code>last_tick</code></td><td>When the application happens while the ability is held.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The delay between applications when the timing is tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>The damage dealt.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>armor_penetration</code></td><td>Float (0.0 ~ 1.0)</td><td>How much of the target's armor is ignored.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>knockback_distance</code></td><td>(Dynamic) Value</td><td>How far the target is knocked back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lift</code></td><td>(Dynamic) Value</td><td>How much the target is lifted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>reset_invulnerability</code></td><td>Boolean</td><td>Whether the target's invulnerability frames are reset so the hit lands.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>applications[].effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>applications[].effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:held_target",
      "applications": []
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "held_target": {
          "type": "argon:held_target",
          "applications": []
        }
      }
    }
    ```

---

### Highlight {#argonhighlight}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:highlight</code></div>

<div class="argon-desc">Client only. Tints the entity's model (and optionally matching blocks in range) with a color, visible through walls to the ability holder only.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>self</code><br><code>others</code></td><td>Whether this ability highlights the entity itself or lets you see other entities (self, others). Seeing others also needs "highlight_entities".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SELF</td></tr><tr><td><code>color</code></td><td>Color</td><td>The highlight color, defaulting to the team color for entities or white for blocks when unset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>opacity</code></td><td>Float (0.0 ~ 1.0)</td><td>How strong the tint is, from 0 (invisible) to 1 (fully opaque).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.1</td></tr><tr><td><code>distance</code></td><td>(Dynamic) Value</td><td>The distance at which entities (in "others" mode) and enabled matching blocks are highlighted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>style</code></td><td><code>tint</code><br><code>outline</code></td><td>How highlighted entities are drawn: tint fills the model with the color, outline draws the vanilla glow outline in the color (works on invisible entities too, and the opacity does not apply).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">TINT</td></tr><tr><td><code>highlight_entities</code></td><td>Boolean</td><td>If true, "others" mode also highlights entities within "distance" through walls. Off by default, so "others" only shows blocks. No effect in "self" mode.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>entities</code></td><td>Entity Type ID(s) / Tag</td><td>The entity types to highlight when "highlight_entities" is true, given as explicit entity type IDs, a tag ("#namespace:tag"), or a mix of both. Left unset, every living entity in range is highlighted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>highlight_blocks</code></td><td>Boolean</td><td>If true, also highlights every block matching "blocks" within "distance", through walls.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The blocks to highlight when "highlight_blocks" is true, given as explicit block IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blocked_by</code></td><td>Block ID(s) / Tag</td><td>Block types that still block line of sight for this effect, hiding anything behind them while everything else stays visible through walls.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hostile_color</code></td><td>Color</td><td>Highlight color for hostile mobs (and neutral ones targeting the holder). When any of the four category colors is set, each highlighted entity uses the color of its category instead of "color"; categories without a color fall back to "color".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ally_color</code></td><td>Color</td><td>Highlight color for allies: the holder's team members, owned pets, and entities allied through vanilla teams.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>neutral_color</code></td><td>Color</td><td>Highlight color for everything else that is not hostile, a player or an ally (animals, villagers, passive mobs).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>player_color</code></td><td>Color</td><td>Highlight color for players who are not allies.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:highlight",
      "mode": "self",
      "color": "#FF0000",
      "opacity": 0.1,
      "distance": 16,
      "highlight_entities": true,
      "entities": [
        "minecraft:zombie",
        "#minecraft:skeletons"
      ],
      "highlight_blocks": true,
      "blocks": [
        "#minecraft:diamond_ores"
      ],
      "blocked_by": [
        "palladium:lead_block"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "highlight": {
          "type": "argon:highlight",
          "mode": "self",
          "color": "#FF0000",
          "opacity": 0.1,
          "distance": 16,
          "highlight_entities": true,
          "entities": [
            "minecraft:zombie",
            "#minecraft:skeletons"
          ],
          "highlight_blocks": true,
          "blocks": [
            "#minecraft:diamond_ores"
          ],
          "blocked_by": [
            "palladium:lead_block"
          ]
        }
      }
    }
    ```

---

### Hunger Rate {#argonhunger_rate}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:hunger_rate</code></div>

<div class="argon-desc">While enabled, scales how fast a player's hunger drains and how much food and saturation they gain back. 100 is vanilla. 50 for drain means hunger drops half as fast, 50 for refill means food only restores half as much hunger and saturation (the fractions carry over, so two food points still add up). Values above 100 speed things up. Several enabled instances multiply their drain.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>drain_percent</code></td><td>Integer</td><td>Percent of the normal exhaustion the player takes from moving, jumping, fighting and regenerating. 0 stops hunger from draining.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>refill_percent</code></td><td>Integer</td><td>Percent of the normal food level and saturation the player gets back whenever either increases.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:hunger_rate",
      "drain_percent": 50,
      "properties": {
        "title": "Hunger Rate"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "hunger_rate": {
          "type": "argon:hunger_rate",
          "drain_percent": 50,
          "properties": {
            "title": "Hunger Rate"
          }
        }
      }
    }
    ```

---

### Immunity {#argonimmunity}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:immunity</code></div>

<div class="argon-desc">While enabled, blocks the listed status effects from being applied to the user, optionally up to a maximum level per effect, and removes matching effects they already have.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effects</code></td><td><em>Immune Effect</em>[]</td><td>List of effects to block, each with an "effect" id and an optional "level" (amplifier cap) below which immunity applies, or all levels if unset.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Immune Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect the user is immune to.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>level</code></td><td>Integer</td><td>The highest effect level that is blocked.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:immunity",
      "effects": [
        {
          "effect": "minecraft:poison"
        },
        {
          "effect": "minecraft:weakness",
          "level": 1
        }
      ],
      "properties": {
        "title": "Immunity"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "immunity": {
          "type": "argon:immunity",
          "effects": [
            {
              "effect": "minecraft:poison"
            },
            {
              "effect": "minecraft:weakness",
              "level": 1
            }
          ],
          "properties": {
            "title": "Immunity"
          }
        }
      }
    }
    ```

---

### Invisibility {#argoninvisibility}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:invisibility</code></div>

<div class="argon-desc">Makes the player invisible. Also makes mobs not see the player anymore. Adds a "fade" style for the transition.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>opacity</code></td><td>Float (&gt;= 0.0)</td><td>Opacity for other players/observers once fully invisible (0 = fully invisible).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>opacity_self</code></td><td>Float</td><td>Opacity for the local player's own view once fully invisible.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.2</td></tr><tr><td><code>mob_visibility_modifier</code></td><td>Float (&gt;= 0.0)</td><td>Multiplier fed into mob-sight/visibility checks once fully invisible.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>fade</code></td><td><code>default</code><br><code>energy</code></td><td>How the invisibility transition is visualized. "default" matches Palladium's own fade exactly. "energy" spreads an irregular, glowing energy boundary across the model's surface as it fades in/out instead of a uniform opacity change.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">default</td></tr><tr><td><code>energy_color</code></td><td>Color</td><td>Only for "fade": "energy". The color of the glowing edge of the transition. Its hottest point still turns toward white.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#6FEAFF</td></tr><tr><td><code>energy_additional_textures</code></td><td>string[]</td><td>Only for "fade": "energy". Texture path prefixes (e.g. "mypack:textures/entity/suits/") of OTHER render layers that should dissolve and tint with the skin. Worn armor and suit textures are found automatically.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:invisibility",
      "energy_additional_textures": "mypack:textures/entity/suits/"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "invisibility": {
          "type": "argon:invisibility",
          "energy_additional_textures": "mypack:textures/entity/suits/"
        }
      }
    }
    ```

---

### Item Database (Create) {#argonitem_database_create}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_database_create</code></div>

<div class="argon-desc">On activation, opens a searchable list of everything in the user's item database. Clicking an entry gives the user one more copy.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>exact_copy</code></td><td>Boolean</td><td>Whether created items are exact duplicates of what was stored (enchantments, damage, name, etc.). When false they are plain default copies of the item type.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>max_uses</code></td><td>Integer (&gt; 0)</td><td>Most items each database entry can create before it must be stored again to reset its count. Unlimited if unset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:item_database_create",
      "max_uses": 5,
      "properties": {
        "title": "Item Database (Create)"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "item_database_create": {
          "type": "argon:item_database_create",
          "max_uses": 5,
          "properties": {
            "title": "Item Database (Create)"
          }
        }
      }
    }
    ```

---

### Item Database (Store) {#argonitem_database_store}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_database_store</code></div>

<div class="argon-desc">On activation, takes one copy of the item in the user's main hand and stores it in their account-wide item database, unless blacklisted in the config.</div>

=== "Example"

    ```json
    {
      "type": "argon:item_database_store",
      "properties": {
        "title": "Item Database (Store)"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "item_database_store": {
          "type": "argon:item_database_store",
          "properties": {
            "title": "Item Database (Store)"
          }
        }
      }
    }
    ```

---

### Item Storage {#argonitem_storage}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_storage</code></div>

<div class="argon-desc">While enabled, shows a scrollable strip of item slots near the hotbar. Right-click swaps a slot with the main hand. Items are stored on the entity by default, or on a given equipment or Curios slot.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>max_items</code></td><td>Integer (&gt; 0)</td><td>The total number of storable slots.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>item_filter</code></td><td>Identifier[]</td><td>List of item ids allowed to be stored, or any item if left empty.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>If set, items are stored on the item in this equipment or Curios slot instead of on the entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>position</code></td><td>Vector 2D</td><td>Pixel offset of the slot strip from its default spot above the hotbar.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">net.minecraft.world.phys.Vec2@631c244c</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:item_storage",
      "max_items": 9
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "item_storage": {
          "type": "argon:item_storage",
          "max_items": 9
        }
      }
    }
    ```

---

### Light Source {#argonlight_source}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:light_source</code></div>

<div class="argon-desc">While enabled, a real light-emitting block follows the entity (only in air or water, removed on disable) with colored particles, since block light has no color.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>light_level</code></td><td>Integer (0 ~ 15)</td><td>How bright the emitted light is, from 0 (none) to 15 (maximum, matching a torch or brighter).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">15</td></tr><tr><td><code>particles</code></td><td><em>Light Particle</em>,<br><em>Light Particle</em>[]</td><td>One or more particle effects (a bare object or a list) spawned around the entity every tick, each with its own "color" (defaults to a warm torch-like tone when unset), "count" (particles per tick, default 3), "offset" ([x, y, z] added to the entity's position, default [0, 0.5, 0]), and "spread" ([x, y, z] random scatter radius per axis, default [0.2, 0.2, 0.2]). Configuring several entries lets you layer differently colored/positioned effects at once; an empty list disables particles entirely, leaving only the real light.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>particles</code> (Light Particle)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color of the particle.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (&gt; 0)</td><td>How many particles spawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>Offset from the origin in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Vector 3D</td><td>How far the particles spread on each axis.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:light_source"
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:light_source",
      "light_level": 12,
      "particles": [
        {
          "color": "#40c0ff",
          "count": 4,
          "offset": [
            0,
            0.5,
            0
          ],
          "spread": [
            0.25,
            0.25,
            0.25
          ]
        },
        {
          "color": "#ffffff",
          "count": 1,
          "offset": [
            0,
            1.6,
            0
          ],
          "spread": [
            0.1,
            0.1,
            0.1
          ]
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "light_source": {
          "type": "argon:light_source"
        }
      }
    }
    ```

---

### Lightning {#argonlightning}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:lightning</code></div>

<div class="argon-desc">On activation, strikes the block or entity the user looks at with a lightning-like beam that damages nearby living entities. Uses maximum range if the raycast hits nothing.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>The maximum distance, in blocks, the raycast can reach when finding a block or entity to strike.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The beam renderer id used to draw the strike, e.g. one under data/<namespace>/palladium/beams/.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>Float</td><td>The damage dealt to living entities near the impact point, or none by default.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>damage_radius</code></td><td>Double</td><td>How far from the impact point, in blocks, entities can still take damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>duration_ticks</code></td><td>Integer</td><td>How many ticks the beam visual stays on screen.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>A damage type ID such as "minecraft:magic" or one from a pack. Left unset, it is a player attack when a player uses this and a mob attack otherwise. Unknown types fall back to that.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:lightning",
      "range": 10,
      "beam_renderer": "example:beam_renderer_id",
      "damage": 6
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "lightning": {
          "type": "argon:lightning",
          "range": 10,
          "beam_renderer": "example:beam_renderer_id",
          "damage": 6
        }
      }
    }
    ```

---

### Lock Slots {#argonlock_slots}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:lock_slots</code></div>

<div class="argon-desc">While enabled, prevents items in the listed slots from being removed, swapped, or otherwise changed.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slots</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slots to lock in place.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:lock_slots",
      "slots": [
        "head",
        "chest",
        "curios:belt"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "lock_slots": {
          "type": "argon:lock_slots",
          "slots": [
            "head",
            "chest",
            "curios:belt"
          ]
        }
      }
    }
    ```

---

### Melee Armor Penetration {#argonmelee_armor_penetration}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:melee_armor_penetration</code></div>

<div class="argon-desc">While enabled, the user's direct melee hits ignore part of the target's armor. Hits from argon:energy_beam and argon:held_target use their own armor_penetration instead.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>penetration</code></td><td>Float</td><td>The fraction from 0 to 1 of the damage armor would have absorbed that is ignored.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:melee_armor_penetration",
      "penetration": 0.25
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "melee_armor_penetration": {
          "type": "argon:melee_armor_penetration",
          "penetration": 0.25
        }
      }
    }
    ```

---

### Modify Durability {#argonmodify_durability}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:modify_durability</code></div>

<div class="argon-desc">While enabled, removes or adds durability on the items in the given slots every interval. Damaging an item to its last point of durability breaks it, unless break_item is false. Items that can't be damaged are skipped.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slots</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slot or slots whose items are changed. A slot with several items, like a curios slot, changes all of them.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;mainhand&quot; ]</td></tr><tr><td><code>operation</code></td><td><code>damage</code><br><code>repair</code></td><td>Whether to remove (damage) or add (repair) durability.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">DAMAGE</td></tr><tr><td><code>amount</code></td><td>(Dynamic) Value</td><td>How many points of durability to remove or add each time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How often the change is applied while the ability is enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>break_item</code></td><td>Boolean</td><td>Whether an item that runs out of durability breaks. When false it stays at 1 durability left.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:modify_durability",
      "slots": "chest",
      "amount": 2,
      "properties": {
        "title": "Modify Durability"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "modify_durability": {
          "type": "argon:modify_durability",
          "slots": "chest",
          "amount": 2,
          "properties": {
            "title": "Modify Durability"
          }
        }
      }
    }
    ```

---

### Movement Reduction {#argonmovement_reduction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:movement_reduction</code></div>

<div class="argon-desc">While enabled, lowers the entity's ground movement or flight speed by a percentage, optionally lowering its attack damage by the same amount.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>movement</code><br><code>flight</code></td><td>Whether to reduce ground movement speed ("movement") or flight speed ("flight").</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>percentage</code></td><td>Float</td><td>The percentage to reduce the chosen speed by, from 0 (no effect) to 100 (fully stopped).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>reduce_attack_damage</code></td><td>Boolean</td><td>If true, also reduces the entity's attack damage by the same percentage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:movement_reduction",
      "mode": "movement",
      "percentage": 30
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "movement_reduction": {
          "type": "argon:movement_reduction",
          "mode": "movement",
          "percentage": 30
        }
      }
    }
    ```

---

### Movement Speed Adjuster {#argonmovement_speed_adjuster}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:movement_speed_adjuster</code></div>

<div class="argon-desc">While enabled and not flying, adds "current_value / division_amount" to movement speed. The dial runs from "min_value" to "max_value" (starting at "default_value") and is changed by a dependent mod's adjust(entity, steps).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>division_amount</code></td><td>Double</td><td>current_value is divided by this to get the actual attribute bonus.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5000.0</td></tr><tr><td><code>min_value</code></td><td>Integer</td><td>The lowest the dial can be adjusted to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>max_value</code></td><td>Integer</td><td>The highest the dial can be adjusted to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>default_value</code></td><td>Integer</td><td>The dial's starting value when this ability is first granted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:movement_speed_adjuster",
      "properties": {
        "title": "Movement Speed Adjuster"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "movement_speed_adjuster": {
          "type": "argon:movement_speed_adjuster",
          "properties": {
            "title": "Movement Speed Adjuster"
          }
        }
      }
    }
    ```

---

### Multi-Jump {#argonmulti_jump}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:multi_jump</code></div>

<div class="argon-desc">While enabled, lets the entity jump again in mid-air, up to a set number of times, until it touches the ground and refills them.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>max_jumps</code></td><td>Integer (&gt;= 0)</td><td>How many extra mid-air jumps the entity can perform before landing again.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>jump_velocity</code></td><td>Float</td><td>The vertical velocity applied per extra jump, defaulting to a normal jump's strength.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.42</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:multi_jump",
      "max_jumps": 1
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "multi_jump": {
          "type": "argon:multi_jump",
          "max_jumps": 1
        }
      }
    }
    ```

---

### Multiversal Variant Swap {#argonmultiversal_variant}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:multiversal_variant</code></div>

<div class="argon-desc">While enabled, shows an icon near the hotbar for the item in "slot" and lets the mouse wheel cycle it through its multiversal variants without touching any other item data.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The equipment or Curios slot whose item's variant gets cycled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>position</code></td><td>Vector 2D</td><td>Pixel offset of the icon and label from their default spot above the hotbar.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">net.minecraft.world.phys.Vec2@631c244c</td></tr><tr><td><code>swap_item</code></td><td>Boolean</td><td>If true, scrolling swaps in the variant's actual item instead of just changing the variant component, keeping the stack's other components.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:multiversal_variant",
      "slot": "head"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "multiversal_variant": {
          "type": "argon:multiversal_variant",
          "slot": "head"
        }
      }
    }
    ```

---

### No Hurt Reaction {#argonno_hurt_reaction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:no_hurt_reaction</code></div>

<div class="argon-desc">While enabled, the user still takes damage but skips the usual reaction to it. The hurt sound, the red flash with the tilt and camera shake, and the knockback can each be turned off. The death sound is not affected.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>cancel_sound</code></td><td>Boolean</td><td>Whether the hurt sound is skipped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>cancel_animation</code></td><td>Boolean</td><td>Whether the red flash, the hurt tilt and the camera shake are skipped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>cancel_knockback</code></td><td>Boolean</td><td>Whether the knockback from taking damage is skipped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:no_hurt_reaction",
      "properties": {
        "title": "No Hurt Reaction"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "no_hurt_reaction": {
          "type": "argon:no_hurt_reaction",
          "properties": {
            "title": "No Hurt Reaction"
          }
        }
      }
    }
    ```

---

### Offset Projectile {#argonoffset_projectile}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:offset_projectile</code></div>

<div class="argon-desc">Shoots a projectile like the built-in projectile ability, but from an x/y/z offset relative to the entity's facing direction.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_type</code></td><td>Entity Type ID</td><td>ID of an entity type (must be a projectile).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entity_data</code></td><td>NBT</td><td>Additional NBT data for the projectile entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>inaccuracy</code></td><td>Float (&gt;= 0.0)</td><td>The inaccuracy applied when shooting the projectile.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>velocity</code></td><td>Float (&gt;= 0.0)</td><td>The velocity with which the projectile is shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>swinging_arm</code></td><td><code>none</code><br><code>main_arm</code><br><code>off_arm</code><br><code>right_arm</code><br><code>left_arm</code><br><code>both</code></td><td>The arm that swings when the projectile is shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">MAIN_ARM</td></tr><tr><td><code>ignore_player_movement</code></td><td>Boolean</td><td>If true, prevents the player's current velocity from being added to the projectile's velocity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>offset_x</code></td><td>Double</td><td>Spawn offset to the entity's right (negative = left), relative to its facing direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>offset_y</code></td><td>Double</td><td>Spawn offset upward from the entity (negative = downward).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>offset_z</code></td><td>Double</td><td>Spawn offset in front of the entity (negative = behind), relative to its facing direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:offset_projectile",
      "offset_x": 0.3,
      "offset_y": -0.2,
      "offset_z": 0.5
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "offset_projectile": {
          "type": "argon:offset_projectile",
          "offset_x": 0.3,
          "offset_y": -0.2,
          "offset_z": 0.5
        }
      }
    }
    ```

---

### Open GUI {#argonopen_gui}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:open_gui</code></div>

<div class="argon-desc">Opens the chosen standalone GUI. Crafting style menus work fully, storage ones get their own persistent inventory, and furnace style ones run a saved simulation of vanilla smelting or brewing.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>gui</code></td><td><code>argon:chemical_synthesizer</code><br><code>argon:dna_power</code><br><code>argon:dna_transfer</code><br><code>argon:tech_table</code><br><code>charginggadgets:charging_station_container</code><br><code>curios:curios_container</code><br><code>fsang:soul_gear</code><br><code>minecraft:anvil</code><br><code>minecraft:blast_furnace</code><br><code>minecraft:brewing_stand</code><br><code>minecraft:cartography_table</code><br><code>minecraft:crafter_3x3</code><br><code>minecraft:crafting</code><br><code>minecraft:enchantment</code><br><code>minecraft:furnace</code><br><code>minecraft:generic_3x3</code><br><code>minecraft:generic_9x1</code><br><code>minecraft:generic_9x2</code><br><code>minecraft:generic_9x3</code><br><code>minecraft:generic_9x4</code><br><code>minecraft:generic_9x5</code><br><code>minecraft:generic_9x6</code><br><code>minecraft:grindstone</code><br><code>minecraft:hopper</code><br><code>minecraft:loom</code><br><code>minecraft:shulker_box</code><br><code>minecraft:smithing</code><br><code>minecraft:smoker</code><br><code>minecraft:stonecutter</code><br><code>palladium:multiversal_iterator</code><br><code>palladium:multiversal_iterator_suit_stand</code><br><code>palladium:tailoring</code></td><td>The registered menu screen to open, as a resource ID (e.g. "minecraft:crafting").</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:open_gui",
      "gui": "minecraft:crafting",
      "properties": {
        "title": "Open GUI"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:open_gui",
      "gui": "minecraft:generic_9x3",
      "properties": {
        "title": "Storage"
      }
    }
    ```

=== "Example 3"

    ```json
    {
      "type": "argon:open_gui",
      "gui": "minecraft:furnace",
      "properties": {
        "title": "Furnace"
      }
    }
    ```

=== "Example 4"

    ```json
    {
      "type": "argon:open_gui",
      "gui": "minecraft:brewing_stand",
      "properties": {
        "title": "Brewing Stand"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "open_gui": {
          "type": "argon:open_gui",
          "gui": "minecraft:crafting",
          "properties": {
            "title": "Open GUI"
          }
        }
      }
    }
    ```

---

### palladium.ability.argon.attack_warning {#argonattack_warning}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:attack_warning</code></div>

<div class="argon-desc">Client only. While enabled, outlines (through walls, only for the holder) every non-allied creature within "radius" that is visibly preparing an attack: a creeper swelling, a ghast or blaze charging, a guardian locking its beam, an illager casting, a skeleton or pillager drawing a bow or crossbow, a warden roaring, a breeze about to shoot.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>How far to look for creatures preparing an attack, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">24.0</td></tr><tr><td><code>color</code></td><td>Color</td><td>The outline color of a creature while it winds up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FF4A2A</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:attack_warning",
      "radius": 24,
      "properties": {}
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "attack_warning": {
          "type": "argon:attack_warning",
          "radius": 24,
          "properties": {}
        }
      }
    }
    ```

---

### palladium.ability.argon.heal {#argonheal}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:heal</code></div>

<div class="argon-desc">On its first enabled tick, heals the user, the ally they are looking at, or every ally nearby. Allies are the user, their team members and their pets. Gives an exact instant amount and can also apply effects such as regeneration.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>self</code><br><code>look_target</code><br><code>area_allies</code></td><td>Who is healed: the user, the ally looked at (look_target), or every ally within range (area_allies).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SELF</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far away the looked-at ally can be, or the radius for area_allies, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">12.0</td></tr><tr><td><code>instant</code></td><td>(Dynamic) Value</td><td>Health restored at once, in half hearts (2 is one heart).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to everyone healed, such as regeneration for healing over time (regeneration level 2 heals about 1 health per 25 ticks).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>self_pitch</code></td><td>Double</td><td>In look_target mode, looking down at least this many degrees heals the user instead of looking for an ally.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60.0</td></tr><tr><td><code>fallback_self</code></td><td>Boolean</td><td>In look_target mode, heal the user when no ally is being looked at. Otherwise nothing happens.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>include_self</code></td><td>Boolean</td><td>In area_allies mode, whether the user is healed too.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>particles</code></td><td><em>Particle Effect</em>[]</td><td>Particles played at the middle of everyone healed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>particles[]</code> (Particle Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>particle</code></td><td>Particle</td><td>The particle to spawn.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (&gt;= 0)</td><td>How many particles spawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Double</td><td>How far the particles spread from the origin.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>Offset from the origin in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:heal",
      "mode": "look_target",
      "range": 12,
      "instant": 6,
      "effects": [
        {
          "effect": "minecraft:regeneration",
          "amplifier": 1
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "heal": {
          "type": "argon:heal",
          "mode": "look_target",
          "range": 12,
          "instant": 6,
          "effects": [
            {
              "effect": "minecraft:regeneration",
              "amplifier": 1
            }
          ]
        }
      }
    }
    ```

---

### palladium.ability.argon.lightning_strikes {#argonlightning_strikes}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:lightning_strikes</code></div>

<div class="argon-desc">When enabled, calls real lightning bolts (visual only, no fire or terrain damage unless ignite_blocks is on) down on a target point and damages enemies around each one. With an interval it keeps striking while enabled, so it can be a timed storm. Optional rain is drawn with particles and never changes the world's weather. Every strike also posts a LightningStrikeEvent so a pack can draw its own bolts.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>target</code></td><td><code>look</code><br><code>hostiles</code><br><code>area</code><br><code>self</code><br><code>look_area</code><br><code>look_hostiles</code></td><td>Where the strikes land: "look" at the block or spot the user looks at, "hostiles" on random hostile mobs within radius, "area" at random spots within radius around the user, "self" exactly where the user stands, "look_area" at random spots within radius around the point the user looks at, "look_hostiles" on different hostile mobs within radius of the look point (random spots there when none).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">hostiles</td></tr><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>For hostiles and area, how far from the user strikes can land. For look, how far strikes beyond the first are scattered around the target spot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>look_range</code></td><td>(Dynamic) Value</td><td>For look, the maximum distance of the target spot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32</td></tr><tr><td><code>strikes</code></td><td>(Dynamic) Value</td><td>How many bolts each volley calls down.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>0 fires one volley when the ability is enabled. Above 0, another volley every interval while it stays enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>Damage each bolt deals to the enemy nearest its impact, and to everything else inside the damage radius unless splash_damage is set.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>damage_radius</code></td><td>(Dynamic) Value</td><td>How far from each bolt's impact entities take damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.5</td></tr><tr><td><code>splash_damage</code></td><td>(Dynamic) Value</td><td>Damage dealt to everything inside the damage radius except the entity nearest the impact point, which takes the full damage. Negative means the same as damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-1</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used; the user's normal attack when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to every entity a bolt damages.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hostile_only</code></td><td>Boolean</td><td>If true, only hostile mobs take damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>ignite_blocks</code></td><td>Boolean</td><td>If true, bolts are real lightning that can start fires and strike for vanilla damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>rain</code></td><td>Boolean</td><td>Draws rain falling over the area while enabled. Storm clouds are drawn by the pack, which can listen for the lightning strike event.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>bolt</code></td><td>Boolean</td><td>Whether each strike spawns a vanilla visual-only lightning bolt. Turn it off when a pack draws its own bolts from the strike event.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>rain_height</code></td><td>Double</td><td>How many blocks above the area the rain starts falling from.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">11.0</td></tr><tr><td><code>max_hits_per_target</code></td><td>Integer</td><td>The most strikes one entity can be damaged by during a single enabling of the ability. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:lightning_strikes",
      "radius": 16,
      "look_range": 32,
      "strikes": 1,
      "interval": 30,
      "damage": 4,
      "damage_radius": 2.5,
      "splash_damage": -1,
      "hostile_only": true,
      "rain": true
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "lightning_strikes": {
          "type": "argon:lightning_strikes",
          "radius": 16,
          "look_range": 32,
          "strikes": 1,
          "interval": 30,
          "damage": 4,
          "damage_radius": 2.5,
          "splash_damage": -1,
          "hostile_only": true,
          "rain": true
        }
      }
    }
    ```

---

### palladium.ability.argon.melee_bonus_damage {#argonmelee_bonus_damage}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:melee_bonus_damage</code></div>

<div class="argon-desc">While enabled, every direct melee hit the user lands that deals damage also deals extra damage of another type (for example electrical) and can apply effects to the target.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>The extra damage added to each melee hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type of the extra damage; the user's normal attack when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to the target of each melee hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>sparks</code></td><td>Boolean</td><td>Whether electric sparks fly from the target on each hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:melee_bonus_damage",
      "damage": 3
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "melee_bonus_damage": {
          "type": "argon:melee_bonus_damage",
          "damage": 3
        }
      }
    }
    ```

---

### palladium.ability.argon.throw_marker {#argonthrow_marker}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:throw_marker</code></div>

<div class="argon-desc">On its first tick marks the living entity the holder is looking at (or unmarks it if it is already marked). Marks are kept per player, shown only to that player as small sparks above the target, and used in the order they were made by the next argon:throwable_item with targeting_mode marked or hybrid, which then uses them up. Marks are cleared when the holder logs out.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far, in blocks, a target can be marked.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">40.0</td></tr><tr><td><code>maximum_marked_targets</code></td><td>(Dynamic) Value</td><td>The most targets that can be marked at once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:throw_marker",
      "range": 40,
      "maximum_marked_targets": 3,
      "properties": {}
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "throw_marker": {
          "type": "argon:throw_marker",
          "range": 40,
          "maximum_marked_targets": 3,
          "properties": {}
        }
      }
    }
    ```

---

### palladium.ability.argon.throw_steer {#argonthrow_steer}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:throw_steer</code></div>

<div class="argon-desc">While this ability is enabled (give it a held key bind) the holder steers every flying argon:throwable_item projectile they own whose flight_control_mode is look_direction or projectile_camera, toward where they look. Releasing the key hands the projectile back to its normal flight, or returns it if the throwable has manual_return_on_release.</div>

=== "Example"

    ```json
    {
      "type": "argon:throw_steer",
      "properties": {}
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "throw_steer": {
          "type": "argon:throw_steer",
          "properties": {}
        }
      }
    }
    ```

---

### palladium.ability.argon.throwable_item {#argonthrowable_item}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:throwable_item</code></div>

<div class="argon-desc">Throws the configured item from the holder's hand as a physical projectile that looks like the item, keeping its exact ItemStack (components, enchantments, durability) in a saved server record so it can never be duplicated or lost. Activating the ability again while the item is out recalls it (when recall_enabled). The projectile can bounce or embed in blocks, damage and pass through entities, return on its own after configured triggers, hit things on the way back, and be caught by its owner. Almost every number is a Value, so power progression can change it between throws. Values are read when the item is thrown, except the return_* settings and catch_radius, which are read again when the item is recalled. The item is restored to its original slot (or the inventory, or the ground) when caught, picked up, or when the owner logs out, dies or changes dimension.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>item</code></td><td>Item ID(s) / Tag</td><td>The item, items or #tag the ability can throw, e.g. "fsang:mjolnir" or ["minecraft:diamond_sword"].</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hand</code></td><td><code>main_hand</code><br><code>off_hand</code><br><code>either</code></td><td>Which hand to take the item from.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">main_hand</td></tr><tr><td><code>pickup</code></td><td><em>Throwable Pickup</em></td><td>Whether and how the owner picks the item up again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>throw</code></td><td><em>Throw Settings</em></td><td>How the item is thrown and how far it can fly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>combat</code></td><td><em>Throw Combat</em></td><td>What the item does to entities it hits.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>block_impact</code></td><td><em>Throw Block Impact</em></td><td>What the item does when it hits a block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>return</code></td><td><em>Throw Return</em></td><td>How and when the item comes back to its owner.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>render</code></td><td><em>Throw Render</em></td><td>How the thrown item looks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>sounds</code></td><td><em>Throw Sounds</em></td><td>Sounds for each stage of the throw. All are optional sound ids from sounds.json.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>targeting</code></td><td><em>Throw Targeting</em></td><td>How the item picks a target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>homing</code></td><td><em>Throw Homing</em></td><td>How the item steers towards its target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ricochet</code></td><td><em>Throw Ricochet</em></td><td>Lets the item jump to further targets after a hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>steering</code></td><td><em>Throw Steering</em></td><td>Lets the owner steer the item in flight while an argon:throw_steer ability is held.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>camera</code></td><td><em>Throw Camera</em></td><td>The camera used when the steering mode is projectile_camera.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>perfect_catch</code></td><td><em>Throw Perfect Catch</em></td><td>A bonus for catching the item at the right moment.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pin</code></td><td><em>Throw Pin</em></td><td>Pins a hit entity to a wall behind it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>deflection</code></td><td><em>Throw Deflection</em></td><td>Lets the item knock projectiles aside while it flies.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>pickup</code> (Throwable Pickup)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>on_touch</code></td><td>Boolean</td><td>The owner picks the item up by walking near it while it is embedded or resting.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>How close the owner has to get to pick it up, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr></tbody></table></div>

    <p class="argon-nested"><code>throw</code> (Throw Settings)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>speed</code></td><td>(Dynamic) Value</td><td>The speed of the throw.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.8</td></tr><tr><td><code>gravity_mode</code></td><td><code>none</code><br><code>vanilla</code><br><code>scaled</code></td><td>How gravity affects the item. None ignores gravity, vanilla uses the normal pull, scaled uses the gravity multiplier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">vanilla</td></tr><tr><td><code>gravity</code></td><td>(Dynamic) Value</td><td>Multiplier for the scaled gravity mode.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>drag</code></td><td>(Dynamic) Value</td><td>How much speed is kept each tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.99</td></tr><tr><td><code>inaccuracy</code></td><td>(Dynamic) Value</td><td>How far the throw direction can scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>inherit_owner_velocity</code></td><td>(Dynamic) Value</td><td>How much of the owner's own movement is added to the throw.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.35</td></tr><tr><td><code>maximum_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The longest the item can fly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">200</td></tr><tr><td><code>maximum_distance</code></td><td>(Dynamic) Value</td><td>The farthest the item can fly from where it was thrown, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">96.0</td></tr><tr><td><code>maximum_owner_distance</code></td><td>(Dynamic) Value</td><td>The farthest the item can get from its owner, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">128.0</td></tr><tr><td><code>out_of_range</code></td><td><code>return</code><br><code>recover</code><br><code>drop</code></td><td>What happens when a limit is reached. The item is never deleted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">return</td></tr><tr><td><code>windup</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The delay before release, so an animation can play.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>combat</code> (Throw Combat)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>The damage dealt on a hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6.0</td></tr><tr><td><code>knockback</code></td><td>(Dynamic) Value</td><td>The knockback dealt on a hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>maximum_targets</code></td><td>(Dynamic) Value</td><td>How many entities one throw can hit. 0 means unlimited.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>entity_impact</code></td><td><code>continue</code><br><code>bounce</code><br><code>return</code><br><code>stop</code><br><code>embed</code></td><td>What the item does after hitting an entity. Embed lodges it in the mob, which it follows until recalled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">continue</td></tr><tr><td><code>allow_repeat_targets</code></td><td>Boolean</td><td>Whether the same entity can be hit more than once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>rehit_cooldown</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long until an entity can be hit again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_impact</code> (Throw Block Impact)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>bounce</code><br><code>embed</code><br><code>return</code><br><code>drop</code><br><code>stop</code></td><td>What the item does when it hits a block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">embed</td></tr><tr><td><code>restitution</code></td><td>(Dynamic) Value</td><td>How much speed a bounce keeps.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>friction</code></td><td>(Dynamic) Value</td><td>How much speed is kept while sliding along a block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.85</td></tr><tr><td><code>maximum_bounces</code></td><td>(Dynamic) Value</td><td>How many times the item can bounce.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>embed_depth</code></td><td>(Dynamic) Value</td><td>How deep the item sinks into the block, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>embed_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the item stays embedded. 0 means until recalled or picked up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>return</code> (Throw Return)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>triggers</code></td><td><code>none</code><br><code>after_hit</code><br><code>after_block_impact</code><br><code>after_timeout</code><br><code>after_distance</code><br><code>always</code>,<br><code>none</code><br><code>after_hit</code><br><code>after_block_impact</code><br><code>after_timeout</code><br><code>after_distance</code><br><code>always</code>[]</td><td>What makes the item return on its own.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;after_hit&quot; ]</td></tr><tr><td><code>timeout</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Return after this long when the timeout trigger is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60</td></tr><tr><td><code>distance</code></td><td>(Dynamic) Value</td><td>Return after this distance in blocks when the distance trigger is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32.0</td></tr><tr><td><code>speed</code></td><td>(Dynamic) Value</td><td>The speed of the return.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.4</td></tr><tr><td><code>acceleration</code></td><td>(Dynamic) Value</td><td>How quickly the return speeds up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>turn_rate</code></td><td>(Dynamic) Value</td><td>How fast the item steers towards its owner, in degrees per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">30.0</td></tr><tr><td><code>accuracy</code></td><td>(Dynamic) Value</td><td>How precisely the item steers, from 0 to 100.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr><tr><td><code>maximum_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>A safety limit for the return flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">200</td></tr><tr><td><code>block_collision</code></td><td><code>pass_through</code><br><code>stop</code></td><td>Whether the returning item passes through blocks or stops at them.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">stop</td></tr><tr><td><code>damage_enabled</code></td><td>Boolean</td><td>Whether the item hurts entities on the way back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>damage_multiplier</code></td><td>(Dynamic) Value</td><td>Multiplies the damage on the way back.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>maximum_damage_targets</code></td><td>(Dynamic) Value</td><td>How many entities the return can hit. 0 means unlimited.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>catch_radius</code></td><td>(Dynamic) Value</td><td>How close to the owner the item counts as caught, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.25</td></tr><tr><td><code>recall</code></td><td>Boolean</td><td>Activating the ability again while the item is out recalls it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

    <p class="argon-nested"><code>render</code> (Throw Render)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>scale</code></td><td>Float</td><td>The size of the item model.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>rotation_mode</code></td><td><code>none</code><br><code>spin</code><br><code>tumble</code></td><td>How the item turns in flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">spin</td></tr><tr><td><code>rotation_speed</code></td><td>Float</td><td>How fast the item turns, in degrees per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">36.0</td></tr><tr><td><code>rotation_axis</code></td><td><code>x</code><br><code>y</code><br><code>z</code></td><td>The axis the item turns around.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">x</td></tr><tr><td><code>rotation_offset</code></td><td>Vector 3D</td><td>A fixed rotation added to the model, as [x, y, z] degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ 0, 0, 0 ]</td></tr><tr><td><code>face_velocity</code></td><td>Boolean</td><td>Whether the item points along its flight direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>embed_spin_angle</code></td><td>Float</td><td>The angle the item sits at while embedded, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>embed_shift</code></td><td>Float</td><td>How far the model is moved along the throw direction while embedded in a block. Negative values pull it back out of the surface.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>sounds</code> (Throw Sounds)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>throw</code></td><td>Identifier</td><td>Played when the item is thrown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entity_hit</code></td><td>Identifier</td><td>Played when the item hits an entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>block_hit</code></td><td>Identifier</td><td>Played when the item hits a block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>recall</code></td><td>Identifier</td><td>Played when the item is recalled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>return</code></td><td>Identifier</td><td>Played when the item starts returning.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>catch</code></td><td>Identifier</td><td>Played when the item is caught.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>flight</code></td><td>Identifier</td><td>Loops while the item is flying.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>targeting</code> (Throw Targeting)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>none</code><br><code>automatic</code><br><code>marked</code><br><code>hybrid</code></td><td>How targets are picked. Marked uses targets set with the mark ability, hybrid combines both.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">none</td></tr><tr><td><code>accuracy</code></td><td>(Dynamic) Value</td><td>The chance of each acquisition attempt succeeding, from 0 to 100.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr><tr><td><code>detection_range</code></td><td>(Dynamic) Value</td><td>How far away targets are found, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">16.0</td></tr><tr><td><code>cone</code></td><td>(Dynamic) Value</td><td>The width of the search cone in front of the item, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">90.0</td></tr><tr><td><code>line_of_sight</code></td><td>Boolean</td><td>Whether targets have to be visible.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>filter</code></td><td><code>hostile</code><br><code>living</code><br><code>players</code><br><code>non_players</code></td><td>Which kinds of entities can be targeted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">hostile</td></tr><tr><td><code>entity_types</code></td><td>Entity Type ID(s) / Tag</td><td>Limits targets to these entity types or tags.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>priority</code></td><td><code>nearest</code><br><code>look_direction</code><br><code>lowest_health</code><br><code>random</code><br><code>marked_order</code></td><td>How one target is chosen from several.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">nearest</td></tr></tbody></table></div>

    <p class="argon-nested"><code>homing</code> (Throw Homing)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>accuracy</code></td><td>(Dynamic) Value</td><td>How precisely the item steers, from 0 to 100, independent of acquisition.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr><tr><td><code>turn_rate</code></td><td>(Dynamic) Value</td><td>How fast the item turns, in degrees per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">14.0</td></tr><tr><td><code>acceleration</code></td><td>(Dynamic) Value</td><td>How quickly the item speeds up while homing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max_speed</code></td><td>(Dynamic) Value</td><td>The top speed while homing. 0 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>prediction</code></td><td>(Dynamic) Value</td><td>How far ahead of a moving target the item aims.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>target_offset</code></td><td>(Dynamic) Value</td><td>The height on the target's body that is aimed at, as a fraction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>lost_target</code></td><td><code>continue</code><br><code>reacquire</code><br><code>return</code></td><td>What happens when the target is lost.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">continue</td></tr></tbody></table></div>

    <p class="argon-nested"><code>ricochet</code> (Throw Ricochet)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether the item jumps to another target after a hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>maximum</code></td><td>(Dynamic) Value</td><td>How many ricochets are allowed. 0 means one fewer than the maximum targets.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>target_range</code></td><td>(Dynamic) Value</td><td>How far the next target can be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10.0</td></tr><tr><td><code>speed</code></td><td>(Dynamic) Value</td><td>The speed between targets.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.6</td></tr><tr><td><code>turn_rate</code></td><td>(Dynamic) Value</td><td>How fast the item turns towards the next target, in degrees per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">40.0</td></tr><tr><td><code>damage_multiplier</code></td><td>(Dynamic) Value</td><td>Multiplies the damage of ricochet hits.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>steering</code> (Throw Steering)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>none</code><br><code>look_direction</code><br><code>projectile_camera</code></td><td>How the owner steers the item while an argon:throw_steer ability is held.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">none</td></tr><tr><td><code>turn_rate</code></td><td>(Dynamic) Value</td><td>How fast the item turns, in degrees per tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10.0</td></tr><tr><td><code>strength</code></td><td>(Dynamic) Value</td><td>How strongly the steering input is applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>maximum_speed</code></td><td>(Dynamic) Value</td><td>The top speed while steering. 0 means the throw speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>acceleration</code></td><td>(Dynamic) Value</td><td>How quickly the item speeds up while steering.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.08</td></tr><tr><td><code>return_on_release</code></td><td>Boolean</td><td>Whether the item returns when the steering ability is let go.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>owner_control</code></td><td><code>normal</code><br><code>limited</code><br><code>immobile</code></td><td>How much the owner can move while steering.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">limited</td></tr></tbody></table></div>

    <p class="argon-nested"><code>camera</code> (Throw Camera)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>distance</code></td><td>(Dynamic) Value</td><td>How far behind the item the camera sits, in blocks. 0 means from the item.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5.0</td></tr><tr><td><code>fov</code></td><td>(Dynamic) Value</td><td>The field of view. 0 leaves it unchanged.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>smoothing</code></td><td>(Dynamic) Value</td><td>How smoothly the camera follows the item.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.35</td></tr><tr><td><code>roll</code></td><td>(Dynamic) Value</td><td>How far the camera is rolled, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>perfect_catch</code> (Throw Perfect Catch)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether a well-timed catch gives a bonus.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>window</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long before arrival the catch counts as perfect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8</td></tr><tr><td><code>damage_bonus</code></td><td>(Dynamic) Value</td><td>Multiplier on the damage of the next throw.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>bonus_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the bonus lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr></tbody></table></div>

    <p class="argon-nested"><code>pin</code> (Throw Pin)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether a hit entity is pinned to a wall behind it. Players and bosses are never pinned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the target stays pinned. 0 means until the owner recalls the item.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">60</td></tr><tr><td><code>distance</code></td><td>(Dynamic) Value</td><td>How far behind the target the wall can be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>deflection</code> (Throw Deflection)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether the item deflects projectiles it flies through.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>How close a projectile has to be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.6</td></tr><tr><td><code>strength</code></td><td>(Dynamic) Value</td><td>Speed multiplier of deflected projectiles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>target_filter</code></td><td>Entity Type ID(s) / Tag</td><td>Limits which projectiles are deflected to these entity types or tags.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:throwable_item",
      "item": [],
      "pickup": {
        "radius": 1.5
      },
      "properties": {}
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "throwable_item": {
          "type": "argon:throwable_item",
          "item": [],
          "pickup": {
            "radius": 1.5
          },
          "properties": {}
        }
      }
    }
    ```

---

### Path Vision {#argonpath_vision}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:path_vision</code></div>

<div class="argon-desc">Client only. Shows where nearby entities and projectiles are heading: a mob's AI route, a short prediction for other movers, a projectile's predicted flight. Drawn as a trail, changes nothing.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>detection_radius</code></td><td>Double (1.0 ~ 256.0)</td><td>How far from the holder, in blocks, entities and projectiles are looked for. Only loaded entities are ever considered.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">24.0</td></tr><tr><td><code>max_targets</code></td><td>Integer (1 ~ 128)</td><td>The most targets shown at once. Which ones are kept when there are more is decided by target_priority.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">16</td></tr><tr><td><code>target_priority</code></td><td><code>closest</code><br><code>hostile_first</code><br><code>projectiles_first</code></td><td>Which targets are kept when more than max_targets are in range and which come first: "closest" orders by distance, "hostile_first" puts hostile mobs before everything else, "projectiles_first" puts projectiles first. Within a group the closest come first.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">closest</td></tr><tr><td><code>path_update_interval</code></td><td>Integer (1 ~ 40)</td><td>How often paths are recalculated. Between updates the trail follows the target smoothly, and a new navigation path from the server updates it immediately.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2</td></tr><tr><td><code>max_path_length</code></td><td>Double (1.0 ~ 512.0)</td><td>The longest stretch of path shown, measured along the path itself from the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32.0</td></tr><tr><td><code>track</code></td><td>string[]</td><td>What is shown, mixing categories ("players", "hostile", "passive", "neutral", "projectiles", "mobs", "all") with entity type ids and "#tags". Listed types and tags are tracked whatever their category. An unknown entry stops the power from loading.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[ &quot;players&quot;, &quot;hostile&quot;, &quot;neutral&quot;, &quot;projectiles&quot; ]</td></tr><tr><td><code>ignore</code></td><td>string[]</td><td>Anything that matches here is never shown, even when it matches track. Takes the same entries as track.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>show_entity_paths</code></td><td>Boolean</td><td>Whether paths are shown for mobs and players.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>predict_entity_movement</code></td><td>Boolean</td><td>Whether an entity with no active path gets a physics prediction from its recent velocity. It is an estimate, not a destination, and assumes the entity keeps going the way it is going.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>entity_prediction_time</code></td><td>Double (0.1 ~ 10.0)</td><td>How far ahead entity movement is predicted. Longer predictions get less reliable.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>show_projectile_paths</code></td><td>Boolean</td><td>Whether the flight of projectiles is shown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>projectile_prediction_time</code></td><td>Double (0.1 ~ 10.0)</td><td>How far ahead a projectile's flight is simulated. The path also stops at the first expected collision.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>show_projectile_impact</code></td><td>Boolean</td><td>Whether a particle marks where a projectile is expected to hit. Nothing shows when no impact is predicted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_time_to_impact</code></td><td>Boolean</td><td>Whether the time left before the predicted impact is written above the impact point, such as 0.8s.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>impact_particle</code></td><td>Particle</td><td>The particle that marks the predicted impact, as a particle type ID or a particle object.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">minecraft:end_rod</td></tr><tr><td><code>preview_aimed_shots</code></td><td>Boolean</td><td>Shows the path a shot would take while its shooter aims (a drawn bow, ready trident or loaded crossbow) instead of following fired projectiles. Ends at the first block or tracked entity hit and uses projectile_trail. Fireworks aren't predicted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>aim_charge_color</code></td><td>Color</td><td>preview_aimed_shots only. The aim line's color when the draw has just started, shifting to the projectile trail's color as the shot gets ready. Set it to the trail's color to turn the shift off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FFD23F</td></tr><tr><td><code>entity_trail</code></td><td>Identifier</td><td>The Palladium trail (palladium/trails/<path>.json) that draws entity paths. Its renderer, lifetime, offset and spacing set the look.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">argon:path_vision_entity</td></tr><tr><td><code>projectile_trail</code></td><td>Identifier</td><td>The Palladium trail that draws projectile paths, set up like entity_trail so projectiles can look different from entities. Defaults to "argon:path_vision_projectile".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">argon:path_vision_projectile</td></tr><tr><td><code>trail_render_distance</code></td><td>Double (4.0 ~ 512.0)</td><td>Paths of targets farther than this from the camera are not drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">64.0</td></tr><tr><td><code>trail_smoothing</code></td><td>Float (0.0 ~ 1.0)</td><td>How much navigation corners are rounded. A rounded stretch that would pass through a block is left sharp instead.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.7</td></tr><tr><td><code>render_through_walls</code></td><td>Boolean</td><td>Whether the trail can be seen through blocks. Applies to trails drawn with Palladium's laser render types, which includes the gradient and lightning trails.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:path_vision",
      "detection_radius": 24,
      "max_targets": 16,
      "entity_trail": "argon:path_vision_entity",
      "projectile_trail": "argon:path_vision_projectile",
      "show_time_to_impact": true,
      "track": [
        "hostile",
        "projectiles",
        "minecraft:villager"
      ],
      "ignore": [
        "#minecraft:undead"
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "path_vision": {
          "type": "argon:path_vision",
          "detection_radius": 24,
          "max_targets": 16,
          "entity_trail": "argon:path_vision_entity",
          "projectile_trail": "argon:path_vision_projectile",
          "show_time_to_impact": true,
          "track": [
            "hostile",
            "projectiles",
            "minecraft:villager"
          ],
          "ignore": [
            "#minecraft:undead"
          ]
        }
      }
    }
    ```

---

### Possess {#argonpossess}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:possess</code></div>

<div class="argon-desc">Lets the user see through, and optionally control the movement of, a possessed living entity until a set exit condition triggers.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far away a living entity can be to be possessed in the first place.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>end_on_damage</code></td><td>Boolean</td><td>If true, the user's own body taking damage while possessing immediately ends the possession.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>jumps</code></td><td>Integer (&gt;= 0)</td><td>How many times the user can jump straight from one possessed target to another, or never if 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>distance_from_body</code></td><td>Double</td><td>If set, possession ends once the target strays this many blocks from the user's stationary body.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>control_target_movement</code></td><td>Boolean</td><td>If true, the user's movement input controls the target instead of being locked. For players it is gated by the possessMovementOverrideCanAffectPlayers config option.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:possess",
      "range": 16,
      "properties": {
        "title": "Possess"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "possess": {
          "type": "argon:possess",
          "range": 16,
          "properties": {
            "title": "Possess"
          }
        }
      }
    }
    ```

---

### Potion Hit {#argonpotion_hit}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:potion_hit</code></div>

<div class="argon-desc">While enabled, applies a list of status effects to any living entity this one lands a damaging hit on.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effects</code></td><td><em>Potion Hit Effect</em>,<br><em>Potion Hit Effect</em>[]</td><td>Each entry configures its own effect, duration, amplifier*, max_amplifier* (ceiling for stackable_amplifier, default 255) and particles* (default true).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>stackable_duration</code></td><td>Boolean</td><td>If true, hitting a target that already has the effect adds the configured duration to its remaining time instead of resetting it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>stackable_amplifier</code></td><td>Boolean</td><td>If true, hitting a target that already has the effect raises its amplifier by one level (up to that entry's max_amplifier) instead of keeping the configured amplifier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>amplifier_stack_condition</code></td><td>Condition,<br>Condition[]</td><td>A condition, tested against the target, that must pass for stackable_amplifier to raise the amplifier on a repeat hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects</code> (Potion Hit Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_amplifier</code></td><td>Integer</td><td>The highest level repeated hits can stack the effect up to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:potion_hit",
      "effects": {
        "effect": "minecraft:poison",
        "duration": 100,
        "max_amplifier": 3
      },
      "stackable_duration": true,
      "stackable_amplifier": true
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:potion_hit",
      "effects": [
        {
          "effect": "minecraft:poison",
          "duration": "5s",
          "amplifier": 0,
          "max_amplifier": 3
        }
      ],
      "stackable_duration": true,
      "stackable_amplifier": true
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "potion_hit": {
          "type": "argon:potion_hit",
          "effects": {
            "effect": "minecraft:poison",
            "duration": 100,
            "max_amplifier": 3
          },
          "stackable_duration": true,
          "stackable_amplifier": true
        }
      }
    }
    ```

---

### Power Transfer {#argonpower_transfer}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:power_transfer</code></div>

<div class="argon-desc">On activation, opens a GUI for transferring superpower powers between the user and a nearby entity under the crosshair.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_range</code></td><td>Double</td><td>Maximum crosshair distance to a living entity for it to become the transfer target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:power_transfer",
      "properties": {
        "title": "Power Transfer"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "power_transfer": {
          "type": "argon:power_transfer",
          "properties": {
            "title": "Power Transfer"
          }
        }
      }
    }
    ```

---

### Projectile Effect {#argonprojectile_effect}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:projectile_effect</code></div>

<div class="argon-desc">Shoots a projectile like the built-in projectile ability, and can also give one or more status effects to the living entity it hits.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_type</code></td><td>Entity Type ID</td><td>ID of an entity type (must be a projectile).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entity_data</code></td><td>NBT</td><td>Additional NBT data for the projectile entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>inaccuracy</code></td><td>(Dynamic) Value</td><td>Inaccuracy when shooting the projectile. A value, so it can change with conditions (for example a wider spread while overloaded).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>velocity</code></td><td>Float (&gt;= 0.0)</td><td>Velocity with which the projectile is being shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>swinging_arm</code></td><td><code>none</code><br><code>main_arm</code><br><code>off_arm</code><br><code>right_arm</code><br><code>left_arm</code><br><code>both</code></td><td>The arm which will swing when the projectile is being shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">MAIN_ARM</td></tr><tr><td><code>ignore_player_movement</code></td><td>Boolean</td><td>Normally the player's current velocity is added to the projectile's velocity. This turns that off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>offset</code></td><td>Vector 3D</td><td>A [x, y, z] spawn offset, relative to the entity's facing direction. Defaults to [0, 0, 0].</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">(0.0, 0.0, 0.0)</td></tr><tr><td><code>hit_effects</code></td><td><em>Projectile Hit Effect</em>,<br><em>Projectile Hit Effect</em>[]</td><td>Each entry configures its own effect, duration, amplifier*, particles*, and powers* (a list of {power, mode} entries, where "power" is an explicit power id, a power tag ("#namespace:tag"), or a mix of both - "include" requires a matching power, "exclude" forbids one) - all entries are granted to whatever living entity the projectile directly hits. Empty by default, meaning no effect is granted.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>item_tint</code></td><td><em>Item Tint</em></td><td>Only meaningful for an entity_type whose appearance includes an "item" appearance (e.g. "palladium:custom_projectile"). Tints every such appearance's item using whatever colour a registered source reads off an item in "slot" (a Palladium player slot, e.g. "mainhand", "curios:hands" - every item currently in that slot is checked, and the first one "source" finds a colour on wins), the same way a dyed item is tinted - so this only has a visible effect if the appearance item's own model has a tint-indexed layer to begin with. An id nothing has registered, or no matching item in the slot, silently leaves the appearance untinted; omit "item_tint" entirely for a projectile that should never be tinted.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_range</code></td><td>Double</td><td>If above 0, the projectile disappears once it has flown this many blocks from where it was shot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>sprint_interrupt</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>If above 0, a living entity the projectile hits cannot sprint for this long.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>hit_effects</code> (Projectile Hit Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>powers</code></td><td><em>Power Requirement</em>,<br><em>Power Requirement</em>[]</td><td>Only targets that match these power requirements get the effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>hit_effects.powers</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

    <p class="argon-nested"><code>item_tint</code> (Item Tint)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slot of the item that is tinted.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>source</code></td><td>Identifier</td><td>The tint source used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:projectile_effect",
      "inaccuracy": 0
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:projectile_effect",
      "inaccuracy": 0,
      "hit_effects": {
        "effect": "minecraft:slowness",
        "duration": 100,
        "amplifier": 1
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "projectile_effect": {
          "type": "argon:projectile_effect",
          "inaccuracy": 0
        }
      }
    }
    ```

---

### Push {#argonpush}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:push</code></div>

<div class="argon-desc">On activation, applies a one-time vertical or horizontal push to every living entity in range. The sign of the amount decides push or pull.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far from the entity other living entities can be to be affected.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>vertical</code><br><code>horizontal</code></td><td>Whether to push vertically (up/down) or horizontally (away from/toward the user).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amount</code></td><td>(Dynamic) Value</td><td>The velocity applied. The sign sets the direction: up/down for vertical, away from/toward the user for horizontal.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:push",
      "range": 5,
      "mode": "horizontal",
      "amount": 1.2
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "push": {
          "type": "argon:push",
          "range": 5,
          "mode": "horizontal",
          "amount": 1.2
        }
      }
    }
    ```

---

### Push Field {#argonpush_field}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:push_field</code></div>

<div class="argon-desc">While enabled, constantly pushes every living entity touching the user's hitbox (optionally inflated), vertically or horizontally. The sign of the amount decides push or pull.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>inflation</code></td><td>Double</td><td>How much to inflate the entity's hitbox when checking for entities to affect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>mode</code></td><td><code>vertical</code><br><code>horizontal</code></td><td>Whether to push vertically (up/down) or horizontally (away from/toward the user).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amount</code></td><td>Double</td><td>The velocity applied each tick. The sign sets the direction: up/down for vertical, away from/toward the user for horizontal.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>affect_projectiles</code></td><td>Boolean</td><td>Whether projectiles touching the hitbox should also be pushed, in addition to living entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:push_field",
      "inflation": 0.5,
      "mode": "horizontal",
      "amount": 0.4
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "push_field": {
          "type": "argon:push_field",
          "inflation": 0.5,
          "mode": "horizontal",
          "amount": 0.4
        }
      }
    }
    ```

---

### Quarry Sense {#argonquarry_sense}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:quarry_sense</code></div>

<div class="argon-desc">Client only. While enabled, outlines (through walls, only for the holder) every non-allied living entity within "radius", colored by how hurt it is: healthy, wounded and critical. Can hide healthy entities so only damaged ones show, can limit the sense to hostile mobs and players, and can leave a fading trail of dust where each outlined entity recently walked.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>How far the sense reaches, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32</td></tr><tr><td><code>healthy_color</code></td><td>Color</td><td>Outline color of an entity above wounded_below.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#B8C8E0</td></tr><tr><td><code>wounded_color</code></td><td>Color</td><td>Outline color of an entity at or below wounded_below.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FF8A3A</td></tr><tr><td><code>critical_color</code></td><td>Color</td><td>Outline color of an entity at or below critical_below.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FF2A2A</td></tr><tr><td><code>wounded_below</code></td><td>Double</td><td>The health fraction (0 to 1) at or below which an entity counts as wounded. The default counts any missing health.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.999</td></tr><tr><td><code>critical_below</code></td><td>Double</td><td>The health fraction (0 to 1) at or below which an entity counts as critical.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>show_healthy</code></td><td>Boolean</td><td>If false, entities that are not wounded are not outlined at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>hostile_only</code></td><td>Boolean</td><td>If true, only hostile mobs (and neutral ones targeting the holder) and non-allied players are sensed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>trails</code></td><td>Boolean</td><td>If true, a fading trail of dust marks where each sensed entity recently walked.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:quarry_sense",
      "radius": 32,
      "properties": {
        "title": "Quarry Sense"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "quarry_sense": {
          "type": "argon:quarry_sense",
          "radius": 32,
          "properties": {
            "title": "Quarry Sense"
          }
        }
      }
    }
    ```

---

### Radar {#argonradar}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:radar</code></div>

<div class="argon-desc">Creates a client-side radar that displays nearby entities within range.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>translate</code></td><td>Vector 2D</td><td>The X/Y onscreen position of the radar relative to the alignment.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">Translate[x=net.threetag.palladium.logic.value.StaticValue@6b37cadf, y=net.threetag.palladium.logic.value.StaticValue@6b37cadf]</td></tr><tr><td><code>alignment</code></td><td><code>top_left</code><br><code>top_center</code><br><code>top_right</code><br><code>middle_left</code><br><code>center</code><br><code>middle_right</code><br><code>bottom_left</code><br><code>bottom_center</code><br><code>bottom_right</code></td><td>Determines where on the screen the radar is anchored.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">TOP_RIGHT</td></tr><tr><td><code>radius</code></td><td>Float</td><td>The radius of the radar, in pixels.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">50.0</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The radius, in blocks, within which entities are detected and shown on the radar.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">net.threetag.palladium.logic.value.StaticValue@2c018211</td></tr><tr><td><code>shape</code></td><td><code>square</code><br><code>circle</code></td><td>The shape of the radar's background and border, either square or circle.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">CIRCLE</td></tr><tr><td><code>rotation</code></td><td><em>Radar Rotation</em></td><td>Whether the radar should rotate with the player, or be static.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">Rotation[mode=LOOK_DIRECTION, staticAngle=net.threetag.palladium.logic.value.StaticValue@6b37cadf]</td></tr><tr><td><code>background_color</code></td><td>Color</td><td>The color of the radar's background fill.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#000000</td></tr><tr><td><code>background_opacity</code></td><td>Float</td><td>How opaque the radar's background fill is, from 0 (invisible) to 1 (fully opaque).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>border</code></td><td><em>Radar Border</em></td><td>The radar's border color and thickness in pixels, where 0 hides the border.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">Border[color=java.awt.Color[r=170,g=170,b=170], thickness=2]</td></tr><tr><td><code>player_color</code></td><td>Color</td><td>The blip color used for the user's own position, and for any other players shown on the radar.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#55FFFF</td></tr><tr><td><code>hostile_color</code></td><td>Color</td><td>The blip color used for hostile mobs.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FF5555</td></tr><tr><td><code>passive_color</code></td><td>Color</td><td>The blip color used for non-hostile mobs.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#55FF55</td></tr><tr><td><code>attachment_overrides</code></td><td><em>Radar Override</em>[]</td><td>Use data_attachments for specialized results in the radar.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>rotation</code> (Radar Rotation)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>look_direction</code><br><code>static</code></td><td>Whether the radar turns with the user's view or stays fixed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>static_angle</code></td><td>(Dynamic) Value</td><td>The fixed angle in degrees when the mode is static.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>border</code> (Radar Border)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>color</code></td><td>Color</td><td>The color of the border.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>thickness</code></td><td>Integer</td><td>The thickness of the border in pixels.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>attachment_overrides[]</code> (Radar Override)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>data_attachment</code></td><td>Data Attachment ID</td><td>The data attachment that is checked.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>String</td><td>The attachment value that triggers the override.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>color</code></td><td>Color</td><td>The color used for matching entities.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The range used for matching entities.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:radar",
      "range": 32,
      "properties": {
        "title": "Radar"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:radar",
      "translate": {
        "x": {
          "type": "palladium:float_data_attachment",
          "attachment": "example:translate_x_attachment"
        },
        "y": {
          "type": "palladium:float_data_attachment",
          "attachment": "example:translate_y_attachment"
        }
      },
      "range": 32,
      "rotation": {
        "mode": "static",
        "static_angle": 90
      },
      "attachment_overrides": [
        {
          "data_attachment": "argon:first_person_view",
          "value": "true",
          "color": "#ffff00",
          "range": 128
        }
      ],
      "properties": {
        "title": "Radar"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "radar": {
          "type": "argon:radar",
          "range": 32,
          "properties": {
            "title": "Radar"
          }
        }
      }
    }
    ```

---

### Random Effect {#argonrandom_effect}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:random_effect</code></div>

<div class="argon-desc">While enabled, gives the user one randomly chosen status effect from a list every "interval" ticks. Each roll is independent, so the same effect can repeat.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effects</code></td><td><em>Random Effect</em>[]</td><td>The pool of effects to randomly choose from, each entry giving an effect, duration, and optional amplifier, particles, and show_icon.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long to wait between rolls.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Random Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect that can be picked.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>show_icon</code></td><td>Boolean</td><td>Whether the effect icon is shown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:random_effect",
      "effects": [
        {
          "effect": "minecraft:speed",
          "duration": 100
        },
        {
          "effect": "minecraft:regeneration",
          "duration": 60,
          "amplifier": 1,
          "particles": false
        }
      ],
      "properties": {
        "title": "Random Effect"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "random_effect": {
          "type": "argon:random_effect",
          "effects": [
            {
              "effect": "minecraft:speed",
              "duration": 100
            },
            {
              "effect": "minecraft:regeneration",
              "duration": 60,
              "amplifier": 1,
              "particles": false
            }
          ],
          "properties": {
            "title": "Random Effect"
          }
        }
      }
    }
    ```

---

### Recite {#argonrecite}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:recite</code></div>

<div class="argon-desc">Says the last spell the user cast, at their current mastery tier, as if typed in chat. Other spell systems can register a recite hook, and whichever system cast most recently is the one recited. If it is a toggle that is already on, it says the stop phrase instead. Cooldown, the spell being unlocked and the voiceless effect still apply.</div>

---

### Reconstruction {#argonreconstruction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:reconstruction</code></div>

<div class="argon-desc">On activation, matches the item in "target_slot" against "reconstructions" and uses up the first match with enough input to make its result. With "recipe", hold to browse crafting recipes for the held item and release to swap.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>reconstructions</code></td><td><em>Reconstruction Entry</em>[],<br><code>recipe</code></td><td>The ordered list of input-to-result conversions this ability can perform, or the literal string "recipe" to browse crafting table recipes that use the held item instead. In recipe mode every other ingredient is ignored and only the held item is consumed.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>target_slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot's item is checked and consumed; defaults to the main hand.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">mainhand</td></tr><tr><td><code>conversion_mode</code></td><td><code>single</code><br><code>maximum</code><br><code>fixed</code></td><td>SINGLE applies the matched recipe once, MAXIMUM as many times as the input allows, FIXED up to "fixed_amount" times. Ignored in recipe mode.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SINGLE</td></tr><tr><td><code>fixed_amount</code></td><td>Integer (&gt; 0)</td><td>How many times to apply the recipe when conversion_mode is FIXED. Ignored in recipe mode.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>overflow_behavior</code></td><td><code>fail</code><br><code>drop</code></td><td>FAIL cancels the whole conversion if the result can't fully fit in the inventory. DROP inserts what fits and drops the rest at the user's feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">FAIL</td></tr><tr><td><code>component_policy</code></td><td><code>result_only</code><br><code>copy_safe</code><br><code>copy_all</code></td><td>RESULT_ONLY uses exactly the result's components. COPY_SAFE also copies cosmetic ones (name, lore, dye color, custom model data) from the input. COPY_ALL copies every component that differs from the item's defaults.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">RESULT_ONLY</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reconstructions[]</code> (Reconstruction Entry)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>input</code></td><td>Ingredient / Item</td><td>The item or tag that is used up.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>input_amount</code></td><td>Integer (&gt; 0)</td><td>How many of the input are used up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>result</code></td><td>Item / ItemStack</td><td>The item stack that is made.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>result_amount</code></td><td>Integer (&gt; 0)</td><td>Overrides the amount of the result.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>priority</code></td><td>Integer</td><td>Entries with a higher priority are checked first.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:reconstruction",
      "reconstructions": {
        "input": "minecraft:iron_ingot",
        "input_amount": 3,
        "result": {
          "id": "minecraft:iron_pickaxe",
          "count": 1
        }
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:reconstruction",
      "reconstructions": "recipe"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "reconstruction": {
          "type": "argon:reconstruction",
          "reconstructions": {
            "input": "minecraft:iron_ingot",
            "input_amount": 3,
            "result": {
              "id": "minecraft:iron_pickaxe",
              "count": 1
            }
          }
        }
      }
    }
    ```

---

### Reveal {#argonreveal}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:reveal</code></div>

<div class="argon-desc">While enabled, shows a nametag above every entity within radius, visible only to the ability holder and through walls unless blocked by the block types in blocked_by.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>The radius, in blocks, within which entities are revealed.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>entities</code></td><td><code>living</code><br><code>all</code></td><td>Which entities to reveal, either living entities only (excluding armor stands) or all entities, including non-living ones which only show a name.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">LIVING</td></tr><tr><td><code>show_name</code></td><td>Boolean</td><td>Whether to show the entity's name.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>show_health</code></td><td>Boolean</td><td>Whether to show the entity's current / max health.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>show_powers</code></td><td>Boolean</td><td>Whether to show the entity's Palladium powers, by name.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>show_effects</code></td><td>Boolean</td><td>Whether to list the entity's active effects with their remaining time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>filter</code></td><td><em>Reveal Filter</em></td><td>If set, only entities that match at least one of these are revealed: their type is in entity_tag, they have any active effect, or they own a matching power.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>look_target_only</code></td><td>Boolean</td><td>If true, only the living entity the user is looking at, within the radius, is revealed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>hostile_name_color</code></td><td>Color</td><td>If set, overrides just the name's color (not health/powers) for hostile entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>passive_name_color</code></td><td>Color</td><td>If set, overrides just the name's color (not health/powers) for non-hostile entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blocked_by</code></td><td>Block ID(s) / Tag</td><td>If set, hides a revealed entity's tag when one of these block types blocks the line of sight to the caster's eyes.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>filter</code> (Reveal Filter)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag are revealed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>any_effect</code></td><td>Boolean</td><td>Only entities with at least one effect are revealed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>power</code></td><td><em>Power Requirement</em></td><td>Only entities that match this power requirement are revealed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>filter.power</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:reveal",
      "radius": 16,
      "show_health": true,
      "show_powers": true,
      "hostile_name_color": "#ff0000",
      "passive_name_color": "#00ff00",
      "properties": {
        "title": "Reveal"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "reveal": {
          "type": "argon:reveal",
          "radius": 16,
          "show_health": true,
          "show_powers": true,
          "hostile_name_color": "#ff0000",
          "passive_name_color": "#00ff00",
          "properties": {
            "title": "Reveal"
          }
        }
      }
    }
    ```

---

### Rotate {#argonrotate}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:rotate</code></div>

<div class="argon-desc">While enabled, turns the entity around the vertical axis by "degrees_per_tick" every tick. The camera turns with it for players.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>degrees_per_tick</code></td><td>Float</td><td>How many degrees of yaw to add each tick while enabled. Negative values spin the other direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">18.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:rotate"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "rotate": {
          "type": "argon:rotate"
        }
      }
    }
    ```

---

### Saturation {#argonsaturation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:saturation</code></div>

<div class="argon-desc">On activation, adds or removes the given amount of saturation and/or food level (hunger bar), each kept between 0 and 20. Only affects players.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>amount</code></td><td>Float</td><td>How much saturation to add, or remove if negative.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>food</code></td><td>Integer</td><td>How much food level (hunger bar) to add, or remove if negative.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:saturation",
      "amount": 4,
      "food": 2
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "saturation": {
          "type": "argon:saturation",
          "amount": 4,
          "food": 2
        }
      }
    }
    ```

---

### Save Location {#argonsave_location}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:save_location</code></div>

<div class="argon-desc">When activated, saves the entity's position, facing and dimension under "namespace" (replacing any earlier save there). It stays on the entity for argon:teleport_to_location to use later.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>namespace</code></td><td>String</td><td>The name the location is saved under. Any argon:teleport_to_location ability on any power can read it with the same namespace.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:save_location",
      "namespace": "home"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "save_location": {
          "type": "argon:save_location",
          "namespace": "home"
        }
      }
    }
    ```

---

### Screen Shake {#argonscreen_shake}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:screen_shake</code></div>

<div class="argon-desc">While enabled, shakes only the holder's camera. Each pulse varies randomly between base_intensity and max_intensity. With an animation_timer both are scaled by it, so the shake builds up and dies down.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>base_intensity</code></td><td>Float</td><td>The weakest a single shake pulse can be.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_intensity</code></td><td>Float</td><td>The strongest a single shake pulse can be.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:screen_shake",
      "base_intensity": 0.5,
      "max_intensity": 2
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "screen_shake": {
          "type": "argon:screen_shake",
          "base_intensity": 0.5,
          "max_intensity": 2
        }
      }
    }
    ```

---

### Seek Strike {#argonseek_strike}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:seek_strike</code></div>

<div class="argon-desc">On activation, picks up to "max_targets" living entities around the user and rushes between them one after another, hitting each once with fixed damage and knockback. Allies are skipped, and a target is skipped when solid blocks are in the way. The user stays beside the last target. All Values are read once on activation.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far from the user targets can be chosen, in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_targets</code></td><td>(Dynamic) Value</td><td>How many targets are hit at most. Each can only be hit once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>The final damage of each hit. The user's attack damage is not added.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used; a player attack when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>knockback</code></td><td>(Dynamic) Value</td><td>Knockback strength of each hit, where 0.4 is a normal hit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>lift</code></td><td>(Dynamic) Value</td><td>Upward velocity added to every hit target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.2</td></tr><tr><td><code>speed</code></td><td>Double</td><td>How many blocks per tick the user travels towards a target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.5</td></tr><tr><td><code>reach</code></td><td>Double</td><td>How close, in blocks, the user gets to a target before striking.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.8</td></tr><tr><td><code>aim</code></td><td><code>look</code><br><code>nearest</code><br><code>marked</code></td><td>"look" picks the entity under the crosshair first, otherwise the nearest one inside cone_angle. "nearest" starts from the entity closest to the user. "marked" only goes for the user's argon:target_mark target (hostile_only is ignored, and nothing happens without a mark).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">look</td></tr><tr><td><code>cone_angle</code></td><td>Double</td><td>The full opening angle of the look cone, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">90.0</td></tr><tr><td><code>hostile_only</code></td><td>Boolean</td><td>If true, only hostile mobs and other players can be picked.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>end_effects</code></td><td><em>Potion Hit Effect</em>,<br><em>Potion Hit Effect</em>[]</td><td>Effects applied to the user after the last hit, for example a short slowdown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>hit_visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle visuals spawned at each target when it is hit, in the same format as the visuals of argon:energy_beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>travel_visuals</code></td><td><em>Beam Visual</em>[]</td><td>Particle visuals spawned along every step of the rush, for example a streak.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>hit_sound</code></td><td>Identifier</td><td>A sound event played at every target when it is hit, instead of the default hit sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>hit_sound_volume</code></td><td>Float</td><td>Volume of hit_sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>hit_sound_pitch</code></td><td>Float</td><td>Pitch of hit_sound.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.9</td></tr><tr><td><code>hit_effects</code></td><td><em>Potion Hit Effect</em>,<br><em>Potion Hit Effect</em>[]</td><td>Effects applied to every target that is hit, for example a short slowdown that interrupts its movement.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>consume_mark</code></td><td>Boolean</td><td>If true, a hit on the user's marked target ends the mark.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>execute_threshold</code></td><td>Double</td><td>A target at or below this health fraction (0 to 1) takes execute_bonus extra damage. 0 disables it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>execute_bonus</code></td><td>(Dynamic) Value</td><td>The extra damage dealt to a target under execute_threshold.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>dash</code></td><td>Boolean</td><td>If true and no target was chosen, the user dashes straight along the look direction for up to range blocks (stopping at walls) and strikes the first valid entity it touches. Not used with aim marked.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>exit_speed</code></td><td>Double</td><td>Speed in blocks per tick the user keeps along the last movement direction when the rush ends, instead of stopping dead.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

    <p class="argon-nested"><code>end_effects</code> (Potion Hit Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_amplifier</code></td><td>Integer</td><td>The highest level repeated hits can stack the effect up to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>hit_visuals[]</code> (Beam Visual)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>shape</code></td><td><code>streak</code><br><code>helix</code><br><code>ring</code><br><code>sphere</code><br><code>burst</code><br><code>crescent</code></td><td>The particle pattern to draw.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor</code></td><td><code>end</code><br><code>caster</code></td><td>Whether the pattern is drawn at the end of the beam or around the caster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>orientation</code></td><td><code>horizontal</code><br><code>vertical</code></td><td>How ring and crescent patterns are turned.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>The particle used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 512)</td><td>How many particles the pattern uses.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Float (0.0 ~ 64.0)</td><td>The radius of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>step</code></td><td>Float (0.05 ~ 16.0)</td><td>The spacing between particles along the beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pitch</code></td><td>Float (0.1 ~ 64.0)</td><td>The length of one full twist for helixes, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strands</code></td><td>Integer (1 ~ 8)</td><td>How many strands a helix has.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>arc</code></td><td>Float (1.0 ~ 360.0)</td><td>How much of a circle is drawn, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>height</code></td><td>Float</td><td>The height of the pattern in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rings</code></td><td>Integer (1 ~ 16)</td><td>How many rings are drawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Float (0.0 ~ 8.0)</td><td>How far the particles scatter.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:seek_strike",
      "range": 10,
      "max_targets": 1,
      "damage": 8,
      "knockback": 0.8,
      "lift": 0.2,
      "execute_bonus": 0,
      "properties": {
        "title": "Seek Strike"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "seek_strike": {
          "type": "argon:seek_strike",
          "range": 10,
          "max_targets": 1,
          "damage": 8,
          "knockback": 0.8,
          "lift": 0.2,
          "execute_bonus": 0,
          "properties": {
            "title": "Seek Strike"
          }
        }
      }
    }
    ```

---

### Sensory Overload {#argonsensory_overload}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:sensory_overload</code></div>

<div class="argon-desc">While enabled, overwhelms the wearer's senses: a visual only warp, lagging camera, screen shake, activation flash, pulsing tint and muffled non-music sound.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>warp_intensity</code></td><td>Float</td><td>How strong the nausea style screen warp is, 0 (none) to 2 (well past the vanilla effect). It copies the vanilla look directly and doesn't apply the real Nausea effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>drag_strength</code></td><td>Float</td><td>How much the rendered view drags behind the wearer's real look direction, 0 (none) to 1 (heavy).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>shake_base_intensity</code></td><td>Float</td><td>The weakest a single camera-shake pulse can be.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.1</td></tr><tr><td><code>shake_max_intensity</code></td><td>Float</td><td>The strongest a single camera-shake pulse can be.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>flash_enabled</code></td><td>Boolean</td><td>Whether a brief full-screen flash plays on activation.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>flash_color</code></td><td>Color</td><td>The color of the activation flash, when flash_enabled is true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FFFFFF</td></tr><tr><td><code>flash_fade_ticks</code></td><td>Integer</td><td>How many ticks the activation flash takes to fade from full brightness to nothing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">15</td></tr><tr><td><code>pulse_color</code></td><td>Color</td><td>The color of the full-screen tint that pulses while enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FFFFFF</td></tr><tr><td><code>pulse_opacity</code></td><td>Float</td><td>The pulsing tint's peak opacity at the brightest point of each pulse.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>pulse_speed</code></td><td>Float</td><td>How many pulses per second the full-screen tint cycles through.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>mute_volume</code></td><td>Float</td><td>Volume multiplier applied to non-music sounds while enabled, from 0 (silent) to 1 (unchanged).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:sensory_overload",
      "properties": {
        "title": "Sensory Overload"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "sensory_overload": {
          "type": "argon:sensory_overload",
          "properties": {
            "title": "Sensory Overload"
          }
        }
      }
    }
    ```

---

### Silence {#argonsilence}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:silence</code></div>

<div class="argon-desc">While enabled, the user makes no sounds, like footsteps and other movement sounds. It doesn't make them invisible or hide their vibrations from sculk sensors (use palladium:sculk_immunity for that).</div>

=== "Example"

    ```json
    {
      "type": "argon:silence"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "silence": {
          "type": "argon:silence"
        }
      }
    }
    ```

---

### State Selector {#argonstate_selector}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:state_selector</code></div>

<div class="argon-desc">On activation, changes a block state property (e.g. "open", "lit", "facing") of the block you target, using "block_properties". With several entries, a held key scrolls a menu of the ones that apply.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Integer (&gt; 0)</td><td>The maximum distance, in blocks, the raycast can reach.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">8</td></tr><tr><td><code>block_filter</code></td><td>Block ID(s) / Tag</td><td>Optional whitelist of blocks (explicit IDs and/or tags) this ability can affect; if unset, any block is eligible.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>block_properties</code></td><td><em>State Selector Property</em>,<br><em>State Selector Property</em>[]</td><td>One or more properties to offer. A single entry applies immediately. Several entries open a scrollable picker.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>allow_block_entities</code></td><td>Boolean</td><td>If false (default), refuses to touch any block with a block entity (chests, furnaces, etc.) for safety.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>notify_neighbors</code></td><td>Boolean</td><td>If true (default), the change triggers normal neighbor updates (redstone, shape updates, etc). The client is always synced either way.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>require_valid_survival</code></td><td>Boolean</td><td>If true (default), the new state must be able to survive at that position or the change is cancelled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>allow_multiblock</code></td><td>Boolean</td><td>If false (default), won't change structural multi-block properties ("half", "part", e.g. doors, beds, tall plants), since one half alone can desync the pair. Modded blocks with other names aren't all covered, use "block_filter" for those.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

    <p class="argon-nested"><code>block_properties</code> (State Selector Property)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>property</code></td><td>String</td><td>The name of the block state property, such as open, facing or waterlogged. Whatever the targeted block actually has is used.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>operation</code></td><td><code>set</code><br><code>next</code><br><code>previous</code><br><code>toggle</code></td><td>How the property changes.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>String</td><td>The value used by the set operation, in its normal string form such as true, east or 3.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>allowed_values</code></td><td>String,<br>String[]</td><td>Restricts and orders the values this property may use.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:state_selector",
      "block_properties": {
        "property": "open",
        "operation": "toggle"
      }
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:state_selector",
      "block_properties": [
        {
          "property": "facing",
          "operation": "next"
        },
        {
          "property": "waterlogged",
          "operation": "toggle"
        }
      ]
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "state_selector": {
          "type": "argon:state_selector",
          "block_properties": {
            "property": "open",
            "operation": "toggle"
          }
        }
      }
    }
    ```

---

### Structure Capture {#argonstructure_capture}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:structure_capture</code></div>

<div class="argon-desc">While held, drag out and scroll-resize a wireframe cuboid (up to "max_size" per axis). On release it captures and clears the blocks into a capsule item, which restores them (rotated to match) on right-click.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Integer (&gt; 0)</td><td>The maximum distance, in blocks, the look-target raycast can reach.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32</td></tr><tr><td><code>max_size</code></td><td>Integer (&gt; 0)</td><td>The maximum size of the captured area along each axis, measured from the block first looked at.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">16</td></tr><tr><td><code>color</code></td><td>Color</td><td>The outline color, defaulting to cyan when unset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:structure_capture"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "structure_capture": {
          "type": "argon:structure_capture"
        }
      }
    }
    ```

---

### Sweeping Edge {#argonsweeping_edge}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:sweeping_edge</code></div>

<div class="argon-desc">While enabled, every melee hit also damages other living entities near the target, like a sweep attack without a sword or full charge. Skipped when vanilla would already sweep.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>damage_multiplier</code></td><td>Float</td><td>Fraction of the primary hit's damage dealt to each other entity caught in the sweep.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>radius</code></td><td>Float (&gt;= 0.0)</td><td>How far, in blocks, beyond the target's own hitbox to search for other entities to sweep.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>max_distance</code></td><td>Float (&gt;= 0.0)</td><td>Maximum distance, in blocks, from the attacker itself that a swept entity can be.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>knockback</code></td><td>Float</td><td>Knockback strength on each swept entity, away from the attacker's facing direction. 0 turns knockback off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>play_effects</code></td><td>Boolean</td><td>Whether to play the vanilla sweep sound and particle whenever this sweeps at least one entity.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:sweeping_edge"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "sweeping_edge": {
          "type": "argon:sweeping_edge"
        }
      }
    }
    ```

---

### Takeoff {#argoncharged_takeoff}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:charged_takeoff</code></div>

<div class="argon-desc">Hold the Takeoff key (Controls > Argon, unbound by default) to charge, release to launch. The longer you hold, the harder it throws you. One push, not flight. Pair it with argon:took_off to continue into flight.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>requires_ground</code></td><td>Boolean</td><td>Whether charging can only begin on the ground (checked on the server).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>cancel_when_airborne</code></td><td>Boolean</td><td>Whether a charge started on the ground is dropped once the player leaves it (walking off a ledge, jumping).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>allow_movement_while_charging</code></td><td>Boolean</td><td>Whether the player can walk while charging. If false, walking speed is held at zero until they release or cancel.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>min_charge_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the key must be held before releasing launches. Releasing sooner cancels, with no launch and no cooldown.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>max_charge_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long a full charge takes. Holding longer adds nothing, they stay fully charged until release.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">40</td></tr><tr><td><code>cooldown</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long after a launch before another can be charged. 0 for none. Cancelled charges don't start it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>min_launch_strength</code></td><td>Double</td><td>Upward speed, in blocks per tick, of the weakest launch (a normal jump is about 0.42). 0.6 gets roughly 2.7 blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>max_launch_strength</code></td><td>Double</td><td>Upward speed of a full charge, never exceeded. 1.7 gets roughly 15 blocks before gravity wins.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.7</td></tr><tr><td><code>flight_at_apex</code></td><td>Boolean</td><td>Starts the player's palladium:flight at the top of the climb so they stay up. Needs an unlocked flight ability, does nothing without one.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>launch_direction</code></td><td><code>vertical</code><br><code>look_direction</code><br><code>hybrid</code></td><td>Which way the push goes: "vertical" (straight up), "look_direction" (where the player looks on release, same strength at any angle) or "hybrid" (up, bent toward the look direction by "directional_influence").</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">vertical</td></tr><tr><td><code>minimum_launch_pitch</code></td><td>Double</td><td>look_direction only. The lowest launch angle, in degrees above the horizon (negative is below). 0 never launches downward, -90 means no limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-90.0</td></tr><tr><td><code>directional_influence</code></td><td>Double</td><td>hybrid only. 0 to 1, how much the look direction bends the launch away from straight up. Strongest looking level, nothing looking straight up or down. It never changes how hard the launch is, only where it points.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.35</td></tr><tr><td><code>minimum_upward_component</code></td><td>Double</td><td>hybrid only. 0 to 1, the least vertical share the launch may have, whatever the camera does. 0.5 keeps at least half the push pointing up, 1 is straight up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>directional_launch_particles</code></td><td>Boolean</td><td>Whether the burst of debris at launch is thrown away from the launch direction (backward for a forward launch) instead of spreading around the player.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>replace_velocity</code></td><td>Boolean</td><td>Whether the push replaces the player's whole velocity. By default sideways speed is kept (never raised above what they had or max_launch_strength), so launches can't be chained into unlimited speed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>charge_curve</code></td><td><code>linear</code><br><code>ease_in</code><br><code>ease_out</code><br><code>ease_in_out</code></td><td>How strength follows the charge: "linear", "ease_in" (weak early, much stronger near full), "ease_out" (strong early, small gains near full) or "ease_in_out".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">linear</td></tr><tr><td><code>charge_particles</code></td><td><em>Charge Particles</em></td><td>Debris from the ground blocks around the player while charging. Keys: enabled (true), radius (2.5), count (4), interval (2 ticks), rise_speed (0.12), lifetime (24 ticks), scale (1), scales_with_charge (none, count, speed or both). Client-only.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{}</td></tr><tr><td><code>launch_particles</code></td><td><em>Launch Particles</em></td><td>Debris thrown up on launch, scaled by its strength. Keys: burst (true), count (40), radius (3), strength (0.4 blocks per tick).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">{}</td></tr></tbody></table></div>

    <p class="argon-nested"><code>charge_particles</code> (Charge Particles)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>Boolean</td><td>Whether particles show while charging.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Double (0.5 ~ 16.0)</td><td>The radius particles gather from, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (1 ~ 32)</td><td>How many particles spawn each time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The delay between spawns.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rise_speed</code></td><td>Double (0.0 ~ 1.0)</td><td>How fast the particles rise.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lifetime</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long each particle lives.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>scale</code></td><td>Double (0.1 ~ 8.0)</td><td>The size of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>scales_with_charge</code></td><td><code>none</code><br><code>count</code><br><code>speed</code><br><code>both</code></td><td>What grows as the charge builds.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>launch_particles</code> (Launch Particles)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>burst</code></td><td>Boolean</td><td>Whether a burst of particles is released on launch.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (0 ~ 200)</td><td>How many particles are released.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Double (0.5 ~ 16.0)</td><td>The radius of the burst in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strength</code></td><td>Double (0.0 ~ 3.0)</td><td>How fast the particles fly outward.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:charged_takeoff",
      "flight_at_apex": true,
      "launch_direction": "hybrid",
      "directional_launch_particles": true,
      "charge_curve": "ease_in",
      "charge_particles": {
        "radius": 3,
        "count": 6,
        "rise_speed": 0.14,
        "lifetime": 26
      },
      "launch_particles": {
        "count": 60,
        "radius": 3.5,
        "strength": 0.5
      },
      "properties": {
        "title": "Takeoff"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "charged_takeoff": {
          "type": "argon:charged_takeoff",
          "flight_at_apex": true,
          "launch_direction": "hybrid",
          "directional_launch_particles": true,
          "charge_curve": "ease_in",
          "charge_particles": {
            "radius": 3,
            "count": 6,
            "rise_speed": 0.14,
            "lifetime": 26
          },
          "launch_particles": {
            "count": 60,
            "radius": 3.5,
            "strength": 0.5
          },
          "properties": {
            "title": "Takeoff"
          }
        }
      }
    }
    ```

---

### Target Mark {#argontarget_mark}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:target_mark</code></div>

<div class="argon-desc">On activation, marks the living entity under the crosshair (or the closest one inside the cone) as the user's prey. Only one mark exists per user and a new mark replaces the old one. While marked, the target is outlined through walls for the user, an edge arrow points at it when it is off screen, and every hit the user lands on it deals extra damage. The mark ends when the duration runs out, the target dies, or something consumes it (see argon:seek_strike). Use the argon:marked_target condition to build abilities that need a mark. All Values are read once on activation.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>How far away a target can be marked, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">32</td></tr><tr><td><code>duration</code></td><td>(Dynamic) Value</td><td>How long the mark lasts, in ticks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">300</td></tr><tr><td><code>damage_bonus</code></td><td>(Dynamic) Value</td><td>Extra damage the user deals to the marked target, in percent.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>color</code></td><td>Color</td><td>The outline and arrow color of the mark.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#F2C451</td></tr><tr><td><code>cone_angle</code></td><td>Double</td><td>The full opening angle of the fallback cone used when no entity is directly under the crosshair, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">24.0</td></tr><tr><td><code>pointer</code></td><td>Boolean</td><td>Whether an arrow at the screen edge points at the marked target when it is off screen.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:target_mark",
      "range": 32,
      "duration": 300,
      "damage_bonus": 10,
      "properties": {
        "title": "Target Mark"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "target_mark": {
          "type": "argon:target_mark",
          "range": 32,
          "duration": 300,
          "damage_bonus": 10,
          "properties": {
            "title": "Target Mark"
          }
        }
      }
    }
    ```

---

### Taunt {#argontaunt}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:taunt</code></div>

<div class="argon-desc">While enabled, forces every mob within range to target the user.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far from the entity other mobs can be to be forced to target it.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:taunt",
      "range": 8
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "taunt": {
          "type": "argon:taunt",
          "range": 8
        }
      }
    }
    ```

---

### Team Chat {#argonteam_chat}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:team_chat</code></div>

<div class="argon-desc">On activation, opens a client side team chat GUI that only online teammates can see. It stays open until closed and tells teammates who aren't viewing it through regular chat.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>custom_title</code></td><td>Text Component</td><td>If set, always used as the chat window's title instead of the default "<Team Name> Chat".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:team_chat",
      "properties": {
        "title": "Team Chat"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "team_chat": {
          "type": "argon:team_chat",
          "properties": {
            "title": "Team Chat"
          }
        }
      }
    }
    ```

---

### Team Formation {#argonteam_formation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:team_formation</code></div>

<div class="argon-desc">On activation, opens a client side GUI to name a team and invite up to 6 online players by username. Each gets a clickable chat message that adds them to the team when accepted.</div>

=== "Example"

    ```json
    {
      "type": "argon:team_formation",
      "properties": {
        "title": "Team Formation"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "team_formation": {
          "type": "argon:team_formation",
          "properties": {
            "title": "Team Formation"
          }
        }
      }
    }
    ```

---

### Telekinesis {#argontelekinesis}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:telekinesis</code></div>

<div class="argon-desc">While enabled, lifts the entity or block you look at within range and holds it in front of you at a distance you scroll, up to max_distance, until released or no longer valid.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far away an entity or block can be to be picked up in the first place.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max_distance</code></td><td>Double</td><td>The farthest the held target can be pushed away via scrolling, with a minimum of 1 block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10.0</td></tr><tr><td><code>blocked_blocks</code></td><td>Block ID(s) / Tag</td><td>Additional blocks that can never be lifted, alongside blocks with a block entity and unbreakable blocks, which are always excluded.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Particle</td><td>If set, this particle effect is continuously spawned around the held target while it's held.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>glow_color</code></td><td>Color</td><td>If set, the held target glows this color, visible only to the user, while held.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:telekinesis",
      "range": 8,
      "particles": {
        "type": "minecraft:end_rod"
      },
      "glow_color": "#00ffff",
      "properties": {
        "title": "Telekinesis"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "telekinesis": {
          "type": "argon:telekinesis",
          "range": 8,
          "particles": {
            "type": "minecraft:end_rod"
          },
          "glow_color": "#00ffff",
          "properties": {
            "title": "Telekinesis"
          }
        }
      }
    }
    ```

---

### Teleport to Location {#argonteleport_to_location}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:teleport_to_location</code></div>

<div class="argon-desc">On activation, teleports the entity to the position, facing and dimension saved under "namespace" by argon:save_location, searching upward for open space. Does nothing if none is saved.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>namespace</code></td><td>String</td><td>The name of the location to teleport to, saved earlier by an argon:save_location ability with the same namespace.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>reset_ability</code></td><td>String</td><td>Another ability, e.g. "fsang:example#driving_ability", to cut short once the teleport happens, so a later step in a shared animation timer sequence doesn't fire after the entity's state changed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:teleport_to_location",
      "namespace": "home"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "teleport_to_location": {
          "type": "argon:teleport_to_location",
          "namespace": "home"
        }
      }
    }
    ```

---

### Teleportation (Menu) {#argonteleport_menu}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:teleport_menu</code></div>

<div class="argon-desc">On activation, opens a client side GUI to teleport by coordinates, saved locations or both, depending on "mode". Opens a portal instead of teleporting instantly when create_portal is true.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>show_dimensions</code></td><td>Boolean</td><td>Whether the coordinate section has a dimension selector. Otherwise the destination is always the user's current dimension.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>excluded_dimensions</code></td><td>Dimension ID[]</td><td>Dimension IDs to hide from the dimension selector when show_dimensions is true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>mode</code></td><td><code>coordinates</code><br><code>saved_locations</code><br><code>both</code></td><td>Which teleport method(s) the menu offers: coordinates (default), saved_locations, or both.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">COORDINATES</td></tr><tr><td><code>saved_slots</code></td><td>Integer</td><td>How many saved-location slots to offer when mode is saved_locations or both.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5</td></tr><tr><td><code>create_portal</code></td><td>Boolean</td><td>If true, opens a pair of linked, reusable portals instead of teleporting instantly, using the settings of "portal" instead of "direct_teleport".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>portal</code></td><td><em>Portal Settings</em></td><td>Portal visuals and behavior used when create_portal is true, with distance measured via raycast from the user (0 = at the user).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">PortalSettings[beamRenderer=Optional.empty, beamVector=(0.0, 128.0, 0.0), duration=200, thickness=1.5, distance=0.0, particles=Optional.empty]</td></tr><tr><td><code>direct_teleport</code></td><td><em>Direct Teleport Settings</em></td><td>Settings used when create_portal is false, including how far nearby entities are brought along and one-time particle/beam effects at the departure and arrival points.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">DirectTeleportSettings[entityRange=0.0, originParticles=Optional.empty, destinationParticles=Optional.empty, originBeam=Optional.empty, destinationBeam=Optional.empty]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>portal</code> (Portal Settings)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The beam renderer used for the portal.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>beam_vector</code></td><td>Vector 3D</td><td>The direction of the portal beam.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the portal stays open.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>thickness</code></td><td>Double</td><td>The thickness of the portal in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>distance</code></td><td>Double</td><td>How far in front of the user the portal opens, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td><em>Teleport Particles</em></td><td>Particles shown at the portal.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>portal.particles</code> (Teleport Particles)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>particle</code></td><td>Particle</td><td>The particle to spawn.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>count</code></td><td>Integer (&gt;= 0)</td><td>How many particles spawn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>spread</code></td><td>Double</td><td>How far the particles spread.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>The speed of the particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>direct_teleport</code> (Direct Teleport Settings)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_range</code></td><td>Double</td><td>Nearby entities within this range, in blocks, are taken along.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>origin_particles</code></td><td><em>Teleport Particles</em></td><td>Particles shown where the user leaves.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>destination_particles</code></td><td><em>Teleport Particles</em></td><td>Particles shown where the user arrives.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>origin_beam</code></td><td><em>Teleport Beam</em></td><td>A beam shown where the user leaves.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>destination_beam</code></td><td><em>Teleport Beam</em></td><td>A beam shown where the user arrives.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>direct_teleport.origin_beam</code> (Teleport Beam)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The beam renderer to show.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer (&gt; 0)</td><td>How long the beam stays, in ticks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:teleport_menu",
      "show_dimensions": true,
      "excluded_dimensions": [
        "example:hidden_dimension"
      ],
      "mode": "both",
      "portal": {
        "beam_renderer": "example:teleport_beam",
        "distance": 3,
        "particles": {
          "particle": {
            "type": "minecraft:portal"
          },
          "count": 10,
          "spread": 0.6
        }
      },
      "direct_teleport": {
        "entity_range": 8,
        "origin_particles": {
          "particle": {
            "type": "minecraft:portal"
          },
          "count": 30
        },
        "destination_particles": {
          "particle": {
            "type": "minecraft:portal"
          },
          "count": 30
        },
        "origin_beam": {
          "beam_renderer": "example:teleport_beam"
        },
        "destination_beam": {
          "beam_renderer": "example:teleport_beam"
        }
      },
      "properties": {
        "title": "Teleportation (Menu)"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "teleport_menu": {
          "type": "argon:teleport_menu",
          "show_dimensions": true,
          "excluded_dimensions": [
            "example:hidden_dimension"
          ],
          "mode": "both",
          "portal": {
            "beam_renderer": "example:teleport_beam",
            "distance": 3,
            "particles": {
              "particle": {
                "type": "minecraft:portal"
              },
              "count": 10,
              "spread": 0.6
            }
          },
          "direct_teleport": {
            "entity_range": 8,
            "origin_particles": {
              "particle": {
                "type": "minecraft:portal"
              },
              "count": 30
            },
            "destination_particles": {
              "particle": {
                "type": "minecraft:portal"
              },
              "count": 30
            },
            "origin_beam": {
              "beam_renderer": "example:teleport_beam"
            },
            "destination_beam": {
              "beam_renderer": "example:teleport_beam"
            }
          },
          "properties": {
            "title": "Teleportation (Menu)"
          }
        }
      }
    }
    ```

---

### Tentacle Arms {#argonappendages}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendages</code></div>

<div class="argon-desc">While enabled, grows the appendages from "profile", opening over "open_time" ticks and closing over "close_time" (0 is instant). Idle animation only. Other appendage abilities give them actions.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>profile</code></td><td>Identifier</td><td>The appendage_profile id (data/<namespace>/argon/appendage_profiles/) that defines count, segments, attachment points and idle behavior.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>open_time</code></td><td>Integer</td><td>Ticks to open fully after enabling (the reference animation is about 10). 0 (default) skips it and they are just there once enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>close_time</code></td><td>Integer</td><td>Ticks to close after disabling. 0 (default) skips it and they just disappear.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendages",
      "profile": "example:octopus_arms",
      "open_time": 10,
      "close_time": 10,
      "properties": {
        "title": "Tentacle Arms"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendages": {
          "type": "argon:appendages",
          "profile": "example:octopus_arms",
          "open_time": 10,
          "close_time": 10,
          "properties": {
            "title": "Tentacle Arms"
          }
        }
      }
    }
    ```

---

### Tentacle Carry {#argonappendage_carry}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendage_carry</code></div>

<div class="argon-desc">Grabs the living entity you look at within "range" with an idle appendage and holds it in front of you until disabled. Mobs get no AI while held.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far, in blocks, the wearer can be looking at a target to grab it.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>carry_distance</code></td><td>Float</td><td>How far in front of the wearer's eyes the carried entity is held.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>carry_height_offset</code></td><td>Float</td><td>Vertical adjustment to the hold point, in blocks. Positive is higher.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendage_carry",
      "range": 6,
      "properties": {
        "title": "Tentacle Carry"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendage_carry": {
          "type": "argon:appendage_carry",
          "range": 6,
          "properties": {
            "title": "Tentacle Carry"
          }
        }
      }
    }
    ```

---

### Tentacle Guard {#argonappendage_guard}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendage_guard</code></div>

<div class="argon-desc">While enabled, idle appendages wrap around your torso and absorb damage from within "block_angle" of where you face, up to "guard_threshold". Past that the guard breaks, you take the damage and can't block for "break_lockout" ticks.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>minimum_wrapped_appendages</code></td><td>Integer</td><td>How many appendages must stay wrapped for the guard to absorb damage. Below this, hits go through.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2</td></tr><tr><td><code>maximum_wrapped_appendages</code></td><td>Integer</td><td>How many appendages this ability claims and wraps at once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>guard_threshold</code></td><td>Float</td><td>Cumulative damage the guard can absorb before it breaks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20.0</td></tr><tr><td><code>break_damage</code></td><td>Float</td><td>Self-damage dealt to the wearer when the guard breaks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>break_lockout</code></td><td>Integer</td><td>Ticks after breaking before guard can absorb damage again.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">40</td></tr><tr><td><code>block_angle</code></td><td>Float</td><td>The cone, in degrees around your facing, that damage must come from to be blocked. Also how wide the appendages spread around you. 180 (default) covers the front, 360 covers every direction.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">180.0</td></tr><tr><td><code>knockback_strength</code></td><td>Float</td><td>Knockback velocity applied to the attacker on a successful block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendage_guard",
      "properties": {
        "title": "Tentacle Guard"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendage_guard": {
          "type": "argon:appendage_guard",
          "properties": {
            "title": "Tentacle Guard"
          }
        }
      }
    }
    ```

---

### Tentacle Retrieval {#argonappendage_item_retrieval}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendage_item_retrieval</code></div>

<div class="argon-desc">While enabled, sends idle appendages to fetch dropped items within "search_range", one per item up to "maximum_active_appendages". Items are pulled in at "pull_speed" and picked up within "pickup_range".</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>search_range</code></td><td>Double</td><td>How far, in blocks, this ability looks for dropped items to fetch.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>maximum_active_appendages</code></td><td>Integer</td><td>How many appendages this ability claims and uses at once, each fetching a separate item.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>pickup_range</code></td><td>Float</td><td>How close a fetched item must get to the wearer before it's added to their inventory.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.2</td></tr><tr><td><code>pull_speed</code></td><td>Float</td><td>Fraction of the remaining distance a fetched item covers toward you each tick, 0 to 1. Higher pulls faster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendage_item_retrieval",
      "search_range": 8,
      "properties": {
        "title": "Tentacle Retrieval"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendage_item_retrieval": {
          "type": "argon:appendage_item_retrieval",
          "search_range": 8,
          "properties": {
            "title": "Tentacle Retrieval"
          }
        }
      }
    }
    ```

---

### Tentacle Strike {#argonappendage_attack}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendage_attack</code></div>

<div class="argon-desc">Sends one idle appendage to strike a target within "attack_range", dealing damage on impact. "attack_pattern": "direct_strike" aims where you look, "auto_nearest" at the nearest target.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>damage</code></td><td>Float</td><td>The damage dealt on impact.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attack_range</code></td><td>Double</td><td>How far, in blocks, the strike can reach.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>extend_ticks</code></td><td>Integer</td><td>How many ticks the strike takes to reach the target and deal damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>retract_ticks</code></td><td>Integer</td><td>How many ticks the appendage takes to retract back to idle after impact.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>knockback</code></td><td>Float</td><td>Knockback velocity applied to the target on impact.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>recovery_time</code></td><td>Integer</td><td>How many ticks after retracting before another strike can begin.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>attack_pattern</code></td><td><code>direct_strike</code><br><code>auto_nearest</code></td><td>"direct_strike" (a random idle appendage strikes whatever the wearer looks at, once per activation) or "auto_nearest" (continuously, whichever idle appendage is nearest strikes the nearest target in range).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">direct_strike</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendage_attack",
      "damage": 4,
      "attack_range": 8,
      "properties": {
        "title": "Tentacle Strike"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendage_attack": {
          "type": "argon:appendage_attack",
          "damage": 4,
          "attack_range": 8,
          "properties": {
            "title": "Tentacle Strike"
          }
        }
      }
    }
    ```

---

### Text Overlay {#argontext_overlay}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:text_overlay</code></div>

<div class="argon-desc">While enabled, renders text on screen with the same translate/rotate/scale/alignment transform as the built-in gui_overlay ability, but for text instead of an image.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>text</code></td><td>Text Component</td><td>The text to render, either a plain string or a full text component (translate/keybind/color/etc).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>translate</code></td><td>Vector 2D</td><td>A [x, y] pixel offset applied to the text's position.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">net.minecraft.world.phys.Vec2@631c244c</td></tr><tr><td><code>rotate</code></td><td>Float</td><td>The rotation of the text, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>scale</code></td><td>Vector 2D</td><td>The [x, y] scale of the text.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">net.minecraft.world.phys.Vec2@3bd99944</td></tr><tr><td><code>alignment</code></td><td><code>top_left</code><br><code>top_center</code><br><code>top_right</code><br><code>middle_left</code><br><code>center</code><br><code>middle_right</code><br><code>bottom_left</code><br><code>bottom_center</code><br><code>bottom_right</code></td><td>Determines how the text is aligned on the screen.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>color</code></td><td>Color</td><td>The color of the rendered text.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">#FFFFFF</td></tr><tr><td><code>shadow</code></td><td>Boolean</td><td>Whether the text has a drop shadow.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:text_overlay",
      "text": "Example Text",
      "alignment": "top_left"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "text_overlay": {
          "type": "argon:text_overlay",
          "text": "Example Text",
          "alignment": "top_left"
        }
      }
    }
    ```

---

### Throw Blocks {#argonthrow_blocks}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:throw_blocks</code></div>

<div class="argon-desc">On activation, picks up to "amount" breakable ground blocks within "radius", optionally lifts them, then launches them where you aim. They deal "damage" and drop their item on impact.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>amount</code></td><td>Integer (&gt; 0)</td><td>How many blocks to throw per activation.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Integer (&gt; 0)</td><td>Horizontal search radius (in blocks) around the user to pick candidate ground-surface blocks from.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>damage</code></td><td>Float</td><td>Damage dealt to a living entity hit by a thrown block.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Float</td><td>Launch speed of each thrown block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.5</td></tr><tr><td><code>spread</code></td><td>Float</td><td>Random aim spread applied to each throw, where 0 is perfectly straight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>particles</code></td><td>Particle</td><td>If set, spawns this particle effect around each block continuously while lifting and in flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>glow_color</code></td><td>Color</td><td>If set, each block glows this color, visible to everyone, while lifting and in flight.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lift_time</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long each block hovers, rising 2 blocks, before being thrown. 0 throws immediately without lifting.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:throw_blocks",
      "amount": 5,
      "radius": 6,
      "damage": 4
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "throw_blocks": {
          "type": "argon:throw_blocks",
          "amount": 5,
          "radius": 6,
          "damage": 4
        }
      }
    }
    ```

---

### Time Control {#argontime_control}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:time_control</code></div>

<div class="argon-desc">While enabled, scales the tick speed of entities, crops and redstone by "speed", per the affect_* settings. Only affects players if TIME_CONTROL_CAN_AFFECT_PLAYERS is enabled.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>speed</code></td><td>(Dynamic) Value</td><td>The time multiplier, where 1.0 is normal, 0.0 is a full stop, and negative results are treated as 0.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>(Dynamic) Value</td><td>The radius around the user that affect_entities covers. affect_crops and affect_redstone are always world-wide.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>affect_entities</code></td><td>Boolean</td><td>Whether entity movement/AI within range is slowed, sped up, or stopped.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>affect_crops</code></td><td>Boolean</td><td>Whether crop growth, leaf decay, and other random-tick-driven behavior is scaled world-wide.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>affect_redstone</code></td><td>Boolean</td><td>Whether scheduled block ticks and block entities (furnaces, hoppers, pistons, redstone) are frozen world-wide. Only happens when speed is exactly 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:time_control",
      "speed": 0,
      "range": 16,
      "properties": {
        "title": "Time Control"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "time_control": {
          "type": "argon:time_control",
          "speed": 0,
          "range": 16,
          "properties": {
            "title": "Time Control"
          }
        }
      }
    }
    ```

---

### Time Growth {#argontime_growth}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:time_growth</code></div>

<div class="argon-desc">Makes attributes grow stronger the longer the ability has been enabled for the player. Every enabled tick counts towards the ability's age (time spent offline or with the ability disabled does not count), and each entry adds "per_day" to its attribute for every day of age between "start_day" and "max_day". The age is available to other abilities through the argon:power_age value and condition.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attributes</code></td><td><em>Growth Entry</em>[]</td><td>The attributes that grow, from 1 to 32 entries.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ticks_per_day</code></td><td>Integer</td><td>How many enabled ticks count as one day of age. 24000 is one Minecraft day, lower it to test growth quickly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">24000</td></tr><tr><td><code>whole_days</code></td><td>Boolean</td><td>If true the bonus only increases once per full day. If false it grows smoothly.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>reset_on_death</code></td><td>Boolean</td><td>If true the age goes back to 0 when the player dies.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>reset_on_power_loss</code></td><td>Boolean</td><td>If true the age goes back to 0 when the player loses the power this ability belongs to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>milestones</code></td><td><em>Growth Milestone</em>[]</td><td>Ages that announce themselves when the player reaches them by natural growth. They do not fire when the age is set with a command.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>attributes[]</code> (Growth Entry)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attribute</code></td><td>Attribute ID</td><td>The attribute that grows.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>operation</code></td><td><code>add_value</code><br><code>add_multiplied_base</code><br><code>add_multiplied_total</code></td><td>How the bonus is applied to the attribute.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">add_value</td></tr><tr><td><code>per_day</code></td><td>Double</td><td>The bonus gained per day of age.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>start_day</code></td><td>Double (0.0 ~ 1000000.0)</td><td>The day growth begins at.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max_day</code></td><td>Double (0.0 ~ 1000000.0)</td><td>The day growth stops at.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>milestones[]</code> (Growth Milestone)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>day</code></td><td>Double (0.0 ~ 1000000.0)</td><td>The day of age the milestone happens at.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>title</code></td><td>Text Component</td><td>The title shown on screen.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>subtitle</code></td><td>Text Component</td><td>The subtitle shown under the title.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>sound</code></td><td>Identifier</td><td>A sound event ID played for the player.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:time_growth",
      "attributes": [
        {
          "attribute": "minecraft:armor",
          "per_day": 0.4,
          "max_day": 20
        }
      ],
      "properties": {
        "title": "Time Growth"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "time_growth": {
          "type": "argon:time_growth",
          "attributes": [
            {
              "attribute": "minecraft:armor",
              "per_day": 0.4,
              "max_day": 20
            }
          ],
          "properties": {
            "title": "Time Growth"
          }
        }
      }
    }
    ```

---

### Tool Hands {#argontool_hands}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:tool_hands</code></div>

<div class="argon-desc">Allows the player to mine a block and receive its drops as if a tool were used.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>drop_block_tags</code></td><td>Block Tag[]</td><td>Block tags controlling what bare hands can harvest and at what tier (e.g. "minecraft:mineable/pickaxe" plus "minecraft:needs_iron_tool"), empty by default with no effect.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>enchantments</code></td><td><em>Enchantment Entry</em>[]</td><td>Enchantments the hand counts as having, each with an "enchantment" id and a "level" value (default 1; 0 turns it off). Efficiency speeds mining; Fortune and Silk Touch shape drops, even on blocks needing no tool. Combat enchantments don't apply.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>enchantments[]</code> (Enchantment Entry)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>enchantment</code></td><td>Identifier</td><td>The enchantment.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>level</code></td><td>Integer / Value</td><td>The enchantment level.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:tool_hands",
      "drop_block_tags": [
        "minecraft:mineable/pickaxe",
        "minecraft:needs_iron_tool"
      ],
      "enchantments": [
        {
          "enchantment": "minecraft:fortune",
          "level": 3
        }
      ],
      "properties": {
        "title": "Tool Hands"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "tool_hands": {
          "type": "argon:tool_hands",
          "drop_block_tags": [
            "minecraft:mineable/pickaxe",
            "minecraft:needs_iron_tool"
          ],
          "enchantments": [
            {
              "enchantment": "minecraft:fortune",
              "level": 3
            }
          ],
          "properties": {
            "title": "Tool Hands"
          }
        }
      }
    }
    ```

---

### Totem Animation {#argontotem_animation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:totem_animation</code></div>

<div class="argon-desc">On activation, plays the Totem of Undying animation and sound for the given item. Client side and only for the holder, without the particle burst others would see.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>item</code></td><td>Item ID</td><td>The item to display in the animation.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:totem_animation",
      "item": "minecraft:totem_of_undying"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "totem_animation": {
          "type": "argon:totem_animation",
          "item": "minecraft:totem_of_undying"
        }
      }
    }
    ```

---

### Untargetable {#argonuntargetable}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:untargetable</code></div>

<div class="argon-desc">While enabled, stops hostile mobs from targeting the user, entirely or narrowed by "mobs" and "mode" ("whitelist" only those mobs, "blacklist" every mob except those).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>whitelist</code><br><code>blacklist</code></td><td>How "mobs" is read: "whitelist" (only these can't target the user) or "blacklist" (everything except these can't target the user). Doesn't matter while "mobs" is unset.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mobs</code></td><td>Entity Type ID(s) / Tag</td><td>The mob type(s) this applies to, as explicit entity type IDs, a tag ("#namespace:tag"), or a mix of both. Left unset, this ability applies to every hostile mob.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:untargetable",
      "properties": {
        "title": "Untargetable"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "untargetable": {
          "type": "argon:untargetable",
          "properties": {
            "title": "Untargetable"
          }
        }
      }
    }
    ```

---

### Vortex {#argonvortex}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:vortex</code></div>

<div class="argon-desc">When enabled, creates a vortex of cutting air where the user looks, on the ground at the end of the aim. While it lasts it pulls living entities inside toward its center and damages them in pulses.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>max_distance</code></td><td>(Dynamic) Value</td><td>How far away, in blocks, the vortex can be placed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">18</td></tr><tr><td><code>radius</code></td><td>Float</td><td>The radius of the vortex in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5.0</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the vortex lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>damage_per_second</code></td><td>Float</td><td>Damage dealt per second to each entity inside. 0 for a vortex that does no damage.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4.0</td></tr><tr><td><code>max_damage</code></td><td>Float</td><td>The most damage the vortex deals to one entity in total.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20.0</td></tr><tr><td><code>pull</code></td><td>Double</td><td>How strongly entities are pulled towards the centre each tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.04</td></tr><tr><td><code>pulse_interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How often damage is dealt.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">5</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>Damage type ID the damage is dealt as. Unset, it is a player attack for players and a mob attack otherwise.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>track_entities</code></td><td>Boolean</td><td>Whether the vortex forms around the living entity the user looks at within max_distance and follows it, instead of forming on the ground.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>center_on_user</code></td><td>Boolean</td><td>Whether the vortex forms around the user and follows them instead of where they are aiming.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>suspend</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>For this long after forming, entities small enough hover inside the vortex instead of falling. 0 for none.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>suspend_max_volume</code></td><td>Float</td><td>The largest bounding box volume, in cubic blocks, of an entity that gets suspended. A zombie is about 0.7, an iron golem about 5. Bosses are never suspended.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>funnel_visual</code></td><td>Boolean</td><td>Whether a layered swirling funnel of wind is drawn over the vortex.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:vortex",
      "max_distance": 18
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "vortex": {
          "type": "argon:vortex",
          "max_distance": 18
        }
      }
    }
    ```

---

### Wall Crawl {#argonappendage_climbing}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:appendage_climbing</code></div>

<div class="argon-desc">While enabled, idle appendages reach for nearby surfaces. While enough of them hold on, you move like in flight with no gravity. With too few, gravity returns.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attachment_range</code></td><td>Double</td><td>How far, in blocks, an appendage looks for a surface. Also the most it can stretch before it lets go and searches again.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>minimum_attached_appendages</code></td><td>Integer</td><td>How many appendages must stay attached to keep flying. Below this, normal gravity returns right away.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2</td></tr><tr><td><code>maximum_attached_appendages</code></td><td>Integer</td><td>How many appendages this ability claims and uses at once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">4</td></tr><tr><td><code>responsiveness</code></td><td>Float</td><td>How fast velocity catches up to the target each tick while flying, 0 to 1. Higher is snappier, lower is floatier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.35</td></tr><tr><td><code>move_speed</code></td><td>Float</td><td>Horizontal WASD-driven flight speed while climbing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr><tr><td><code>lift_speed</code></td><td>Float</td><td>Vertical speed while holding jump (up) or shift (down) while climbing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.4</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:appendage_climbing",
      "attachment_range": 10,
      "properties": {
        "title": "Wall Crawl"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "appendage_climbing": {
          "type": "argon:appendage_climbing",
          "attachment_range": 10,
          "properties": {
            "title": "Wall Crawl"
          }
        }
      }
    }
    ```

---

### Wall Crawling {#argonwall_crawling}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:wall_crawling</code></div>

<div class="argon-desc">Lets the user climb flat vertical walls and optionally ceilings with look-relative WASD. Turns around outside corners on its own and rolls the camera so the attached surface reads as "down".</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>base_speed</code></td><td>Float</td><td>The base crawling speed, in blocks per tick, before speed_multiplier is applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.13</td></tr><tr><td><code>speed_multiplier</code></td><td>Float</td><td>Multiplies base_speed, so different powers can reuse this ability at different crawl speeds (0.5 is half speed, 2.0 is double).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>attach_distance</code></td><td>Float</td><td>How close to a wall or ceiling face the user must be to attach to (or remain attached to) it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>detach_strength</code></td><td>Float</td><td>How hard jumping off a surface pushes the user in whichever direction they're currently looking.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.3</td></tr><tr><td><code>gravity_pull_strength</code></td><td>Float</td><td>A small constant velocity into the attached surface every tick, whether or not the user is moving. The same solid block collision that stops it confirms the surface is still there, so there is no distance check.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.08</td></tr><tr><td><code>ceiling_crawling</code></td><td>Boolean</td><td>Whether ceilings (not just vertical walls) are valid attachment surfaces.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>camera_roll</code></td><td>Boolean</td><td>If true, smoothly rolls the local user's camera so the attached surface reads as "down", making the wall or ceiling their floor and not just their movement plane.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>third_person_camera_roll</code></td><td>Boolean</td><td>Whether camera_roll also applies in third person, not only first person. Off by default, since third person shows the user's own model and the roll doesn't reorient it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>use_directional_gravity</code></td><td>Boolean</td><td>If true, attaching to a surface turns the player's gravity toward it (the surface becomes their floor, and the hitbox, camera and model turn with it) instead of steering velocity along it. The options below apply to this mode.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>gravity_strength</code></td><td>Float</td><td>A multiplier on normal gravity while attached; it is how firmly the player is held to the surface.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>rotate_camera</code></td><td>Boolean</td><td>Whether the camera turns with the surface. If missing, camera_roll is used. When false the view stays upright to the world while the body and movement still turn.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>camera_transition_time</code></td><td>Integer</td><td>Ticks the camera takes to turn to a new surface. 0 turns it at once.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>smooth_transitions</code></td><td>Boolean</td><td>Whether the camera and body turn gradually. When false every turn is instant.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>transition_duration</code></td><td>Integer</td><td>Ticks the drawn body takes to turn to a new surface.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6</td></tr><tr><td><code>transition_easing</code></td><td>String</td><td>linear, ease_in, ease_out or ease_in_out: how the turns speed up and slow down.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">ease_in_out</td></tr><tr><td><code>view_orientation</code></td><td>String</td><td>What a turn between surfaces does to where the player looks. relative: same angles in the new gravity. world: angles are recomputed so the player keeps looking at the same point in the world.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">relative</td></tr><tr><td><code>surface_detection_range</code></td><td>Float</td><td>How close a surface must be to grab or keep hold of it, in blocks. If missing, attach_distance is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>surface_transition_tolerance</code></td><td>Float</td><td>How far before the edge of a surface the player starts turning round it, in blocks (0 to 0.3).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.15</td></tr><tr><td><code>movement_mode</code></td><td>String</td><td>surface_relative: W goes up the wall (or along the heading) whatever the camera does. camera_relative: W goes where the camera points, along the surface.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">surface_relative</td></tr><tr><td><code>surface_jump_strength</code></td><td>Float</td><td>How hard jumping pushes the player straight off the surface. If missing, detach_strength is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>auto_crawl</code></td><td>Boolean</td><td>Whether the player may turn onto surfaces where only a crawl sized body fits, crawling through tight spaces.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>allow_ceiling_crawling</code></td><td>Boolean</td><td>Whether ceilings are valid surfaces. If missing, ceiling_crawling is used.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>allow_corner_transitions</code></td><td>Boolean</td><td>Whether the player turns from one surface to the next at corners on their own (and from the floor onto a wall they walk into). When false they can only grab a surface from the air.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>preserve_surface_momentum</code></td><td>Boolean</td><td>Whether speed is kept through a turn between surfaces.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>surface_speed_multiplier</code></td><td>Float</td><td>Multiplies the crawling speed (base_speed times speed_multiplier) on a surface only.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>allow_surface_sprinting</code></td><td>Boolean</td><td>Whether sprinting makes the player crawl faster.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>crawl_when_not_sprinting</code></td><td>Boolean</td><td>If true, the player is crawl sized (the vanilla crawling pose, a 0.6 block hitbox that fits one block gaps) on a wall or ceiling unless sprinting. Sprinting stands them back up as far as there is room.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>play_running_animation</code></td><td>Boolean</td><td>Whether sprinting along a wall or ceiling plays the running animation. Vanilla only starts it from ground movement, which doesn't happen while climbing. Only while sprinting.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:wall_crawling",
      "properties": {
        "title": "Wall Crawling"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "wall_crawling": {
          "type": "argon:wall_crawling",
          "properties": {
            "title": "Wall Crawling"
          }
        }
      }
    }
    ```

---

### Ward {#argonward}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ward</code></div>

<div class="argon-desc">On its first enabled tick, gives the user an absorption pool that soaks up all incoming damage until it runs out or the duration ends. Can reduce knockback, cost some health (never below 1) and briefly stop natural regeneration.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>pool</code></td><td>(Dynamic) Value</td><td>How much damage the ward absorbs, read once when it starts.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the ward lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">120</td></tr><tr><td><code>knockback_reduction</code></td><td>Float</td><td>The fraction from 0 to 1 of knockback removed while the ward is up.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>self_cost</code></td><td>Double</td><td>Health the user pays to cast it. It never takes them below half a heart.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>regen_lock</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>If above 0, stops healing for this long after casting.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ward",
      "pool": 16,
      "knockback_reduction": 0.75
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "ward": {
          "type": "argon:ward",
          "pool": 16,
          "knockback_reduction": 0.75
        }
      }
    }
    ```

---

### Web Swing {#argonweb_swing}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:web_swing</code></div>

<div class="argon-desc">On activation, attaches a rope anchor and swings you like a pendulum while enabled. The rope only cancels motion past its length, turning momentum into an arc. Movement keys steer. Ends on disable, or optionally on ground contact or lost line of sight.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>The maximum distance an anchor can attach to, measured from the eye to the exact hit point.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>attach_to</code></td><td><code>block</code><br><code>entity</code><br><code>both</code></td><td>Which kind of raycast hit can be attached to: a fixed "block" anchor, a "entity" living entity that becomes a moving anchor followed for the rest of the swing, or "both" (whichever the raycast hits first).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">BOTH</td></tr><tr><td><code>beam_renderer</code></td><td>Identifier</td><td>The id of the beam renderer used to draw the rope from the user to the anchor point.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>initial_slack</code></td><td>Float</td><td>Extra rope length, in blocks, on top of the exact distance when the web attaches. 0 (default) starts the rope as long as the current distance, so attaching never snaps or stalls you. Raise it for a more dramatic catch.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>gravity_multiplier</code></td><td>Float</td><td>Scales gravity's pull while swinging. 1 (default) is normal gravity. Other values adjust vanilla's gravity rather than replace it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>pump_acceleration</code></td><td>Float</td><td>Acceleration, blocks/tick^2, from holding forward or back along the rope's tangent plane. It fades out as speed nears max_speed and stops below a minimum speed so you can't hover. 0 is momentum only.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.025</td></tr><tr><td><code>air_drag</code></td><td>Float</td><td>Extra multiplier on velocity every tick while swinging, 0 to 1. 1 (default) keeps momentum (vanilla's own air drag is already undone, see drag_compensation).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>hand</code></td><td><code>right</code><br><code>left</code></td><td>Which hand the web comes from (drives left/right animation mirroring). Defaults to left if the beam_renderer id ends in "left", otherwise right.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>auto_tighten</code></td><td>Boolean</td><td>Slowly takes slack out of the rope (never pulling the user, and never below their current distance plus rope_slack_tolerance), so a swing that goes slack gets a usable rope again instead of the web quietly failing.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>rope_reel_speed</code></td><td>Float</td><td>How fast auto_tighten removes slack, blocks/tick.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.12</td></tr><tr><td><code>minimum_rope_length</code></td><td>Float</td><td>Auto-tightening never shortens the rope below this length, blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">3.0</td></tr><tr><td><code>rope_slack_tolerance</code></td><td>Float</td><td>How much slack, blocks, auto_tighten leaves in the rope.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.6</td></tr><tr><td><code>max_rope_correction</code></td><td>Float</td><td>The most, in blocks per tick, the rope may move the user back onto its radius after an overshoot, so a correction is paid off gradually instead of as a snap.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>drag_compensation</code></td><td>Boolean</td><td>Undo vanilla's per-tick air drag (x0.91 horizontal, x0.98 vertical) while swinging in the air, so a swing keeps its momentum. Turn it off only to compare against plain vanilla drag.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>max_speed</code></td><td>Float</td><td>Caps the user's total speed, blocks/tick, while swinging. Defaults to 2.6; 0 removes the cap.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slack_visual_scale</code></td><td>Float</td><td>How far the rope must sag, as a fraction of its length, before the beam looks fully loose. Only beam renderers like argon:segmented_textured use it, and only on the swinging player's client. Everyone else sees a taut web.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>reel</code></td><td><em>Web Swing Reel</em></td><td>If present, holding jump reels the rope in and holding sneak reels it back out (up to the original attach length), both at "speed" blocks/tick, down to "min_length" blocks at the shortest. Leave unset (the default) to disable manual reeling.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>auto_release</code></td><td><em>Web Swing Auto Release</em></td><td>Which conditions automatically detach the rope: "on_ground" when the user touches the ground, and "on_blocked_line" when a solid block ends up blocking the straight line between the user and the anchor point. Both default to true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">AutoReleaseSettings[onGround=true, onBlockedLine=true]</td></tr><tr><td><code>swing_assist</code></td><td><em>Web Swing Assist</em></td><td>Targeting and assist tuning. Targeting is a direct raycast along the aim first (a valid hit always wins); only if that misses, or hits closer than "min_anchor_distance", a small cone of "anchor_cone_degrees" (default 10) is searched, with aim accuracy weighted far above "anchor_height_weight" (default 0.4, the most a high target can gain over an on-aim one). "velocity_blend_speed" (default 0 = off) blends the travel direction into the aim direction. "ground_clearance_strength" (default 0.5) softens downward speed just before grazing the ground. "lateral_steering_strength" (default 0.02) is the left/right equivalent of pump_acceleration. "swing_jump_strength" (default 0 = pure momentum release) is an optional boost applied if jump is held on release. "fall_damage_grace_ticks" (default 15) forgives fall damage for that long after release. "rope_wrap" (default true) lets the rope catch on the nearest obstruction between the anchor and the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">SwingAssistSettings[anchorConeDegrees=10.0, minAnchorDistance=3.0, anchorHeightWeight=0.4, velocityBlendSpeed=0.0, groundClearanceStrength=0.5, lateralSteeringStrength=0.02, swingJumpStrength=0.0, fallDamageGraceTicks=15, ropeWrap=true]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>reel</code> (Web Swing Reel)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>speed</code></td><td>Float (&gt;= 0.0)</td><td>How fast the line reels in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_length</code></td><td>Float</td><td>The shortest the line can get, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>auto_release</code> (Web Swing Auto Release)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>on_ground</code></td><td>Boolean</td><td>Release the line when the user lands.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>on_blocked_line</code></td><td>Boolean</td><td>Release the line when something blocks it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>swing_assist</code> (Web Swing Assist)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>anchor_cone_degrees</code></td><td>Float (0.0 ~ 45.0)</td><td>How far from the crosshair an anchor can be and still be picked, in degrees.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10.0</td></tr><tr><td><code>min_anchor_distance</code></td><td>Float (&gt;= 0.0)</td><td>The closest an anchor can be, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>anchor_height_weight</code></td><td>Float (&gt;= 0.0)</td><td>How much higher anchors are preferred.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>velocity_blend_speed</code></td><td>Float (&gt;= 0.0)</td><td>How quickly the swing direction follows the user's movement.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ground_clearance_strength</code></td><td>Float (0.0 ~ 1.0)</td><td>How strongly the swing lifts the user away from the ground.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lateral_steering_strength</code></td><td>Float (&gt;= 0.0)</td><td>How strongly the user can steer sideways while swinging.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>swing_jump_strength</code></td><td>Float (&gt;= 0.0)</td><td>How strong the jump off the line is.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fall_damage_grace_ticks</code></td><td>Integer (&gt;= 0)</td><td>For this many ticks after releasing, fall damage is ignored.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>rope_wrap</code></td><td>Boolean</td><td>Whether the line wraps around corners.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:web_swing",
      "range": 30,
      "beam_renderer": "example:beam_renderer_id",
      "max_speed": 2.6,
      "reel": {}
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "web_swing": {
          "type": "argon:web_swing",
          "range": 30,
          "beam_renderer": "example:beam_renderer_id",
          "max_speed": 2.6,
          "reel": {}
        }
      }
    }
    ```

---

### Web Walking {#argonweb_walking}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:web_walking</code></div>

<div class="argon-desc">While enabled, the user walks through cobwebs without being slowed down.</div>

=== "Example"

    ```json
    {
      "type": "argon:web_walking"
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "web_walking": {
          "type": "argon:web_walking"
        }
      }
    }
    ```

---

### Zone {#argonzone}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:zone</code></div>

<div class="argon-desc">On its first enabled tick, makes a circle on the ground at the user or where they look. Every interval it damages enemies inside and applies effects to them and allies, and allies take less damage. Ends when time is up or the user strays too far.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>radius</code></td><td>(Dynamic) Value</td><td>The radius of the circle in blocks, read once when it is created.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the zone lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100</td></tr><tr><td><code>look_target_range</code></td><td>Double</td><td>If set, the zone is created where the user looks, up to this many blocks away, instead of at the user.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>interval</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How often damage and effects are applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>damage</code></td><td>(Dynamic) Value</td><td>Damage dealt to each enemy on every interval.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>damage_type</code></td><td>Damage Type ID</td><td>The damage type used; the user's normal attack when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to enemies on every interval.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ally_effects</code></td><td><em>Beam Effect</em>[]</td><td>Effects applied to the user, their team and their pets on every interval.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ally_damage_reduction</code></td><td>(Dynamic) Value</td><td>The fraction from 0 to 1 of damage the user, their team and their pets do not take while inside. A Value read once when the zone is created, so it can scale with power age.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>follow_user</code></td><td>Boolean</td><td>If true, the zone moves with the user instead of staying where it was created.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>reduction_affects_user</code></td><td>Boolean</td><td>If false, the damage reduction applies only to allies, not the user (useful when the user has their own reduction).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>end_with_ability</code></td><td>Boolean</td><td>If true, the zone ends as soon as this ability is no longer enabled.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>end_beyond</code></td><td>Double</td><td>If set, the zone ends when the user is farther than this many blocks from its centre.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particle</code></td><td>Particle</td><td>A particle drawn around the edge of the zone.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[]</code> (Beam Effect)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>The effect to apply.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long the effect lasts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>The effect level, starting at 0.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>particles</code></td><td>Boolean</td><td>Whether the effect shows its particles.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>size_tiers</code></td><td><em>Size Tier</em>[]</td><td>Changes or skips the effect depending on the width or type of the target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>effects[].size_tiers[]</code> (Size Tier)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>tag</code></td><td>Entity Type Tag</td><td>Only entities in this tag use the tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min_width</code></td><td>Double (0.0 ~ 64.0)</td><td>The tier applies to entities at least this wide, in blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>skip</code></td><td>Boolean</td><td>If true, matching entities do not get the effect at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>effect</code></td><td>Mob Effect ID</td><td>Replaces the effect for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amplifier</code></td><td>Integer (0 ~ 255)</td><td>Replaces the amplifier for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Replaces the duration for matching entities.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:zone",
      "radius": 5,
      "damage": 2,
      "ally_damage_reduction": 0
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "zone": {
          "type": "argon:zone",
          "radius": 5,
          "damage": 2,
          "ally_damage_reduction": 0
        }
      }
    }
    ```

---

### Zoom {#argonzoom}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:zoom</code></div>

<div class="argon-desc">While enabled, zooms your view to the magnification in "zoom" and eases back out when disabled. It follows "zoom" as it changes, so a data attachment can let scrolling adjust it. Only affects your own view.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>zoom</code></td><td>(Dynamic) Value</td><td>The magnification: 1 is normal, 2 is twice the size, 4 four times. A value, so a data attachment can change it while zoomed. Below 1 counts as 1, 100 is the max. With "level_factor" above 1 it is a level instead.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2.0</td></tr><tr><td><code>rate</code></td><td>Double</td><td>How quickly the view closes on the magnification, per second, when zooming and when "zoom" changes. Higher is snappier. 6 covers about 63% of the way in a sixth of a second.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">6.0</td></tr><tr><td><code>level_factor</code></td><td>Double</td><td>1 (default) means "zoom" is the magnification. Above 1, "zoom" is a level and the magnification is level_factor raised to it, so every scroll step changes the view by the same proportion.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>scale_sensitivity</code></td><td>Boolean</td><td>Whether turning the camera slows down as the view zooms in, so aiming stays steady (like a spyglass). At 4x the camera turns a quarter as far for the same mouse movement.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>scale_render_distance</code></td><td>Boolean</td><td>Whether draw distances grow with the zoom so magnified things stay visible: block entities, other entities, sign outlines and name tags. Only already loaded terrain can show.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">true</td></tr><tr><td><code>reset_on_disable</code></td><td>Boolean</td><td>Whether turning the zoom off puts the level back to "base_level" (in "level_attachment"), so the next zoom starts from the base instead of wherever it was scrolled to. Needs "level_attachment".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>level_attachment</code></td><td>Data Attachment ID</td><td>The number data attachment that holds the zoom level (the one "zoom" reads and scrolling changes), which "reset_on_disable" sets back to "base_level". Only used by "reset_on_disable".</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">none</td></tr><tr><td><code>base_level</code></td><td>Integer</td><td>The value "reset_on_disable" sets the level attachment to.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:zoom",
      "zoom": 4,
      "rate": 8,
      "reset_on_disable": true,
      "properties": {
        "title": "Zoom"
      }
    }
    ```

=== "In a power"

    ```json
    {
      "name": "Example Power",
      "icon": "minecraft:command_block",
      "abilities": {
        "zoom": {
          "type": "argon:zoom",
          "zoom": 4,
          "rate": 8,
          "reset_on_disable": true,
          "properties": {
            "title": "Zoom"
          }
        }
      }
    }
    ```

---


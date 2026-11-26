---
title: Conditions
---

# Conditions

<p class="argon-intro">Conditions are checks that return true or false. They are used in ability states, targets, visibility rules and anywhere else a condition is accepted. Every condition that comes with Argon is listed below.</p>

<p class="argon-count">61 listed &middot; Argon 1.0.1</p>

### Ability Bar Active {#argonability_bar_active}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_bar_active</code></div>

<div class="argon-desc">True while this ability sits in a slot of the given argon:ability_bar. Uses the crouch variant of the slot if it has one and the entity is crouching.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability_bar</code></td><td>String</td><td>The argon:ability_bar ability to check, e.g. "fsang:marvel/mutant/reality_warping#my_bar". Left out, any bar of any power counts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback"></td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_bar_active",
      "ability_bar": "argon:example#my_bar"
    }
    ```

---

### Ability Bar Active (Crouch) {#argonability_bar_active_crouch}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_bar_active_crouch</code></div>

<div class="argon-desc">True while the entity is crouching and this ability sits in a crouch slot of the given argon:ability_bar.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability_bar</code></td><td>String</td><td>The argon:ability_bar ability to check, e.g. "fsang:marvel/mutant/reality_warping#my_bar". Left out, any bar of any power counts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback"></td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_bar_active_crouch",
      "ability_bar": "argon:example#my_bar"
    }
    ```

---

### Ability Enabled Activation {#argonability_enabled_activation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_enabled_activation</code></div>

<div class="argon-desc">Like the vanilla "Ability enabled" condition, but sticky. Once the ability is seen enabled, it keeps passing for the given time after it stops.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The ability to watch for being enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long this stays true after the referenced ability was last seen enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_enabled_activation",
      "ability": "example:power#some_ability",
      "duration": 100
    }
    ```

---

### Ability Type Enabled Activation {#argonability_type_enabled_activation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_type_enabled_activation</code></div>

<div class="argon-desc">Like the vanilla "Ability type enabled" condition, but sticky. Once any ability of "ability_type" is seen enabled, it keeps passing for the given time after they stop.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability_type</code></td><td>Ability Type ID(s) / Tag</td><td>The ability type(s) to watch for being enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long this stays true after an ability of a matching type was last seen enabled.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_type_enabled_activation",
      "ability_type": [
        "argon:effect"
      ],
      "duration": "5s"
    }
    ```

---

### Advancement {#argonadvancement}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:advancement</code></div>

<div class="argon-desc">Checks if the user has a given advancement. Server only, so it is always false on the client. Don't use it in a render_layer's conditions.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>advancement</code></td><td>Identifier</td><td>The id of the advancement the user must have completed.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:advancement",
      "advancement": "minecraft:story/mine_diamond"
    }
    ```

---

### Beam Firing {#argonbeam_firing}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:beam_firing</code></div>

<div class="argon-desc">True while a charged Energy Beam is showing a shot, and for "lead" ticks before the next shot of a multi-shot beam. Use it to raise an arm for each shot.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The Energy Beam ability that has a "charge" setting.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>lead</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long before the next shot of a multi-shot beam this turns true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>If set, only true for this long after each shot instead of the whole time it shows.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:beam_firing",
      "ability": "example:power#some_beam",
      "lead": 2,
      "duration": 3
    }
    ```

---

### Biome {#argonbiome}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:biome</code></div>

<div class="argon-desc">Checks if the user is currently standing in one of the specified biomes.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>biomes</code></td><td>Biome ID(s) / Tag</td><td>The biome(s) to check for, as explicit biome IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:biome",
      "biomes": [
        "minecraft:desert",
        "#minecraft:is_nether"
      ]
    }
    ```

---

### Biome Swap Area {#argonbiome_swap_area}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:biome_swap_area</code></div>

<div class="argon-desc">Checks if the user stands inside an active argon:biome_swap area, optionally one made with a specific biome.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>biome</code></td><td>Identifier</td><td>A biome the area must have been made with to count. Otherwise any active area counts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:biome_swap_area",
      "biome": "minecraft:desert"
    }
    ```

---

### Block Below {#argonblock_below}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:block_below</code></div>

<div class="argon-desc">Checks if the block directly beneath the user's feet matches "blocks". Fluids count as blocks, so "minecraft:water" is true while standing on water, for example with fluid walking.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The block(s) to look for, as explicit block IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>distance</code></td><td>Double</td><td>How many blocks below the feet are searched. 0.5 only checks the block the user is standing on, a larger value also passes while hovering above a matching block.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.5</td></tr><tr><td><code>require_ground</code></td><td>Boolean</td><td>If true, the user also has to be on the ground (or on a fluid they can walk on).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:block_below",
      "require_ground": true,
      "blocks": [
        "#minecraft:sand"
      ]
    }
    ```

---

### Carriable {#argoncarriable}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:carriable</code></div>

<div class="argon-desc">True while you look at something palladium:carry could pick up: any other living entity within "range" blocks. Handy for showing a prompt only when there is a target.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far along the look direction to search, in blocks. Left out, it uses the referenced argon:carry ability's range, or 3 blocks without one.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ability</code></td><td>Ability Reference</td><td>An argon:carry ability ("namespace:power#ability") to check for. A target only counts if that ability could grab it: clear line of sight, not already carried, allowed by allow_mobs / allow_players. Left out, Palladium's own carry rules apply.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:carriable",
      "range": 2
    }
    ```

---

### Carried {#argoncarried}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:carried</code></div>

<div class="argon-desc">True while the entity is held by someone's "argon:carry" ability (the carrier's side is "argon:carrying"). Works for any living entity that can be carried.</div>

=== "Example"

    ```json
    {
      "type": "argon:carried"
    }
    ```

---

### Carrying {#argoncarrying}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:carrying</code></div>

<div class="argon-desc">True while the entity holds something with argon:carry. Unlike palladium:carrying, which only sees palladium:carry, this works for any living carrier.</div>

=== "Example"

    ```json
    {
      "type": "argon:carrying"
    }
    ```

---

### Chat Activation {#argonchat_activation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:chat_activation</code></div>

<div class="argon-desc">Passes briefly after the player says one of the phrases in chat. Works like a key bind in activation mode, but the key is a spoken incantation. Put it straight in the enabling condition. Inside an "and" it only runs while the conditions before it pass.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>incantation</code></td><td>Identifier</td><td>A spell definition from data/<namespace>/incantations/<name>.json. It holds the phrases for each mastery tier, the always-accepted fallback phrases and the cast thresholds. Casting counts toward its mastery.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>phrases</code></td><td>string[]</td><td>Extra fixed phrases that always work, whatever the mastery tier. Letters are compared without case, accents or punctuation, and Greek letters are read as their Latin spelling.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long it stays true after the phrase is said.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>cooldown</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>The cooldown the ability gets after a cast. It uses the ability's cooldown component, so cooldown control abilities and the cooldown condition work with it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

---

### Chat Toggled {#argonchat_toggled}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:chat_toggled</code></div>

<div class="argon-desc">Turns on when the player says a start phrase in chat. Stays on until they say a stop phrase or the maximum duration runs out. The cooldown starts when it turns off. Put it straight in the enabling condition.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>incantation</code></td><td>Identifier</td><td>A spell definition from data/<namespace>/incantations/<name>.json. Its tiers hold the start phrases and its "stop" list holds the stop phrases. Casting counts toward its mastery.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>phrases</code></td><td>string[]</td><td>Extra start phrases that always work, whatever the mastery tier.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>stop_phrases</code></td><td>string[]</td><td>Extra phrases that turn it off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>cooldown</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Cooldown the ability gets once it turns off.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>max_duration</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>Turns itself off after this long. 0 means it never does.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr></tbody></table></div>

---

### Danger Sense Active {#argondanger_sense_active}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:danger_sense_active</code></div>

<div class="argon-desc">Checks if the user has an enabled argon:danger_sense ability that is detecting at least one danger: a nearby hostile mob or a player who recently hurt the user.</div>

=== "Example"

    ```json
    {
      "type": "argon:danger_sense_active"
    }
    ```

---

### Danger Sense Count {#argondanger_sense_count}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:danger_sense_count</code></div>

<div class="argon-desc">Checks how many dangers the user's enabled argon:danger_sense ability is detecting (the largest count if there are several). Useful for triggering an overload once enough threats are around.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Integer</td><td>The fewest detected dangers that still pass.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The most detected dangers that still pass.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2147483647</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:danger_sense_count",
      "min": 8
    }
    ```

---

### Dodge Direction {#argondodge_direction}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dodge_direction</code></div>

<div class="argon-desc">Checks if the referenced dodge ability is showing its dodge pose and the dodge went mostly in the given direction relative to where the entity faces. Diagonals count as whichever axis is stronger.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The dodge ability to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>direction</code></td><td><code>forward</code><br><code>back</code><br><code>left</code><br><code>right</code></td><td>The direction to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dodge_direction",
      "ability": "example:power#dodge",
      "direction": "forward"
    }
    ```

---

### Dodging {#argondodging}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:dodging</code></div>

<div class="argon-desc">Checks if the referenced dodge ability is actively showing its dodge pose right now.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The dodge ability to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:dodging",
      "ability": "example:power#dodge"
    }
    ```

---

### Durability {#argondurability}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:durability</code></div>

<div class="argon-desc">Checks if the item worn or held in the given slot has durability left, as a percentage, between min and max. Fails for an empty slot or an item that can't be damaged.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to check, e.g. an armor slot.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">chest</td></tr><tr><td><code>min</code></td><td>Double</td><td>The minimum remaining durability percentage required (0-100).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max</code></td><td>Double</td><td>The maximum remaining durability percentage allowed (0-100).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:durability",
      "max": 20
    }
    ```

---

### Falling {#argonfalling}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:falling</code></div>

<div class="argon-desc">Checks if the user is in the air and moving downward, so not on the ground and not rising.</div>

=== "Example"

    ```json
    {
      "type": "argon:falling"
    }
    ```

---

### Flight Speed Percent {#argonflight_speed_percent}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:flight_speed_percent</code></div>

<div class="argon-desc">True while the referenced argon:flight_speed_adjuster dial is within min and max (inclusive). The flight version of argon:movement_speed_percent.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The flight speed adjuster ability whose dial to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min</code></td><td>Integer</td><td>The lowest dial value that passes (inclusive). Unset means no lower limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The highest dial value that passes (inclusive). Unset means no upper limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:flight_speed_percent",
      "ability": "example:power#flight_speed_adjuster",
      "min": 25,
      "max": 100
    }
    ```

---

### Grappling {#argongrappling}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:grappling</code></div>

<div class="argon-desc">Checks if the referenced grapple ability (argon:grapple or palladium:grapple) is currently grappled to a block, an entity or either, depending on the mode.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The grapple ability to check (argon:grapple or palladium:grapple).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>block</code><br><code>entity</code><br><code>either</code></td><td>Which kind of grapple to check for.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">EITHER</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:grappling",
      "ability": "example:power#grapple"
    }
    ```

---

### Ground Distance {#argonground_distance}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ground_distance</code></div>

<div class="argon-desc">Checks if the user is on the ground or within max_distance blocks of solid ground directly below.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>max_distance</code></td><td>Double</td><td>The maximum distance, in blocks, to the ground below the user.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ground_distance",
      "max_distance": 3
    }
    ```

---

### Has Energy {#argonhas_energy}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_energy</code></div>

<div class="argon-desc">Checks if the item in the given slot has stored energy between min and max. Infinite and creative energy items always pass.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to look for the energy-storing item in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">curios:hands</td></tr><tr><td><code>min</code></td><td>Integer</td><td>The minimum stored energy required.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The maximum stored energy allowed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2147483647</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_energy",
      "min": 1000,
      "max": 5000
    }
    ```

---

### Has Fluid {#argonhas_fluid}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_fluid</code></div>

<div class="argon-desc">Checks whether the fluid item in the given slot has a stored fluid amount between min and max.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Which slot to look for the fluid-storing item in.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">curios:hands</td></tr><tr><td><code>min</code></td><td>Integer</td><td>The minimum stored fluid amount required.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The maximum stored fluid amount allowed.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2147483647</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_fluid",
      "min": 100,
      "max": 500
    }
    ```

---

### Has Input {#argonhas_input}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_input</code></div>

<div class="argon-desc">Checks if the user is holding a movement key (forward, back, left or right). Unlike palladium:has_movement_input it also works while a world is loading and in single player's built-in server.</div>

=== "Example"

    ```json
    {
      "type": "argon:has_input"
    }
    ```

---

### Has Item {#argonhas_item}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_item</code></div>

<div class="argon-desc">Checks if the user has at least one matching item anywhere on them: inventory, worn equipment and Curios slots where they apply.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>items</code></td><td>Item ID(s) / Tag</td><td>The item(s) to search for, given as explicit item IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_item",
      "items": [
        "minecraft:totem_of_undying"
      ]
    }
    ```

---

### Has Power {#argonhas_power}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_power</code></div>

<div class="argon-desc">Checks if the user has a matching power. "include" (default) needs at least one present, "exclude" needs all of them absent.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power(s) to check for, given as explicit power IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether a matching power must be present ("include") or absent ("exclude").</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">INCLUDE</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_power",
      "power": "#palladium:arachnid"
    }
    ```

---

### Has Stored Equipment {#argonhas_stored_equipment}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_stored_equipment</code></div>

<div class="argon-desc">Checks if the store_equipment ability has anything currently stored under the given ID.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>id</code></td><td>String</td><td>The ID to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_stored_equipment",
      "id": "ranger_armor"
    }
    ```

---

### Has Stored Item {#argonhas_stored_item}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_stored_item</code></div>

<div class="argon-desc">Checks if at least one matching item is stored in any slot of the referenced argon:item_storage ability.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>item_storage</code></td><td>String</td><td>The argon:item_storage ability whose slots to check, e.g. "fsang:example#my_storage".</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>items</code></td><td>Item ID(s) / Tag</td><td>The item(s) to search for among the stored slots, given as explicit item IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_stored_item",
      "item_storage": "fsang:example#my_storage",
      "items": [
        "minecraft:totem_of_undying"
      ]
    }
    ```

---

### Has Suit Modification {#argonhas_suit_modification}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_suit_modification</code></div>

<div class="argon-desc">Checks if the entity wears a complete Palladium suit with the given Tech Table modification installed on every piece. Can be limited to one suit set.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>modification</code></td><td>String</td><td>The id of the suit modification (the file name under data/<namespace>/argon/suit_modification/).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>suit</code></td><td>String</td><td>The id of a Palladium suit set the worn suit has to be; any suit when left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback"></td></tr><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>Check the item worn or held in this slot instead of a suit (for modules installed on a device item in the Modify tab).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">chest</td></tr><tr><td><code>min_level</code></td><td>Integer</td><td>For modules that can be installed several times: the lowest level that counts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_suit_modification",
      "modification": "example:reserve_battery"
    }
    ```

---

### Has Tech Slot Item {#argonhas_tech_slot_item}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:has_tech_slot_item</code></div>

<div class="argon-desc">True while the item in the given player slot has something in one of its Tech Table Customize slots. "tech_slot" limits it to one slot ID, "items" to certain items or item tags ("#namespace:tag").</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The player slot holding the customized item.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>tech_slot</code></td><td>Identifier</td><td>Only check the Customize slot with this ID.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>items</code></td><td>String, String[]</td><td>Only count these items or item tags.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:has_tech_slot_item",
      "slot": "chest",
      "tech_slot": "example:core"
    }
    ```

---

### Health {#argonhealth}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:health</code></div>

<div class="argon-desc">Checks if the user's current health, as a percentage of their current max health (with max health modifiers), is between min and max (inclusive).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Double</td><td>The minimum health percentage required (0-100).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max</code></td><td>Double</td><td>The maximum health percentage allowed (0-100).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">100.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:health",
      "max": 25
    }
    ```

---

### Is Female {#argonis_female}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:is_female</code></div>

<div class="argon-desc">True if the wearer picked "Female" in the argon:body customization. A shorthand for palladium:customization_selected, handy for limiting a body overlay to one chestplate.</div>

=== "Example"

    ```json
    {
      "type": "argon:is_female"
    }
    ```

---

### Item Component {#argonitem_component}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_component</code></div>

<div class="argon-desc">Checks if the item in the given slot has a specific data component set to a specific text value.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slot whose item is checked.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>component</code></td><td>Identifier</td><td>The id of the data component to check, e.g. "argon:weapon_mode".</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>String</td><td>The value the component must currently equal.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:item_component",
      "slot": "mainhand",
      "component": "argon:weapon_mode",
      "value": "blaster"
    }
    ```

---

### Jumping {#argonjumping}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:jumping</code></div>

<div class="argon-desc">Checks if the user is in the air and moving upward, not standing on the ground or falling.</div>

=== "Example"

    ```json
    {
      "type": "argon:jumping"
    }
    ```

---

### Karma Alignment {#argonkarma_alignment}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:karma_alignment</code></div>

<div class="argon-desc">True while the player's alignment is the given one. Use positive, neutral or negative for a whole side, or an alignment id such as hero or mastermind.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>alignment</code></td><td><code>positive</code><br><code>neutral</code><br><code>negative</code><br><code>mastermind</code><br><code>villain</code><br><code>thug</code><br><code>lackey</code><br><code>neutral</code><br><code>vigilante</code><br><code>protector</code><br><code>hero</code><br><code>legend</code></td><td>The alignment id or side to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:karma_alignment",
      "alignment": "mastermind"
    }
    ```

---

### Karma Range {#argonkarma_range}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:karma_range</code></div>

<div class="argon-desc">True while the player's karma is within the inclusive range. Karma goes from -5000 to 5000 by default. Use a maximum of -501 for "below -500".</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>minimum</code></td><td>Integer</td><td>The lowest karma that passes, inclusive.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-2147483648</td></tr><tr><td><code>maximum</code></td><td>Integer</td><td>The highest karma that passes, inclusive.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2147483647</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:karma_range",
      "minimum": -5000,
      "maximum": -501
    }
    ```

---

### Key Press On Block {#argonkey_press_on_block}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:key_press_on_block</code></div>

<div class="argon-desc">True while the referenced ability's key is held and you look at a block matching "blocks" within "range". Handy for climbing, which needs both the key and a climbable surface.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The ability whose key_bind key-press state to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The block(s) the user must be looking at, as explicit block IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>Double</td><td>How far, in blocks, the look-direction raycast reaches.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:key_press_on_block",
      "ability": "example:power#wall_crawling",
      "range": 5,
      "blocks": [
        "#minecraft:walls"
      ]
    }
    ```

---

### Looking At Entity {#argonlooking_at_entity}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:looking_at_entity</code></div>

<div class="argon-desc">True while the entity is looking at another entity within range. The entity can be limited to certain types, a single type or a tag. Blocks in the way hide entities behind them unless through_blocks is set.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_types</code></td><td>Entity Type ID(s) / Tag</td><td>The entity types that count, as one entity type ID, a tag ("#namespace:tag"), or a list mixing both. Left out, any entity counts.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>Double (0.1 ~ 512.0)</td><td>How far along the look direction to search, in blocks.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>through_blocks</code></td><td>Boolean</td><td>If true, entities behind blocks still count. If false, a block in the way hides them.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:looking_at_entity",
      "range": 8
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:looking_at_entity",
      "range": 12,
      "entity_types": [
        "minecraft:villager",
        "#minecraft:skeletons"
      ]
    }
    ```

---

### Main Hand {#argonmain_hand}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:main_hand</code></div>

<div class="argon-desc">Checks the player's main hand setting (left or right handed), not which hand holds an item. Always false for non-players.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>hand</code></td><td><code>none</code><br><code>main_arm</code><br><code>off_arm</code><br><code>right_arm</code><br><code>left_arm</code><br><code>both</code></td><td>The main hand to check for.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:main_hand",
      "hand": "right"
    }
    ```

---

### Marked Target {#argonmarked_target}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:marked_target</code></div>

<div class="argon-desc">Checks if the entity has a living, unexpired target mark from argon:target_mark.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>moving_toward</code></td><td>Boolean</td><td>If true, the entity must also be moving toward the marked target.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr><tr><td><code>max_distance</code></td><td>Double</td><td>If above 0, the marked target must be within this many blocks.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:marked_target",
      "moving_toward": true
    }
    ```

---

### Movement Speed {#argonmovement_speed}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:movement_speed</code></div>

<div class="argon-desc">True while the entity's actual speed, measured from how far it moved since the previous tick, is within min and max (inclusive), in blocks per second. Works on the client too, so it can drive trails and other visuals.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Double</td><td>The lowest speed in blocks per second that passes.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max</code></td><td>Double</td><td>The highest speed in blocks per second that passes. Unset means no upper limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>horizontal_only</code></td><td>Boolean</td><td>If true, vertical movement is ignored.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:movement_speed",
      "min": 12,
      "horizontal_only": true
    }
    ```

---

### Movement Speed Percent {#argonmovement_speed_percent}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:movement_speed_percent</code></div>

<div class="argon-desc">True while the referenced movement_speed_adjuster dial is within "min" and "max" (inclusive). Handy for gating a speed tier on the dial being turned up.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The movement_speed_adjuster ability whose dial to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min</code></td><td>Integer</td><td>The lowest dial value this still passes for.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">-2147483648</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The highest dial value this still passes for.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">2147483647</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:movement_speed_percent",
      "ability": "example:power#movement_speed_adjuster",
      "min": 50
    }
    ```

---

### Nearby Block {#argonnearby_block}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:nearby_block</code></div>

<div class="argon-desc">Checks if at least one block matching "blocks" is within "radius" of the user. Scans every block in range on each check.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>blocks</code></td><td>Block ID(s) / Tag</td><td>The block(s) to search for, as explicit block IDs, a tag ("#namespace:tag"), or a mix of both.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>radius</code></td><td>Double</td><td>How far from the user to search.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:nearby_block",
      "radius": 8,
      "blocks": [
        "#minecraft:diamond_ores"
      ]
    }
    ```

---

### Nearby Entities {#argonnearby_entities}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:nearby_entities</code></div>

<div class="argon-desc">Checks if at least one other entity is within range, optionally only living or only non-living ones, and/or ones that do or don't have specific powers.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>entity_filter</code></td><td><code>living</code><br><code>non_living</code><br><code>all</code></td><td>Which kinds of entities count: 'living' for players/mobs, 'non_living' for everything else.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">ALL</td></tr><tr><td><code>radius</code></td><td>Double</td><td>How far from the entity to search.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>powers</code></td><td><em>Power Requirement</em>,<br><em>Power Requirement</em>[]</td><td>Restricts which entities count based on the powers they hold. Each entry lists a "power" (an explicit power id, a power tag ("#namespace:tag"), or a mix of both) and an optional "mode" - "include" (default) requires at least one matching power to be present, "exclude" requires all of them to be absent; an entity only counts if it satisfies every entry. Non-living entities never satisfy an "include" entry. Leave unset (the default) to not filter by power at all.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

    <p class="argon-nested"><code>powers</code> (Power Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Power ID(s) / Tag</td><td>The power or powers the entity has to have.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>mode</code></td><td><code>include</code><br><code>exclude</code></td><td>Whether the entity must have the power (include) or must not have it (exclude).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">include</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:nearby_entities",
      "entity_filter": "living",
      "radius": 8
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:nearby_entities",
      "entity_filter": "living",
      "radius": 8,
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
    ```

---

### Perspective {#argonperspective}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:perspective</code></div>

<div class="argon-desc">Checks if the owning player is in first or third person, synced from the client to the server. Defaults to first person and is always false for non-players.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>first_person</code></td><td>Boolean</td><td>True to check for first person, false to check for third person (front or back).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:perspective",
      "first_person": true
    }
    ```

---

### Possessing {#argonpossessing}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:possessing</code></div>

<div class="argon-desc">Passes while the entity is possessing another entity with an argon:possess ability. Without an ability set, any possess ability the entity has counts.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>Only check this possess ability. Any possess ability counts if unset.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example 1"

    ```json
    {
      "type": "argon:possessing"
    }
    ```

=== "Example 2"

    ```json
    {
      "type": "argon:possessing",
      "ability": "example:power#possess"
    }
    ```

---

### Power Age {#argonpower_age}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:power_age</code></div>

<div class="argon-desc">True while the age counted by the referenced argon:time_growth ability, in days, is within min and max (inclusive).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The argon:time_growth ability whose age to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min</code></td><td>Double</td><td>The lowest age in days that passes.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr><tr><td><code>max</code></td><td>Double</td><td>The highest age in days that passes. Unset means no upper limit.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:power_age",
      "ability": "example:power#growth",
      "min": 10,
      "max": 20
    }
    ```

---

### Reacted {#argonreacted}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:reacted</code></div>

<div class="argon-desc">Checks if the referenced argon:damage_reaction ability reacted to a hit within the given time, optionally to one specific reaction.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The damage reaction ability to check.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>within</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How recently the reaction must have happened.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">20</td></tr><tr><td><code>reaction</code></td><td>String</td><td>Only count the reaction with this id.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:reacted",
      "ability": "example:power#reaction"
    }
    ```

---

### Recently Attacked {#argonrecently_attacked}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:recently_attacked</code></div>

<div class="argon-desc">Checks if the entity dealt damage to anything (melee, ranged or from an ability) within the given time.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>within</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How recently the entity must have last attacked something for this to pass.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>or_hurt_by_hostile</code></td><td>Boolean</td><td>If true, the condition also passes when a hostile mob damaged the entity within that time.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:recently_attacked",
      "within": 60
    }
    ```

---

### Saturation {#argonsaturation}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:saturation</code></div>

<div class="argon-desc">Checks if the user's saturation level is at least the given amount. Always false for non-players.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>amount</code></td><td>Float</td><td>The minimum saturation level required.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:saturation",
      "amount": 4
    }
    ```

---

### Sky Access {#argonsky_access}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:sky_access</code></div>

<div class="argon-desc">Passes while nothing solid is above the user's head, so they can see the open sky. Combine with a not condition to detect being underground or under a roof.</div>

=== "Example"

    ```json
    {
      "type": "argon:sky_access"
    }
    ```

---

### Targeted By Mob {#argontargeted_by_mob}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:targeted_by_mob</code></div>

<div class="argon-desc">Checks if at least one mob within range has the user as its AI attack target. Scans nearby mobs' targets rather than a global registry.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>range</code></td><td>Double</td><td>How far out to search for mobs that might be targeting the user.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:targeted_by_mob",
      "range": 24
    }
    ```

---

### Tech Toggle {#argontech_toggle}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:tech_toggle</code></div>

<div class="argon-desc">True while a Tech Table Customize button is switched on for the item in the given player slot.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The player slot holding the customized item.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>toggle</code></td><td>Identifier</td><td>The ID of the button.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:tech_toggle",
      "slot": "chest",
      "toggle": "example:overdrive"
    }
    ```

---

### Throw Event {#argonthrow_event}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:throw_event</code></div>

<div class="argon-desc">True for a short time after the entity threw, recalled or caught an item with an argon:throwable_item ability. It works on the client too, so animation controllers can use it to play a throw, recall or catch animation. The arm option restricts it to players whose main arm matches, so left-handed players can get a mirrored animation.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>event</code></td><td><code>throw</code><br><code>recall</code><br><code>catch</code></td><td>Which event to look for.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ticks</code></td><td>Integer</td><td>How many ticks the condition stays true after the event.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr><tr><td><code>arm</code></td><td><code>any</code><br><code>right</code><br><code>left</code></td><td>any, right or left: only players with that main arm pass.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">any</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:throw_event",
      "event": "catch",
      "ticks": 8,
      "arm": "right"
    }
    ```

---

### Time Of Day {#argontime_of_day}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:time_of_day</code></div>

<div class="argon-desc">Checks if the overworld's time of day is between min and max inclusive. Wraps around midnight if max is smaller than min.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min</code></td><td>Integer</td><td>The start of the time range, in ticks (0 = dawn, 6000 = midday, 12000 = dusk, 18000 = midnight).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The end of the time range, in ticks, wrapping around midnight if smaller than min.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:time_of_day",
      "min": 13000,
      "max": 23000
    }
    ```

---

### Took Off {#argontook_off}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:took_off</code></div>

<div class="argon-desc">True for a short time after an "argon:charged_takeoff" launched the entity. Use it to hand the launch over to a flight ability, e.g. as the enabling of an "argon:force_start_flight".</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>within</code></td><td>Integer,<br>Time String (&quot;40s&quot;, &quot;2m&quot;, etc.)</td><td>How long after the launch this stays true.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">10</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:took_off"
    }
    ```

---

### Wall Crawling Active {#argonwall_crawling_active}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:wall_crawling_active</code></div>

<div class="argon-desc">Checks if the user has an enabled argon:wall_crawling ability that is attached to a wall or ceiling. Only true while on a surface, not whenever the ability is enabled.</div>

=== "Example"

    ```json
    {
      "type": "argon:wall_crawling_active"
    }
    ```

---

### Weather {#argonweather}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:weather</code></div>

<div class="argon-desc">Passes while the world the entity is in has the given weather. Only the real world weather counts; local storms made by abilities do not change it.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>weather</code></td><td><code>clear</code><br><code>raining</code><br><code>thundering</code></td><td>The weather to test for. Raining also passes during a thunderstorm.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">thundering</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:weather"
    }
    ```

---

### Y Level {#argony_level}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:y_level</code></div>

<div class="argon-desc">Checks if the user is currently at or above a specified Y level.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>min_y</code></td><td>Double</td><td>The minimum Y coordinate the user must be at or above.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:y_level",
      "min_y": 64
    }
    ```

---


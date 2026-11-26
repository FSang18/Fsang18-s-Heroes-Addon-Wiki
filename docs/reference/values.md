---
title: Values
---

# Values

<p class="argon-intro">Values are numbers, text or colors that are calculated while the game runs, so a setting can follow a level, a dial, a stat or any other changing source instead of staying fixed.</p>

<p class="argon-count">6 listed &middot; Argon 1.0.1</p>

### Ability Bar Slot {#argonability_bar_slot}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ability_bar_slot</code></div>

<div class="argon-desc">The slot, counting from 0, that the player has put the given ability in on the given ability bar (in the current preset, normal or crouch), or -1 if it is not assigned. Use it as an ability's list_index so assigned abilities sit together on one page of the ability list in the order of their slots, however many abilities the pool holds.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability_bar</code></td><td>Ability Reference</td><td>The argon:ability_bar ability.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>ability</code></td><td>Ability Reference</td><td>The pooled ability to look up.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ability_bar_slot",
      "ability_bar": "example:power#bar",
      "ability": "example:power#ability"
    }
    ```

---

### Beam Charge {#argonbeam_charge}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:beam_charge</code></div>

<div class="argon-desc">Scales a value by how charged the shot of a charged argon:energy_beam was. Use it in that beam's damage, knockback or lift. Multiplies "value" by "min" at no charge and "max" at full charge.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The value to scale.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>min</code></td><td>Double</td><td>The multiplier at the lowest charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr><tr><td><code>max</code></td><td>Double</td><td>The multiplier at full charge.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:beam_charge",
      "value": 10,
      "max": 2
    }
    ```

---

### Flight Speed {#argonflight_speed}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:flight_speed</code></div>

<div class="argon-desc">A flight speed that follows an argon:flight_speed_adjuster dial: "base" plus the dial's value divided by its division_amount. Use it for a flight type's "speed" and "sprint_speed". Just "base" while the ability is off.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The flight speed adjuster ability whose dial to follow.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>base</code></td><td>Double</td><td>The speed with the dial at zero; the dial's bonus is added to this.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:flight_speed",
      "ability": "example:power#flight_speed_adjuster",
      "base": 1.5
    }
    ```

---

### Item Custom Value {#argonitem_custom_value}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_custom_value</code></div>

<div class="argon-desc">A number a Tech Table module wrote onto the item in the given slot with its "argon:custom_value" effect, under the name given there. Uses the fallback if the item has no such value.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>slot</code></td><td><code>mainhand</code><br><code>offhand</code><br><code>head</code><br><code>chest</code><br><code>legs</code><br><code>feet</code><br><code>body</code><br><code>curios:head</code><br><code>curios:necklace</code></td><td>The slot whose item to read, e.g. an armor slot or a curios slot.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>key</code></td><td>String</td><td>The name the value was given in the module's effect.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fallback</code></td><td>Double</td><td>What to use when the item does not have the value.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:item_custom_value",
      "slot": "chest",
      "key": "example:core_power"
    }
    ```

---

### Power Age {#argonpower_age}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:power_age</code></div>

<div class="argon-desc">The age, in days, counted by an argon:time_growth ability: the time the ability has been enabled for the player, as a decimal. 0 if the ability is missing.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The argon:time_growth ability whose age to read.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:power_age",
      "ability": "example:power#growth"
    }
    ```

---

### Smoothed {#argonsmoothed}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:smoothed</code></div>

<div class="argon-desc">A number that slides toward another value at a steady speed instead of jumping, so stepped values like a beam's range change smoothly. Each entity has its own figure, which restarts if unread for half a second.</div>

<div class="argon-returns"><span class="argon-meta-label">Returns</span> Double</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>value</code></td><td>(Dynamic) Value</td><td>The value to follow.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>speed</code></td><td>Double</td><td>How far it moves towards a higher value each second, in the wrapped value's own unit.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>fall_speed</code></td><td>Double</td><td>How far it moves towards a lower value each second; the same as "speed" if left out.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0.0</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:smoothed",
      "value": 10,
      "speed": 12,
      "fall_speed": 12
    }
    ```

---


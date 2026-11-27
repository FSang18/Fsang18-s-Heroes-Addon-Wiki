---
title: Module Functions
---

# Module Functions

<p class="argon-intro">Module functions change an item at the Tech Table. They go in the <code>effects</code> of a <a href="../../guides/tech-table/modules/">module</a>, or in the <code>functions</code> of a <a href="../../guides/tech-table/customize/">Customize slot or button</a>. Entries marked "Modules only" can't be used in Customize files. On a suit module, powers and attribute bonuses go on the chestplate (or the first piece the suit has) and the other functions go on every piece, unless <code>pieces</code> says otherwise.</p>

<p class="argon-count">10 listed &middot; Argon 1.1.0</p>

### Add Power {#argonadd_power}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:add_power</code></div>

<div class="argon-desc">Gives the item a Palladium power while it is in one of the listed slots. The power is taken away when the function stops applying.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>power</code></td><td>Identifier</td><td>The power to give.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>slots</code></td><td>String, String[]</td><td>Player slots such as mainhand, chest or curios:body.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">The slots the item already gives powers in, else its equipment slot, else mainhand</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:add_power",
      "power": "example:jet_boots",
      "slots": "feet"
    }
    ```

---

### Attribute Modifier {#argonattribute_modifier}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:attribute_modifier</code></div>

<div class="argon-desc">Adds an attribute bonus while the item is worn or held. On a module the amount is multiplied by the installed level.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>attribute</code></td><td>Identifier</td><td>The attribute to change.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>amount</code></td><td>Double</td><td>How much to change it by.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>operation</code></td><td><code>add_value</code><br><code>add_multiplied_base</code><br><code>add_multiplied_total</code></td><td>How the amount is applied.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">add_value</td></tr><tr><td><code>slots</code></td><td>String, String[]</td><td>mainhand, offhand, hand, head, chest, legs, feet, armor, body, any, or curios:&lt;slot&gt;.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">The curios slot the item gives powers in, else its equipment slot, else mainhand</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:attribute_modifier",
      "attribute": "minecraft:armor",
      "amount": 2,
      "slots": "curios:body"
    }
    ```

---

### Copy Component {#argoncopy_component}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:copy_component</code></div>

<div class="argon-desc">Copies a data component from the inserted item to the base item, for example a dye color. Only does something in a Customize slot, where there is an inserted item.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>component</code></td><td>Identifier</td><td>The component written on the base item.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>from</code></td><td>Identifier</td><td>The component read from the inserted item.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">The value of component</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:copy_component",
      "component": "minecraft:dyed_color"
    }
    ```

---

### Custom Value {#argoncustom_value}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:custom_value</code></div>

<div class="argon-desc">Modules only. Stores a named number on the item that depends on which material was used. Each level adds its own number. Read it with the argon:item_custom_value value.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>key</code></td><td>Identifier</td><td>The name the number is stored under.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>values</code></td><td>Object[]</td><td>Entries with item (an ingredient) and value (a whole number).</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>fallback</code></td><td>Integer</td><td>The number used when no entry matches.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">0</td></tr><tr><td><code>tooltip</code></td><td>String</td><td>A tooltip line, with %s for the total.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:custom_value",
      "key": "example:core_power",
      "values": [ { "item": "minecraft:diamond_block", "value": 5 } ],
      "fallback": 1,
      "tooltip": "Core Power: %s"
    }
    ```

---

### Energy Capacity {#argonenergy_capacity}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:energy_capacity</code></div>

<div class="argon-desc">Modules only. Raises the energy capacity of an item that stores energy.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>per_level</code></td><td>Integer</td><td>Capacity added for each level.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>max</code></td><td>Integer</td><td>The highest capacity the effect can reach.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:energy_capacity",
      "per_level": 5000,
      "max": 50000
    }
    ```

---

### Fluid Capacity {#argonfluid_capacity}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:fluid_capacity</code></div>

<div class="argon-desc">Modules only. Raises the capacity of an item that stores fluid, up to the item's own maximum.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>per_level</code></td><td>Integer</td><td>Capacity in mB added for each level.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:fluid_capacity",
      "per_level": 500
    }
    ```

---

### Integer Component {#argoninteger_component}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:integer_component</code></div>

<div class="argon-desc">Modules only. Sets a whole number data component to the level multiplied by per_level.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>component</code></td><td>Identifier</td><td>The component to set.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>per_level</code></td><td>Integer</td><td>Amount for each level.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">1</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:integer_component",
      "component": "example:charges",
      "per_level": 2
    }
    ```

---

### Item ID To Component {#argonitem_id_to_component}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:item_id_to_component</code></div>

<div class="argon-desc">Writes the inserted item's name (the part after the namespace) to a text component. Nothing is written if the name does not start with strip_prefix. Only does something in a Customize slot.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>component</code></td><td>Identifier</td><td>A text data component.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>strip_prefix</code></td><td>String</td><td>Text removed from the start of the name.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">Empty</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:item_id_to_component",
      "component": "example:casing",
      "strip_prefix": "casing_"
    }
    ```

---

### Set Component {#argonset_component}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:set_component</code></div>

<div class="argon-desc">Sets any data component on the item. When the function stops applying, the component goes back to the item's default.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>component</code></td><td>Identifier</td><td>The component to set.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>value</code></td><td>Any</td><td>The value, written the way the component is written in an item file.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>clears</code></td><td>Identifier[]</td><td>Other components reset along with this one.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:set_component",
      "component": "minecraft:max_damage",
      "value": 500
    }
    ```

---

### Tooltip {#argontooltip}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:tooltip</code></div>

<div class="argon-desc">Adds a line to the item's tooltip.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>text</code></td><td>Component</td><td>The text to show.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>pieces</code></td><td>String[]</td><td>On a suit module, the armor pieces it goes on: head, chest, legs, feet.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">See above</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:tooltip",
      "text": "Jet boots installed"
    }
    ```

---


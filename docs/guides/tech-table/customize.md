---
title: Customize Slots
blurb: Give any item its own slots, buttons and color pickers.
---

# Customize Slots

A customization file gives an item its own **slots**, **buttons** and **color pickers** on the Tech Table's Customize tab. The player puts the item in the top slot, and everything the pack defined for it appears.

`data/<namespace>/argon/tech_table_customization/<name>.json`

## A full example

A gauntlet that takes a core and a dye chip.

```json
{
  "items": "example:gauntlet",
  "slots": [
    {
      "id": "example:core",
      "accepts": "#example:gauntlet_cores",
      "preview": "minecraft:diamond",
      "functions": [
        { "type": "argon:add_power", "power": "example:gauntlet_powered", "slots": "mainhand" }
      ],
      "variants": [
        {
          "items": "minecraft:netherite_ingot",
          "functions": [
            { "type": "argon:attribute_modifier", "attribute": "minecraft:attack_damage", "amount": 4, "slots": "mainhand" },
            { "type": "argon:tooltip", "text": "Netherite core" }
          ]
        }
      ]
    },
    {
      "id": "example:dye_chip",
      "accepts": "example:chip"
    }
  ],
  "toggles": [
    {
      "id": "example:overdrive",
      "title": "Overdrive",
      "requires": ["example:core"],
      "functions": [ { "type": "argon:tooltip", "text": "Overdrive on" } ]
    }
  ],
  "colors": [
    {
      "id": "example:trim",
      "title": "Trim",
      "component": "minecraft:dyed_color",
      "requires": ["example:dye_chip"]
    }
  ]
}
```

While a core is in the gauntlet, it gives the power in the main hand. A netherite core also adds attack damage. The Overdrive button appears once a core is in, and the Trim color picker appears once the chip is in.

## File settings

| Key | Description | Required | Fallback |
|---|---|---|---|
| `items` | The item, item tag (`"#namespace:tag"`) or list of them that the file applies to. | Yes | |
| `slots` | The item's slots. | No | Empty |
| `toggles` | The item's buttons. | No | Empty |
| `colors` | The item's color pickers. | No | Empty |
| `replace` | `true` throws away what earlier files defined for the item. | No | `false` |
| `priority` | Files with a higher number are applied later. | No | `0` |

## Slots

| Key | Description | Required | Fallback |
|---|---|---|---|
| `id` | A unique name for the slot. The inserted item is saved under it. | Yes | |
| `accepts` | Items or item tags that can go in. | Yes | |
| `preview` | An item shown faintly while the slot is empty. | No | None |
| `max_stack` | How many items fit, from 1 to 99. | No | `1` |
| `functions` | [Module functions](../../reference/module-functions.md) active while the slot is filled. | No | Empty |
| `variants` | Extra functions for particular inserted items. Each has `items` and `functions`. | No | Empty |
| `legacy_index` | Reads an item saved in the vanilla container component at this position, for items that used the older Java slot system. | No | None |

## Buttons

| Key | Description | Required | Fallback |
|---|---|---|---|
| `id` | A unique name for the button. | Yes | |
| `title` | The button's label. | Yes | |
| `on` | Text shown after the title while on. | No | "ON" |
| `off` | Text shown after the title while off. | No | "OFF" |
| `component` | A true or false data component to store the state in, so models and render layers can read it. | No | Stored by Argon |
| `requires` | Slot IDs that must be filled for the button to appear. | No | Empty |
| `functions` | Functions active while the button is on. | No | Empty |
| `off_functions` | Functions active while the button is off. | No | Empty |

## Color pickers

| Key | Description | Required | Fallback |
|---|---|---|---|
| `id` | A unique name for the picker. | Yes | |
| `title` | The name shown above the sliders when there are several pickers. | Yes | |
| `component` | The data component the color is written to. It has to accept a number, or be `minecraft:dyed_color`. | Yes | |
| `requires` | Slot IDs that must be filled for the picker to appear. Emptying one removes the color. | No | Empty |

The player picks a color with the red, green and blue sliders or types a hex code.

## Functions that work here

Customize files can use `argon:set_component`, `argon:copy_component`, `argon:item_id_to_component`, `argon:add_power`, `argon:attribute_modifier` and `argon:tooltip`. The capacity, number and custom value effects only work on [modules](modules.md), and a file that uses one in a slot is rejected with an error in the log.

## Reading slots in a power

Powers added by `argon:add_power` need nothing else. For your own powers, two conditions check an item's slots and buttons:

```json
"state": {
  "enabling": {
    "type": "argon:has_tech_slot_item",
    "slot": "mainhand",
    "tech_slot": "example:core",
    "items": "minecraft:netherite_ingot"
  }
}
```

```json
"state": { "enabling": { "type": "argon:tech_toggle", "slot": "mainhand", "toggle": "example:overdrive" } }
```

See [Conditions](../../reference/conditions.md) for every setting.

## Several files for one item

Files that match the same item are **merged**, so an add-on can give another pack's item a new slot without copying its file.

- Files are applied in order of `priority`, then by file name.
- A slot, button or color picker with the same `id` as an earlier one replaces it.
- `replace: true` discards everything applied before that file.

The tab shows three slots and three buttons at a time. With more than that, arrows appear, and the mouse wheel scrolls the slot column.

## Good to know

- Customization files reload with `/reload`. An item that already has parts in it picks up a changed file the next time something on it is changed at a Tech Table.
- Inserted items are saved on the base item, so they travel with it.
- When a function stops applying, the components it set go back to the item's default. Attribute bonuses from other sources are left alone.
- Do not let two sources manage the same component on one item, because the one worked out last wins.

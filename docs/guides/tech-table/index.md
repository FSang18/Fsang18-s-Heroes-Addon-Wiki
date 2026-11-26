---
title: Tech Table
menu_title: Tech Table
blurb: Timed crafting, modules, and custom item slots, all from JSON.
---

# Tech Table

The Tech Table (`argon:tech_table`) is a workbench for powered gear. It has three tabs, and a pack sets all of them up with JSON.

| Tab | What the player does | Where a pack defines it |
|---|---|---|
| **Craft** | Runs timed recipes on a 5x5 grid. | `data/<namespace>/recipe/` |
| **Modify** | Installs modules on a suit or a device. | `data/<namespace>/argon/suit_modification/` |
| **Customize** | Puts items into an item's own slots, presses its buttons and picks its colors. | `data/<namespace>/argon/tech_table_customization/` |

## Which one to use

- Use a **module** for an upgrade that costs materials, can have levels, and can be permanent. See [Modules](modules.md).
- Use a **Customize slot** for a part the player can swap in and out freely, such as a casing, a chip or a core. See [Customize Slots](customize.md).

Both can use the same [module functions](../../reference/module-functions.md) to change an item, give it a power or add stats.

## Recipes

`data/<namespace>/recipe/<name>.json`, `"type": "argon:tech_table_crafting"`.

```json
{
  "type": "argon:tech_table_crafting",
  "pattern": ["ccc", "cdc", "ccc"],
  "key": { "c": "minecraft:copper_ingot", "d": { "ingredient": "minecraft:diamond", "count": 2 } },
  "tool": { "ingredient": "minecraft:shears", "mode": "damaged", "amount": 3 },
  "result": { "item": { "id": "minecraft:diamond", "count": 2 } },
  "name": { "translate": "recipe.mypack.diamonds" },
  "time": 200
}
```

| Key | Description | Required | Fallback |
|---|---|---|---|
| `pattern` and `key` | A shaped recipe of any size up to 5x5. | One of `pattern` or `ingredients` | None |
| `ingredients` | A shapeless recipe with up to 25 entries. | One of `pattern` or `ingredients` | None |
| `mirror` | Whether a shaped recipe also works mirrored. | No | `true` |
| `tool` | An item that has to be in the separate tool slot. `mode` is `consumed`, `retained` or `damaged`, with `amount` for damage. | No | None (`mode`: `retained`) |
| `result` | `{"item": ...}`, or `{"suit_set": "namespace:path"}` to give every piece of a Palladium suit set. | Yes | |
| `name` | The name shown above the preview. | No | None |
| `time` | Crafting time in ticks. `0` is instant. | No | `100` |

When the player presses Craft, the table takes the ingredients and runs a timer. It keeps going with the screen closed, and the finished items wait in the output slots.

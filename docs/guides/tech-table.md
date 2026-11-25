---
title: Tech Table
menu_title: Tech Table
blurb: Timed crafting, suit and device modules, and accessory slots, all from JSON.
---

# Tech Table

Three tabs: **Craft** (timed recipes on a 5x5 grid), **Modify** (install modules on a suit or a device) and **Customize** (the old accessory slots). It is all set up with JSON. The full reference with every setting is `tech_table.html`, which the game writes to `palladium/documentation/palladium/` when it launches.

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

- Use `pattern` + `key` (shaped, any size up to 5x5) or `ingredients` (shapeless, up to 25).
- `tool` is optional. It has to be in the separate tool slot, and `mode` is `consumed`, `retained` (default) or `damaged`.
- `result` is either `{"item": ...}` or `{"suit_set": "ns:path"}`, which gives every piece of a Palladium suit set.
- `name` is the name shown above the preview. `time` is in ticks, default 100, 0 is instant.

Hit Craft and the table takes the ingredients and runs a timer. It keeps going with the screen closed, and the finished items wait in the output slots.

## Modules

`data/<namespace>/argon/suit_modification/<name>.json`. Needs a `category` (`active`, `passive` or `cosmetic`) and either `suits` (suit sets it goes on) or `items` (things it goes on in the device slot).

Most of the rest is optional: `requirements` (taken from the player's inventory), `prerequisites`, `conflicts`, `max_level`, `removal` (`permanent`, `removable`, or a refund), `highlight`, `preview_layers`, `icon`, `name`, `description`, `effects`.

### Effects

Effects change the item itself. They're reapplied for the current level whenever something is installed or removed.

- `argon:fluid_capacity` (`per_level`): more capacity for fluid items like the web shooters.
- `argon:energy_capacity` (`per_level`, `max`): the same for things like the arc reactor.
- `argon:integer_component` (`component`, `per_level`): sets a whole-number component.
- `argon:custom_value` (`key`, `values`, `fallback`, `tooltip`): a named number based on which item you used.

For `custom_value`, say a module accepts three different cores and you want the number to depend on which one was used:

```json
"requirements": [ { "ingredient": ["minecraft:redstone_block", "minecraft:diamond_block", "minecraft:netherite_ingot"], "count": 1 } ],
"max_level": 3,
"effects": [ {
  "type": "argon:custom_value",
  "key": "example:core_power",
  "values": [
    { "item": "minecraft:redstone_block", "value": 2 },
    { "item": "minecraft:diamond_block", "value": 5 },
    { "item": "minecraft:netherite_ingot", "value": 10 }
  ],
  "fallback": 1,
  "tooltip": "Core Power: %s"
} ]
```

Each level adds its own number (so 2 + 5 + 10 = 17) and removing a level takes the last one off. To use it in a power, use the `argon:item_custom_value` value (`slot`, `key`, `fallback`), for example as a beam's `max_distance`.

## In a power

`argon:has_suit_modification` is a condition that's true while a module is installed on the worn suit. It takes `modification`, and optionally `suit`, `slot` (to check a device instead) and `min_level`.

```json
"state": { "enabling": { "type": "argon:has_suit_modification", "modification": "example:reserve_battery" } }
```

## Good to know

- Modules are saved on the items themselves, not the player, so they go wherever the item goes. A suit only counts as having a module while every piece has it.
- Modules are loaded from the normal data pack folders, not Palladium's addon loader.

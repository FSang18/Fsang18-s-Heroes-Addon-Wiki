---
title: Modules
blurb: Upgrades installed on suits and devices from the Modify tab.
---

# Modules

A module is an upgrade the player installs on the **Modify** tab, either on a full Palladium suit or on a single device item.

`data/<namespace>/argon/suit_modification/<name>.json`

```json
{
  "category": "passive",
  "suits": ["example:runner_suit"],
  "icon": { "item": "minecraft:feather" },
  "requirements": [ { "ingredient": "minecraft:feather", "count": 4 } ],
  "max_level": 3,
  "removal": "removable",
  "effects": [
    { "type": "argon:attribute_modifier", "attribute": "minecraft:movement_speed", "amount": 0.1, "operation": "add_multiplied_base", "pieces": ["feet"] },
    { "type": "argon:tooltip", "text": "Light soles fitted", "pieces": ["feet"] }
  ]
}
```

## Settings

| Key | Description | Required | Fallback |
|---|---|---|---|
| `category` | `active`, `passive` or `cosmetic`. Decides the column it is listed in. | Yes | |
| `suits` | Suit sets the module goes on. | `suits` or `items` | Empty |
| `items` | Items the module goes on in the device slot. | `suits` or `items` | Empty |
| `name` | Display name. | No | `suit_modification.<namespace>.<path>` |
| `description` | Description text. | No | The name's key with `.description` |
| `icon` | `{"item": "..."}` or `{"texture": "..."}`. | No | None |
| `requirements` | Materials taken from the player's inventory for each install. | No | None |
| `consume_requirements` | `false` means the player only needs to carry the materials. | No | `true` |
| `prerequisites` | Modules that must be installed first. | No | None |
| `conflicts` | Modules it can't be combined with. Only one of the two has to list the other. | No | None |
| `max_level` | How many times it can be installed, from 1 to 1000. Each install uses the requirements again. | No | `1` |
| `removal` | `permanent`, `removable`, or `{"mode": "refund", "refund": [{"id": "minecraft:gold_ingot", "count": 1}]}`. A refund is given for each level removed. | No | `permanent` |
| `effects` | What the module does to the item. | No | None |
| `highlight` | A body part to outline on the preview: `head`, `body`, `arms`, `left_arm`, `right_arm`, `legs`, `left_leg` or `right_leg`. | No | None |
| `preview_layers` | Render layers shown on the preview while the module is installed or selected. | No | None |
| `sort_order` | Order within its column, lowest first. | No | `0` |

## Effects

A module's `effects` change the item it is installed on. They are worked out again whenever something is installed or removed, so taking everything off puts the item back the way it was.

Every type is listed with its settings on the [Module Functions](../../reference/module-functions.md) page.

### On a suit

A suit has several pieces, so each function chooses where it goes:

- Powers and attribute bonuses go on the chestplate, or on the first piece the suit has.
- The other functions go on every piece.
- Set `pieces` to choose, for example `["head", "chest"]`.

The capacity, number and custom value effects apply to every piece.

### A value that depends on the material

Say a module accepts three different cores, and a number should depend on which one was used:

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

Each level adds its own number (so 2 + 5 + 10 = 17), and removing a level takes the last one off. A power reads it with the [`argon:item_custom_value`](../../reference/values.md) value (`slot`, `key`, `fallback`), for example as a beam's `max_distance`.

## Checking for a module in a power

[`argon:has_suit_modification`](../../reference/conditions.md) is true while a module is installed on the worn suit. It takes `modification`, and optionally `suit`, `slot` (to check a device instead) and `min_level`.

```json
"state": { "enabling": { "type": "argon:has_suit_modification", "modification": "example:reserve_battery" } }
```

## Good to know

- Modules are saved on the items, not on the player, so they go wherever the item goes. A suit only counts as having a module while every piece has it.
- Module files are loaded from the normal data pack folders, not Palladium's addon loader. Rejoin the world after changing them.

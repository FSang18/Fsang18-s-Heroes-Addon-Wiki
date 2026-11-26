---
title: Entities, Controls and Tags
---

# Entities, Controls and Tags

## Entities

| Entity | ID | What it is |
|---|---|---|
| Clone | `argon:clone` | A copy of a player made by the `argon:clone` ability. |
| Thrown Block | `argon:thrown_block` | A block that has been picked up and thrown. |

## Key bindings

All are in the Controls screen under the **Argon** category.

| Key binding | What it does |
|---|---|
| Previous Ability Bar Preset | Switches an `argon:ability_bar` to its previous preset. |
| Next Ability Bar Preset | Switches an `argon:ability_bar` to its next preset. |
| Takeoff | Starts a charged takeoff for the `argon:charged_takeoff` ability. |

## Damage types

| Damage type | Death message |
|---|---|
| `argon:sound` | "was deafened to death" |
| `argon:psionic` | "'s mind was shattered by" |
| `argon:cosmic` | "was unmade by the cosmic power of" |
| `argon:shock` | "was electrocuted by" |
| `argon:bleeding` | "bled out" |
| `argon:dna_transfer` | "was lost in a DNA transfer" |

The `argon:sonic` damage type tag groups `minecraft:sonic_boom` and `argon:sound` so they can be treated as one kind of damage.

## Tags

Argon ships these tags so packs can adjust its behavior by adding or removing entries.

| Tag | Type | Purpose |
|---|---|---|
| `argon:bloodless` | Entity type | Creatures that can't bleed. |
| `argon:spellcasters` | Entity type | Mobs that [Voiceless](effects.md) silences. |
| `argon:voiceless_immune` | Entity type | Creatures Voiceless ignores. |
| `argon:pheromone_immune` | Entity type | Creatures immune to Fear, Disoriented and Pacified. |
| `argon:stagger_immune` | Entity type | Creatures that can't be staggered. |
| `argon:stagger_reduced` | Entity type | Creatures staggered less. |
| `argon:karma_boss`, `argon:karma_dangerous`, `argon:karma_exempt` | Entity type | How killing a creature changes karma. |
| `argon:beam_unmeltable` | Block | Blocks that beams can't melt. |
| `argon:mineable/hammer` | Block | Blocks hammers mine efficiently. |
| `argon:hammers` | Item | Items that count as hammers. Empty until a pack adds its own. |

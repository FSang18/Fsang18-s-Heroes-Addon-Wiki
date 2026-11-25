---
title: Items
---

# Items

| Item | ID | What it is |
|---|---|---|
| Structure Capsule | `argon:structure_capsule` | Holds a captured structure. Right-click a block to place the structure next to it, turned to face the way you are looking. The capsule is used up. |
| Empty DNA Vial | `argon:empty_dna_vial` | Used at a [DNA Transfer Station](../guides/dna-transfer.md) to take a power from a player. |
| Filled DNA Vial | `argon:filled_dna_vial` | Holds a power. Does nothing by itself, it needs the DNA Power Transfer Machine. |

## Hammers

Hammers are heavy tools that stagger what they hit. There is one for each material: wooden, stone, copper, iron, golden, diamond and netherite (`argon:wooden_hammer`, `argon:stone_hammer`, `argon:copper_hammer`, `argon:iron_hammer`, `argon:golden_hammer`, `argon:diamond_hammer`, `argon:netherite_hammer`).

- A hit applies the [Stagger](effects.md) effect, which slows the target. Creatures in the `argon:stagger_immune` tag ignore it, and `argon:stagger_reduced` creatures are slowed less.
- Any item can become a hammer by giving it the `argon:hammer` data component, which is how modded and addon hammers are made. All hammers belong to the `argon:hammers` item tag.

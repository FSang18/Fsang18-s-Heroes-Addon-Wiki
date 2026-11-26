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

Argon adds the hammer tool type, not hammers of its own. A pack makes one with the `argon:hammer` item type, or turns any item into a hammer with the `argon:hammer` data component. Hammers are heavy tools that stagger what they hit.

- A hit applies the [Stagger](effects.md) effect, which slows the target. Creatures in the `argon:stagger_immune` tag ignore it, and `argon:stagger_reduced` creatures are slowed less.
- Add a pack's hammers to the `argon:hammers` item tag so the hammer enchantments can go on them.

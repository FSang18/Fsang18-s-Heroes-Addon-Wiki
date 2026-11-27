---
title: Blocks
---

# Blocks

| Block | ID | What it is |
|---|---|---|
| Tech Table | `argon:tech_table` | A workbench for powered gear with Craft, Modify and Customize tabs. See the [Tech Table](../guides/tech-table/index.md) guide. |
| Chemical Synthesizer | `argon:chemical_synthesizer` | A machine with a 3 by 3 grid, an input tank and an output tank. It turns grid items and fluids into other fluids and items through recipes. |
| DNA Transfer Station | `argon:dna_transfer_screen` | The control screen of the DNA Power Transfer Machine. |
| Power Block | `argon:dna_transfer_power_block` | Supplies power to the DNA Power Transfer Machine. |
| Chamber | `argon:dna_transfer_chassis` | The chamber a player stands in during a transfer. |

The three DNA blocks are built together as one machine. See the [DNA Transfer Station](../guides/dna-transfer.md) guide.

## Crafting recipes

Added in Argon 1.1.0. Each block has two recipes, and only one is active at a time:

- With the `palladium:material/circuits` feature flag **enabled**, the recipe uses a Palladium Quartz Circuit.
- With the flag **disabled**, the same recipe uses a Redstone Comparator in that spot.

A pack enables the flag in its `pack.mcmeta`:

```json
{
  "pack": { "description": "My pack" },
  "features": {
    "enabled": ["palladium:material/circuits"]
  }
}
```

### Tech Table

| Left | Middle | Right |
|:---:|:---:|:---:|
| Iron Ingot | **Quartz Circuit** or **Redstone Comparator** | Iron Ingot |
| Redstone Dust | Crafting Table | Redstone Dust |
| Iron Ingot | *(empty)* | Iron Ingot |

Makes one `argon:tech_table`.

### Chemical Synthesizer

| Left | Middle | Right |
|:---:|:---:|:---:|
| Glass | Brewing Stand | Glass |
| Glass | **Quartz Circuit** or **Redstone Comparator** | Glass |
| Iron Ingot | Iron Ingot | Iron Ingot |

Makes one `argon:chemical_synthesizer`.

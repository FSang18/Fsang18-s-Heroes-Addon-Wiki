---
title: Getting Started
---

# Getting Started

Argon is a library mod for [Palladium](https://docs-preview.threetag.net/docs/intro/). It adds a large set of abilities, conditions, values, actions, beams, effects and a few machines, so addon packs can build powers without writing code. FSang18's Heroes is built on top of it.

## What you need

- Minecraft 26.1.2 with NeoForge.
- The Palladium mod. Argon needs it and does nothing without it.
- The Argon mod file, placed in the `mods` folder next to Palladium.

## Using Argon in a power

Argon's abilities work exactly like Palladium's own. Put one in the `abilities` map of a power and give it a `type` starting with `argon:`.

```json
{
  "name": "Example Power",
  "icon": "minecraft:command_block",
  "abilities": {
    "my_flight": {
      "type": "palladium:flight",
      "flight_type": {
        "type": "argon:controlled_flight",
        "profile": "natural"
      }
    }
  }
}
```

Argon's conditions, values and actions are used the same way, anywhere Palladium accepts a condition, a value or an action.

## How to read the reference

Every page in the Reference section follows the same layout:

- **ID** is the value to use as `type`. Click it to copy it.
- **Settings** lists every key with its type, what it does, whether it is required, and the fallback used when it is left out.
- **Example** shows a working JSON snippet. **In a power** shows the same snippet inside a complete power.

Types written like `Float / Value` mean either a plain number or a [value](../reference/values.md) that changes while the game runs. A type with `[]` after it accepts a list.

## Where to go next

- [Guides](../guides/index.md) explain the bigger systems step by step.
- [Abilities](../reference/abilities.md) and [Conditions](../reference/conditions.md) are the pages most packs use.
- [Content](../content/index.md) lists the items, blocks, effects and commands Argon adds.
- [Feature Flags](feature-flags.md) explains the optional features a world or data pack has to switch on.

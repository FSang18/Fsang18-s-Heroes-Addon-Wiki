---
title: Commands
---

# Commands

Every Argon command starts with `/argon` and needs permission level 2. Where a command takes `[targets]`, leaving it out uses yourself.

## Grant

Give experience, levels or skill points to a power.

| Command | What it does |
|---|---|
| `/argon grant <targets> <power> exp <amount>` | Gives experience points to the power. |
| `/argon grant <targets> <power> levels <amount>` | Gives levels to the power. |
| `/argon grant <targets> <power> skill_points <amount>` | Gives skill points to the power. |

## Gravity

Reads and changes directional gravity. See the [Directional Gravity](../guides/gravity.md) guide.

| Command | What it does |
|---|---|
| `/argon gravity get [targets]` | Shows the gravity direction. |
| `/argon gravity set <direction> [targets]` | Sets the direction. |
| `/argon gravity reset [targets]` | Back to normal gravity. |
| `/argon gravity strength [targets]` | Shows the gravity strength. |
| `/argon gravity strength <multiplier> [targets]` | Sets the strength multiplier. |
| `/argon gravity sources [targets]` | Lists what is currently changing the gravity. |

## Karma

Reads and changes the karma of a player.

| Command | What it does |
|---|---|
| `/argon karma get <target>` | Shows the karma. |
| `/argon karma alignment <target>` | Shows the alignment it adds up to. |
| `/argon karma history <target>` | Shows recent karma changes. |
| `/argon karma set <targets> <amount>` | Sets the karma. |
| `/argon karma add <targets> <amount>` | Adds karma. |
| `/argon karma remove <targets> <amount>` | Removes karma. |
| `/argon karma reset <targets>` | Resets it. |

## Growth

Reads and changes the growth stored by a Time Growth ability.

| Command | What it does |
|---|---|
| `/argon growth get <target> <power> <ability>` | Shows the days of growth. |
| `/argon growth set <targets> <power> <ability> <days>` | Sets the days. |
| `/argon growth add <targets> <power> <ability> <days>` | Adds days. |
| `/argon growth reset <targets> <power> <ability>` | Resets the growth. |

## DNA vials

| Command | What it does |
|---|---|
| `/argon dna_vial <player> <power>` | Gives the player a filled DNA vial of a power that is registered for the [DNA Transfer Station](../guides/dna-transfer.md). |

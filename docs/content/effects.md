---
title: Effects
---

# Effects

Argon adds these status effects. Give them with `/effect give <target> argon:<id>`, or through an effect ability. Amplifier 0 is level I.

## Damage over time

| Effect | ID | What it does |
|---|---|---|
| Burning | `argon:burning` | Sets the target visibly on fire and deals fire damage once a second: 1 plus 1 per amplifier. Does nothing to fire immune creatures. |
| Freezing | `argon:freezing` | Builds up freezing (the powder snow effect) every tick, 4 per tick plus 4 per amplifier. Only affects creatures that can freeze. |
| Shock | `argon:shock` | Lightning damage every 2.5 seconds: 1 plus 1 per amplifier. |
| Sound | `argon:sound` | Sonic damage every 2 seconds (1 plus 0.5 per amplifier), 20% slower movement and flight, muted hearing, and from level III a desaturated screen. |
| Bleeding | `argon:bleeding` | Bleed damage once a second: 1 plus 1 per amplifier, reduced by armor. Creatures in the `argon:bloodless` tag take none. |

## Movement and control

| Effect | ID | What it does |
|---|---|---|
| Slowness | `argon:slowness` | Argon's own slowness: 15% less movement speed per level, and it slows flight by the same amount. |
| Stagger | `argon:stagger` | Slows the target. Applied by hammer hits; creatures in `argon:stagger_immune` ignore it and `argon:stagger_reduced` take less. |
| Entrapped | `argon:entrapped` | Holds the target hovering about 1.3 blocks above the ground with no movement, flight or jumping. |
| Restrained | `argon:restrained` | 60% less movement speed and no jumping. |
| Restrained (boss) | `argon:restrained_boss` | The lighter version for bosses: 20% less movement speed. |

## Mind effects

| Effect | ID | What it does |
|---|---|---|
| Fear | `argon:fear` | Mobs run away from the source of the fear. |
| Disoriented | `argon:disoriented` | Scrambles the movement controls. |
| Pacified | `argon:pacified` | 15% slower attacks and 20% less damage dealt. |
| Calmed | `argon:calmed` | Mobs with a player target drop it. Checked every quarter second. |
| Calm Lockout | `argon:calm_lockout` | Applied by the Calm ability so it can't be used again straight away. |
| Voiceless | `argon:voiceless` | Spellcasting mobs (the `argon:spellcasters` tag) lose their target and stop casting. Creatures in `argon:voiceless_immune` ignore it. Players can't cast by speaking. |

## Attribute debuffs

| Effect | ID | What it does |
|---|---|---|
| Transmuted | `argon:transmuted` | 40% smaller, 25% slower and 30% less damage. |
| Transmuted (large) | `argon:transmuted_large` | For big creatures: 20% smaller and 15% less damage. |
| Transmuted (boss) | `argon:transmuted_boss` | For bosses: 10% less damage. |
| Malediction | `argon:malediction` | 25% less damage. |

## Dampening

These switch off every power that carries the matching Palladium tag for as long as the effect lasts.

| Effect | ID | Switches off |
|---|---|---|
| Biological Dampening | `argon:dampening_biological` | Genetic powers |
| Technological Dampening | `argon:dampening_technological` | Mechanical powers |
| Mystical Dampening | `argon:dampening_mystical` | Magical powers, including spellcasting |
| Cosmic Dampening | `argon:dampening_cosmic` | Cosmic powers |

## Marker effects

These have no behavior of their own. Argon's abilities apply them, and conditions and other abilities can check for them.

| Effect | ID | Used by |
|---|---|---|
| Blessed | `argon:blessed` | The Color Cycle Glow ability |
| Wounded | `argon:wounded` | The Ward ability and Argon's damage handling |
| Dazzled | `argon:dazzled` | Argon's ability event handling |

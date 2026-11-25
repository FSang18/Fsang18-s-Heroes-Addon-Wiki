---
title: argon:throwable_item
menu_title: Throwable Item
blurb: Makes any item throwable, with bounce, return, recall, homing and more.
---

# argon:throwable_item

One reusable Palladium ability that makes any item throwable. The projectile looks like the real item, keeps the exact item with all its data, can bounce or embed in blocks, damage and embed in entities, return on its own, be recalled, hit enemies on the way back, home in, ricochet, be steered through a camera, and be caught. Everything is configured in the ability JSON; nothing is specific to one item.

## Layout

Everything except `item` is optional, and so is every section and every key inside a section.

```json
{
  "type": "argon:throwable_item",
  "item": "fsang:mjolnir",
  "hand": "main_hand",
  "throw":        { "speed": 2.6, "windup": 5, "gravity_mode": "none", "drag": 1.0, "maximum_time": 160 },
  "combat":       { "damage": 9, "maximum_targets": 3, "entity_impact": "continue" },
  "block_impact": { "mode": "embed" },
  "return":       { "triggers": ["after_hit"], "speed": 3.0, "block_collision": "pass_through", "damage_enabled": true, "recall": true },
  "targeting":    { "mode": "none" },
  "homing":       { "accuracy": 100 },
  "ricochet":     { "enabled": false },
  "steering":     { "mode": "none" },
  "camera":       { "distance": 5 },
  "perfect_catch": { "enabled": true },
  "pin":          { "enabled": true, "duration": 0 },
  "deflection":   { "enabled": false },
  "render":       { "scale": 1.8, "rotation_mode": "spin", "rotation_axis": "x", "rotation_offset": [180, 0, 0] },
  "sounds":       { "throw": "fsang:mjolnir_throw", "flight": "fsang:mjolnir_flight" },
  "state": { "enabling": { "type": "palladium:key_bind", "behaviour": "activation", "time": 11, "cooldown": 10 } }
}
```

Every number that is a Value can be driven by Palladium (power age, data attachments, molang) and is read when the item is thrown, except the `return` settings (`speed`, `acceleration`, `turn_rate`, `accuracy`, `maximum_duration`, `damage_multiplier`, `catch_radius`), which are read again at the moment of recall.

## Sections and keys

- **item / hand / pickup**: `item` (id, list or tag; required), `hand` (main_hand, off_hand, either), `pickup.on_touch` (true) and `pickup.radius` (1.5): the owner picks the item up by walking near it while it is embedded in a block or resting.
- **throw**: `speed` (1.8), `windup` (0 ticks; the item stays in the hand and the aim is taken at release), `gravity_mode` (none, vanilla, scaled), `gravity` (1), `drag` (0.99), `inaccuracy` (0), `inherit_owner_velocity` (0.35), `maximum_time` (200), `maximum_distance` (96), `maximum_owner_distance` (128), `out_of_range` (return, recover or drop; the item is never deleted).
- **combat**: `damage` (6), `knockback` (0.6), `damage_type`, `maximum_targets` (1, 0 = unlimited), `entity_impact` (continue, bounce, return, stop, embed), `allow_repeat_targets`, `rehit_cooldown` (10).
- **block_impact**: `mode` (bounce, embed, return, drop, stop), `restitution` (0.6), `friction` (0.85), `maximum_bounces` (3), `embed_depth` (0.3), `embed_duration` (0 = until recalled or picked up).
- **return**: `triggers` (a list of none, after_hit, after_block_impact, after_timeout, after_distance, always), `timeout` (60), `distance` (32), `speed` (2.4), `acceleration` (0.3), `turn_rate` (30), `accuracy` (100), `maximum_duration` (200), `block_collision` (pass_through, stop), `damage_enabled`, `damage_multiplier`, `maximum_damage_targets`, `catch_radius` (1.25), `recall`.
- **targeting**: `mode` (none, automatic, marked, hybrid), `accuracy` (100), `detection_range` (16), `cone` (90), `line_of_sight` (true), `filter` (hostile, living, players, non_players), `entity_types`, `priority` (nearest, look_direction, lowest_health, random).
- **homing**: `accuracy` (100), `turn_rate` (14), `acceleration`, `max_speed`, `prediction`, `target_offset` (0.5), `lost_target` (continue, reacquire, return).
- **ricochet**: `enabled`, `maximum`, `target_range` (10), `speed` (2.6), `turn_rate` (40), `damage_multiplier`.
- **steering**: `mode` (none, look_direction, projectile_camera), `turn_rate` (10), `strength` (1), `maximum_speed` (0 = the throw speed), `acceleration` (0.08), `return_on_release`, `owner_control` (normal, limited, immobile).
- **camera**: `distance` (5), `fov` (0 = unchanged), `smoothing` (0.35), `roll` (0).
- **perfect_catch**: `enabled`, `window` (8), `damage_bonus` (1.5), `bonus_duration` (100).
- **pin**: `enabled`, `duration` (60; 0 = until recalled), `distance` (4).
- **deflection**: `enabled`, `radius` (1.6), `strength` (1), `target_filter`.
- **render**: `scale` (1 = the item model at its full block size; flat item sprites like swords are a block across, so 0.6 to 0.8 usually looks right), `rotation_mode` (none, spin, tumble), `rotation_speed` (36), `rotation_axis` (x, y, z), `rotation_offset` ([x, y, z] degrees), `face_velocity` (true), `embed_spin_angle`.
- **sounds**: plain sound ids from `sounds.json`, all optional: `throw`, `entity_hit`, `block_hit`, `recall`, `return`, `catch`, `flight` (loops while flying).

## How it behaves

1. Pressing the key (a `palladium:key_bind` with `behaviour: activation`) while the item is in the chosen hand throws it. The item leaves the hand and is saved in a per-player record (full ItemStack, original slot, projectile id) in the `argon:thrown_records` attachment. No placeholder is left, so there is no second copy.
2. Pressing the same key while the item is out recalls it (needs `return.recall`).
3. The projectile is server-driven; the client only interpolates and renders.
4. The item returns to its original slot (or any free slot, or the owner's feet if full) when it is caught, picked up, recovered by a safety rule, or when the owner logs out, dies, changes dimension or logs back in. The record is removed before the item is given back, so it is restored exactly once, and a watchdog restores it if the projectile disappears.
5. Phases: OUTBOUND (swept in sub-steps of at most 0.9 blocks), EMBEDDED in a block, EMBEDDED in an entity, RESTING, RETURNING (turns toward the owner's chest at `return.turn_rate` times `return.accuracy`, caught inside `catch_radius`; `return.maximum_duration` restores the item directly as a safety net).

## Targeting, homing and ricochet

- `targeting.mode`: none (no selection; ricochet still picks its own targets), automatic, marked (only targets marked with `argon:throw_marker`, in the order marked) or hybrid (marked first, then automatic).
- Acquisition attempts happen at the throw, after each ricochet and when a target is lost. Each succeeds with `targeting.accuracy` percent when the mode is automatic or hybrid, rolled on the server. It is never re-rolled every tick, never stops a real collision from hitting, and marked targets need no roll.
- Candidates must be inside `detection_range` (and, for the first target, the `cone`), visible when `line_of_sight` is on, pass `filter` and `entity_types`, and not be the owner, allies, the owner's pets, or players the owner may not harm.
- Homing is separate from acquisition: `homing.accuracy` scales `homing.turn_rate`. Accuracy 0 acquires a target but never steers. A target that dies, leaves range or stays out of sight for more than 12 ticks follows `homing.lost_target`. Gravity and drag are skipped while chasing.
- Ricochet flies on to the next valid target after each hit (physically, at `ricochet.speed` and `ricochet.turn_rate`, damage times `damage_multiplier`), up to `ricochet.maximum` (0 = one fewer than `combat.maximum_targets`), then the return rules apply. Targets already struck are skipped unless `allow_repeat_targets`.
- `argon:throw_marker` marks (or unmarks) the living entity you look at, up to `maximum_marked_targets`. Marks are shown only to the marker as sparks, cleared on logout, and used up by the next marked or hybrid throw.

## Steering and the projectile camera

- Set `steering.mode` to `look_direction` or `projectile_camera` and give the player an `argon:throw_steer` ability with a held key bind. While held, every flying projectile of theirs with a mode turns toward where they look. Gravity, drag and homing are off while steering. Letting go hands the projectile back to its normal flight, or sends it back with `return_on_release`.
- `projectile_camera` also moves the camera to a chase view behind the projectile (`camera.distance`, clipped by blocks) with optional `fov`, `smoothing` and `roll`. The player stays the camera entity, so movement, look and packets keep working. Argon's flight and gravity camera adjustments, the wall-crawl roll, the first-person hand and first-person screen overlays are skipped while it is active.
- The camera ends the moment the key is released, the projectile hits something that stops it, is recalled, caught or removed, or the owner dies, logs out or changes dimension; the client also drops it by itself if the projectile entity disappears.
- `owner_control` while the camera is active: normal, limited (movement speed -65 percent) or immobile (no walking or jumping), done with transient attribute modifiers.

## Pinning, deflection, perfect catch and animations

- `pin`: a mob hit by the outbound item is moved against a wall within `pin.distance` behind it and held there (maximum slowness, position locked) for `pin.duration` ticks, or with 0 until the owner recalls (refreshed every second so a crash cannot leave anything slowed). While a mob is pinned the item does not start an automatic return at all; it stops and falls where it is. Players, the Ender Dragon, the Wither and `#c:bosses` are never pinned.
- `entity_impact: embed`: the item lodges in the mob it hits and follows it until recalled, the mob dies (it then falls) or `block_impact.embed_duration` runs out. Ends the throw at that hit; does not combine with ricochet.
- `deflection`: while flying, any projectile within `radius` that is not the owner's is reversed with vanilla's deflection and becomes the owner's.
- `perfect_catch`: pressing the ability while the item is returning and within `window` ticks of arriving catches it at once; the next throw within `bonus_duration` ticks deals `damage_bonus` times damage.
- `argon:throw_event` is a condition that is true for a number of ticks after the entity threw, recalled or caught with a throwable (`event`, `ticks`, optional `arm` right or left to match the player's main arm), so animation controllers can play throw, recall and catch clips and mirrored ones for left-handed players. The times are a synced attachment, so other players see them too.

## Damage

Damage uses `combat.damage_type` if set, otherwise the vanilla thrown-projectile source attributed to the owner. The item's own attack damage and enchantments are not added, so nothing is applied twice. The owner, allies, the owner's tamed pets, spectators and players the owner may not harm are skipped.

## Known limits

- Removing the power while the item is out does not interrupt the flight; the item still returns, can be picked up, or is restored on logout, death or dimension change.
- The release point is computed from the shoulder and the look direction, not read from the player model, so it can sit slightly off the visible hand with some animations and suits.

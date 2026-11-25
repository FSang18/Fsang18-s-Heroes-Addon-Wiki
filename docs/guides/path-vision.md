---
title: Path Vision
menu_title: Path Vision
blurb: Shows the holder where nearby entities and projectiles are going.
---

# Path Vision

`argon:path_vision` shows the holder where nearby entities and projectiles are going. The path is drawn ahead of the target with a Palladium trail. Everything is drawn on the holder's own client and nobody else sees it. The ability only reads existing movement data: it never changes an entity's movement, AI or collision, and never changes a projectile's flight.

## Adding it to a power

Add it like any other ability. With no other settings it uses the defaults below and Argon's two built in trails.

```json
"path_vision": {
    "type": "argon:path_vision",
    "detection_radius": 24.0,
    "max_targets": 16,
    "entity_trail": "argon:path_vision_entity",
    "projectile_trail": "argon:path_vision_projectile",
    "show_time_to_impact": true,
    "track": ["hostile", "projectiles", "minecraft:villager"],
    "ignore": ["#minecraft:undead"],
    "properties": {
        "icon": "minecraft:ender_eye"
    }
}
```

It follows Palladium's normal activation: it runs while the ability is unlocked and enabled, so a toggle, a key bind or any enabling condition works. Turning it off, or losing the power, removes every path at once and stops all work on the server and the client.

## Properties

General and filtering

| Property | Default | Meaning |
|---|---|---|
| `detection_radius` | `24.0` | Blocks around the holder that are searched. Only loaded entities are ever looked at; no chunk is loaded for a prediction. |
| `max_targets` | `16` | Most targets shown at once. |
| `target_priority` | `closest` | Which targets are kept when there are more than `max_targets`: `closest` (by distance), `hostile_first` (hostile mobs before everything else) or `projectiles_first`. Within a group the closest come first. A "current combat target first" mode does not exist because clients are not told who the holder last attacked. |
| `path_update_interval` | `2` | Ticks between recalculations. The trail follows the target smoothly in between, and a new navigation path from the server is applied immediately. |
| `max_path_length` | `32.0` | Longest path shown, measured along the path itself from the target. |
| `track` | `["players", "hostile", "neutral", "projectiles"]` | What is shown. One list that mixes categories with specific entity types and tags. See below. |
| `ignore` | `[]` | Anything matching here is never shown, even if it matches `track`. Same entries as `track`. |

### What `track` and `ignore` take

Both are a single list. Each entry is one of:

| Entry | Matches |
|---|---|
| `players` | Other players. |
| `hostile` | Anything implementing `Enemy`. |
| `neutral` | Anything implementing `NeutralMob`. |
| `passive` | Any other mob. |
| `projectiles` | Any `Projectile` entity, including modded ones. |
| `mobs` | `hostile`, `neutral` and `passive` together. |
| `all` | Every category above. |
| `namespace:entity` | One entity type, such as `minecraft:villager`. It matches whatever its category is, so it works for things outside the categories, like armor stands. |
| `#namespace:tag` | An entity type tag, such as `#minecraft:skeletons`. |

So `["hostile", "projectiles"]` tracks every hostile mob and every projectile, `["mobs", "players"]` tracks all mobs and players, and `["all"]` with `"ignore": ["minecraft:armor_stand"]` tracks everything except armor stands. An entry that is not one of these stops the power from loading, and the error names the entry.

Entity paths

| Property | Default | Meaning |
|---|---|---|
| `show_entity_paths` | `true` | Paths for mobs and players. |
| `predict_entity_movement` | `true` | Prediction for entities that have no navigation path. |
| `entity_prediction_time` | `2.0` | Seconds ahead that movement is predicted. |

Projectile paths

| Property | Default | Meaning |
|---|---|---|
| `show_projectile_paths` | `true` | Flight paths of projectiles. |
| `projectile_prediction_time` | `3.0` | Seconds ahead that flight is simulated. |
| `show_projectile_impact` | `true` | A particle at the predicted impact point. |
| `show_time_to_impact` | `false` | The time left before impact, such as `0.8s`, written above the impact point. |
| `impact_particle` | `minecraft:end_rod` | The particle used as the marker. |
| `preview_aimed_shots` | `false` | Instead of following projectiles after they are fired, show the path a shot would take for as long as its shooter is aiming. See below. |
| `aim_charge_color` | `#FFD23F` | Only for `preview_aimed_shots`. The colour of the line when the shot has just started being drawn; it shifts to the projectile trail's own colour as the draw builds, so the trail colour means ready. See below. |

Trails and rendering

| Property | Default | Meaning |
|---|---|---|
| `entity_trail` | `argon:path_vision_entity` | The Palladium trail that draws entity paths. |
| `projectile_trail` | `argon:path_vision_projectile` | The Palladium trail that draws projectile paths. |
| `trail_render_distance` | `64.0` | Paths of targets farther than this from the camera are not drawn. |
| `trail_smoothing` | `0.7` | How much navigation corners are rounded, from `0` (the raw route) to `1` (the smoothest). A rounded stretch that would pass through a block is left sharp instead, so corners around walls stay corners. |
| `render_through_walls` | `false` | Draw the trail through blocks. |

## Where paths come from

A target gets its path from the first of these that applies, and nothing is drawn if none does.

1. Actual AI navigation. The server reads the mob's own navigation path and sends the nodes that are still ahead of it. It reads the path the mob already has: it never asks Minecraft to compute a new route, so it cannot change what the mob does. The trail follows the real nodes, so a route around a wall is drawn as the route around the wall. Only mobs with a path that is in progress show one, and the server sends nothing for the rest.
2. Predicted movement, for anything else that is moving: players, entities with custom movement, and mobs that are moving without a navigation path. The client takes the entity's recent velocity (smoothed over a few ticks) and walks it forward for `entity_prediction_time`: horizontal speed is kept, gravity and drag apply to anything that is falling, walls stop the path, and flying entities keep a straight line. This is an estimate of where the entity goes if it carries on, not a known destination, so the further ahead it looks the less it can be trusted. An entity that is standing still gets no path.
3. Projectiles are simulated with Minecraft's own per-tick rules, from the projectile's current position and velocity.

## Projectile prediction

The physics are chosen from the kind of projectile, using the gravity the entity itself reports:

| Projectile | Order each tick |
|---|---|
| Arrows and tridents | Water drag (0.6, tridents 0.99), move, air drag 0.99, then gravity. |
| Thrown items (snowballs, eggs, ender pearls, potions) | Gravity, then drag (0.99 in air, 0.8 in water), then move. |
| Fireballs | Acceleration along the movement, then drag (0.95 in air, 0.8 in water), then move. No gravity. |
| Any other projectile | The thrown item rules, as a fallback. |

The simulation stops at the first of: the prediction time, `max_path_length`, a block hit (a block raycast each tick, so it cannot pass through a wall), an entity hit (checked against the other targets and the holder, not the projectile's owner), or the edge of the loaded world. The path ends at the hit point and the impact marker and time are only shown when a hit was found. A projectile that is not moving, such as an arrow stuck in a block, shows nothing.

## Previewing aimed shots

With `"preview_aimed_shots": true`, projectiles are no longer followed once they are in flight. Instead, anything that is aiming a ranged weapon shows the path its shot would take, and the path stays up for as long as it keeps aiming and goes when it stops. It uses the `projectile_trail`, the same impact marker and the same time to impact, and it follows the same `track` and `ignore` lists as everything else, so the shooters are whoever you track.

| Weapon | When a path is shown | Shot speed |
|---|---|---|
| Bow | While it is being drawn, once the arrow would fire (a player's draw power sets the speed). | Players: draw power times 3. Mobs: 1.6. |
| Trident | While it is held ready, after the 10 tick draw for players. | Players 2.5, mobs 1.6. |
| Crossbow | While it is loaded. | Players 3.15, mobs 1.6. Fireworks are not predicted. |

The line also shows how close the shot is to being fired. It starts as `aim_charge_color` and blends into the projectile trail's own colour as the bow is drawn, a player's draw power or a skeleton's 20 tick draw, so the trail's colour means the shot is ready. A loaded crossbow and a trident are always ready. Set `aim_charge_color` to the trail's colour to turn this off. The blend changes the colour of the trail's lines and ribbons (gradient and lightning trails), not copies drawn by an after image trail.

A player's path uses their real aim and their own movement, like the arrow would. A mob's path uses the direction it is looking and, if that lines up with a tracked entity (including you), the same upward correction vanilla gives a mob's aim at its target, so a skeleton aiming at you shows the arc that would actually reach you. The path ends at the first block or tracked entity it would hit, and a shot that would hit you shows the impact and the time left. A loaded crossbow counts as aiming, so a player standing with one loaded keeps a path up.

A shot is never exactly the line. Vanilla adds a little random spread to every shot, about one degree for a player's bow and several degrees for a skeleton depending on difficulty, and the line shows the middle of it. Everything else is taken from the same rules the game uses: where the arrow spawns (a tenth of a block below the eyes), its speed, drag, gravity, and the first block or living entity it would hit, whether or not you are tracking that entity. The line updates every tick.

The client cannot see who a mob is targeting, only what it is looking at and holding. A mob that is aiming without looking at the target yet, or an unusual mob with its own shooting rules, can show a path that does not match the real shot.

## Palladium trails

Path Vision reuses Palladium's own trail renderers. A trail is a normal `palladium/trails/<path>.json` file, and `entity_trail` and `projectile_trail` are their IDs. Palladium's trail system draws a trail behind a moving entity from recorded history, so Argon builds the trail segments from the predicted path instead and hands them to the same renderer. Argon's two defaults are gradient trails in `assets/argon/palladium/trails/`:

```json
{
    "requires_movement": false,
    "renderer": {
        "type": "palladium:gradient",
        "color": "#33E6FF",
        "opacity": 0.6,
        "orientation": "horizontal",
        "offset": 0.0
    }
}
```

To use another look, make your own trail file in the same place and name it in the power. Use `horizontal` for a ribbon lying along the path and `vertical` for a wall of the target's height.

The appearance is all in the trail file, not in the ability, so a power only names which trail to use. What is read from it:

- `renderer`: the type and all of its own settings, such as colour, opacity, orientation and the lightning settings. This is where the opacity of a path is set.
- `lifetime`: the ticks a path takes to fade in when a target appears and to fade out when it leaves the radius or stops having a path. `0` is instant. If a trail file holds several trails, the longest lifetime is used.
- `offset`: moves every point of the path, in blocks.
- `spacing`: for after image trails, the gap between copies. See below.

What is not used, because a path has no history to space or age: `tick_delay`, `requires_movement` and `anchor`. The far end of a path also fades a little, and the width of an entity path is the target's own width, while projectile paths (in flight or aimed) are a thin line, 0.08 of a block wide.

| Renderer | Works along a path |
|---|---|
| `palladium:gradient` | Yes. |
| `palladium:lightning` | Yes. |
| `palladium:after_image` | Yes, as spaced copies of the target. See below. |
| `palladium:lightning_aura` | No. It is drawn around an entity's model parts, so it is skipped. |

Ribbon trails are lifted a few centimetres off the ground (a little more with distance from the camera) so they do not flicker against the block surface they lie on.

### Ghost trail

`argon:path_vision_ghost` draws the target as faded copies of itself walking ahead along its path, using `palladium:after_image`:

```json
{
    "spacing": 2.5,
    "lifetime": 5,
    "requires_movement": false,
    "renderer": {
        "type": "palladium:after_image",
        "color": "#FFFFFF",
        "opacity": 0.22
    }
}
```

Use it with `"entity_trail": "argon:path_vision_ghost"`. For after image trails the trail's `spacing` is used, as a multiple of the target's width, to place the copies along the path (at least half a block apart), and at most ten copies are drawn per target, the nearest ones, and at most 24 across all targets together, because every copy is a full draw of the model. Each copy faces the direction the path is heading and gets its own walking phase from how far along the path it is, so the copies read as a stride. A copy keeps the look the target had when the copy was first created, such as its armour and held items. A lower `opacity` is more ghostly; `color` tints the copies and white leaves them untinted. Copy this file into your own pack and change those two values for a different ghost.

`render_through_walls` swaps Palladium's laser render types (gradient and lightning) for versions that ignore depth, only for Path Vision's own trails. Nothing else in the game is changed.

## Multiplayer

Nothing is shown to anyone but the player who is using the ability. It is drawn only on that player's own client, and only while that ability is enabled: another player who has Path Vision but has it off sees nothing, and sees nothing of the holder's paths either. If the ability stops being ticked, for example on leaving a world, the client switches it off by itself after three ticks. If a power has two Path Vision abilities, only the one that switched it on can switch it off.

The server only sends path data to a player whose Path Vision is enabled right now. The server picks the targets from the ability's own `detection_radius`, filters and `max_targets`, so a client cannot ask for anything. It sends navigation nodes (not world data), only when a path actually changes, quantised to 1/16 of a block, and lists targets whose path ended so the client drops them. Everything else, including projectile and movement prediction, is calculated on the client from positions and velocities the client already has. No packets are sent every frame.

## Limits

- Predictions are estimates. Another player can turn at any moment and a mob can change its mind; the path updates as soon as it does, but it can never show what has not been decided.
- Movement prediction follows the centre line of the body, so it can stop early at a one block step that the entity would jump.
- Impact tests use block collision and the bounding boxes of the other targets; an entity that is not a current target is not hit, and entity hit boxes are widened a little for the projectile's size.
- Projectiles with custom flight that Argon cannot read are drawn with the fallback rules and may be wrong. Leave them out with `ignore`.
- Mobs that use their own movement controller instead of Minecraft navigation show a prediction, not a route.

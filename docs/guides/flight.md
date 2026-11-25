---
title: Controlled Flight
menu_title: Controlled Flight
blurb: Momentum, banking and a body that leans into its direction of travel.
---

# Controlled Flight

`argon:controlled_flight` is a Palladium flight type with momentum, banking and a body that leans into its direction of travel. It is opt-in: `palladium:flight` and `argon:forced_flight` are untouched.

Only the movement feel is new. Flying is still toggled, landed and started the way it is for `palladium:flight`, and the permitted speed still comes from `speed` and `sprint_speed`. That means `argon:flight_speed`, the flight speed dial and flight slowness all keep working, and the acceleration settings only decide how quickly the player reaches that speed.

## Using it

Use it as the `flight_type` of a `palladium:flight` ability:

```json
{
    "type": "argon:controlled_flight",
    "profile": "natural",
    "speed": 1.5,
    "sprint_speed": {
        "type": "argon:flight_speed",
        "ability": "fsang:dc/kryptonian/absolute#kryptonian_absolute_flight_speed_adjuster",
        "base": 1.5
    },
    "propelled_sound": "palladium:player.flight.propelled"
}
```

## Profiles

A profile sets the default for every setting below, and any setting can still be given on its own.

| Profile | Feel |
|---|---|
| `controlled` | Balanced. Smooth acceleration, moderate momentum, settles into a hover. The default. |
| `propelled` | Heavier momentum and slower corrections. Sinks while no direction is held. |
| `natural` | Quick to turn and stop, no gravity. For flight without propulsion. |
| `gliding` | Keeps its heading, gravity always pulls and fades as speed rises, and height and speed trade for each other (see Gliding). |

## Movement

| Property | What it does |
|---|---|
| `flight_acceleration` | Fraction of the gap to top speed closed per tick when speeding up. |
| `flight_deceleration` | Fraction closed per tick when slowing while a direction is held. Also bleeds speed during sharp reversals. |
| `flight_response_curve` | 1 is constant. Above 1 starts slower and pushes harder near top speed. |
| `momentum_retention` | How much turning is held back at speed. 0 turns as sharply at speed as when slow. |
| `turn_responsiveness` | Degrees the heading can turn per tick at low speed. |
| `air_braking_strength` | Fraction of speed lost per tick when no direction is held. |
| `gravity_influence` | Pull of gravity while no direction is held (always for gliding). |
| `hover_stabilization` | Extra speed removed per tick when almost stopped. |
| `hover_velocity_threshold` | Speed under which hover stabilization starts (it applies up to three times this). |

Speed never rises above the permitted top speed because of turning: changes of direction rotate the velocity, and speed only moves toward the target. Speed above it, such as from Charged Takeoff, decays at `flight_deceleration`.

## Orientation

| Property | What it does |
|---|---|
| `enable_body_rotation` | Leans the whole rendered body, with armor, layers and cape, into the direction of travel. |
| `lean_start_speed`, `lean_full_speed` | Fractions of top speed where the lean starts and where the body is fully aligned. |
| `orientation_responsiveness` | How fast the body follows the direction of travel. |
| `enable_flight_banking`, `max_bank_angle` | Roll into turns, up to this angle. |
| `bank_responsiveness`, `bank_recovery_speed` | How fast the bank builds and returns to level. |
| `bank_speed_influence` | How much the bank scales with speed. |

The lean is a pitch about the body's own right axis, and nothing else. The body keeps facing the way it normally does, then tips forward or back by the angle of the direction of travel measured in that frame (0 is upright, 90 is horizontal and facing forward, 180 is head down), eased in with speed. The angle is kept continuous, so it carries on past vertical through a loop without flipping, and the body is never turned about any other axis to get there. Bank and barrel roll are then added as a roll about the body's own forward axis (the chest axis when upright, the head axis when leaning), so rolls always spin around the body whichever way it is pointing.

The orientation is a world orientation. While gravity is turning, the model is not carried by the gravity animation: the animated turn is taken out and the final orientation put in, so the body stays where it is in the world while the camera swings. It uses the entity's own look yaw frame and never changes gravity or the hitbox.

The animation handler also fills Palladium's flight Molang queries: `palladium.flight_roll` is the bank, and `palladium.flight_pitch` is the forward lean in degrees (negative when leaning back). An animation should not rotate the `body` bone itself any more, but can use `flight_pitch` to counter-rotate the head, as the Absolute animation does.

## Camera

| Property | What it does |
|---|---|
| `camera_roll_mode` | `none`, `partial` (default) or `full`: how much of the bank the camera rolls by. |
| `camera_bank_multiplier` | The share of the bank used in `partial` mode. |
| `enable_speed_fov`, `speed_fov_multiplier` | Widen the field of view with flight speed. Off by default. |
| `enable_third_person_framing`, `third_person_framing_offset` | Frame the body in third person, with the character at or a little below the middle of the screen. On by default, offset 0.25. |

First person is not attached to the body: only the camera bank applies.

In third person the camera frames the body while flying (`enable_third_person_framing`, on by default). Normally the camera aims at the eyes, so when the body leans or the eye height drops while sprint-flying the character slides off the middle of the screen. The camera now aims at the middle of the body, plus `third_person_framing_offset` blocks (0.25 by default, which sits the character a little below the middle), eased in and out with the start and end of flight. It follows the player's own up direction, so it works while gravity is turned.

## Barrel roll

Off by default. With `enable_barrel_roll`, double-tapping left or right while flying rolls the body once around the direction of travel. There is no new key. The roll is a visual rotation shared with other players, and it pushes the player a little to the side.

| Property | What it does |
|---|---|
| `enable_barrel_roll` | Turns the double-tap on. |
| `barrel_roll_duration` | Ticks the roll takes (14). |
| `barrel_roll_lateral_strength` | A sideways push as a fraction of top speed (0.3). Forward speed is kept. |
| `barrel_roll_cooldown` | Ticks before another roll (30). |
| `barrel_roll_camera_influence` | How much of the roll the camera follows. 0 keeps the view steady (default), 1 rolls with the body. |
| `barrel_roll_min_speed` | Fraction of top speed needed to start a roll (0.2). |

The roll is a model rotation added to the bank, so it follows the same axis as banking and never changes gravity.

## Collisions

Off by default. With `enable_flight_collision`, hitting a block or flying into an entity at speed hurts.

| Property | What it does |
|---|---|
| `enable_flight_collision` | Turns collisions on. |
| `flight_impact_speed` | The impact speed in blocks per tick below which nothing happens (0.45). |
| `flight_block_collision_damage` | Multiplier on block impact damage, worked out from the speed of the impact the way elytra damage is. |
| `flight_entity_collision_damage` | Multiplier on the damage to a flown-into entity. |
| `flight_entity_knockback` | How hard that entity is pushed away. |
| `flight_collision_stop` | Whether an impact stops the player's speed. |

The flying client spots the impact from the speed it lost against the block, or the speed it closed on an entity. The server checks that the player is flying with this type, caps the reported speed to about 2.5 times the top speed, applies a short cooldown and works out the damage itself. Blocks use the vanilla fly-into-wall damage and entities take a player attack. Minecraft already sweeps a moving player against block shapes, so fast flight does not pass through walls.

## Gravity following

Off by default. With `enable_gravity_following`, gravity follows the direction the player is flying and looking, the way it follows a surface for Wall Crawling, so loops and vertical flight have no pitch limit. It uses Argon's directional gravity (see `GRAVITY.md`): while flying, the flight adds its own gravity source and the camera and model turn with it.

| Property | What it does |
|---|---|
| `enable_gravity_following` | Turns it on. |
| `gravity_wrap_pitch` | How far up or down the player has to look, in degrees (30 to 80), before gravity turns. Default 55. |
| `gravity_turn_ticks` | How many ticks the camera and model take to turn. Default 8. |

Flying is always aimed by the look direction: the forward key goes where the player is looking, whatever way gravity is turned, unlike Wall Crawling where movement follows the surface.

Once the player looks past `gravity_wrap_pitch` while pushing forward or moving at least a tenth of top speed, gravity turns 90 degrees about their right side: looking up makes the direction they are facing the new gravity, looking down makes the opposite. After a turn the view sits well inside the new horizon, so turns do not repeat, and keeping on round a loop turns gravity down, forward, up, back and down again. Looking back the other way undoes the last turn, so gravity updates as you fly with no key to press. Nothing turns during the first half second of flight, and merely hovering and looking around never turns it. Each turn keeps the view direction, converts the speed and keeps the player's eye where it is, so the view does not jump and the body swings around the head. Setting `gravity_turn_ticks` to 0 makes the turn instant.

Gravity only has the six axis directions, so with a heading that is not along an axis the turn uses the nearest one. A turn is skipped if the rotated hitbox would not fit.

Gravity goes back to normal, with the same animated turn, when flight ends. The flight source has a lower priority than Wall Crawling's, and the server removes it if the player is no longer flying with this type.

While gravity is bent, speed, input and view angles are all in the player's own frame, as the gravity framework does for everything else. The look direction the game reports is the world one, so the flight turns it into the player's frame before using it. The ground check for landing looks along the player's own down, and other players' lean is worked out in their own frame.

## Landing

Controlled flight lands by itself when the player is dropping towards the ground, the way `palladium:flight` does, but the touchdown is now controlled. Landing starts when the player is dropping more than they are travelling sideways, within a few blocks of a surface (along their own down when gravity is turned), and not faster than `landing_speed_threshold`.

| Property | What it does |
|---|---|
| `enable_superhero_landing` | Turns the automatic landing on (default). |
| `landing_speed_threshold` | The downward speed in blocks per tick up to which a landing is controlled. Default 1. |
| `landing_recovery_duration` | Ticks on the ground before flight stops. Moving cancels it early. Default 15. |
| `landing_damage_reduction` | How much of a hard landing's damage is prevented (0 to 1). Default 0.5. |

During a landing the descent is slowed in proportion to how far the surface is, down to a soft touchdown, sideways speed bleeds off and the body stands upright. The flight phase is 5 while landing (and 4 while descending), so an animation controller can use `palladium.flight_phase()` for a landing pose.

A controlled landing deals no damage. Diving faster than the threshold does not brake, and touching the ground then is a hard landing: the flying client reports the speed it hit at, the server caps it and deals fall damage, reduced by `landing_damage_reduction`. It is ordinary fall damage, so Palladium's fall protection abilities still reduce it, and nothing makes the flight immune.

## Diving

Off by default. With `enable_diving`, looking steeply down while pushing forward is a dive. There is no key: it follows the look direction.

| Property | What it does |
|---|---|
| `enable_diving` | Turns diving on. |
| `dive_pitch` | How far down the player has to look, in degrees (30 to 85). A dive builds up from here and is full at 85. Default 45. |
| `dive_acceleration_multiplier` | The top speed of a full dive as a multiple of the normal top speed (1 to 4). Default 1.6. |
| `dive_speed_retention` | How much of the extra dive speed carries on afterwards. 0 loses it at the normal deceleration, 1 at `dive_momentum_decay`. Default 0.8. |
| `dive_momentum_decay` | The fraction of the extra speed lost each tick at full retention. Default 0.015. |
| `dive_pullout_responsiveness` | How much easier it is to turn while above top speed, so pulling out does not need a huge circle (1 to 4). Default 1.8. |

The permitted speed never changes: it still comes from `speed`, `sprint_speed` and the speed level. A dive only lets the player go faster than that for a while, up to the dive speed, and the extra always fades, so it can't build without limit. The body already follows the direction of travel, so a dive shows as head down with no extra setting.

## Gliding

For the `gliding` profile, speed and height trade for each other: `glide_energy_exchange` (0 to 0.3, default 0.05) adds speed when the player drops and takes it away when they climb, capped at top speed (or the dive speed when diving is on). `glide_lift_speed` (0.05 to 1, default 0.6) is the fraction of top speed at which gravity is fully cancelled; slower than that the player sinks, so a glider that stops pushing slowly drops.

## Animation states

The handler works out a state for every flying player on each client, so animation controllers can pose each one from the same Molang queries:

| Query | Value |
|---|---|
| `argon.flight_state()` | 0 none, 1 hover, 2 accelerating, 3 cruising, 4 turning, 5 diving, 6 braking, 7 rolling, 8 landing |
| `argon.flight_dive()` | 0 to 1, how deep into a dive |
| `argon.flight_rolling()` | 1 while a barrel roll is happening |
| `argon.flight_roll_progress()` | 0 to 1 through a barrel roll |

These sit alongside Palladium's own queries: `palladium.flight_phase()`, `flight_speed_forward`, `flight_speed_sideways`, `flight_yaw_delta`, `flight_roll` (the bank), `flight_pitch` (the lean) and `flight_propulsion_scale`. Nothing needs animations: the body leans, banks and rolls without any.

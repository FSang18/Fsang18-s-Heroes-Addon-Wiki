---
title: Directional Gravity
menu_title: Directional Gravity
blurb: A gravity framework: pull a player toward any of six directions and everything follows.
---

# Directional Gravity

Argon can pull a player toward any of the six directions instead of down. Everything follows the new gravity: walking, standing, jumping, falling, the hitbox, the eyes, where the player looks, the camera and the drawn model. [Wall Crawling](wall-crawling.md) uses it to make the surface under the player their floor, and the `/argon gravity` command lets you try it by hand.

## Directions

`down` is normal gravity. Every other direction turns the player so that direction is their floor.

| Gravity | Floor |
|---|---|
| `down` | The ground, as normal |
| `up` | The ceiling |
| `north`, `south`, `east`, `west` | The wall on that side |

Gravity also has a **strength**, a multiplier from 0 to 10 on how hard it pulls. 1 is normal.

## What follows the gravity

- **Movement and collision.** Walking, sprinting, jumping, friction, swimming and elytra steering all behave as they do on a floor. Landing on a surface wins over sliding along it, and stepping up a block steps along the new up.
- **Hitbox.** The upright box is turned about the feet. A player who cannot fit lying along a wall drops to the crouch and then crawl pose automatically.
- **Eyes and aiming.** The eyes, the view direction, block interaction and aiming all use the new up, so what you point at is what you hit.
- **Falling.** Fall distance and fall damage count along the new down, and step sounds follow the new floor.
- **Camera.** The camera turns with the gravity, blended over a short time. With `rotate_camera` off in Wall Crawling, the camera keeps the world's up while the body and physics still turn.
- **Model.** The whole model, with its armor, held items and layers, turns about the feet, and other players see the correct orientation.

When gravity changes, the view is recomputed so the player keeps looking at the same point. Aim does not swing; only the roll of the camera changes. The body stays where it is and turns around the edge it was touching, so turning toward a wall you were touching puts your feet on the wall.

## How the gravity is chosen

Several things can try to bend gravity at once, so each one is a source with a priority.

- **Direction.** The source with the highest priority that has a direction wins. Equal priorities go to the most recent one.
- **Strength.** The strengths of all sources are multiplied together and limited to 0 to 10. Priority does not matter for strength.
- **Expiry.** A source can end after a set time. When it does, the next best source takes over. With no sources left, gravity is normal.
- **Staying after relogging.** Only a source marked persistent is saved with the player. Everything else is dropped when the player leaves, and all temporary sources are cleared on death.
- **Suspended.** Spectators, passengers and the dying have their gravity put aside, so nobody ends up sideways in a boat or stuck after death.

Surface-walking abilities such as Wall Crawling sit at a lower priority than temporary effects, and commands sit highest.

## Commands

Needs permission level 2. Each command takes an optional player list and defaults to you.

```
/argon gravity get [targets]
/argon gravity set <up|down|north|south|east|west> [targets]
/argon gravity reset [targets]
/argon gravity strength <0-10> [targets]
/argon gravity sources [targets]
```

`sources` lists what is currently bending gravity, which helps when two abilities disagree.

## Limits

- Players only.
- Other movement abilities (flight, Charged Takeoff, web swinging, grappling and dashing) move the player in world terms and misbehave while gravity is bent by a command. Run `/argon gravity reset` before using them. Wall Crawling lets go of the surface by itself when one of them starts.
- Checks for a block in the eyes (drowning, the in-wall overlay) and the player's name tag still use the upright player, and water under the eyes while lying on a wall is not handled.
- The name tag, the shadow and the hitbox outline are drawn in the upright frame.
- Argon cape physics stays upright, and custom player animations are drawn inside the turned frame without being aware of it.

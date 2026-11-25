---
title: Wall Crawling with directional gravity
menu_title: Wall Crawling
blurb: Walk on walls and ceilings, with the hitbox, camera and model following.
---

# Wall Crawling with directional gravity

`argon:wall_crawling` lets a player climb walls and cross ceilings. It has two modes. With `"use_directional_gravity": true` it works on [directional gravity](gravity.md): the surface the player is on becomes their floor, so the hitbox, eyes, camera, model, jumping and fall damage all follow. With it off (the default) the player is steered along the surface by the original crawl. The two never run at once for the same ability.

## How it behaves

- **Attaching.** Walking into a wall from the ground turns you up it. In the air, a wall (or a ceiling, if allowed) within `surface_detection_range` is grabbed. Slabs, stairs and other steps you could just walk up do not count as walls.
- **Surfaces are real collision.** Every question the crawl asks is a sweep of the actual hitbox against the blocks' collision shapes, so slabs, fences, trapdoors, walls and modded blocks are what they really are, and a surface only counts if it is under the body.
- **Corners.** The directions you are heading toward are tried best-aligned first; for each, an obstacle ahead taller than a step turns you onto it (inside corner, wall to ceiling, ceiling to wall, wall to floor), and the connected surface running out under your next step turns you round the edge (outside corner, wall to roof, wall to wall). Both pivot about the edge, so you stay in contact with the surface you left, and a turn is moved by the smallest nudge needed to clear a block it grazes. There is no fixed cooldown: what stops two nearby surfaces flickering is that turning straight back to the surface you just left is refused for 12 ticks unless you have clearly started moving back.
- **Roofs.** After climbing onto a roof you keep crawling on it (steered by the same heading) so you can walk across and back down over any edge. It ends when you jump, leave the ground, or stop moving for two seconds.
- **Controls.** In `surface_relative` mode W goes along a heading kept on the surface, not toward the camera: up a wall, or the way you faced across a floor or ceiling. The heading is carried round every corner, so looking around never changes where W goes. In `camera_relative` mode the heading is the camera direction flattened onto the surface; movement is tangent to the surface either way.
- **Speed.** `base_speed` times `speed_multiplier` times `surface_speed_multiplier`, along the surface only; sprinting multiplies by 1.3 if allowed. Gravity into the surface is separate and `gravity_strength` scales it.
- **Jumping.** Pushes you straight off the surface by `surface_jump_strength`, keeping your speed along it, and the surface cannot be grabbed again for 8 ticks. Detaching from height falls and takes fall damage normally; staying attached never accumulates fall distance.
- **Tight spaces.** If the full-height body does not fit on the next surface but the crawl-sized one does, and `auto_crawl` is on, you turn onto it crawl-sized (vanilla's pose logic does the rest).
- **Surface disappears.** If the surface under you is gone for 2 ticks you move onto the nearest other surface, or let go and fall.
- **Other abilities.** The crawl lets go whenever something else needs the player's movement: Palladium flight, creative flight, a Charged Takeoff, a web swing in hand, gliding, swimming, a vehicle, spectator, death, or the ability ending. The crawl never fights them for the velocity.

## Multiplayer

The client chooses the surface (as it does for ordinary movement), turns gravity at once, and tells the server, which checks there is a surface at the reported position and makes it official; other players then see the turn. A choice the server refuses is answered with the server's gravity, which the client adopts. The server also drops the crawl if there has been no surface near the body for about two seconds. Only changes are sent.

## Properties

These properties belong to the directional gravity mode. Where one is not set it falls back to the matching original property, written in the Default column:

| Property | Default | Notes |
|---|---|---|
| `use_directional_gravity` | `false` | Turns everything below on. |
| `gravity_strength` | `1.0` | Multiplier on gravity while attached. |
| `rotate_camera` | `camera_roll` | Whether the camera turns with the surface. `false` keeps the view upright to the world. |
| `camera_transition_time` | `6` | Ticks for the camera to turn. 0 is instant. |
| `smooth_transitions` | `true` | `false` makes every turn instant. |
| `transition_duration` | `6` | Ticks for the drawn body to turn. |
| `transition_easing` | `ease_in_out` | `linear`, `ease_in`, `ease_out`, `ease_in_out`. |
| `surface_detection_range` | `attach_distance` (0.5) | How close a surface must be to grab or keep. |
| `surface_transition_tolerance` | `0.15` | How far before an edge the turn starts, 0 to 0.3. |
| `movement_mode` | `surface_relative` | Or `camera_relative`. |
| `surface_jump_strength` | `detach_strength` | Push off the surface when jumping. |
| `auto_crawl` | `true` | Allow turning onto surfaces only a crawl-sized body fits. |
| `allow_ceiling_crawling` | `ceiling_crawling` | Ceilings are valid surfaces. |
| `allow_corner_transitions` | `true` | Turn at corners and from floor onto a wall. `false` leaves only grabbing from the air. |
| `preserve_surface_momentum` | `true` | Keep speed through a turn. |
| `surface_speed_multiplier` | `1.0` | Extra multiplier on speed along the surface. |
| `allow_surface_sprinting` | `true` | |
| `play_running_animation` | `true` | Sprinting along a wall or ceiling plays the running animation (legs and arms swinging). Vanilla only starts it from how far you move across the ground, which is nothing while climbing. Only while sprinting. |
| `crawl_when_not_sprinting` | `false` | On a wall or ceiling the player is crawl-sized (vanilla crawling pose, a 0.6 block hitbox that fits one-block gaps) unless sprinting. Sprinting stands them back up as far as there is room. The server applies the same rule, so both use the same hitbox. |
| `view_orientation` | `relative` | `relative`: a turn keeps the same look angles in the new gravity. `world`: it keeps the same point in the world. |

In this mode `third_person_camera_roll` and `gravity_pull_strength` do nothing; the whole camera turns in either perspective, and gravity does the pulling.

## Examples

Spider-Man style, using the original speeds:

```json
{
    "type": "argon:wall_crawling",
    "use_directional_gravity": true,
    "ceiling_crawling": true,
    "base_speed": 0.5,
    "speed_multiplier": 0.75,
    "detach_strength": 1.0,
    "rotate_camera": true,
    "movement_mode": "surface_relative",
    "auto_crawl": true
}
```

A slower climber that keeps the camera upright and stays off ceilings:

```json
{
    "type": "argon:wall_crawling",
    "use_directional_gravity": true,
    "base_speed": 0.1,
    "rotate_camera": false,
    "allow_ceiling_crawling": false,
    "allow_corner_transitions": false,
    "surface_speed_multiplier": 0.5,
    "allow_surface_sprinting": false
}
```

## Limits

- Looking straight into the surface you stand on is a gimbal point of any yaw-and-pitch camera: a tiny change of aim there can swing the roll. A turn itself does not spin the view, but aiming straight at your feet while on a wall can roll the view as you move the mouse.

- Flight, a takeoff, a web swing and gliding make the crawl let go; it does not resume by itself until the player lands or lets go of them and touches a surface again.
- Swimming and lava let go too; there is no crawling in water.
- The player's own `Takeoff`, web and appendage animations are not aware of being on a wall.
- Climbing an unbroken wall relies on the wall being under the whole body footprint; a wall of a single thin block, or one broken by gaps wider than the tolerance, is crossed by turning round it.

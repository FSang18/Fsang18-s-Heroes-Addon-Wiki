---
title: Feature Flags
blurb: The optional Argon features a world or data pack has to switch on.
---

# Feature Flags

Some Argon features change how the base game or Palladium behaves, so they stay off until a pack asks for them. They are normal Minecraft feature flags, the same kind Palladium uses for its own optional features. A flag does nothing until it is enabled, so installing Argon on its own never changes an existing world.

Argon adds three flags.

| Flag | What it turns on |
|---|---|
| <code class="argon-id" title="Click to copy">argon:power_tag_parents</code> | Powers can name a tag of parent powers instead of a single parent. |
| <code class="argon-id" title="Click to copy">argon:customization/secondary_eye_selection</code> | A second set of eye pixels, picked on a **Secondary** tab of the eye screen. |
| <code class="argon-id" title="Click to copy">argon:customization/mouth_selection</code> | A set of mouth pixels, picked on a **Mouth** tab of the eye screen. |

## Enabling a flag

### From a data pack

Add the flags to the `features` section of the pack's `pack.mcmeta`. This is how FSang18's Heroes switches on Palladium's flags too.

```json
{
  "pack": {
    "description": "My pack"
  },
  "features": {
    "enabled": [
      "argon:power_tag_parents",
      "argon:customization/secondary_eye_selection",
      "argon:customization/mouth_selection"
    ]
  }
}
```

A world gets the flags when it is created with the pack selected, because the flags are saved in the world's `level.dat` under `enabled_features`. Add the pack on the data pack screen of the Create World menu.

### In an existing world

The flags a world has are stored in its `level.dat` under `enabled_features`, so a world made without the pack does not have them. The flags can be added to that list with an NBT editor while the world is closed. Make a copy of the world first.

## Power Tag Parents

<div class="argon-meta"><span class="argon-meta-label">Flag</span><code class="argon-id" title="Click to copy">argon:power_tag_parents</code></div>

Palladium's `depends_on` ties a power to one specific parent power. With this flag, a power can instead name a **tag of powers**, and a player can get the power while they hold any power in that tag.

Two settings are added to the power file (`data/<namespace>/palladium/power/<name>.json`).

| Key | Type | Description | Required | Fallback |
|---|---|---|---|---|
| `parent_tag` | Power tag | The tag of powers that count as a parent, for example `palladium:main_power`. A power without this key behaves as it does in Palladium. | No | None |
| `parent_required` | Boolean | When `true`, the player must hold a power in `parent_tag`. When `false`, the power can be added whether or not they do. | No | `true` |

A power that already uses Palladium's `depends_on` keeps that behavior and ignores these settings.

```json
{
  "name": {
    "translate": "power.example.herald.name"
  },
  "parent_tag": "palladium:main_power",
  "parent_required": false
}
```

Without the flag, both keys are ignored and powers use Palladium's normal rules.

## Secondary Eye Selection

<div class="argon-meta"><span class="argon-meta-label">Flag</span><code class="argon-id" title="Click to copy">argon:customization/secondary_eye_selection</code></div>

Palladium's eye screen lets a player pick which pixels of the face are eyes. This flag adds a **Primary** and a **Secondary** tab to that screen, so the player can pick a second set of pixels. A pixel is either primary or secondary, never both.

- Packs color the second set with the [Secondary Eye Selection Texture](../reference/dynamic-textures.md) (`argon:eye_selection_secondary`), the same way `palladium:eye_selection` colors the first.
- The **Reset** button sends the primary pixels back to Palladium's default eyes and empties the secondary set. **Save** stores both.
- The eye screen itself only appears when Palladium's own flag, `palladium:customization/eye_selection`, is enabled as well.

## Mouth Selection

<div class="argon-meta"><span class="argon-meta-label">Flag</span><code class="argon-id" title="Click to copy">argon:customization/mouth_selection</code></div>

Adds a **Mouth** tab to the same eye screen, with its own set of pixels. A pixel can be an eye, a secondary eye or a mouth, never more than one.

- Packs color the mouth with the [Mouth Selection Texture](../reference/dynamic-textures.md) (`argon:mouth_selection`).
- The mouth pixels also give beams an anchor. A beam with the body part `argon:mouth` starts from the mouth the player picked.
- If both customization flags are enabled, the eye screen shows all three tabs.

The server checks the flags before it accepts a selection, so a player cannot save mouth or secondary pixels in a world that does not have the flag.

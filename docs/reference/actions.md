---
title: Actions
---

# Actions

<p class="argon-intro">Actions are things that happen once, for example running inside an action ability or when a beam hits something. These are the actions Argon adds.</p>

<p class="argon-count">3 listed &middot; Argon 1.1.0</p>

### Directional Leap {#argondirectional_leap}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:directional_leap</code></div>

<div class="argon-desc">Like palladium:leap, but sets the velocity to your look direction scaled by the velocity modifier instead of adding to it, so the leap always goes where you aim.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>velocity_modifier</code></td><td>Float</td><td>The multiplier applied to the entity's look direction when this action runs.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:directional_leap",
      "velocity_modifier": 2
    }
    ```

---

### Jump {#argonjump}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:jump</code></div>

<div class="argon-desc">Launches the entity straight up like a jump, keeping its sideways movement. A normal jump is about 0.42 and gets roughly 1.25 blocks, 0.8 gets roughly 4.5.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>velocity</code></td><td>(Dynamic) Value</td><td>The upward speed, in blocks per tick.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>additive</code></td><td>Boolean</td><td>Whether the speed is added to the entity's current vertical speed instead of replacing it.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">false</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:jump",
      "velocity": 0.8
    }
    ```

---

### Ride {#argonride}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:ride</code></div>

<div class="argon-desc">Mounts the entity you look at, once. "ride_target" makes you ride it, "target_rides_player" puts it on top of you instead (toggled off if triggered again).</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>mode</code></td><td><code>ride_target</code><br><code>target_rides_player</code></td><td>Which way to mount: "ride_target" (user rides target) or "target_rides_player" (target rides user).</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>range</code></td><td>Double</td><td>How far away, along the user's line of sight, an entity can be to be targeted.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

=== "Example"

    ```json
    {
      "type": "argon:ride",
      "mode": "ride_target",
      "range": 8
    }
    ```

---


---
title: Ability State Handlers
---

# Ability State Handlers

<p class="argon-intro">State handlers decide when an ability is unlocked or enabled. These are the ones Argon adds on top of Palladium's own.</p>

<p class="argon-count">1 listed &middot; Argon 1.0.0</p>

### Buyables {#argonbuyables}

<div class="argon-meta"><span class="argon-meta-label">ID</span><code class="argon-id" title="Click to copy">argon:buyables</code></div>

<div class="argon-desc">Like the buyable handler, but the listed abilities must all be unlocked first, and each can be left out of the power tree's connection lines.</div>

=== "Settings"

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>cost</code></td><td>Cost</td><td>What the player has to pay to unlock the ability.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>requires</code></td><td><em>Buyable Requirement</em>[]</td><td>Abilities that have to be unlocked first. Each entry has an "ability" reference and an optional "draw_line" flag.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">[]</td></tr></tbody></table></div>

    <p class="argon-nested"><code>requires[]</code> (Buyable Requirement)</p>

    <div class="argon-table-wrap"><table class="argon-fields"><thead><tr><th>Key</th><th>Type</th><th>Description</th><th>Required</th><th>Fallback</th></tr></thead><tbody><tr><td><code>ability</code></td><td>Ability Reference</td><td>The ability that has to be unlocked first.</td><td class="argon-center"><span class="argon-yes">&#10003;</span></td><td class="argon-fallback">/</td></tr><tr><td><code>draw_line</code></td><td>Boolean</td><td>Whether a line to the requirement is drawn in the power tree.</td><td class="argon-center"><span class="argon-no">&#10007;</span></td><td class="argon-fallback">/</td></tr></tbody></table></div>

---


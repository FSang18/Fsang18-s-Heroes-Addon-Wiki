---
title: DNA Transfer Station (the DNA Power Transfer Machine)
menu_title: DNA Transfer Station
blurb: A multiblock machine that moves powers between players and vials.
---

# DNA Transfer Station (the DNA Power Transfer Machine)

A multiblock machine that takes a Palladium superpower out of a player and into a vial, or gives a power from a vial to a player. DNA vials are only containers: they never grant anything by themselves. The machine does every transfer.

Config: `config/argon-dna-transfer.toml`.

## Building it

Seen from the front, the machine is four blocks. All of them have to face the same way, and the Chassis can be on either side.

```
 [Station] [Chassis top]
 [Power ] [Chassis bottom]
```

| Block | ID | What it is |
| --- | --- | --- |
| DNA Transfer Station | `argon:dna_transfer_screen` | The controller. Right-click for the screen. Its face shows the machine state (dark, lit, blinking), and its screen is the frame of the machine screen. |
| Power Block | `argon:dna_transfer_power_block` | Directly under the Station. Required. Stores the RF (FE) the machine runs on; right-click it for its screen. |
| Chamber (the Chassis in the code and below) | `argon:dna_transfer_chassis` | Two blocks high (placed like a door). The chamber the player stands in, with a sliding glass door. |

The Station scans only these positions (never loads a chunk), claims the Chassis so no second Station can run it, and lets go of it when it is broken or the structure stops being valid. A transfer running at that moment is cancelled and the door opens.

## Using it

1. Open the door (right-click the Chassis from outside), step in. You must be inside the chamber, between its walls.
2. Right-click the chamber wall (or the Station from outside) for the screen. Sneak and right-click inside to open or shut the door without the screen.
3. Put a **filled vial** in the top slot and/or an **empty vial** in the bottom slot. If you have more than one power the machine can touch, pick one in the list.
4. Shut the chamber door (the door icon on the screen, or right-click the Chamber from outside before you step in, then close it from the screen). START only works with the door shut; the status line says **CLOSE THE CHAMBER DOOR TO START** until it is.
5. Press START. The door is locked for the whole transfer (100 ticks by default; nothing can open it, from inside or out), then it opens by itself (`open_door_on_completion`). If a transfer is cancelled the door opens at once.

| Vials | Player has a registered power | Result |
| --- | --- | --- |
| Empty only | yes | **Extract**: power goes into the empty vial. |
| Filled only | no | **Grant**: the filled vial is left empty. |
| Filled only | yes | **Overwrite**: the power they have is destroyed and replaced. Needs an explicit CONFIRM OVERWRITE every time. |
| Filled + empty | yes | **Exchange**: their power goes into the empty vial, the new one is granted. |
| Filled + empty | no | **Grant** (the empty vial is left alone). |

Damage: `damage_per_vial_operation` (0.5 HP) for each vial filled or emptied, dealt only when the transfer completes. An exchange is two. By default it can never take the player below half a heart.

A transfer is cancelled, changing nothing and costing nothing, if the occupant leaves, dies or disconnects, a part of the structure is removed, the energy runs out, or anything about the player or the vials differs from what was agreed when Start was pressed.

## Vials

* `argon:empty_dna_vial`, `argon:filled_dna_vial`.
* A filled vial holds `argon:stored_power` (the power id and its liquid colour) and, for powers with `persistent_data`, `argon:stored_power_state` (that power's saved progress: level, experience, skill points, bought abilities). Filled vials do not stack, so different powers never merge.
* Extracting with state preserved also clears the progress from the donor, so progress exists in one place only.
* `/argon dna_vial <player> <power>` (permission level 2) gives a filled vial of a registered power, for testing and staff.

## Which powers the machine touches

The machine only ever works on powers listed in data, and only on a player's **superpowers** (the ones Palladium keeps in the player's superpower list: `SuperpowerUtil`). Suit powers, ability-given powers and anything else are never listed by it and so are never touched.

Each file in `data/<namespace>/dna_transfer/powers/` can register one power, or a whole list of them in one script. It can take any of three shapes:

**1. One power** (an object):

```json
{
  "power": "fsang:dc/kryptonian/absolute",
  "can_extract": true,
  "can_grant": true,
  "can_overwrite": true,
  "can_be_overwritten": true,
  "preserve_state": true,
  "display_name": { "text": "Kryptonian" },
  "colors": ["#3BF2C4", "#1B7A8C"],
  "requires": [],
  "blocked_if_holding": [],
  "energy_cost_to_start": 2000,
  "energy_cost_per_tick": 30,
  "processing_ticks": 100
}
```

**2. An array of powers.** Each item is an object like the one above, or just a power id:

```json
[
  "mypack:mutant/regeneration",
  { "power": "mypack:mutant/telepathy", "can_overwrite": false }
]
```

**3. An object with a `powers` list and a `defaults` area.** Whatever `defaults` sets (the costs, or any other field below) applies to every power in the list that does not set it itself, so a pack's costs are written once and a power overrides them only if it needs to:

```json
{
  "defaults": {
    "energy_cost_to_start": 2000,
    "energy_cost_per_tick": 30,
    "processing_ticks": 100
  },
  "powers": [
    { "power": "mypack:mutant/regeneration" },
    { "power": "mypack:mutant/telepathy", "processing_ticks": 160 },
    { "power": "mypack:cosmic/herald", "energy_cost_to_start": 8000, "energy_cost_per_tick": 80, "processing_ticks": 300 }
  ]
}
```

**Vial colours in a script.** `colors` is an ordinary field, so it works in `defaults` too: put it there for every power in the file to share, and give a power its own `colors` to replace it (the whole array is replaced, not merged):

```json
{
  "defaults": { "colors": ["#3BF2C4"] },
  "powers": [
    { "power": "mypack:mutant/regeneration" },
    { "power": "mypack:mutant/telepathy", "colors": ["#B07CFF"] },
    { "power": "mypack:cosmic/herald", "colors": ["#55FF55", "#8B1A1A"] },
    { "power": "mypack:speed/force", "colors": ["#FFD83B", "#FF7A1A", "#8B1A1A"] }
  ]
}
```

The first power gets the default colour, the second its own single colour, the third a two-tone liquid (green on the upper left, dark red on the lower right) and the fourth three diagonal bands, yellow then orange then dark red. A power with no colour anywhere gets one picked from its id. A vial keeps the colours it was filled with, so changing a script does not recolour vials that already exist.

FSang's own powers are one script like this (`data/fsang/dna_transfer/powers/fsang_powers.json`). An entry that does not parse is logged and skipped; the rest of the file still loads.

All fields except `power` / `power_tag` are optional and the values above are the defaults.

| Field | Meaning |
| --- | --- |
| `power` or `power_tag` | The power's id, or a power tag to register many at once. An id wins over a tag. |
| `enabled` | `false` takes the power out again. Use it in a later pack to exclude a power another pack or a tag registered. |
| `can_extract` | May be taken out of a player and stored in an empty vial. |
| `can_grant` | A vial holding it may be used to give it to a player. |
| `can_overwrite` | When granted, it may replace a power the player already has. |
| `can_be_overwritten` | A player's copy may be destroyed by an overwrite (no vial to keep it). |
| `preserve_state` | The vial also carries the power's saved progress. Also needs the power's own `persistent_data`, and is off everywhere if the config says so. |
| `display_name` | A text component to show instead of the power's own name. |
| `colors` | The colours of its vials' liquid: an array of one to three hex codes (`"#3BF2C4"`, `"0x3BF2C4"` or `"3BF2C4"`; plain numbers work too). **The order written is the order they are used.** One colour fills the liquid. Two split it along the diagonal from its top right corner to its bottom left corner, the first on the upper left and the second on the lower right. Three cut it into three diagonal bands, the first on the upper left, the second in the middle and the third on the lower right. A lone `"color": "#3BF2C4"` still works as a one-entry array. By default one colour is picked from the power's id. |
| `requires` | Powers the player must already hold for this one to be granted. |
| `blocked_if_holding` | Powers that stop this one being granted while the player holds them. |
| `energy_cost_to_start` | Energy (FE) taken from the Power Block when a transfer of this power starts. Default: the config's `energy_cost_to_start`. |
| `energy_cost_per_tick` | Energy (FE) taken every tick while it runs. Default: the config's `energy_cost_per_tick`. |
| `processing_ticks` | How long the transfer takes, in ticks (20 = one second). Default: the config's `processing_ticks`. |

Whose costs a transfer uses: an extraction uses the power taken out, a grant or an overwrite the power that arrives, and an exchange (which moves both) the larger of the two for each of the three numbers.

Powers that are the parent of another power the player holds cannot be extracted or overwritten until the child is gone. A grant also has to fit Palladium's own rules (a free superpower slot, or the parent power for a child power); the machine checks this before changing anything.

Examples:

```json
{ "power_tag": "mypack:dna_compatible" }
```

```json
{ "power": "mypack:mutant/regeneration", "can_overwrite": false, "requires": ["mypack:mutant/gene"] }
```

```json
{ "power": "fsang:marvel/mutant/toad", "enabled": false }
```

## Config (`argon-dna-transfer.toml`)

`processing_ticks` (100), `damage_per_vial_operation` (0.5), `damage_can_kill` (false), `energy_cost_to_start` (2000), `energy_cost_per_tick` (30), `energy_transfer_rate` (2000), `fuel_energy_per_tick` (40), `allow_username_lock` (true), `open_door_on_completion` (true), `require_occupant_to_start` (true), `preserve_power_state` (true), `max_state_bytes` (65536).

A default transfer therefore costs 2,000 FE to start plus 30 FE a tick (5,000 FE in all over the default 100 ticks). Set both to 0 and the machine needs no energy at all. If you already have a `argon-dna-transfer.toml`, edit it or delete it to get the new defaults.

## Power Block

The Power Block (id `argon:dna_transfer_power_block`) stores the energy (FE) the machine runs on. Cables and generators can fill it from any side, and nothing can pull energy back out through them.

Right-click it for its screen: an energy bar, a **charge from** slot on the left (an item that holds energy, such as a battery, is emptied into the block) and a **charge to** slot on the right (an item that takes energy is charged from the block), up to `energy_transfer_rate` FE a tick each. Any item that can hold energy works, including Argon's energy items. A **fuel** slot in the middle burns anything a furnace burns into energy: `fuel_energy_per_tick` FE for every tick of the item's burn time (40 FE a tick, so a piece of coal gives 64,000 FE). It only burns while the buffer has room for the energy, so nothing is wasted.

**Capacity and keeping the energy.** A Power Block holds 100,000 FE by default. Capacity modules are installed from the Tech Table's Modify tab (put the Power Block in the device slot): each module adds 50,000 FE, up to 500,000 FE (eight modules). The capacity is not a config value: it is the `argon:energy_capacity` component on the item, which the `argon:energy_capacity` modification effect changes, so the numbers live in the modification file (in FSang: `data/fsang/argon/suit_modification/power_block_capacity.json`, using `fsang:module_capacity`; copy it with your own module item for another pack). The DNA Transfer Station takes no modules.

When a Power Block is broken it drops as an item that keeps its capacity (`argon:energy_capacity`), the Tech Table modules recorded as installed (`argon:suit_modifications`, which is what the Tech Table reads back) and the energy it held (`argon:energy`), and placing it again gives them back. This is done by its loot table copying those three components from the block entity. The Power Block item is itself an energy item, so it can also be charged, or drained into another Power Block. The slot contents (including the fuel) drop separately, as with any container.

A transfer is paid for from this block: the start cost is taken when Start is accepted, and the per-tick cost every tick while it runs. If the buffer runs dry the transfer is cancelled and nothing changes.

## Access lock

Public, Private (owner only), or a named player. The player who places the Station owns it. In named-player mode **only** that player can use the machine (the owner included, who can still change the lock to let themselves back in). Only the owner (or an operator) can change the lock. The lock stores UUIDs; names are only shown. It limits who may use the machine and never traps anyone. Clicking the access button cycles Public, Private, then the named player (once one has been set), then back to Public.

## Safety and multiplayer rules

* Every decision is made on the server from its own data: who is in the chamber (found from positions), what powers they hold (Palladium), what the vials hold, and whether the lock allows it. Packets from the screen are only requests and are checked again. A client cannot send a power id to be granted; the text is only compared with what the occupant really has.
* By default only the player inside the chamber can start a transfer, so nobody can strip another player from outside.
* Both vial slots shut while a transfer runs; the door cannot be opened by hand until it ends.
* The chamber interior is empty, so a closed door never suffocates anyone. A world reload never leaves a transfer running; it just leaves the door as it was, and the player can open it from inside.

## Limits

* Powers a player gets from anything other than the superpower list (suit sets, abilities) are not superpowers, so the machine leaves them alone on purpose.
* Saved power data in a vial can be edited by anyone with creative or NBT tools. The machine caps its size (`max_state_bytes`) but cannot judge what is inside.

## Credits

Machine, vial and chassis textures are adapted from the "unused-textures" pack by Malcolm Riley (https://github.com/malcolmriley/unused-textures), licensed CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changes: copied and renamed, and the chassis glass has its transparent middle filled with a faint translucent blue. The machine screen is framed with the Station block's own front texture and uses the SOL menu's button outline from this workspace, with a grid and scan lines copied from the Tech Table's look; its chamber picture is drawn from the Chassis block's textures.

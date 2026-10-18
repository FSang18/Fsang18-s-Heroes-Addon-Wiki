---
title: "Commands"
---

# Commands List

Below is a list of all relevant commands for the addonpack.

**Note, not all of these commands are accessible without cheats enabled / Operator rights.**

## **Superpower Commands:**

**/superpower add fsang:powername @**

* This command can be used to add powers to any player. Just replace the @ with the name of the player.

**/superpower query @**

* This command can be used to list any / all powers a player has. Just replace the @ with the name of the player.

**/superpower remove fsang:powername @**

* This command can be used to remove powers from any player. Just replace the @ with the name of the player.

**/superpower replace fsang:powername fsang:powername @**

* This command can be used to replace powers from any player. Just replace the @ with the name of the player.

**/superpower set fsang:powername @**

* This command can be used to set powers from any player, erasing all others. Just replace the @ with the name of the player.

**/ability unlock @s fsang:power_name all**

* This command can unlock every ability for the power you have, just replace the _power_name_ with the name of the power you have.

**/ability lock @s fsang:power_name all**

* This command can lock every ability for the power you have, just replace the _power_name_ with the name of the power you have.

## **FSang Skill Point Commands**

**/FSang.EXP set @s #**

* This command sets your Exp to whatever you replace # with.

**/FSang.Level set @s #**

* This command sets your Level to whatever you replace # with. Max level 50.

**/FSang.SkillPoints set @s #**

* This command sets your Skill Points to whatever you replace # with.

## **FSang Gamerule Commands**

**/gamerule FsangItemCooldown true**

* Enables the cooldown timer to swap powers (not including symbiotes)

**/gamerule FsangItemCooldown**

* Disables the cooldown timer to swap powers (not including symbiotes)

**/gamerule FsangSymbiote Cooldown true**

* Enables the cooldown timer to swap symbiotes

**/gamerule FsangSymbiote Cooldown false**

* Disables the cooldown timer to swap symbiotes

**/gamerule FsangStrongPunch false**

* Disables the Strong Punch shockwave effect.

**/gamerule FsangStrongPunchDamage #**

* This command sets your Strong Punch Shockwave to kick in whatever you replace the # with it.

## Power-Specific Scoreboard Commands

### Age-based Powers

**/FSang.Age set #**

* This command can work with any power that uses an Age-based system to set their age to whatever you replace # with.

### Bone Claws:

**/scoreboard players set @s X_Gene 20**

* This command sets your [Bone Claws](powers/main-powers/mutations-x-gene/bone-claws/index.md) to Logan's

**/scoreboard players set @s X_Gene 21**

* This command sets your [Bone Claws](powers/main-powers/mutations-x-gene/bone-claws/index.md) to Laura's

**/scoreboard players set @s X_Gene 22**

* This command sets your [Bone Claws](powers/main-powers/mutations-x-gene/bone-claws/index.md) to Dakkon's

### Electrokinesis:

**/scoreboard players set @s FSang.Electrokinesis.Color 1**

* This command sets your [Electrokinesis Mutation](powers/main-powers/mutations-x-gene/electrokinesis.md) color to Blue

**/scoreboard players set @s FSang.Electrokinesis.Color 2**

* This command sets your [Electrokinesis Mutation](powers/main-powers/mutations-x-gene/electrokinesis.md) color to Gold

**/scoreboard players set @s FSang.Electrokinesis.Color 3**

* This command sets your [Electrokinesis Mutation](powers/main-powers/mutations-x-gene/electrokinesis.md) color to Purple

### Karma:

/FSang.Karma set @s #

* This command can be used set your [Karma ](karma.md)Levels to whatever you replace the # with.

### Teleportation:

**/scoreboard players set @s X_Gene 1**

* This command sets your [Teleportation Mutation](powers/main-powers/mutations-x-gene/teleportation.md) color to Blue

**/scoreboard players set @s X_Gene 90**

* This command sets your [Teleportation Mutation](powers/main-powers/mutations-x-gene/teleportation.md) color to Red

### Secondary Powers:

/FSang.Secondary add &lt;power&gt; #

* This command allows you to add as many tokens to the secondary power designated within the &lt;power&gt; section based on the number placed in the # section.

/FSang.Secondary remove &lt;power&gt; #

* This command allows you to remove as many tokens to the secondary power designated within the &lt;power&gt; section based on the number placed in the # section.

/scoreboard players set @ Fsang.Age.Symbiote #

* This command sets your [Natural Symbiote](powers/secondary-powers/symbiotes/natural.md) Codex Bond to whatever you replace # with.

### Speedforce (Not Tachyon):

**/Fsang.SpeedTrail get (primary / sescondary)**

* This command gets either your primary or secondary [Speedforce](powers/main-powers/speedforce/index.md) Trail hex color depending on which you use (primary or secondary)

**/Fsang.SpeedTrail set (primary / sescondary) (hex)**

* This command sets either your primary or secondary [Speedforce](powers/main-powers/speedforce/index.md) Trail hex color depending on which you use (primary or secondary) based on the hex color code you enter at the end.

### 

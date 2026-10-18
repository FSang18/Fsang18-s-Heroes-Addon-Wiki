---
title: "Accessory Support"
---

# Accessory Support

The following content will only be compatible with FSang18's Heros v12.0.0+

Here, you can find step by step instructions for creating a custom addon to my addon specifically for adding in accessories for custom skins on the following powers which have accessory support. Download the Test Pack then click on which of the available powers you'd like to add a custom accessory for:

* [Metal Mimicry](powers/main-powers/mutations-x-gene/metal-mimicry/index.md)
* [Cryokinesis](powers/main-powers/mutations-x-gene/cryokinesis.md)

## Instructions:

* Download the More Skins Test Pack below:
  * [More Fsang Skins Test Pack.zip](uploads/af37c530b81bf5329064b17e36710a96/More_Fsang_Skins_Test_Pack.zip)
* Unzip the folder and navigate to addon\\more_fsang_skins\\accessories\\
  * Here you will see two files named "colossus_test.json" and "colossus2_test.json" with each being for the Metal and Diamond forms, respectively
    * Change the "test" part of the names to whatever unique identifier you want your skin to use (**Make sure to remember the exact name you use instead of "test"**)
* Now, navigate to assets\\fsang\\textures\\models\\dynamic_textures\\
  * Here, you will see two folders, one named "colossus" and one named "colossus2" each folder contains the base texture for the Metal and Diamond forms, respectively. Additionally, the Blockbench color paletts can be downloaded below:
  * [colossus_palette.gpl](uploads/c8d90eb26a18cdd181406742e08824af/colossus_palette.gpl)
  * [colossus2_palette.gpl](uploads/bf0ee6230e028c40245d319f2ccfa8d6/colossus2_palette.gpl)
  * [cryokinesis_palette.gpl](uploads/0b6415328daf0bd3d8ab170d0448803a/cryokinesis_palette.gpl)
* Once your custom skin is made, save it in the correct folder(s) using the **same identifier** from the accessory menu setup.
* Now, we can navigate to: assets\\fsang\\lang\\ where you should find a file named "en_us"
  * In this file, you will be designating a name for your accessory slot in-game. Change the "test" portion in this to whatever your identifier was from before, then assign your accessory a name.
* Once you have done all of this, navigate back to your "more_fsang_skins-1.0.0" folder. here you will be selecting everything you see, and zipping it all together.
  * Once Zipped, you will change the .zip file extension to a .jar
* If you have done everything correctly, then when you drag / drop that .jar file into your mods folder, you should see your new skin / accessory menu when you equip the compatible powers

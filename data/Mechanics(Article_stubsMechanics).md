# Engine

Rust uses Unity 5.6 as its game engine.
# Game Interface

Main Article: Game Interface
The game interface... GUI... Console... Settings... Server Browser...
# Character

Each player is assigned a character model based on their personal Steam ID, meaning the character model persists across servers. There are currently five face models, two skin types and different hair types, allowing for ten possible unique faces. The player's skin tone is selected from a range with much more variety. As of Devblog 106, female character models were added in to add extra variation for players. 
# NPCs

Several different NPC (Non-playable Character) classes can be found in Experimental Rust. They used to be divided into two categories - Hostile and Peaceful. This was until a recent update, Devblog 155, where even peaceful animals turned hostile when approached.
## Hostile

Hostile NPCs are aggressive towards the player. They will generally attempt to engage players, who attack or approach them.
Hostile NPCs include:
Bears
Bradley APC
Scientist
Wolves
Attack Helicopters
Boars
Note: In Legacy Rust it is possible for a player to encounter hostile Rad (Irradiated) Wolves and Bears as well. Those have not been implemented in Experimental Rust yet. Nonetheless, the implementation is still subject to discussion.
## Peaceful

Peaceful NPCs are usually quite passive towards the player, they will generally avoid the player but when approached, they can often attack - even chickens.
Peaceful NPCs include:
Horses
Deer
Chicken
# Environment

Main Article: Environment
The environment can be affected greatly by the seed used to procedurally generate the Map. 
# Spawning

When a player wakes up for the first time on a server they are spawned at a random point on a shore, usually a beach bordering an ocean. There are no longer any chances of spawning on the coastline of a lake.
## You spawn with:

About 60 health points (can be more or less, out of 100)
about 40 hunger points (out of 500)
roughly 50 thirst points (out of 250)
a Rock, to be used as a tool or a weapon.
a Torch, to help the player see at night.
# Wounded

Main Article: Wounded_(aka_Downed)
Once a player's Health is reduced to 0 the player is "wounded" or "downed". Whilst in this state, the player will be able to slowly crawl around, until their body is accessed by another player or they are killed. Nearby players can either help the player up or the player could die. However, there is a chance that a player can get back up on their feet after this state.. A wounded player's inventory can be freely accessed by all players, so they will take even your pants.
To prevent group fights from unnecessarily prolonging, the wounded status will be available only once every 60 seconds at most. Being mortally wounded more than twice in those 60 seconds will cause the player to die the second time.
# Death

When a player takes more damage than their remaining health they die. Upon death a screen is displayed announcing the death. Two options are presented as well - to either respawn at a random location on a shore or at a Sleeping Bag/Bed, that has been deployed prior to dying. The death screen also shows how long you were alive, how much of your life was spent sleeping, who killed you as well as the weapon used to kill you, and the distance at which your killer killed you from.
# Combat

Combat is essential for fighting off animals and other players. There is melee and ranged combat. Melee Weapons include Rocks and Spears. The best way to fight with melee is to move constantly to avoid being hit and time your swings well to hit the opponent.
Ranged weaponry includes a bow and a variety of handmade guns. Projectiles fired are their own entity, meaning they are affected by gravity and will fall over large distances. Fired arrows and high velocity arrows (either by a crossbow or a hunting bow) can be retrieved if they hit the ground.
As of Devblog 75, it has been proposed that the devteam is trying to make melee combat more diverse in the future by implementing mechanics like parrying, dodging and blocking.
Pro Tip: Practice with the bow! It's low craft time and low ammo cost make it a quality weapon for getting quick kills on players with better gear. In a fight with 2 or more players with bows vs one player with a gun in a field, bet on the bowmen.
# Gathering

Gathering throughout rust is a simple as pressing the use key (by default it's "E") on entities such as hemp / mushrooms or rocks / metal / sulfur sometimes found on the floor. Gathering is essential for gaining scrap, which is used in research to expand your crafting knowledge.
# Research

LEGACY RUST:
In rust scrap is used to craft and workbench and or a research table. The workbench allows you to use scrap to "Experiment" which will randomly generate an unknown blueprint corresponding with the level of work bench used. There are three levels of work bench, each level of bench has a higher crafting cost and requires the last level of workbench to craft (ie a level 2 workbench requires a level 1 bench to craft.)
The research table is used in conjunction with a work bench to make blueprints at the cost of items you have found. The appropriate tier of workbench will be required to create blueprints from the items you find (ie you will need a level 2 work bench near your research bench in order to create blueprints from level two items.)
Pro Tip: It's worth it to save space and replace a level 1 work bench by destroying it after using it to craft a level 2 work bench, but whenever possible try to keep the level 2 work bench after crafting a level 3 bench. The fairly high cost of the level 2 bench makes it worth keeping around for insurance and crafting.
RUST:
In rust scrap is used to craft workbenches and research tables. Workbenches allow you to use scrap to progress down a tech tree to unlock the ability to craft new items. Workbenches have three tiers: Tier 1, Tier 2 and Tier 3, with the Tier 1 tech tree containing mainly early game items, the Tier 2 containing mid-game items such as the rocket launcher and high velocity rockets, and the Tier 3 containing end game items such as timed explosive charge (commonly referred to as c4) and the rocket.
The research table can be used to make blueprints of items you already have without needing to progress down the relevant tech tree, however you will be unable to progress further down the tech tree until you have researched all the previous items.
## Durability

All weapons and tools, including the rock, have a durability. Over time, usage causes the durability to go down, and eventually the item will break. However, the item will remain in the inventory and can be repaired using a Repair Bench. This will repair the item to full durability, but it will break faster each time it is repaired due to the fact that the maximum durability is limited each time it is repaired as shown below.
## Correct Usage of Tools

In Experimental Rust, using a tool that does not correspond with a resource will result in higher and more rapid durability loss. For example, using a Pick Axe with a mineral rock is normal, but using one on a tree would result in the Pickaxe breaking faster, as well as a less efficient rate of resource gathering. A clue that one may be using the wrong tool for the job is a high recoil when hitting the object, as well as a louder sound effect.
# Crafting

Crafting is executed through the inventory screen. There is a list of possible items to craft, each requiring a certain amount of different resources. Clicking on one of these items adds it to the crafting queue, where its crafting progress is shown on the bottom right of the screen. Different items have different crafting times.
Once the item you want to craft is selected via right-click, an info box shows above the inventory screen, just left of the crafting screen. This shows info like how long it will take to craft the item, how many of the item will be made, the resources required, and the description/icon of the item. You can also select how many of the item you want to craft, and confirm the crafting request to begin crafting.
The items available for crafting are sorted into categories for the convenience of the player. Most items are craft in between 2 - 20 seconds, with more complex items like guns and attachments taking up to a minute and a half.
# Building

Main Article: Building
Players can build their own shelters to protect them from threats and to store their possessions. A schematic can be crafted from one piece of paper, which can be crafted from wood. Hold Right click to select what type of wall/floor you wish to build. This allows you to place stick structures for a low cost of wood. To upgrade, rotate, or destroy what you have built, you must also make a wooden hammer out of 100 wood.
The ability to destroy structures with a hammer lasts only 24 hours, so it is wise to build as much as possible at once, in case you need to make edits. The ability to destroy placed walls is also lost if your teammate places a Tool Cupboard, on top of the structure you built. Once this ability is lost, structures must be destroyed manually with tools or explosives.
Without placing a Tool Cupboard (TC), your structure will degrade over time. Craft and place a tool cupboard in the safest point of your building, and then place resources inside to prevent decay as well as prevent building within a radius around your base (this does not prevent ladder placement). It is wise to put a key lock or code lock on your TC to prevent theft.
## Decay

Main Article: Decay
Decay is a natural process that causes structures to slowly lose health and eventually collapse after a certain period of time. It helps clear out unused bases, and also acts as an incentive to make the player check back, and play Rust more often. Decay can be repaired, and can also be prevented. Cost of decay is determined by the size of your base as well as what your base is made of, and can be viewed be accessing the inventory of your TC. See the decay main page for more info.
Pro Tip: Degrading bases can be a great source of resources that have been left abandoned, but beware of turrets!
# Raiding

Main Article: Raiding
Raiding is an offensive process of players breaking and entering other players' bases in an attempt to either take loot, physically alter the base or conquer it, or kill any residing occupants inside.
# Vehicles

Currently, there's only 3 Vehicle in the game. They are divided into two categories -Released and Experimental(But still can be spawn by using console command)
Released Vehicle
Boat (Need a wikia page) (Information from rustafield)
Experimental Vehicle
Car
CH47 Chinook (Need a wikia page) (Information from rustafield)
# Guide Videos

 TLDR on Healing, Bleeding, & Revival in Rust 
Mechanics
Attack
Damage Types • Projectiles
Environment
Animals • Barrels • Biomes • Flora • Loot Crates • Monuments • Rocks • Trees
Gameplay
Attack Helicopter • Airdrops • Building • Combat • Crafting • Gathering • Raiding • Repairing • Researching
Player
Food & Hunger • Health • Hydration & Thirst • Protection • Sleeping • Spawning
XP System
Experience • Skill Tree • Tech Tree
Status Effects
Bleeding • Building Privilege • Comfort • Injured • Poisoning • Radiation • Starvation & Dehydration • Warmth • Wet & Drowning • Wounded

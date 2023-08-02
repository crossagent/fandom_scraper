# Update 2018-01-01 Build:25211

Devblog 196
Mini Water Well Monuments
Added hilltop rocks
New network interpolation and extrapolation
AI no longer ghost through fences and other transparent walls
AI no longer ghost through barricades
Fixed an ice lake exploit that allowed people build near trucks
Fixed Hapis floating barrels at Site A
Fixed spawning in the ocean on Savas
Military Tunnels Level Design Refresh
Added recycler to Savas KOTH
Ak47 admire animation
Double shotgun admire animation
Eoka admire animation
Mp5 admire animation
Water bucket admire animation
Rock admire animation
Players no longer spawn on islands
Maps have significantly more cliffs and hills
Rivers have a nicer color
EAC SDK update
Monuments no longer spawn on islands
Reduced player tick delay (peeker's advantage)
Removed wood cost from double sheet metal doors
Hapis old caves now have lighting
Hapis updated with new water well monuments
Updated Savas KOTH loot table with newly introduced items
Removed pillar building block
Added 10 tutorials
Added functional water wells
# Update 2015-04-09 Build:583540

Devblog 55
Added Camera.
Added Acoustic Guitar.
Added Wooden Barricade.
Added Metal Barricade.
Added Barbed Wooden Barricade.
Added F1 Grenade.
Added Grass Slider to adjust level of grass detail.
Fixed being able to loot players from a long distance (and when alive).
Fixed network toggle exploits.
Fixed instances where exceptions weren’t being reported properly.
Tweaked animal speeds.
Fixed decals sticking around forever.
Added admin teleport <name|steamid|nothing> (players only).
Added admin teleportany <name|steamid|entityname|nothing> (any entity).
Fixed chicken ragdoll using wolf colliders.
Limited where signs can be placed (to prevent lemming bridges).
Can place signs rotated.
Fixed sleeping bag placement exploits.
Fixed vitals sometimes not showing.
Fixed items ejected from furnace/campfire/storagebox falling through the world.
Fixed bleeding notification not showing.
Fixed queued damage effects sometimes showing after respawn.
Fixed decals on OSX rendering pink.
Added Camp Fire sit animation.
Added leaning to animation while running in an arc.
Fixed Texture tearing near waters edge.
Your player will no longer uncrouch if there isn’t any head clearance.
Assault Rifle was nerfed – Less Rate of fire, more recoil.
All weapons had their ADS fov reduced, except for the bolt action which was increased.
Tracers were made thicker to correspond to the new texture they use.
Bandages are cheaper.
Metal Helmets (coffee, bucket, facemask ) protect less against bullet damage.
Metal Facemask & Body Plate cost much more.
Firearms are more expensive and have a wider cost gap between them.
Armored building parts cost waaay more & Stone building parts cost a bit more, making sheet metal more viable.
Disabled PVT by default as some people were having issues with it and it only improves performance for some people.
The setting is still saved, you just have to manually enable it in case it improves performance for your specific hardware.
Rocks now use less memory by properly cleaning up their child objects.
Added LOD multiplier to grass system. (Used by the grass quality slider.)
Mountains are no longer placed partially outside of the world and better blend with the terrain.
Monuments now use a similar terrain blending system as mountains, which will allow artists more control over the surrounding terrain in future radtowns.
The poles next to roads now switch side if one side of the road is blocked.
Bridge placement and road network generation got another set of improvements.
The terrain resolution is now 1 vertex per world unit, which will be the resolution of the upcoming custom map.
Fixed some grass placement weirdness on certain terrain blended rocks.
Ores spawn in smaller clusters again for a more even distribution.
Reduced the number of overhang rocks that are placed on beaches.
Added a few models for dropped items.
# Update 7.04.13 #1

Melee changes:
• Added Pick Axe - A slower version of the hatchet that mines resources faster, but skins animals much slower• Added rudimentary impact effect system• Things that aren't supposed to cause bleeding should no longer bleed when hit with melee weapons• Redid gathering logic• Hatchet should gather from static trees every 3 blows consistently• Lowered melee range, you need to crouch to hit the ground nowBR KRL
LOD Changes:• Added a ton of LOD'ing to the structure components which should make the game run faster in some placesPlease note; the LOD changes are not set up to be seamless yet and happen at the wrong distance so you will notice some popping when approachng buildings
# Update 7.03.13 #2

Cooking/Smelting:- Fixed a bug where cooking may not work- Wood no longer needs to be the first item in a campfire for cooking to take place
Doors:- doors should now properly serialize their state ( being open or not )- doors should now properly position themselves from level reload.
Chat:- colors are now illegal- using a '<' followed by a '>' is now illegal- using \n or \t is now illegal- illegal messages wont send.- names with illegal character sequences in them will not be able to connect.
Administration:- tuned detection- reset ban log
Administration:- tuned detection
- reset ban log
# Update 7.03.13 #1

Chat:- character limit in chat- message flood protection- no more need to manually scroll down after multi-lined chat messages expire.
Options:- fixed missing textures for options.- new look to options, matches the ui used in other parts of the game.- simplified graphics tab.
Context Menu (campfire/fire barrel):- less glitchy dongr movement- ui matches rest of the game.
Connecting/Disconnecting:- When connection fails due to 'Could not reach server', 'Timeout to connect to server', or 'Player count limit reached' the webplayer will reattempt to connect every 10 seconds there after.- The disconnect messages now properly show the reason why you were disconnected ( in most cases )
Administration:- added banning system- we keep a log of kick's that occur- lightened and tuned detection for banning- unbanned users which may have been banned for false detection
General:- accounts which contain color codes in the display name are no longer allowed to play.
# Update 6.30.13

Balance changes:
• Slightly increased wood you earn from regular trees• Added gunpowder as a default blueprint• Lowered headshot multiplier slightly for zombies ( they all die in one headshot except the black one takes two)• Rebalanced door health
Bug fixes:
• Fixed collision box on structure walls• You should no longer be able to kill yourself with a blood draw kit• Fixed item duplication when lagging out• Fixed spawning multiple objects when lagging out• You can no longer place deployables through tiny cracks in peoples houses (like sleeping bags...)• Item mods will no longer remove the item they are being placed on• Item mods will no longer exist after being placed on an item• You will no longer waste paper by trying to re-research an item that you already know how to craft• Fixed losing blueprints in some cases• Fixed losing slots/stacksize upon death• Fixed grenades not colliding with doors under some conditions• Fixed grenades not dealing damage to doors; it should take about 8 now
Improvements:
• You now spawn at your most recently placed sleeping bag• Default items are placed in the proper belt slots• Adjusted item descriptions to represent the current methods of using them• You can no longer place structure foundations in mid air, they must be touching terrain• Staggered wildlife calculations, this should prevent some server hiccups• Fixed lag when inventory changes often (shooting rapid fire caused hiccups on some machines)• Adjusted some of the wood structure models to be lower poly• Updated hatchet and flare textures• Added distance culling to players and zombies; this should result in higher fps in some cases• Many more spawnpoints, and spawns are now further apart
# Update 8.2.13

• Structures now take 5 days to decay• Flashlights now illuminate the player holding them• Adjusted weapon fire audio, it should be more apparent how far away things are now• Added distant sounds for weapons• Added Silencer functionality! Short sound distance, no muzzle flash, minor recoil reduction, damage reduction• Tracers are now smaller, move faster, and aren't always the same size• Anisotropic textures set to by texture instead of forced on (performance improvement)• Fixed bug with recoil bonuses from aiming and crouching not stacking
Silencer changes :-35% range-25% damage-10% recoil
LODBias reset to 1 for all quality levels
# Update 8.1.13

• You can no longer place structures too close to each other• Placing structures should be easier visually (you'll always see the component, j• Resource repair now displays proper values indicating how much was actually repaired• You can no longer stack foundations on foundations• You can now repair doors (Thanks Xant )
# Update 7.27.13

• Deployables and structures decay over time (12–24 hours) to prevent server overload.• Objects can be repaired by pressing a key with the correct resource while aiming at the damaged object.• Ramps can be placed on ceilings to allow angled roofs.• Foundations can no longer be placed on top of foundations.• P250 rebalanced to be more useful.
# Update 7.12.13

• All building parts except Foundation, Pillar, and Ceiling are now destroyable!• Added Explosive Charge item, easily takes down a door but very difficult to craft• Added Kevlar Pants, Kevlar Shoes• Added Radiation suit armor• Rebalanced all armor stats
• You can only build foundations on Terrain• You can no longer stack wooden boxes (temporary fix)• Fixed M4 holosight clipping the near plane when firing in ADS mode• Grenades should no longer bounce erratically• Grenades are slightly easier to construct• You can now see the damage to walls by the shade of their color (darker = more damaged )• Doors now leave a 'corpse' which lasts for 5 minutes. You can not place a door ontop of a door corpse (Should make it slightly harder to defend )• Sleeping bags now have a 4 minute cooldown ( Should make it harder to zerg attack a base )• Fixed alpha channel on some icons• Barricades are now higher to prevent jumping over them• Ceilings should be easier to place when under the target spot• Radiation armor will lower the screenspace effect but you'll still hear the geiger counter indicating the radiation level in the area• Melee weapons now properly grab the right impact effect if the target object uses hitboxes• Destroyed building components have a death effect• Metal doors are significantly harder to craft
# Update 7.05.13

• System upgrade: wipes should now happen less frequently.• Door skips an optimization check which could have been why the previous fix did not fix them.• Night is now shorter than day.
# Update 7.04.13 #3

• Fixed sleeping bag deploy rotation• Fixed some icons being mipped at low quality settings• Fixed campfire collision being too large
• Added small stash blueprint• Added Wood Planks - All structure require these now• Added Metal Door - Does not take melee damage• Added Wood Shelter - Easy to make, serves the same purpose as a 1x1 house
• You can no longer stack Barricades• You can no longer jump over Barricades• You can no longer stack many doors together• You can no longer get infinite wood from trees.. If it runs out, move to the next one• You can no longer deploy items while jumping• You can no longer use the sleeping bag to glitch into peoples houses
• "/do unstick" should now work when locked in a 'jail'• Walls can now be placed even if a pillar is blocking them
# Update 7.04.13 #2

• Hatchet uses half the calories it used to• Pickaxe gathers 25% less wood than it used to• Fixed Pickaxe blueprint naming• Fixed missing Pickaxe icon• Fixed random spawns in the ocean
# Update 7.04.13 #1

Melee changes :
• Added Pick Axe - better, slower version of hatchet• Added rudimentary impact effect system• Things that aren't supposed to should no longer bleed when hit with melee weapons• Redid gathering logic• Hatchet should gather from static trees every 3 blows consistently• Pickaxe gathers everything faster except animal corpses• Lowered melee range, You need to crouch to hit the ground now
LOD Changes :• Added a tonne of LOD'ing to the structure components which should make the game run faster in some placesPlease note; the LOD changes are not set up to be seamless yet and happen at the wrong distance so you will notice some popping when approaching buildings
# Update 7.03.13 #2

Cooking/Smelting:- fixed cooking some times not working- processes unique ingredients ( with unique cooked item output ) per cook phase ( when wood is consumed )- no more need to have wood be the first thing in the inventory of the cooker.
Doors:- doors should now properly serialize their state ( being open or not )- doors should now properly position themselves from level reload.
Chat:- colors are now illegal- using a '<' followed by a '>' is now illegal- using \n or \t is now illegal- illegal messages wont send.- names with illegal character sequences in them will not be able to connect.
Administration:- tuned detection- reset ban log
Administration:- tuned detection
- reset ban log
# Update 7.03.13 #1

Chat:- character limit in chat- message flood protection- no more need to manually scroll down after multi-lined chat messages expire.
Options:- fixed missing textures for options.- new look to options, matches the ui used in other parts of the game.- simplified graphics tab.
Context Menu (campfire/fire barrel):- less glitchy with movement- ui matches rest of the game.
Connecting/Disconnecting:- When connection fails due to 'Could not reach server', 'Timeout to connect to server', or 'Player count limit reached' the webplayer will reattempt to connect every 10 seconds there after.- The disconnect messages now properly show the reason why you were disconnected ( in most cases )
Administration:- added banning system- we keep a log of kick's that occur- lightened and tuned detection for banning- unbanned users which may have been banned for false detection
General:- accounts which contain color codes in the display name are no longer allowed to play.

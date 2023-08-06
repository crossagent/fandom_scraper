# Client Commands


## Client Commands

Command
Description
find *
Lists all commands
gfx.ssaa true/false
Enables or disables screen space anti-aliasing.
gfx.grain true/false
Enables or disables radiation grain effect
gfx.shafts true/false
Enables or disables sun shafts
gfx.damage true/false
Enables or disables damage indicators
grass.on true/false
Enables or disables grass; Improves FPS for some
grass.displacement true/false
Enables or disables grass displacements.
gui.show
Turns the ui on.
gui.hide
Turns the ui off.
gui.show_branding
Turns the branding ui in top-right corner on.
gui.hide_branding
Turns the branding ui in top-right corner off.
net.connect "Server IP"
Connect to a direct server IP.
net.disconnect
Disconnects from a server.
net.reconnect
Reconnect to the last server you were on.
censor.nudity true/false
Disabled censorship.
kill
Kills your character allowing for a respawn.
terrain.idleinterval 0-100
Sets how often to draw unseen terrain; setting to 0 will disable.
quit
Quits the game.
## Server Commands

Note: You must be signed in using the correct RCON password to use these commands.
Command 
Description 
rcon.login password
Use your 'Password' to login into Rcon via in-game console (F1).
rcon.password "password"
Setup Rcon password.
status
See which players are currently connected to the server.
notice.popupall "message"
Sends a notice to everyone in the server. It will pop up in the top-middle of the screen.
say "message"
Sends a chat message as "SERVER CONSOLE" just like every other player.
find *
Lists available console commands.
kick "player"
Kicks player from the server.
ban "player" or "steamid"
Bans player. You still must kick them from the server.
banid "steamid" "reason"
Bans a steamid from the server.
removeid "steamid"
Unbans "steamid".
unbanall
Unbans all players.
banlist
List all the steam ID's that you have banned.
banlistex
List all the steam ID's that you have banned with ban reasons and names (if you added in extra info upon ban)
truth.enforce true/false
Server kicks people automatically when they are potentially hacking.
save.all
Saves world map and player inventory.
save.autotime **
Sets how often your server will perform an auto-save in seconds. (600 Default)
teleport.toplayer "player 1" "player 2"
Teleports 'player 1' to 'player 2'. Case sensitive. Full name required.
teleport.topos "player" "Pos X" "Pos Y" "Pos Z"
Teleports 'player 1' to the coordinates. Full name required.
inv.giveplayer "player" "item" "amount"
Gives 'Player' the 'Item'. Full name and Item name required.
inv.giveall "item" "amount"
Gives all players 'Item'. Full Item name required.
dmg.godmode true/false
Gives all logged in admins god-mode.
crafting.complete
Completes every single crafting job in progress for everyone.
crafting.cancel
Cancels every single crafting job in progress for everyone.
crafting.instant true/false
Sets crafting to be instant for everyone.
crafting.instant_admins true/false
Sets crafting to be instant for logged in admins only.
crafting.timescale "amount"
Sets the timescale of crafting to 'amount' (1 = default, 0.5 = half time).
conditionloss.damagemultiplier "amount"
Sets the time it takes for used items to lose durability. (1 = default, 0.0 = no durability loss)
conditionloss.armorhealthmult "amount"
Sets the time it takes for items to break from taking damage. (.25 = default, 0.0 = no durability loss)
airdrop.drop
Starts an airdrop.
airdrop.min_players "amount"
Starts airdrops only when minimum X players are online.
server.hostname
Sets a hostname.
server.clienttimeout "time"
Sets the time until someone times out. Good to fight item glitchers. (Default 2 minutes)
server.maxplayers "amount"
Sets maximum amount of server slots.
server.pvp true/false
Sets PVP on or off.
server.steamgroup "steamgroup ID"
Makes people only able to join the server when they are in that steamgroup
sleepers.on true/false
Sets sleepers on or off.
env.timescale "amount"
Sets the passage of time (day/night cycle) to a certain speed, default is "0.0066666667".
env.time "amount"
Sets the time of day to a specified value. A value of 12 is noon.
env.daylength "amount"
Sets how long daytime will last. (45 Default)
env.nightlength "amount"
Sets how long nighttime will last. (15 Default)
falldamage.enabled true/false
Turns fall damage on or off.
cheaters.log true/false
Logs joining cheaters in the remote console
player.backpackLockTime "amount"
Set the locktime from the Backpack (0 = OFF)(300 = 5min)

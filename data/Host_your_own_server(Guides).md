# Installing SteamCMD

SteamCMD is the essential tool for installing the Rust Server. To install it, follow the first part of the guide and copy & paste this script into a .bat file:
C:\steamCMD\steamcmd.exe +login anonymous +force_install_dir C:\Users\User\Desktop\MyRustServer +app_update 258550 +quit
# Updating and starting your server

Here's the script that updates and starts your server, make sure to fill in the blanks correctly:
C:\steamCMD\steamcmd.exe +login anonymous +force_install_dir +app_update 258550 +quit
RustDedicated.exe -batchmode +server.hostname "Servername" +server.identity servername +server.maxplayers 50 +server.port 28015 +rcon.port 28016 +rcon.password 0123456+server.worldsize 4000 +server.description"Description"

# General binds

To check whether a key is already bound to something try this command:
bind z
if it returns ie. chat.say /stophorse it means that the key already has a bind. Trying the same on a key that isn't bound to anything:
bind p
it will return (nothing)
# Binds for PvE

Sometimes on some PvE servers there are various menus that pop up after you type /info or /event etc. You can bind these commands to keys so it is easier to access them.
As an example on modded servers with mountable horses you can stop a horse with /stophorse though the time it takes open the chat and type that command may cause the horse to run away and you missing the opportunity to get on it. If you bind "/stophorse" to a key it will be way easier to stop and mount it.
Type the following after hitting F1 to open the console
bind z chat.say /stophorse
You can use the same style to bind various modded commands, ie. on some servers you can get godmode or fly mode, so if you wanted to fly whenever you pressed n and activate godmode whenver you pressed m do the following after opening the console with the keyboard key F1:
bind n chat.say /noclip
and
bind m chat.say /god
would be able to help you to quickly just push m or n to toggle between godmode and noclip mode

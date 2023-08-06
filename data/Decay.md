# No Decay Servers

Some servers (mostly low population) like to opt out of the decay system to make the game more friendly to new players / roleplayers / casuals. These servers usually associate with other friendly tags such as PVE, FRIENDLY COMMUNITY, NO KOS, NO HELI, ANTI - GRIEF.
# Repairing Decay

If a certain part of your base has been partly decayed, then you need to repair it with the resource used to create it. Metal Fragments fix metal structures, Wood fixes wood structures, and so on. To repair, take the Hammer tool, and ensure you have the relevant resources in your inventory. Hit the structure by left clicking, and on each successful hit, the health of the structure will visibly and physically increase until it is repaired fully. If a structure has already collapsed, it is not repairable and must be rebuilt.
# Preventing Decay

Main Article: Tool Cupboard
Decay is prevented by building a Tool Cupboard and filling it with materials which are consumed over time.
## Decay Timers

Material: TwigTime to Decay: 1 hours
Material: WoodTime to Decay: 3 hours
Material: StoneTime to Decay: 5 hours
Material: Sheet MetalTime to Decay: 8 Hours
Material: ArmouredTime to Decay: 12 hours
# Server Settings (Legacy)

There were two server variables that were relevant for controlling the decay speed of structures in Legacy:
decay.decaytickrate (default 300)
This controls the interval in which all outstanding decay on the server is performed. The faster (shorter) the interval, the more often decay is applied to structures.
decay.deploy_maxhealth_sec (default N/A)
Maxhealth controls how much damage will be dealt per second. However, the values for these variables are not straight forward to set. Changing the decay time of structures should be done by changing the deploy_maxhealth_sec setting. Changing decaytickrate is only necessary if there are too many structures on the server that cause lag every time the damage is applied.
To estimate the time a structure needs to decay with given decay settings the following formula can be used:
Damager per Time unit = Structure Max Health / (deploy_maxhealth_sec / decaytickrate)
This can be used to calculate the amount of time needed for an untouched structure to fully decay:
Days until complete decay = Structure Max Health / (Damage per Time unit / decaytickrate) / 60 / 60 / 24
Example
deploytickrate = 300masmis
deploy_maxhealth_sec = 432500
This setting will result in the decay of a normal 1000 hp Wood Wall
1000 hp / (432500 hp / 300 s) = 1000 hp / 1441.66 parts of hp per 300 seconds = 0.6936448261 hp per 300 seconds
1000 hp / (0.6936448261 hp per 300 seconds / 300 seconds) / 60s / 60m / 24h = 1000 hp / 0.00231214942 hp/s / 60s / 60m / 24h
= 432498 s / 60s / 60m / 24h = 5 days until 100% decay
With the above settings a standard 1000 hp Wooden Wall will take 5 days until is has decayed completely and take 0.693645 hp damage every 300 / 60 = 5 minutes after 24 hours of idle.
This graph will show the decay time in days by deploy_maxhealth_sec with deploytickrate at 300 for a structure with 1000 hp (e.g. Wood Wall).
 

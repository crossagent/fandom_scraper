# Server Commands

Syntax: admin.mutevoice "player"Shorthand: Description: Notes: 
Syntax: admin.unmutevoice Shorthand: Description: Unmute a players or admins in-game capability of speakingNotes: 
Syntax: admin.mutechat "player"Shorthand: Description: Mute a players in-game capability of speaking in the in-game chatNotes: 
Syntax: admin.unmutechat "player"Shorthand: Description: Unmute a players in-game capability of speaking in the in-game chatNotes: 
Syntax: global.statusShorthand: statusDescription: Print out currently connected clients etcNotes: Only available for admins nowadays.
Syntax: global.kick "player"Shorthand: kick "player"Description: Kick a player/AdminNotes: 
Syntax: global.kickallShorthand: kickall "reason"Description: Kick everyone in the gameNotes: 
Syntax: global.ban "player"Shorthand: ban "player"Description: Banish a player/AdminNotes: 
Syntax: global.moderatorid "SteamID"Shorthand: moderatorid "SteamID"Description: Make a player moderatorNotes: AuthLevel 1, (Moderator)
Syntax: global.ownerid "SteamID"Shorthand: ownerid "SteamID"Description: Make a player/moderator ownerNotes: AuthLevel 2, (Admin)
Syntax: global.removemoderator "SteamID"Shorthand: removemoderator "SteamID"Description: Remove a moderatorNotes: 
Syntax: global.removeowner "SteamID"Shorthand: removeowner "SteamID"Description: Remove an ownerNotes: 
Syntax: global.banid "SteamID"Shorthand: banid "SteamID"Description: on descriptionNotes: 
Syntax: global.unban "SteamID"Shorthand: unban "SteamID"Description: no descriptionNotes: 
Syntax: global.playersShorthand: playersDescription: Print out currently connected clients etcNotes: 
Syntax: global.say "text"Shorthand: say "text"Description: Sends a message in chatNotes: 
Syntax: global.users( )Shorthand: usersDescription: Show user info for players on server.Notes: 
Syntax: global.banlistShorthand: banlistDescription: List of banned users (sourceds compat)Notes: 
Syntax: global.banlistex( )Shorthand: banlistexDescription: List of banned users - shows reasons and usernamesNotes: 
Syntax: global.listid( )Shorthand: listidDescription: List of banned users, by ID (sourceds compat)Notes: 
Syntax: chat.say "text"Shorthand: chat.say "text"Description: Prints your text in the chat e.g "t0kenz: Hello"Notes: 
Syntax: draft.add( void )Shorthand: Description: no descriptionNotes: 
Syntax: craft.canceltask( void )Shorthand: Description: no descriptionNotes: 
Syntax: craft.cancel( void )Shorthand: Description: no descriptionNotes: 
Syntax: data.export( void )Shorthand: Description: no descriptionNotes: 
Syntax: entity.debug_toggle( void )Shorthand: Description: no descriptionNotes: 
Syntax: entity.nudge( void )Shorthand: Description: no descriptionNotes: 
Syntax: env.addtime( void )Shorthand: Description: no descriptionNotes: 
Syntax: event.run( void )Shorthand: Description: no descriptionNotes: 
Syntax: gc.collect( void )Shorthand: Description: no descriptionNotes: 
Syntax: global.restart( )Shorthand: restartDescription: Restart the server - with 300 seconds warning at 5 second intervals.Notes: 
Syntax: global.quit( )Shorthand: quitDescription: Leave the gameNotes: 
Syntax: global.report( void )Shorthand: reportDescription: no descriptionNotes: 
Syntax: global.objects( void )Shorthand: objectsDescription: no descriptionNotes: 
Syntax: global.textures( void )Shorthand: texturesDescription: no descriptionNotes: 
Syntax: global.colliders( void )Shorthand: collidersDescription: no descriptionNotes: 
Syntax: global.error( void )Shorthand: errorDescription: no descriptionNotes: 
Syntax: global.queue( void )Shorthand: queueDescription: no descriptionNotes: 
Syntax: global.setinfo( void )Shorthand: setinfoDescription: no descriptionNotes: 
Syntax: global.sleep( void )Shorthand: sleepDescription: no descriptionNotes: 
Syntax: global.kill( void )Shorthand: killDescription: Suicide commandNotes: Used for respawning
Syntax: global.respawn( void )Shorthand: respawnDescription: no descriptionNotes: 
Syntax: global.injure( void )Shorthand: injureDescription: no descriptionNotes: 
Syntax: global.spectate( void )Shorthand: spectateDescription: no descriptionNotes: 
Syntax: global.respawn_sleepingbag( void )Shorthand: Description: no descriptionNotes: 
Syntax: global.respawn_sleepingbag_remove( void )Shorthand: Description: no descriptionNotes: 
Syntax: global.teleport( void )Shorthand: teleport "name"Description: no descriptionNotes: 
Syntax: global.teleport2me( void )Shorthand: teleport2me "name"Description: no descriptionNotes: 
Syntax: global.teleportany( void )Shorthand: teleportany "bear, deer.."Description: no descriptionNotes: 
Syntax: hierarchy.ls( void )Shorthand: Description: no descriptionNotes: 
Syntax: hierarchy.cd( void )Shorthand: Description: no descriptionNotes: 
Syntax: hierarchy.del( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.endloot( void )Shorthand: Description: on descriptionNotes: 
Syntax: inventory.give( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.giveall( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.givebpall( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.giveto( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.giveid( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.givearm( void )Shorthand: Description: no descriptionNotes: 
Syntax: inventory.givebp( void )Shorthand: Description: no descriptionNotes: 
Syntax: pool.status( void )Shorthand: Description: no descriptionNotes: 
Syntax: pool.clear( void )Shorthand: Description: on descriptionNotes: 
Syntax: server.start( )Shorthand: Description: Starts a serverNotes: 
Syntax: server.stop( string DisconnectMessage )Shorthand: Description: Stops a serverNotes: 
Syntax: server.backup( )Shorthand: Description: Backup server folderNotes: 
Syntax: server.writecfg( )Shorthand: writecfgDescription: Writes config filesNotes: 
Syntax: server.fps( void )Shorthand: Description: no descriptionNotes: 
Syntax: server.save( )Shorthand: saveDescription: Force save the current gameNotes: 
Syntax: server.readcfg( void )Shorthand: Description: no descriptionNotes: 
Syntax: spawn.fill_populations( void )Shorthand: Description: no descriptionNotes: 
Syntax: spawn.fill_groups( void )Shorthand: Description: no descriptionNotes: 
Syntax: weather.clouds( void )Shorthand: Description: no descriptionNotes: 
Syntax: weather.fog( void )Shorthand: Description: no descriptionNotes: 
Syntax: weather.wind( void )Shorthand: Description: no descriptionNotes: 
Syntax: weather.rain Shorthand: Description: Sets the rain factor where 0 is none and 1.0 is 100%.Notes: Using anything other than a valid value will set it to "auto".
Syntax: world.monuments( void )Shorthand: Description: prints pos of all monuments and caves to consoleNotes: DISABLED
Syntax: global.dump( void )Shorthand: Description: dump server diagnostics to Notes: 
Syntax: global.find( string Name )Shorthand: Description: Search for a commandNotes: 
Syntax: global.echo( string output )Shorthand: Description: Prints something to the debug outputNotes: 
Syntax: airdrop.drop( void )Shorthand: Description: no descriptionNotes: 
Syntax: cui.test( void )Shorthand: Description: no descriptionNotes: 
Syntax: global.ent killShorthand: ent killDescription: Destroys/kills the entity you're targeting (looking at)Notes: Useful binding for admins:bind q “ent kill”
Syntax: global.ent lockShorthand: ent lockDescription: locks the sign/painting you're targeting (looking at)Notes: 
Syntax: global.ent unlockShorthand: ent unlockDescription: unlocks the sign/painting you're targeting (looking at)Notes: 
# Server Variables

Syntax: aianimation.groundorientDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: aianimation.speedscaleDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: aianimation.qualitydistanceDescription: no descriptionDefault: 100Range: Notes: 
Syntax: lerp.enabledDescription: Enables interpolation on network positionsDefault: TrueRange: BooleanNotes: 
Syntax: lerp.smoothingDescription: The higher this value the more post process smoothing applied. 0 = accurate, 1 = smoothDefault: 0.5Range: 0 - 1.0Notes: 
Syntax: lerp.timeDescription: How many seconds behind to lerp. 0 is the most accurate but can be the most jitteryDefault: 0.1Range: Notes: 
Syntax: ai.thinkDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: ai.moveDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: ai.sensetimeDescription: no descriptionDefault: 1Range: Notes: 
Syntax: antihack.enabledDescription: is antihack enabled at allDefault: TrueRange: BooleanNotes: 
Syntax: antihack.userlevelDescription: 0 == users, 1 == admins, 2 == developersDefault: 0Range: 0 - 2Notes: 
Syntax: antihack.enforcementlevelDescription: 0 == no enforcement, 1 == kick, 2 == ban (DISABLED)Default: 0Range: 0 - 2Notes: 
Syntax: antihack.relaxationrateDescription: the rate at which violation values go back downDefault: 0.1Range: Notes: 
Syntax: antihack.relaxationpauseDescription: the time before violation values go back downDefault: 5Range: Notes: 
Syntax: antihack.maxviolationDescription: violation value above this results in enforcementDefault: 5Range: Notes: 
Syntax: antihack.noclip_protectionDescription: 0 == disabled, 1 == raycast, 2 == spherecastDefault: 2Range: 0 - 2Notes: 
Syntax: antihack.noclip_rejectDescription: whether or not to reject movement when noclip is detectedDefault: TrueRange: BooleanNotes: 
Syntax: antihack.noclip_penaltyDescription: violation penalty to hand out when noclip is detectedDefault: 4Range: Notes: 
Syntax: antihack.speedhack_protectionDescription: 0 == disabled, 1 == enabledDefault: 1Range: Notes: 
Syntax: antihack.speedhack_rejectDescription: whether or not to reject movement when speedhack is detectedDefault: FalseRange: BooleanNotes: 
Syntax: antihack.speedhack_penaltyDescription: violation penalty to hand out when speedhack is detectedDefault: 4Range: Notes: 
Syntax: antihack.speedhack_forgivenessDescription: speed threshold to assume speedhacking, lower value = more false positivesDefault: 2Range: Notes: 
Syntax: antihack.speedhack_deltatimeDescription: time interval to calculate speed in, lower value = more false positivesDefault: 0.2Range: Notes: 
Syntax: antihack.speedhack_ticketsDescription: required number of speeding tickets to trigger a violationDefault: 15Range: Notes: 
Syntax: antihack.speedhack_historyDescription: speeding ticket history lengthDefault: 20Range: Notes: 
Syntax: antihack.flyhack_protectionDescription: 0 == disabled, 1 == simple, 2 == advancedDefault: 1Range: 0 - 2Notes: 
Syntax: antihack.flyhack_rejectDescription: whether or not to reject movement when flyhack is detectedDefault: FalseRange: BooleanNotes: 
Syntax: antihack.flyhack_penaltyDescription: violation penalty to hand out when flyhack is detectedDefault: 4Range: Notes: 
Syntax: antihack.flyhack_forgivenessDescription: distance threshold to assume flyhacking, lower value = more false positivesDefault: 2Range: Notes: 
Syntax: antihack.debuglevelDescription: 0 == silent, 1 == print max violation, 2 == print every violationDefault: 1Range: 0 - 2Notes: 
Syntax: audio.masterDescription: VolumeDefault: 1Range: Notes: 
Syntax: audio.musicDescription: VolumeDefault: 1Range: Notes: 
Syntax: audio.gameDescription: VolumeDefault: 1Range: Notes: 
Syntax: audio.voiceDescription: VolumeDefault: 1Range: Notes: 
Syntax: audio.speakersDescription: VolumeDefault: 2Range: Notes: 
Syntax: chat.enabledDescription: Enable or disable chat displayingDefault: TrueRange: BooleanNotes: 
Syntax: chat.serverlogDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: construct.frameminutesDescription: How many minutes before a placed frame gets destroyedDefault: 30Range: Notes: 
Syntax: craft.instantDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: decay.scaleDescription: no descriptionDefault: 1Range: Notes: 
Syntax: decay.debugDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: env.timeDescription: Time of day. 12 is midday.Default: 12Range: 0 - 24.0Notes: 
Syntax: env.dayDescription: DayDefault: 26Range: Notes: 
Syntax: env.monthDescription: MonthDefault: 5Range: Notes: 
Syntax: env.yearDescription: YearDefault: 2024Range: Notes: 
Syntax: file.timeDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: fps.limitDescription: The maximum number of frames to render per secondDefault: 256Range: Notes: 
Syntax: fps.graphDescription: no descriptionDefault: 0Range: Notes: 
Syntax: global.developerDescription: no descriptionDefault: 0Range: Notes: 
Syntax: global.safemodeDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: global.debugmodeDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: global.warmupDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: global.censornudityDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: global.perfDescription: no descriptionDefault: 0Range: Notes: 
Syntax: global.godDescription: If you're an admin this will enable god modeDefault: TrueRange: BooleanNotes: 
Syntax: global.skincolDescription: If you're an admin you can change your skin colour using this variable (0-1)Default: -1Range: Notes: 
Syntax: global.skintexDescription: If you're an admin you can change your skin texture using this variable (0-1)Default: -1Range: Notes: 
Syntax: global.skinmeshDescription: If you're an admin you can change your head mesh using this variable (0-1)Default: -1Range: Notes: 
Syntax: graphics.shadowlightsDescription: no descriptionDefault: 1Range: Notes: 
Syntax: graphics.drawdistanceDescription: no descriptionDefault: 2500Range: Notes: 
Syntax: graphics.fovDescription: no descriptionDefault: 75Range: Notes: 
Syntax: graphics.hudDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: graphics.chatDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: graphics.brandingDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: graphics.dofDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: graphics.qualityDescription: The currently selected quality levelDefault: 0Range: Notes: 
Syntax: graphics.shadowdistanceDescription: no descriptionDefault: 100Range: Notes: 
Syntax: graphics.lodbiasDescription: no descriptionDefault: 0.5Range: Notes: 
Syntax: graphics.shaderlodDescription: no descriptionDefault: 2147483647Range: Notes: 
Syntax: graphics.uiscaleDescription: no descriptionDefault: 1Range: Notes: 
Syntax: graphics.afDescription: no descriptionDefault: 0Range: Notes: 
Syntax: graphics.parallaxDescription: no descriptionDefault: 0Range: Notes: 
Syntax: net.visdebugDescription: Turns on debug display of network visibilityDefault: FalseRange: BooleanNotes: 
Syntax: net.debugDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: net.logDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: physics.bouncethresholdDescription: no descriptionDefault: 2Range: Notes: 
Syntax: physics.sleepthresholdDescription: no descriptionDefault: 0.005Range: Notes: 
Syntax: physics.solveriterationcountDescription: The default solver iteration count permitted for any rigid bodies (default 7). Must be positiveDefault: 3Range: Notes: 
Syntax: physics.stepsDescription: The amount of physics steps per secondDefault: 30.003Range: Notes: 
Syntax: server.ipDescription: no descriptionDefault: Range: Notes: 
Syntax: server.portDescription: no descriptionDefault: 28015Range: Notes: 
Syntax: server.maxplayersDescription: no descriptionDefault: 200Range: Notes: 
Syntax: server.hostnameDescription: no descriptionDefault: Range: Notes: 
Syntax: server.identityDescription: no descriptionDefault: my_server_identityRange: Notes: 
Syntax: server.levelDescription: no descriptionDefault: Procedural MapRange: Notes: 
Syntax: server.seedDescription: no descriptionDefault: 8675309Range: Notes: 
Syntax: server.worldsizeDescription: no descriptionDefault: 4000Range: Notes: 
Syntax: server.saveintervalDescription: no descriptionDefault: 300Range: Notes: 
Syntax: server.secureDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: server.tickrateDescription: no descriptionDefault: 10Range: Notes: 
Syntax: server.entityrateDescription: no descriptionDefault: 16Range: Notes: 
Syntax: server.officialDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: server.globalchatDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: server.stabilityDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: server.radiationDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: server.npctickrateDescription: no descriptionDefault: 5Range: Notes: 
Syntax: server.itemdespawnDescription: no descriptionDefault: 180Range: Notes: 
Syntax: server.aihandlermsDescription: no descriptionDefault: 50Range: Notes: 
Syntax: server.pveDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: server.descriptionDescription: no descriptionDefault: No server description has been provided.Range: Notes: 
Syntax: server.headerimageDescription: no descriptionDefault: Range: Notes: 
Syntax: server.urlDescription: no descriptionDefault: Range: Notes: 
Syntax: server.eacDescription: no descriptionDefault: 1Range: Notes: 
Syntax: server.planttickDescription: Plants tick every x seconds. This is how many seconds between ticks.Default: 60Range: Notes: 
Syntax: server.planttickscaleDescription: Setting this to 2 will make plants grow, fruit and die two times faster than normal.Default: 1Range: Notes: 
Syntax: server.maxunackDescription: Max amount of unacknowledged messages before we assume we're congestedDefault: 4Range: Notes: 
Syntax: server.rootfolderDescription: no descriptionDefault: server/my_server_identityRange: Notes: 
Syntax: server.backupfolderDescription: no descriptionDefault: backup/0/my_server_identityRange: Notes: 
Syntax: server.backupfolder1Description: no descriptionDefault: backup/1/my_server_identityRange: Notes: 
Syntax: server.backupfolder2Description: no descriptionDefault: backup/2/my_server_identityRange: Notes: 
Syntax: server.backupfolder3Description: no descriptionDefault: backup/3/my_server_identityRange: Notes: 
Syntax: server.compressionDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: server.netlogDescription: no descriptionDefault: TrueRange: BooleanNotes: 
Syntax: spawn.min_rateDescription: no descriptionDefault: 0.1Range: Notes: 
Syntax: spawn.max_rateDescription: no descriptionDefault: 1Range: Notes: 
Syntax: spawn.min_densityDescription: no descriptionDefault: 0.1Range: Notes: 
Syntax: spawn.max_densityDescription: no descriptionDefault: 1Range: Notes: 
Syntax: terrain.qualityDescription: no descriptionDefault: 100Range: Notes: 
Syntax: terrain.pvtDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: time.fixeddeltaDescription: Fixed delta time in secondsDefault: 0.03333Range: Notes: 
Syntax: time.maxdeltaDescription: The minimum amount of times to tick per frameDefault: 0.33Range: Notes: 
Syntax: vis.damageDescription: Turns on debug display of damagesDefault: FalseRange: BooleanNotes: 
Syntax: vis.attackDescription: Turns on debug display of attacksDefault: FalseRange: BooleanNotes: 
Syntax: vis.metabDescription: Turns on debug display of metabolismDefault: FalseRange: BooleanNotes: 
Syntax: vis.triggersDescription: Show trigger entriesDefault: FalseRange: BooleanNotes: 
Syntax: voice.loopbackDescription: no descriptionDefault: FalseRange: BooleanNotes: 
Syntax: water.qualityDescription: no descriptionDefault: 0Range: Notes: 
Syntax: rcon.passwordDescription: no descriptionDefault: 1234Range: Notes: 
Syntax: rcon.portDescription: no descriptionDefault: 0Range: Notes: 
Syntax: rcon.ipDescription: no descriptionDefault: 127.0.0.1Range: Notes: 
Syntax: nametags.enabledDescription: no descriptionDefault: TrueRange: BooleanNotes: 
# External Links

Google Docs Spreadsheet detailing additional server commands and variables, by dudemanbroguy.
System
In-game
Cosmetic Items • Store
Server
Server Commands
Market
Market • Trading • Trading Cards • Workshop
Steam
Console Commands • Controls • HUD • In-game Settings

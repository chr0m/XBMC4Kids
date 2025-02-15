########################################################################################################################################
'''
	Script by Rocky5
	Used to update XBMC4Kids & migrate profiles
	
	Update: 10 December 2016
	-- Gets the xbe name dynamically now, this will allow installations to work with custom xbe names.
	-- Added some error handling.
	
	Update: 08 August 2016
	-- Added dynamic progress dialogues and improved the code.
'''
########################################################################################################################################


import os
import xbmcgui
import xbmc
import shutil
import time


########################################################################################################################################
# Start markings for the log file.
########################################################################################################################################
print "================================================================================"
print "| Scripts\Updater.py loaded."
print "| ------------------------------------------------------------------------------"
	

########################################################################################################################################
# Sets paths, for profiles names & locations.
########################################################################################################################################

# Gets current XBMC4Kids directory.
CharCount = 100 # How many characters you want after 'The executable running is: '
with open( xbmc.translatePath( "special://xbmc" ) + "xbmc.log", "r" ) as XBMCLOG:
	for line in XBMCLOG:
		left,sep,right = line.partition("The executable running is: ")
		if sep:
			Working_Directory = ( right[:CharCount] )
			Working_Directory = Working_Directory[:-20] # Removed Updater\default.xbe
			for XBE in os.listdir( Working_Directory ):
				if XBE.endswith( ".xbe" ):
					XBMC4KidsXBE = XBE

XBMC4Kids_Update_Path				= os.path.join( Working_Directory,"Updater\\Update Files\\" )
XBMC4Kids_Update_Path_Profiles		= os.path.join( XBMC4Kids_Update_Path,"UserData\\Profiles\\" )
Profiles							= os.path.join( Working_Directory,"UserData\\Profiles\\" )
pDialog								= xbmcgui.DialogProgress()
dialog								= xbmcgui.Dialog()
##

########################################################################################################################################
# Get list of directories and then parse them so I can id each directory then remove everything & then copy the new stuff over.
########################################################################################################################################
if os.path.isfile( os.path.join( Working_Directory, XBMC4KidsXBE ) ):

	dialog.ok( "XBMC4Kids Updater","","Welcome to the XBMC4Kids Updater","Press (A) to proceed with the update." )

	pDialog.create( "XBMC4Kids Updater" )

	if os.path.isdir( Profiles + "DVD2Xbox" ):
		shutil.rmtree( Profiles + "DVD2Xbox" )
	else:
		pass

	try:
		Profile_Directory = [x for x in os.listdir( Profiles ) if os.path.isdir( os.path.join( Profiles,x ) )]
	except:
		pass

	Header_Data = '<profiles>\n\
			<lastloaded>0</lastloaded>\n\
			<useloginscreen>true</useloginscreen>\n'
	Profile_Data = '			<profile>\n\
					<name>%s</name>\n\
					<directory pathversion="1">%s</directory>\n\
					<thumbnail pathversion="1">%s</thumbnail>\n\
					<hasdatabases>true</hasdatabases>\n\
					<canwritedatabases>true</canwritedatabases>\n\
					<hassources>true</hassources>\n\
					<canwritesources>true</canwritesources>\n\
					<useavpacksettings>false</useavpacksettings>\n\
					<lockaddonmanager>false</lockaddonmanager>\n\
					<locksettings>false</locksettings>\n\
					<lockfiles>false</lockfiles>\n\
					<lockmusic>false</lockmusic>\n\
					<lockvideo>false</lockvideo>\n\
					<lockpictures>false</lockpictures>\n\
					<lockprograms>false</lockprograms>\n\
					<lockmode>0</lockmode>\n\
					<lockcode>-</lockcode>\n\
					<lastdate>Has Never Logged In</lastdate>\n\
			</profile>\n'
	Footer_Data = '</profiles>'

	WriteXML = open( XBMC4Kids_Update_Path + "UserData\\Profiles.xml",'w' )

	WriteXML.write( Header_Data )
	ProfileMP = Profile_Data % ( "Manage Profiles","special://masterprofile/","special://masterprofile/Thumbnails/Profiles/ManageProfiles.tbn" )
	WriteXML.write( ProfileMP )
	ProfileD2X = Profile_Data % ( "DVD2Xbox","profiles/DVD2Xbox","special://masterprofile/Thumbnails/Profiles/DVD2Xbox.tbn" )
	WriteXML.write( ProfileD2X )

	try:
		if os.path.isdir( Profiles + Profile_Directory[0] ):
			Profile1 = Profile_Data % ( Profile_Directory[0],"profiles/" + Profile_Directory[0],"" )
			WriteXML.write( Profile1 )
		if os.path.isdir( Profiles + Profile_Directory[1] ):
			Profile2 = Profile_Data % ( Profile_Directory[1],"profiles/" + Profile_Directory[1],"" )
			WriteXML.write( Profile2 )
		if os.path.isdir( Profiles + Profile_Directory[2] ):
			Profile3 = Profile_Data % ( Profile_Directory[2],"profiles/" + Profile_Directory[2],"" )
			WriteXML.write( Profile3 )
		if os.path.isdir( Profiles + Profile_Directory[3] ):
			Profile4 = Profile_Data % ( Profile_Directory[3],"profiles/" + Profile_Directory[3],"" )
			WriteXML.write( Profile4 )
		if os.path.isdir( Profiles + Profile_Directory[4] ):
			Profile5 = Profile_Data % ( Profile_Directory[4],"profiles/" + Profile_Directory[4],"" )
			WriteXML.write( Profile5 )
		if os.path.isdir( Profiles + Profile_Directory[5] ):
			Profile6 = Profile_Data % ( Profile_Directory[5],"profiles/" + Profile_Directory[5],"" )
			WriteXML.write( Profile6 )
		if os.path.isdir( Profiles + Profile_Directory[6] ):
			Profile7 = Profile_Data % ( Profile_Directory[6],"profiles/" + Profile_Directory[6],"" )
			WriteXML.write( Profile7 )
		if os.path.isdir( Profiles + Profile_Directory[7] ):
			Profile8 = Profile_Data % ( Profile_Directory[7],"profiles/" + Profile_Directory[7],"" )
			WriteXML.write( Profile8 )
		if os.path.isdir( Profiles + Profile_Directory[8] ):
			Profile9 = Profile_Data % ( Profile_Directory[8],"profiles/" + Profile_Directory[8],"" )
			WriteXML.write( Profile9 )
		if os.path.isdir( Profiles + Profile_Directory[9] ):
			Profile10 = Profile_Data % ( Profile_Directory[9],"profiles/" + Profile_Directory[9],"" )
			WriteXML.write( Profile10 )
	except:
		pass


	WriteXML.write( Footer_Data )
	WriteXML.close()

	# Copy profile directories over.
	progress = 0
	pDialog.update( 0,"Removing Game Thumbnails","Processing" )
	for Items in os.listdir( Profiles ):
		CopyFrom	= os.path.join( Profiles, Items )
		CopyTo		= os.path.join( XBMC4Kids_Update_Path_Profiles, Items )
		progress += 1
		pDialog.update( int ( progress / float( len ( os.listdir( Profiles ) ) ) *100 ),"Copying Profiles",Items )
		if os.path.isdir( CopyFrom ):
			try:
				shutil.copytree( CopyFrom, CopyTo )
			except:
				pass
		else:
			try:
				shutil.copy2( CopyFrom, CopyTo )
			except:
				pass

	# Remove old files.
	pDialog.update(0,"Removing Old Folders","Please Wait..." )
	pDialog.update(2,"Removing","Apps" )
	if os.path.exists( os.path.join( Working_Directory, "Apps" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "Apps" ) )
		pDialog.update(5,"Removing","language" )
	if os.path.exists( os.path.join( Working_Directory, "language" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "language" ) )
		pDialog.update(10,"Removing","media" )
	if os.path.exists( os.path.join( Working_Directory, "media" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "media" ) )
		pDialog.update(20,"Removing","plugins" )
	if os.path.exists( os.path.join( Working_Directory, "plugins" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "plugins" ) )
		pDialog.update(25,"Removing","screensavers" )
	if os.path.exists( os.path.join( Working_Directory, "screensavers" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "screensavers" ) )
		pDialog.update(30,"Removing","scripts" )
	if os.path.exists( os.path.join( Working_Directory, "scripts" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "scripts" ) )
		pDialog.update(40,"Removing","skin" )
	if os.path.exists( os.path.join( Working_Directory, "skin" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "skin" ) )
		pDialog.update(55,"Removing","sounds" )
	if os.path.exists( os.path.join( Working_Directory, "sounds" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "sounds" ) )
		pDialog.update(60,"Removing","system" )
	if os.path.exists( os.path.join( Working_Directory, "system" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "system" ) )
		pDialog.update(70,"Removing","UserData" )
	if os.path.exists( os.path.join( Working_Directory, "UserData" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "UserData" ) )
		pDialog.update(80,"Removing","visualisations" )
	if os.path.exists( os.path.join( Working_Directory, "visualisations" ) ):
		shutil.rmtree( os.path.join( Working_Directory, "visualisations" ) )
		pDialog.update(85,"Removing","xbmc.log" )
	if os.path.isfile( os.path.join( Working_Directory, "xbmc.log" ) ):
		os.remove( os.path.join( Working_Directory, "xbmc.log" ) )
		pDialog.update(90,"Removing","xbmc.old.log" )
	if os.path.isfile( os.path.join( Working_Directory, "xbmc.old.log" ) ):
		os.remove( os.path.join( Working_Directory, "xbmc.old.log" ) )
		pDialog.update(95,"Removing",XBMC4KidsXBE )
	if os.path.isfile( os.path.join( Working_Directory, XBMC4KidsXBE ) ):
		os.remove( os.path.join( Working_Directory, XBMC4KidsXBE ) )
		pDialog.update(100,"","Done" )

	# Copy new files over.
	progress = 0
	for Items in os.listdir( XBMC4Kids_Update_Path ):
		CopyFrom	= os.path.join( XBMC4Kids_Update_Path, Items )
		CopyTo		= os.path.join( Working_Directory, Items )
		progress += 1
		pDialog.update( int ( progress / float( len ( os.listdir( XBMC4Kids_Update_Path ) ) ) *100 ),"Installing Update Files",Items )
		if os.path.isdir( CopyFrom ):
			try:
				shutil.copytree( CopyFrom, CopyTo )
			except:
				pass
		else:
			try:
				shutil.copy2(  CopyFrom, CopyTo )
			except:
				pass			

	Success_File = open( Working_Directory + "Updater/update_complete",'w' )
	Success_File.write( " " )
	Success_File.close()

	# Rename xbe back to what it was before the updater was run.
	if not os.path.isfile( os.path.join( Working_Directory, XBMC4KidsXBE ) ):
		os.rename( os.path.join( Working_Directory, "default.xbe" ), os.path.join( Working_Directory, XBMC4KidsXBE ) )
	else:
		pass

	pDialog.close()
	dialog.ok( "XBMC4Kids Updater","","Done, XBMC will now reload." )
	
	xbmc.executebuiltin( "XBMC.RunXBE(%s)" % os.path.join( Working_Directory, XBMC4KidsXBE ) )
else:
	dialog.ok( "Error","","Have you placed the [B]Updater[/B] folder","inside your [B]XBMC4Kids[/B] directory?" )
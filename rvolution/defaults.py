COMMAND_CODES = {
	#"3D":"",
	"Audio":"BB44BF00",#ok
	"Down":"E916BF00",#ok
	"Enter":"EB14BF00",#ok
	"Left":"E817BF00",#ok
	"Right":"E718BF00",#ok
	"Up":"EA15BF00",#ok
	"Delete":"EC0C4040",
	"Digit 0":"F50ABF00",#ok
	"Digit 1":"F40BBF00",#ok
	"Digit 2":"F30CBF00",#ok
	"Digit 3":"F20DBF00",#ok
	"Digit 4":"F10EBF00",#ok
	"Digit 5":"F00FBF00",#ok
	"Digit 6":"FE01BF00",#ok
	"Digit 7":"EE11BF00",#ok
	"Digit 8":"ED12BF00",#ok
	"Digit 9":"EC13BF00",#ok
	#"Dimmer":"",
	#"Explorer":"",
	"Fast Forward":"E41BBF00",#ok
	"Fast Reverse":"E31CBF00",#ok
	#"Format Scroll":"",
	"Green":"E01FBF00",#untested
	"Yellow":"FF00BF00",#untested
	"Red":"BF40BF00",#untested
	"Blue":"BE41BF00",#untested
	"Info":"AF50BF00",#ok
	"Menu":"F807BF00",#ok
	# "Mouse":"B04FBF00", #does not work
	"Mute":"B946BF00",#ok
	"Page Down":"B34CBF00",#ok
	"Page Up":"B44BBF00",#ok
	"Next":"E21DBF00",#ok
	"Previous":"B649BF00",#ok
	"Play / Pause":"B748BF00",#ok
	"Power Toggle":"BC43BF00",#?????
	"Power Off":"A15EBF00",
	"Power On":"A05FBF00",#not working when "power off" as no Network, onlx in "Video Output off" mode
	"Repeat":"B04FBF00",#untested
	"Return":"FB04BF00",#ok
	"Subtitle":"AB54BF00",#ok
	"Volume Down":"AC53BF00",#ok
	"Volume Up":"AD52BF00",#ok
	"Zoom":"FD02BF00",#ok
	"Home":"AE51BF00",#ok verlässt R_Video
	"Stop":"E619BF00",#ok
	"Search":"F906BF00", #ok
	"60 sec forward":"EE114040", #OK
	"60 sec rewind":"EF104040", #ok
	"10 sec forward":"B44BBF00",#ok
	"10 sec rewind": "B34CBF00", 	#ok
	"App Setup":"B14EBF00",#ok
	"App R_video":"B847BF00", #ok
	"App Recent":"9E61BF00", #ok
	"HDMI/XMOS Audio Toggle button":"BA45BF00",#?????
	"Mode":"BA45BF00" #undtestd
}

DEFAULT_MEDIA_TITLE = {
    'Id': '', 
    'Title': '', 
    'PosterUrl': '', 
    'BackgroundUrl': '', 
    'Type': 'Movie', 
    'SeenState': 'Seen', 
    'AllowedForChildren': False,
    'Episode': 0, 
    'Season': 0, 
    'TvShowName': None, 
    'Synopsis': '', 
    'Rating100': 0,
    'ReleaseDate': 000000000000000000, 
    'Actors': [], 
    'Directors': [], 
    'TechnicalInfo': {
        'Container': 'MKV', 
        'VideoCodec': 'AVC', 
        'VideoFramerate': '23.976', 
        'Width': 1920, 
        'Height': 1080,     
        'AudioTrackTechnicalInfos': [
            {'Index': 0, 'UserIndex': 0,'Format': 'DTS','FormatCommercial': 'DTS-HD Master Audio', 'FormatProfile': '', 'Channels': '6', 'NumberOfDynamicObjects': '', 'BedChannelCount': '', 'Language': 'en'}, 
        ], 
        'Subtitles': 'EN', 
        'Runtime': 0, 
        'HDR': '_BT.709'
    }
}
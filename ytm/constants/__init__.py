'''
Package containing constants.

These constants help the super package achieve general tasks.

Example:
    >>> from ytm import constants
    >>>
    >>> constants.__all__
    ...
    >>>
'''

# Params
PARAMS_SHUFFLE = 'wAEB8gECGAE%3D'
PARAMS_RADIO   = 'wAEB'
PARAMS_WATCH   = 'wAEB'

PARAMS_RADIO_SONG = 'mgMDCNgE'

PLAYER_PARAMS_RADIO_SONG = 'igMDCNgE'

# Prefixes
PREFIX_RADIO    = 'RDAMPL' # These exist in /types/constants. Are they needed here?
PREFIX_PLAYLIST = 'VL'

# API_KEYS = \
# (
#     'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
#     'AIzaSyDK3iBpDP9nHVTk2qL73FLJICfOC3c51Og',
#     'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
# )
#
# API_KEY = API_KEYS[0]

# Domains
DOMAIN_YOUTUBE_MUSIC = 'music.youtube.com'
DOMAIN_YOUTUBE       = 'www.youtube.com'

# Protocols
PROTOCOL_HTTPS = 'https'
PROTOCOL_HTTP  = 'http'

# Domain Protocols
PROTOCOL_YOUTUBE       = PROTOCOL_HTTPS
PROTOCOL_YOUTUBE_MUSIC = PROTOCOL_HTTPS

# Versions
VERSION_YTM_API = 1 # page_data['PLAYER_CONFIG']['args']['innertube_api_version']

# YouTube Music Endpoints
ENDPOINT_YTM_HOME                   = ''
ENDPOINT_YTM_HOTLIST                = 'hotlist'
ENDPOINT_YTM_SEARCH                 = 'search'
ENDPOINT_YTM_PLAYLIST               = 'playlist'
ENDPOINT_YTM_CHANNEL                = 'channel'
ENDPOINT_YTM_WATCH                  = 'watch'
ENDPOINT_YTM_API                    = f'youtubei/v{VERSION_YTM_API}'
ENDPOINT_YTM_API_SEARCH             = 'search'
ENDPOINT_YTM_API_BROWSE             = 'browse'
ENDPOINT_YTM_API_NEXT               = 'next'
ENDPOINT_YTM_API_GUIDE              = 'guide'
ENDPOINT_YTM_API_SEARCH_SUGGESTIONS = 'music/get_search_suggestions'
ENDPOINT_YTM_API_GET_QUEUE          = 'music/get_queue'

# YouTube Endpoints
ENDPOINT_YT_VIDEO_INFO = 'get_video_info'

# Browse IDs
BROWSE_ID_HOME    = 'FEmusic_home'
BROWSE_ID_HOTLIST = 'FEmusic_trending'

# Page Types
PAGE_TYPE_ALBUM    = 'MUSIC_PAGE_TYPE_ALBUM'
PAGE_TYPE_ARTIST   = 'MUSIC_PAGE_TYPE_ARTIST'
PAGE_TYPE_PLAYLIST = 'MUSIC_PAGE_TYPE_PLAYLIST'

# Music video types
MUSIC_VIDEO_TYPE_OMV = 'MUSIC_VIDEO_TYPE_OMV'

# Automix settings
AUTOMIX_SETTING_NORMAL = 'AUTOMIX_SETTING_NORMAL'

# URL_PARAMS = \
# {
#     'alt': 'json',
#     'key': API_KEY,
# }

SEARCH_PARAM_PREFIX    = 'Eg-KAQwIA'
SEARCH_PARAM_SUFFIX    = 'MABqChADEAQQCRAKEAU%3D'
SEARCH_PARAM_ALBUMS    = 'BAAGAEgACgA'
SEARCH_PARAM_PLAYLISTS = 'BAAGAAgACgB'
SEARCH_PARAM_VIDEOS    = 'BABGAAgACgA'
SEARCH_PARAM_ARTISTS   = 'BAAGAAgASgA'
SEARCH_PARAM_SONGS     = 'RAAGAAgACgA'

SEARCH_FILTER_ALBUMS    = 'albums'
SEARCH_FILTER_PLAYLISTS = 'playlists'
SEARCH_FILTER_VIDEOS    = 'videos'
SEARCH_FILTER_ARTISTS   = 'artists'
SEARCH_FILTER_SONGS     = 'songs'

SEARCH_PARAMS_MAP = \
{
    SEARCH_FILTER_ALBUMS:    SEARCH_PARAM_ALBUMS,
    SEARCH_FILTER_PLAYLISTS: SEARCH_PARAM_PLAYLISTS,
    SEARCH_FILTER_VIDEOS:    SEARCH_PARAM_VIDEOS,
    SEARCH_FILTER_ARTISTS:   SEARCH_PARAM_ARTISTS,
    SEARCH_FILTER_SONGS:     SEARCH_PARAM_SONGS,
}

SEARCH_PARAMS_MAP_REV = \
{
    val: key
    for key, val in SEARCH_PARAMS_MAP.items()
}

# PAYLOAD = \
# {
#     'context': \
#     {
#         'activePlayers': {},
#         'capabilities': {},
#         'client': \
#         {
#             'clientName': 'WEB_REMIX',
#             'clientVersion': '0.1',
#             'experimentIds': [],
#             'experimentsToken': '',
#             'gl': 'GB', # GL
#             'hl': 'en',
#             'locationInfo': \
#             {
#                 'locationPermissionAuthorizationStatus': 'LOCATION_PERMISSION_AUTHORIZATION_STATUS_UNSUPPORTED',
#             },
#             'musicAppInfo': \
#             {
#                 'musicActivityMasterSwitch': 'MUSIC_ACTIVITY_MASTER_SWITCH_INDETERMINATE',
#                 'musicLocationMasterSwitch': 'MUSIC_LOCATION_MASTER_SWITCH_INDETERMINATE',
#                 'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_UNKNOWN',
#             },
#             'utcOffsetMinutes': 0,
#         },
#         'request': \
#         {
#             'internalExperimentFlags': \
#             [
#                 {
#                     'key': 'force_music_enable_outertube_playlist_detail_browse',
#                     'value': 'true',
#                 },
#                 {
#                     'key': 'force_music_enable_outertube_tastebuilder_browse',
#                     'value': 'true',
#                 },
#                 {
#                     'key': 'force_music_enable_outertube_search_suggestions',
#                     'value': 'true',
#                 },
#             ],
#             'sessionIndex': {},
#         },
#         'user': \
#         {
#             'enableSafetyMode': False,
#         },
#     },
# }

# PAYLOAD = \
# {
#     'context': \
#     {
#         'client': \
#         {
#             'clientName': 'WEB_REMIX', # INNERTUBE_CLIENT_NAME
#             'clientVersion': '0.1', # INNERTUBE_CONTEXT_CLIENT_VERSION, INNERTUBE_CLIENT_VERSION
#         },
#     },
# }

'''
Package containing constants.

These constants help the super package achieve general tasks.
'''

from ....constants import *

SEARCH_PARAM_PREFIX    = 'Eg-KAQwIA'
SEARCH_PARAM_SUFFIX    = 'MABqChADEAQQCRAKEAU%3D'
SEARCH_PARAM_ALBUMS    = 'BAAGAEgACgA'
SEARCH_PARAM_PLAYLISTS = 'BAAGAAgACgB'
SEARCH_PARAM_VIDEOS    = 'BABGAAgACgA'
SEARCH_PARAM_ARTISTS   = 'BAAGAAgASgA'
SEARCH_PARAM_SONGS     = 'RAAGAAgACgA'

SEARCH_PARAMS_MAP = \
{
    'albums':    SEARCH_PARAM_ALBUMS,
    'artists':   SEARCH_PARAM_ARTISTS,
    'playlists': SEARCH_PARAM_PLAYLISTS,
    'songs':     SEARCH_PARAM_SONGS,
    'videos':    SEARCH_PARAM_VIDEOS,
}

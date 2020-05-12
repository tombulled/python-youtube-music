'''
Author:  Tom Bulled
License: GNU General Public License v3.0
Site:    https://github.com/tombulled/python-youtube-music

Python 3 YouTube Music Web API Client.

The library facilitates *unauthenticated* requests to music.youtube.com.
API classes are easily available and should provide all of the required functionality.
Code documentation is available throughout.

Getting Started:
    Import the library:
        >>> import ytm
    Create an API instance:
        >>> api = ytm.YouTubeMusic()
        >>> api
        <YouTubeMusic()>
    See available methods:
        >>> from pprint import pprint
        >>>
        >>> pprint(list(api._methods))
        ['_search_filter',
         'album',
         'artist',
         'artist_albums',
         'artist_singles',
         'guide',
         'home',
         'hotlist',
         'playlist',
         'search',
         'search_albums',
         'search_artists',
         'search_playlists',
         'search_songs',
         'search_suggestions',
         'search_videos',
         'song',
         'watch',
         'watch_radio',
         'watch_shuffle']
        >>>
    View documentation on a method:
        >>> help(api.search_suggestions)
        Help on method search_suggestions in module ytm.apis.AbstractYouTubeMusic.methods.search_suggestions:

        search_suggestions(query: str) -> list method of ytm.apis.YouTubeMusic.YouTubeMusic.YouTubeMusic instance
            Retrieve search suggestions.

            Args:
                self: Class Instance
                query: Search query
                    Example: 'imagine'

            Returns:
                List of search suggestions

            Raises:
                MethodError: Method encountered an error

            Example:
                >>> api = ytm.AbstractYouTubeMusic()
                >>>
                >>> suggestions = api.search_suggestions('imagine')
                >>>
                >>> suggestions[0]
                'imagine dragons'
                >>>

        >>>
    Call a method:
        >>> from pprint import pprint
        >>>
        >>> data = api.search_suggestions('foo')
        >>>
        >>> pprint(data)
        ['footloose',
         'foo fighters',
         'football songs',
         'foogiano',
         'foolish ashanti',
         'foo fighters everlong',
         'foolio']
        >>>
'''

from . import utils
from . import apis

__inherit = utils.__include(apis.__spec__)

locals().update(__inherit)

__all__ = \
(
    *tuple(__inherit),
    *tuple(utils.__include(__spec__)),
)

''' xxx '''

from ...utils import _import
from ..BaseYouTubeMusic import BaseYouTubeMusic

_import(locals())

locals()['__all__'] = __name__.split('.')[-1:]

class YouTubeMusic(object):
    def __init__(self):
        self.base = BaseYouTubeMusic()

        methods = \
        (
            'song_info',
            'search_suggestions',
            'home',
            'hotlist',
            'guide', # Although implemented, pointless...
            #
            'playlist',
            'album',
            'search',

            # Final, TODO
            # 'search' (filter by: artists, songs, albums, videos, playlists. Continuations)
            # 'next' (or better name. Needs make_radio=). Wrapper using .song(...)?
                # .list(...)
            # 'artist' () NOTE: Has other pages: artist_songs, ...

            # --------------------------

            # 'song', # (next?) a radio'd song
            # 'artist',
            # 'search',
            # search_albums(...), ...
            # next? (needs a make_radio)

            # Song get recommendations (next)
            # shuffle? # pointless
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

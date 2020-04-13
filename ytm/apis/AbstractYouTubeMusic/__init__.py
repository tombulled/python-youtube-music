''' xxx '''

from ...utils import _import
from ..BaseYouTubeMusic import BaseYouTubeMusic

__all__ = __name__.split('.')[-1:]

_import(locals())

# locals()['__all__'] = __name__.split('.')[-1:]

class AbstractYouTubeMusic(object):
    def __init__(self):
        self.base = BaseYouTubeMusic()

        methods = \
        (
            'home',
            # 'guide', # Made but so pointless
            'hotlist',
            'song',
            'suggest',
            'watch',
            'playlist',
            'album',

            'search', # Here last

            'search_albums',
            'search_playlists',
            'search_videos',
            'search_artists',
            'search_songs',

            'artist',

            # 'artist_singles', # (artist_id, params)
            # 'artist_albums', # (artist_id, params)

            # 'shuffle',
            # 'radio',

            # 'video_id' # ?? or just 'video'

            # others? artist_songs, search_songs
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

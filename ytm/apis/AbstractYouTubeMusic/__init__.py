''' xxx '''

from ...utils import _import
from ..BaseYouTubeMusic import BaseYouTubeMusic

__all__ = __name__.split('.')[-1:]

_import(locals())

class AbstractYouTubeMusic(object):
    def __init__(self):
        # This should be _base or __base
        # ... so not confused with a method when dir(...)
        self.base = BaseYouTubeMusic()

        methods = \
        (
            'home',
            # 'guide', # Made but so pointless
            'hotlist',
            'song',
            'suggest', # Rename to search_suggest ??
            'watch',   # Rename to next?
            'playlist',
            'album',

            'search',

            'search_albums',
            'search_playlists',
            'search_videos',
            'search_artists',
            'search_songs',

            'artist',

            'artist_albums',  # (artist_id, params)
            'artist_singles', # (artist_id, params)

            # 'shuffle', # 'playlist_shuffle' ?
            # 'radio',   # 'playlist_radio'   ?

            # Others?

            #########################################

            # 'download'
            # 'video_id' # ?? or just 'video'
            # Can use YouTubeMusicDL
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

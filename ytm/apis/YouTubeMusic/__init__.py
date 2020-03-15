''' xxx '''

from ...utils import _import
from ..BaseYouTubeMusic import BaseYouTubeMusic

_import(locals())

print(__name__, __file__)

class YouTubeMusic(object):
    def __init__(self):
        self.base = BaseYouTubeMusic()

        methods = \
        (
            song_info,
            search_suggestions,
            # home,
            # hotlist,
            # search,
            # playlist,
            # artist,
            # song,
            # album,
            # guide,
        )

        for method in methods:
            setattr(self.__class__, method.__name__.split('.')[-1], method)

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

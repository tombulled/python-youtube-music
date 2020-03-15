''' xxx '''

from ..BaseYouTubeMusic import BaseYouTubeMusic

from .song_info import song_info
from .search_suggestions import search_suggestions

__all__ = __name__.split('.')[-1:]

class YouTubeMusic(object):
    def __init__(self):
        self.base = BaseYouTubeMusic()

        methods = \
        (
            song_info,
            search_suggestions
        )

        for method in methods:
            def wrapper(*args, **kwargs):
                print()

            setattr(self.__class__, method.__name__.split('.')[-1], method)

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

    def home(self):
        ...

    def hotlist(self):
        ...

    def search(self):
        ...

    def playlist(self):
        ...

    def artist(self):
        ...

    def song(self):
        ...

    def album(self):
        ...

    def guide(self):
        ...

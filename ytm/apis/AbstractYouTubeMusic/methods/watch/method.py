from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.parse(parser.parse)
def method(self, song_id=None, playlist_id=None, params=None, continuation=None):
    return self._base.next \
    (
        video_id     = song_id,
        playlist_id  = playlist_id,
        params       = params,
        continuation = continuation,
    )

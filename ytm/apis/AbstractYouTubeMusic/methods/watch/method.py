from . import parser
from ... import decorators
from ...types import SongId, SongListId, WatchContinuation, Params

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method \
        (
            self:         object,
            song_id:      SongId            = None,
            playlist_id:  SongListId        = None,
            params:       Params            = None,
            continuation: WatchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._base.next \
    (
        video_id     = song_id,
        playlist_id  = playlist_id,
        params       = params,
        continuation = continuation,
    )

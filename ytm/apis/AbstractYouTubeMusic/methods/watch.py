# from . import parser
from .. import parsers
from .. import decorators
from ..types import SongId, SongListId, WatchContinuation, Params

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.watch)
def watch \
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

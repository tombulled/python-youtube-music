from . import parser
from ... import decorators
from ...types import SongId

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, song_id: SongId) -> dict:
    return self._base.video_info \
    (
        video_id = song_id,
    )

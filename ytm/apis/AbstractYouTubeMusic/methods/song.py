# from . import parser
from .. import parsers
from .. import decorators
from ..types import SongId

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.song)
def song(self: object, song_id: SongId) -> dict:
    return self._base.video_info \
    (
        video_id = song_id,
    )

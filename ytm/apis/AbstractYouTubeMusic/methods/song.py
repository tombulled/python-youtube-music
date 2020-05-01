from .. import decorators
from .... import parsers
from ....types import SongId

@decorators.method(parsers.song)
def song(self: object, song_id: SongId) -> dict:
    return self._base.video_info \
    (
        video_id = song_id,
    )

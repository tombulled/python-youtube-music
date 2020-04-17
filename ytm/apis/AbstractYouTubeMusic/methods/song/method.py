from . import parser
from ... import decorators

__all__ = __name__.split('.')[-1:]

@decorators.parse(parser.parse)
def method(self, song_id):
    return self._base.video_info \
    (
        video_id = song_id,
    )

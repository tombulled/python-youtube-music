from . import parser
from ... import decorators
from ...types import ArtistId

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, artist_id: ArtistId) -> dict:
    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

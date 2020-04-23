from . import parser
from ... import decorators
from ...types import ArtistId, ArtistSinglesParams

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, artist_id: ArtistId, params: ArtistSinglesParams) -> list:
    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

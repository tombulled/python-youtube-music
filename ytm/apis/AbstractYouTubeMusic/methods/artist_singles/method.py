from . import parser
from ... import decorators
from ... import types

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

ArtistId = types.ArtistId
ArtistSinglesContinuation = types.ArtistSinglesContinuation

@decorators.parse(parser.parse)
def method(self, artist_id: ArtistId, params: ArtistSinglesContinuation):
    artist_id = types.ArtistId(artist_id)
    params    = types.ArtistSinglesContinuation(params)

    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

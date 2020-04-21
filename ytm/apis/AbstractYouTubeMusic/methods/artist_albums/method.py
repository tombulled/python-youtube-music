from . import parser
from ... import decorators
from ... import types

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

ArtistId = types.ArtistId
ArtistAlbumsContinuation = types.ArtistAlbumsContinuation

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, artist_id: ArtistId, params: ArtistAlbumsContinuation) -> list:
    # artist_id = types.ArtistId(artist_id)
    # params    = types.ArtistAlbumsContinuation(params)

    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

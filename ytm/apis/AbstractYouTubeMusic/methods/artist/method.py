from . import parser
from ... import decorators
from ... import types

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

ArtistId = types.ArtistId

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, artist_id: ArtistId) -> dict:
    # artist_id = types.ArtistId(artist_id)

    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

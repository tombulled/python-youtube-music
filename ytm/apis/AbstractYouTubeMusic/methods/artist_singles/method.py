from . import parser
from ... import decorators
from ... import types

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

ArtistId = types.ArtistId

@decorators.parse(parser.parse)
def method(self, artist_id: ArtistId, params):
    artist_id = types.ArtistId(artist_id)
    
    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

# import re
from . import parser
from ... import decorators
# from ... import exceptions
from ... import types

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

ArtistId = types.ArtistId

@decorators.parse(parser.parse)
def method(self, artist_id: ArtistId):
    artist_id = types.ArtistId(artist_id)

    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

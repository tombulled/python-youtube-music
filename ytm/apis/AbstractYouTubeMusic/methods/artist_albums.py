# from . import parser
from .. import parsers
from .. import decorators
from ..types import ArtistId, ArtistAlbumsParams

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.artist_albums)
def artist_albums(self: object, artist_id: ArtistId, params: ArtistAlbumsParams) -> list:
    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

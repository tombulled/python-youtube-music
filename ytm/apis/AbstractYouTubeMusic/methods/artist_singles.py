# from . import parser
from .. import parsers
from .. import decorators
from ..types import ArtistId, ArtistSinglesParams

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.artist_singles)
def artist_singles(self: object, artist_id: ArtistId, params: ArtistSinglesParams) -> list:
    return self._base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

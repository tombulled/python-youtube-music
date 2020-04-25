# from . import parser
from .. import parsers
from .. import decorators
from ..types import ArtistId

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.artist)
def artist(self: object, artist_id: ArtistId) -> dict:
    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

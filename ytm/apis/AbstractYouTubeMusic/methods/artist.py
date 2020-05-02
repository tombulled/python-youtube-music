from .. import decorators
from .... import parsers
from .... import types
from ....types import \
(
    Union,
    ArtistId,
    ArtistBrowseId,
)

@decorators.method(parsers.artist)
def artist \
        (
            self:      object,
            artist_id: Union \
            (
                ArtistId,
                ArtistBrowseId,
            ),
        ) -> dict:
    '''
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse_artist \
    (
        browse_id = artist_browse_id,
    )

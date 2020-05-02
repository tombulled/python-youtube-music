from .. import decorators
from .... import parsers
from .... import types
from ....types import \
(
    Union,
    ArtistId,
    ArtistBrowseId,
    ArtistSinglesParams,
)

@decorators.method(parsers.artist_singles)
def artist_singles \
        (
            self:      object,
            artist_id: Union \
            (
                ArtistId,
                ArtistBrowseId,
            ),
            params:    ArtistSinglesParams,
        ) -> list:
    '''
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse \
    (
        browse_id = artist_browse_id,
        params    = params,
    )

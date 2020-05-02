from .. import decorators
from .... import parsers
from .... import types
from ....types import \
(
    Union,
    ArtistId,
    ArtistBrowseId,
    ArtistAlbumsParams,
)

@decorators.method(parsers.artist_albums)
def artist_albums \
        (
            self:      object,
            artist_id: Union \
            (
                ArtistId,
                ArtistBrowseId,
            ),
            params:    ArtistAlbumsParams,
        ) -> list:
    '''
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse \
    (
        browse_id = artist_browse_id,
        params    = params,
    )

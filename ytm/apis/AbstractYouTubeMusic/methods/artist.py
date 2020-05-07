'''
Module containing the method: artist
'''

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
    Fetch Artist data.

    Args:
        self: Class Instance
        artist_id: Artist Id
            Example: 'UCRI-Ds5eY70A4oeHggAFBbg'

    Returns:
        Artist data.

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> artist = api.artist('UCTK1maAvqrDlD2agZDGZzjw')
        >>>
        >>> artist['name']
        'Take That'
        >>>
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse_artist \
    (
        browse_id = artist_browse_id,
    )

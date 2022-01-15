'''
Module containing the method: artist_albums
'''

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
    Fetch Artist's Albums data.

    These are like a continuation on the list of albums from the Artist's
    channel page.
    These can only be fetched once the Artist's data has been obtained
    as this will contain the 'params' required.
    The Artist Id should also be the one obtained by fetching the Artist's data
    as it may return a different Artist Id.

    Args:
        self: Class Instance
        artist_id: Artist Id
            Example: 'UCRI-Ds5eY70A4oeHggAFBbg'
        params: Artist Albums Params
            Example: '6gPUAUNwd0JDbjBLYmdBQVpXNEFBVWRDQUFGSFFnQUJBRVpGY...'

    Returns:
        Artist's Albums data.

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> # Artist data should always be fetched first
        >>> artist = api.artist('UCTK1maAvqrDlD2agZDGZzjw')
        >>>
        >>> artist['name']
        'Take That'
        >>>
        >>> # Important: Extract the artist_id from the data, don't reuse the original
        >>> artist_id = artist['id']
        >>> # Extract albums params
        >>> params = artist['albums']['params']
        >>>
        >>> # Fetch albums
        >>> albums = api.artist_albums(artist_id, params)
        >>>
        >>> albums[0]['name']
        'Wonderland (Deluxe)'
        >>>
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse \
    (
        browse_id = artist_browse_id,
        params    = params,
    )

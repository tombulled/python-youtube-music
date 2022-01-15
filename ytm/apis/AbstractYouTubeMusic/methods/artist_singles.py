'''
Module containing the method: artist_singles
'''

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
    Fetch Artist's Singles data.

    These are like a continuation on the list of singles from the Artist's
    channel page.
    These can only be fetched once the Artist's data has been obtained
    as this will contain the 'params' required.
    The Artist Id should also be the one obtained by fetching the Artist's data
    as it may return a different Artist Id.

    Args:
        self: Class Instance
        artist_id: Artist Id
            Example: 'UCRI-Ds5eY70A4oeHggAFBbg'
        params: Artist Singles Params
            Example: '6gPUAUNwd0JDbjBLYmdBQVpXNEFBVWRDQUFGSFFnQUJBRVpGYlhWemF...'

    Returns:
        Artist's Singles data.

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
        >>> params = artist['singles']['params']
        >>>
        >>> singles = api.artist_singles(artist_id, params)
        >>>
        >>> singles[0]['name']
        'Cry (Live)'
        >>>
    '''

    artist_browse_id = types.ArtistBrowseId(artist_id)

    return self._base.browse \
    (
        browse_id = artist_browse_id,
        params    = params,
    )

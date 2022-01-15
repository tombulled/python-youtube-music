'''
Module containing the method: search_artists
'''

from .. import decorators
from .... import constants
from ....types import SearchContinuation

@decorators.method()
def search_artists \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a search for only Artists.

    Args:
        self: Class Instance
        query: Search query
            Example: 'bastille'
        continuation: Search Continuation
            Example: 'Eo0GEghpbiB1dGVybxqABkVnLUtBUXdJQUJBQUdBRWdBQ2dBTUFCSUZ...'

    Returns:
        Artists search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search_artists('bastille')
        >>>
        >>> data['items'][0]['name']
        'Bastille'
        >>>
        >>> more_data = api.search_artists(continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'FRENSHIP'
        >>>
    '''

    return self._search_filter \
    (
        filter       = constants.SEARCH_FILTER_ARTISTS,
        query        = query,
        continuation = continuation,
    )

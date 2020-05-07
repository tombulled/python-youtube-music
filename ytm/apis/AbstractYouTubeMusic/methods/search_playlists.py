'''
Module containing the method: search_playlists
'''

from .. import decorators
from .... import constants
from ....types import SearchContinuation

@decorators.method()
def search_playlists \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a search for only Playlists.

    Args:
        self: Class Instance
        query: Search query
            Example: 'love'
        continuation: Search Continuation
            Example: 'Eo0GEghpbiB1dGVybxqABkVnLUtBUXdJQUJBQUdBRWdBQ2dBTUFCSUZ...'

    Returns:
        Playlists search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search_playlists('love')
        >>>
        >>> data['items'][0]['name']
        'Love Metal'
        >>>
        >>> more_data = api.search_playlists(continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'Love Your Inner Goddess'
        >>>
    '''

    return self._search_filter \
    (
        filter       = constants.SEARCH_FILTER_PLAYLISTS,
        query        = query,
        continuation = continuation,
    )

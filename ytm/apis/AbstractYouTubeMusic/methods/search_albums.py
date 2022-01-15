'''
Module containing the method: search_albums
'''

from .. import decorators
from .... import constants
from ....types import SearchContinuation

@decorators.method()
def search_albums \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a search for only Albums.

    Args:
        self: Class Instance
        query: Search query
            Example: 'in utero'
        continuation: Search Continuation
            Example: 'Eo0GEghpbiB1dGVybxqABkVnLUtBUXdJQUJBQUdBRWdBQ2dBTUFCSUZ...'

    Returns:
        Albums search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search_albums('in utero')
        >>>
        >>> data['items'][0]['name']
        'In Utero (20th Anniversary Remaster)'
        >>>
        >>> # Fetch more results
        >>> more_data = api.search_albums(continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'Nirvana'
        >>>
    '''

    return self._search_filter \
    (
        filter       = constants.SEARCH_FILTER_ALBUMS,
        query        = query,
        continuation = continuation,
    )

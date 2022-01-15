'''
Module containing the method: search_songs
'''

from .. import decorators
from .... import constants
from ....types import SearchContinuation

@decorators.method()
def search_songs \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a search for only Songs.

    Args:
        self: Class Instance
        query: Search query
            Example: 'simple song'
        continuation: Search Continuation
            Example: 'Eo0GEghpbiB1dGVybxqABkVnLUtBUXdJQUJBQUdBRWdBQ2dBTUFCSUZ...'

    Returns:
        Songs search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search_songs('simple song')
        >>>
        >>> data['items'][0]['name']
        'Simple Song'
        >>>
        >>> more_data = api.search_songs(continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'The Simple Song'
        >>>
    '''

    return self._search_filter \
    (
        filter       = constants.SEARCH_FILTER_SONGS,
        query        = query,
        continuation = continuation,
    )

'''
Module containing the method: _search_filter
'''

from .. import decorators
from .... import constants
from .... import parsers
from ....types import SearchContinuation

@decorators.method()
def _search_filter \
        (
            self:         object,
            filter:       str,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a filtered search.

    Searching can be performed using *either* a query or a continuation.
    Both should not be specified at the same time, and one is required.

    Args:
        self: Class Instance
        filter: Search filter
            Example: 'albums'
        query: Search query
            Example: 'nirvana'
        continuation: Search continuation
            Example: 'EpIJEgVibHVlcxqICUVnLUtBUXdJQUJBQUdBQWdBQ2dCTUFCSUt...'

    Returns:
        Filtered search data.

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api._search_filter(filter = 'playlists', query = 'love')
        >>>
        >>> data['items'][0]['name']
        'Love Metal'
        >>>
        >>> # Fetch more data using the continuation token
        >>> more_data = api._search_filter(filter = 'playlists', continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'Love Your Inner Goddess'
        >>>
    '''

    filter = filter.strip().lower()

    param = constants.SEARCH_PARAMS_MAP.get(filter)

    assert param, f'Invalid search filter: {repr(filter)}'

    if query:
        query  = query.strip()

        assert query, 'No search query provided'

        data = self._base.search \
        (
            query  = query,
            params = ''.join \
            (
                (
                    constants.SEARCH_PARAM_PREFIX,
                    param,
                    constants.SEARCH_PARAM_SUFFIX,
                ),
            ),
        )
    elif continuation:
        data = self._base.search \
        (
            continuation = continuation,
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'query\' or \'continuation\''
        )

    parsed_data = parsers._search_filter(data, filter)

    return parsed_data

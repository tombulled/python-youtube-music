'''
Module containing the parser: search_albums
'''

from ._search_filter import _search_filter as parse_search_filter
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_albums(data: dict) -> dict:
    '''
    Parse data: Search Albums.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> params = ytm.constants.SEARCH_PARAM_PREFIX \
        		   + ytm.constants.SEARCH_PARAM_ALBUMS \
        		   + ytm.constants.SEARCH_PARAM_SUFFIX
        >>>
        >>> data = api.search('bad blood', params = params)
        >>>
        >>> parsed_data = ytm.parsers.search_albums(data)
        >>>
        >>> parsed_data['items'][0]['name']
        'Bad Blood (The Extended Cut)'
        >>>
    '''

    return parse_search_filter \
    (
        data   = data,
        filter = 'albums',
    )

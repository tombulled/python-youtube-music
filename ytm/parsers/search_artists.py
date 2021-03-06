'''
Module containing the parser: search_artists
'''

from ._search_filter import _search_filter as parse_search_filter
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_artists(data: dict) -> dict:
    '''
    Parse data: Search Artists.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> params = ytm.constants.SEARCH_PARAM_PREFIX  \
        		   + ytm.constants.SEARCH_PARAM_ARTISTS \
        		   + ytm.constants.SEARCH_PARAM_SUFFIX
        >>>
        >>> data = api.search('easy life', params = params)
        >>>
        >>> parsed_data = ytm.parsers.search_artists(data)
        >>>
        >>> parsed_data['items'][0]['name']
        'Easy Life'
        >>>
    '''

    return parse_search_filter \
    (
        data   = data,
        filter = 'artists',
    )

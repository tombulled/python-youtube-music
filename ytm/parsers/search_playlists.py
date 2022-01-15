'''
Module containing the parser: search_playlists
'''

from ._search_filter import _search_filter as parse_search_filter
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_playlists(data: dict) -> dict:
    '''
    Parse data: Search Playlists.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> params = ytm.constants.SEARCH_PARAM_PREFIX    \
        		   + ytm.constants.SEARCH_PARAM_PLAYLISTS \
        		   + ytm.constants.SEARCH_PARAM_SUFFIX
        >>>
        >>> data = api.search('indie rock', params = params)
        >>>
        >>> parsed_data = ytm.parsers.search_playlists(data)
        >>>
        >>> parsed_data['items'][0]['name']
        'Indie Rock Chasers'
        >>>
    '''

    return parse_search_filter \
    (
        data   = data,
        filter = 'playlists',
    )

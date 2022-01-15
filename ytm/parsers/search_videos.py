'''
Module containing the parser: search_videos
'''

from ._search_filter import _search_filter as parse_search_filter
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_videos(data: dict) -> dict:
    '''
    Parse data: Search Videos.

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
        		   + ytm.constants.SEARCH_PARAM_VIDEOS \
        		   + ytm.constants.SEARCH_PARAM_SUFFIX
        >>>
        >>> data = api.search('grace kelly', params = params)
        >>>
        >>> parsed_data = ytm.parsers.search_videos(data)
        >>>
        >>> parsed_data['items'][0]['name']
        'Grace Kelly'
        >>>
    '''

    return parse_search_filter \
    (
        data   = data,
        filter = 'videos',
    )

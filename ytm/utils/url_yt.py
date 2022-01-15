'''
Module containing the utility function: url_yt
'''

from .. import constants
from ._url import _url

def url_yt(*endpoints: str, params: dict = None) -> str:
    '''
    Create a YouTube URL.

    Formulates a YouTube URL using the provided arguments

    Args:
        *endpoints: URL endpoints
            Example: ['feed', 'trending']
        params: URL query string parameters
            Example: {'search_query': 'test'}

    Returns:
        A YouTube URL

    Example:
        >>> url_yt('results', params = {'search_query': 'test'})
        'https://www.youtube.com/results?search_query=test'
        >>>
    '''

    return _url \
    (
        constants.PROTOCOL_YOUTUBE,
        constants.DOMAIN_YOUTUBE,
        *endpoints,
        params = params,
    )

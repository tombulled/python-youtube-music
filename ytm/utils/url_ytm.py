'''
Module containing the utility function: url_ytm
'''

from .. import constants
from ._url import _url

def url_ytm(*endpoints: str, params: dict = None) -> str:
    '''
    Create a YouTubeMusic URL.

    Formulates a YouTube Music URL using the provided arguments

    Args:
        *endpoints: URL endpoints
            Example: ['playlist']
        params: URL query string parameters
            Example: {'q': 'test'}

    Returns:
        A YouTube Music URL

    Example:
        >>> url_ytm('search', params = {'q': 'test'})
        'https://music.youtube.com/search?q=test'
        >>>
    '''

    return _url \
    (
        constants.PROTOCOL_YOUTUBE_MUSIC,
        constants.DOMAIN_YOUTUBE_MUSIC,
        *endpoints,
        params = params,
    )

'''
Module containing the method: _url_api
'''

from .. import utils
from .. import constants

@staticmethod
def _url_api(*endpoints: str, params: dict = None) -> str:
    '''
    Generate a YouTube Music Api URL.

    Args:
        *endpoints: Url endpoints
        params: Url query-string parameters

    Returns:
        YouTube Music Api URL

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> api._url_api('music', 'get_search_suggestions')
        'https://music.youtube.com/youtubei/v1/music/get_search_suggestions'
        >>>
    '''

    return utils.url_ytm \
    (
        constants.ENDPOINT_YTM_API,
        *endpoints,
        params = params,
    )

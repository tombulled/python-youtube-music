'''
Module containing the method: _url_yt
'''

from .. import utils

@staticmethod
def _url_yt(*endpoints: str, params: dict = None) -> str:
    '''
    Generate a YouTube URL.

    Args:
        *endpoints: Url endpoints
        params: Url query-string parameters

    Returns:
        YouTube URL

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> api._url_yt('get_video_info', params = {'video_id': 'KuVt9Cnbhwg'})
        'https://www.youtube.com/get_video_info?video_id=KuVt9Cnbhwg'
        >>>
    '''

    return utils.url_yt \
    (
        *endpoints,
        params = params,
    )

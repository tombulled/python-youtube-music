'''
Module containing the method: _url
'''

from .. import utils

@staticmethod
def _url(*endpoints: str, params: dict = None) -> str:
    '''
    Generate a YouTube Music URL.

    Args:
        *endpoints: Url endpoints
        params: Url query-string parameters

    Returns:
        YouTube Music URL

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> api._url('watch', params = {'v': 'KuVt9Cnbhwg'})
        'https://music.youtube.com/watch?v=KuVt9Cnbhwg'
        >>>
    '''

    return utils.url_ytm \
    (
        *endpoints,
        params = params,
    )

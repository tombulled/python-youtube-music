'''
Module containing the method: page_watch
'''

from .. import constants
from .. import utils

def page_watch(self: object, v: str, list: str = None) -> dict:
    '''
    Return page configuration data for: Watch.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance
        v: Video Id
            Example: 'QtXby3twMmI'
        list: Playlist list id
            Example: 'RDCLAK5uy_ktv79aJ_zAi049KdFWFaAZEfgnm5jNZpk'

    Returns:
        Watch page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_watch \
        (
        	v = 'QtXby3twMmI',
        	list = 'RDCLAK5uy_ktv79aJ_zAi049KdFWFaAZEfgnm5jNZpk',
        )
        >>>
        >>> data['INITIAL_ENDPOINT']['watchEndpoint']
        {'videoId': 'QtXby3twMmI', 'playlistId': 'RDCLAK5uy_ktv...}
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_WATCH,
        params = utils.filter \
        (
            {
                'v':    v,
                'list': list,
            }
        ),
    )

'''
Module containing the method: page_playlist
'''

from .. import constants

def page_playlist(self: object, list: str) -> dict:
    '''
    Return page configuration data for: Playlist.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance
        list: Playlist list id
            Example: 'RDCLAK5uy_ktv79aJ_zAi049KdFWFaAZEfgnm5jNZpk'

    Returns:
        Playlist page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_playlist('RDCLAK5uy_ktv79aJ_zAi049KdFWFaAZEfgnm5jNZpk')
        >>>
        >>> data['INITIAL_ENDPOINT']['browseEndpoint']['browseId']
        'VLRDCLAK5uy_ktv79aJ_zAi049KdFWFaAZEfgnm5jNZpk'
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_PLAYLIST,
        params = \
        {
            'list': list,
        },
    )

'''
Module containing the method: page_hotlist
'''

from .. import constants

def page_hotlist(self: object) -> dict:
    '''
    Return page configuration data for: Hotlist.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance

    Returns:
        Hotlist page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_hotlist()
        >>>
        >>> data['INITIAL_ENDPOINT']['browseEndpoint']['browseId']
        'FEmusic_trending'
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_HOTLIST,
    )

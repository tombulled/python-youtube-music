'''
Module containing the method: page_home
'''

from .. import constants

def page_home(self: object) -> dict:
    '''
    Return page configuration data for: Home.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance

    Returns:
        Home page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_home()
        >>>
        >>> data['INITIAL_ENDPOINT']['browseEndpoint']['browseId']
        'FEmusic_home'
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_HOME,
    )

'''
Module containing the method: browse_home
'''

from .. import constants

def browse_home(self: object) -> dict:
    '''
    Return browse data for: Home.

    See help for the 'browse' method for more information

    Args:
        self: Class instance

    Returns:
        Home browse data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_home()
        >>>
        >>> tabs = data['contents']['singleColumnBrowseResultsRenderer']['tabs']
        >>> tab = tabs[0]['tabRenderer']
        >>>
        >>> tab['title']
        'Home'
        >>>
    '''

    return self.browse \
    (
        browse_id = constants.BROWSE_ID_HOME,
    )

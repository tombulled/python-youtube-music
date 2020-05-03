'''
Module containing the method: browse_hotlist
'''

from .. import constants

def browse_hotlist(self: object) -> dict:
    '''
    Return browse data for: Hotlist.

    See help for the 'browse' method for more information

    Args:
        self: Class instance

    Returns:
        Hotlist browse data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> tabs = data['contents']['singleColumnBrowseResultsRenderer']['tabs']
        >>> tab = tabs[0]['tabRenderer']
        >>>
        >>> tab['title']
        'Hotlist'
        >>>
    '''

    return self.browse \
    (
        browse_id = constants.BROWSE_ID_HOTLIST,
    )

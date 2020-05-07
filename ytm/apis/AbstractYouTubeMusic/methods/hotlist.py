'''
Module containing the method: hotlist
'''

from .. import decorators
from .... import parsers

@decorators.method(parsers.hotlist)
def hotlist(self: object):
    '''
    Fetch Hotlist data.

    Args:
        self: Class Instance

    Returns:
        Hotlist data.

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> hotlist = api.hotlist()
        >>>
        >>> hotlist[0]['name']
        'Rosa'
        >>>
    '''

    return self._base.browse_hotlist()

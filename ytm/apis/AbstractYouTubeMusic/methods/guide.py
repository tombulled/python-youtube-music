'''
Module containing the method: guide
'''

from .. import decorators
from .... import parsers

@decorators.method(parsers.guide)
def guide(self: object) -> dict:
    '''
    Fetch Guide data.

    Args:
        self: Class Instance

    Returns:
        Guide data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> guide = api.guide()
        >>>
        >>> guide['Home']
        'FEmusic_home'
        >>>
    '''

    return self._base.guide()

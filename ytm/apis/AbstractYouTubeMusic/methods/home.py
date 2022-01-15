'''
Module containing the method: home
'''

from .. import decorators
from .... import parsers
from ....types import HomeContinuation

@decorators.method(parsers.home)
def home(self: object, continuation: HomeContinuation = None) -> dict:
    '''
    Fetch Home data.

    Args:
        self: Class Instance
        continuation: Home Continuation
            Example: '4qmFsgKIARIMRkVtdXNpY19ob21lGnhDQU42VmtOcVJVRkJSMVoxUV...'

    Returns:
        Home data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> home = api.home()
        >>>
        >>> home['shelves'][0]['name']
        'Morning sunshine'
        >>>
        >>> # Fetch more home data
        >>> more_home = api.home(home['continuation'])
        >>>
        >>> more_home['shelves'][0]['name']
        'Beast mode'
        >>>
    '''

    if continuation:
        return self._base.browse \
        (
            continuation = str(continuation),
        )
    else:
        return self._base.browse_home()

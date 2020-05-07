'''
Module containing the method: search_videos
'''

from .. import decorators
from .... import constants
from ....types import SearchContinuation

@decorators.method()
def search_videos \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    Perform a search for only Videos.

    Args:
        self: Class Instance
        query: Search query
            Example: 'about a girl'
        continuation: Search Continuation
            Example: 'Eo0GEghpbiB1dGVybxqABkVnLUtBUXdJQUJBQUdBRWdBQ2dBTUFCSUZ...'

    Returns:
        Videos search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search_videos('about a girl')
        >>> 
        >>> data['items'][0]['name']
        'About a Girl (MTV Unplugged)'
        >>>
        >>> more_data = api.search_videos(continuation = data['continuation'])
        >>>
        >>> more_data['items'][0]['name']
        'Nirvana - About A Girl [BBC Sessions]'
        >>>
    '''

    return self._search_filter \
    (
        filter       = constants.SEARCH_FILTER_VIDEOS,
        query        = query,
        continuation = continuation,
    )

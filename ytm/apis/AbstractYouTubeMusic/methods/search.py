'''
Module containing the method: search
'''

from .. import decorators
from .... import parsers

@decorators.method(parsers.search)
def search(self: object, query: str) -> dict:
    '''
    Fetch Search data.

    Args:
        self: Class Instance
        query: Search query
            Example: 'down by the river'

    Returns:
        Search data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.search('down by the river')
        >>>
        >>> top_result = data['top_result']
        >>> top_result
        'video'
        >>>
        >>> data[top_result + 's'][0]['name']
        'Down by the River'
        >>>
    '''

    return self._base.search \
    (
        query = query,
    )

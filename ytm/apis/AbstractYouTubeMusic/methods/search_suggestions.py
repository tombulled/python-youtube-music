'''
Module containing the method: search_suggestions
'''

from .. import decorators
from .... import parsers

@decorators.method(parsers.search_suggestions)
def search_suggestions(self: object, query: str) -> list:
    '''
    Retrieve search suggestions.

    Args:
        self: Class Instance
        query: Search query
            Example: 'imagine'

    Returns:
        List of search suggestions

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> suggestions = api.search_suggestions('imagine')
        >>>
        >>> suggestions[0]
        'imagine dragons'
        >>>
    '''

    return self._base.search_suggestions \
    (
        query = query
    )

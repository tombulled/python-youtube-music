'''
Module containing the method: page_search
'''

from .. import constants

def page_search(self: object, q: str) -> dict:
    '''
    Return page configuration data for: Search.

    Page configuration data will contain player information and the initial
    endpoint

    Args:
        self: Class instance
        q: Search query
            Example: 'foo fighters'

    Returns:
        Search page configuration data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.page_search('foo fighters')
        >>>
        >>> data['INITIAL_ENDPOINT']['searchEndpoint']
        {'query': 'foo fighters'}
        >>>
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_SEARCH,
        params = \
        {
            'q': q,
        },
    )

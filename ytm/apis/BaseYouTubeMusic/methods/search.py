'''
Module containing the method: search
'''

import copy
from .. import constants
from .. import decorators

@decorators.catch
def search \
        (
            self:         object,
            query:        str = None,
            params:       str = None,
            continuation: str = None,
        ) -> dict:
    '''
    Return search data.

    Returns results for a search

    Args:
        self: Class instance
        query: Search query string
            Example: 'coldplay'
        params: Search params
            Example: 'Eg-KAQwIABAAGAAgASgAMABqChAKEAMQCRAEEAU%3D'
            Note: These are used to filter search results, e.g. only artists
        continuation: Search continuation
            Example: 'Eo0GEghjb2xkcGxheRqABkVnLUtBUXdJQUJBQUdBQWdBU2d...'

    Returns:
        Search data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.search('foo f')
        >>>
        >>> shelves = data['contents']['sectionListRenderer']['contents']
        >>>
        >>> for shelf in shelves:
        	shelf = shelf['musicShelfRenderer']
        	print(shelf['title'])

        {'runs': [{'text': 'Top result'}]}
        {'runs': [{'text': 'Songs'}]}
        {'runs': [{'text': 'Albums'}]}
        {'runs': [{'text': 'Videos'}]}
        {'runs': [{'text': 'Playlists'}]}
        {'runs': [{'text': 'Artists'}]}
        >>>
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_SEARCH)

    url_params = copy.deepcopy(self._params)
    payload    = copy.deepcopy(self._payload)

    if continuation:
        url_params['continuation'] = continuation

    if not query:
        query = ''

    payload['query'] = query

    if params:
        payload['params'] = params
    else:
        payload['suggestStats'] = \
        {
            'clientName': 'youtube-music',
            'inputMethod': 'KEYBOARD',
            'originalQuery': query,
            'parameterValidationStatus': 'VALID_PARAMETERS',
            'searchMethod': 'ENTER_KEY',
            'validationStatus': 'VALID',
            'zeroPrefixEnabled': True,
        }

    resp = self._session.post \
    (
        url    = url,
        params = url_params,
        json   = payload,
    )

    data = resp.json()

    return data

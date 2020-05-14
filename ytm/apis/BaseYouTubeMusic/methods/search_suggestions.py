'''
Module containing the method: search_suggestions
'''

from .. import constants
from .. import decorators
from typing import List

@decorators.catch
def search_suggestions(self: object, query: str = None) -> List[str]:
    '''
    Retrieve search suggestions for a query.

    Args:
        self: Class instance
        query: Search query string
            Example: 'foo f'

    Returns:
        List of search suggestions

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.search_suggestions('foo f')
        >>>
        >>> suggestions = data['contents'][0]['searchSuggestionsSectionRenderer']['contents']
        >>>
        >>> for suggestion in suggestions:
        	suggestion = suggestion['searchSuggestionRenderer']
        	print(suggestion['suggestion'])

        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters everlong'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters learn to fly'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters times like these'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters best of you'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters live'}]}
        {'runs': [{'text': 'foo f', 'bold': True}, {'text': 'ighters pretender'}]}
        >>>
    '''

    resp = self._session.post \
    (
        url    = self._url_api(constants.ENDPOINT_YTM_API_SEARCH_SUGGESTIONS),
        params = self._params,
        json   = \
        {
            **self._payload,
            'input': query or '',
        },
    )

    data = resp.json()

    return data

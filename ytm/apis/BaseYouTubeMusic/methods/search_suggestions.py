'''
'''

from .. import constants
from .. import decorators
from typing import List

@decorators.catch
def search_suggestions(self: object, query: str = None) -> List[str]:
    '''
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_SEARCH_SUGGESTIONS)

    params  = constants.URL_PARAMS
    payload = constants.PAYLOAD

    payload['input'] = query or ''

    resp = self.session.post \
    (
        url    = url,
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data

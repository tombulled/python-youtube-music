'''
'''

from . import constants
from . import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.catch
def search \
        (
            self:         object,
            query:        str = None,
            params:       str = None,
            continuation: str = None,
        ) -> dict:
    '''
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_SEARCH)

    url_params = constants.URL_PARAMS
    payload    = constants.PAYLOAD

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

    resp = self.session.post \
    (
        url = url,
        params = url_params,
        json = payload,
    )

    data = resp.json()

    return data

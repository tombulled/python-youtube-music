'''
'''

from . import constants
from . import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.catch
def browse \
        (
            self:         object,
            browse_id:    str = None,
            page_type:    str = None,
            continuation: str = None,
            params:       str = None,
        ) -> dict:
    '''
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_BROWSE)

    request_params = constants.URL_PARAMS

    if continuation:
        request_params['continuation'] = continuation
        request_params['ctoken']       = continuation

    payload = constants.PAYLOAD

    if browse_id:
        payload['browseId'] = browse_id

    if params:
        payload['params'] = params

    if page_type:
        payload['browseEndpointContextSupportedConfigs'] = \
        {
            'browseEndpointContextMusicConfig': \
            {
                'pageType': page_type,
            }
        }

    resp = self.session.post \
    (
        url    = url,
        params = request_params,
        json   = payload,
    )

    data = resp.json()

    return data

'''
'''

from . import constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def guide(self: object) -> dict:
    '''
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_GUIDE)

    params  = constants.URL_PARAMS
    payload = constants.PAYLOAD

    resp = self.session.post \
    (
        url    = url,
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data

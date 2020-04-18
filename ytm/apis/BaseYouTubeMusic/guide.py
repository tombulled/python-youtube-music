'''
'''

from ... import constants as ytm_constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def guide(self: object) -> dict:
    '''
    '''
    
    url = self._url_api(ytm_constants.ENDPOINT_YTM_API_GUIDE)

    params  = ytm_constants.URL_PARAMS
    payload = ytm_constants.PAYLOAD

    resp = self.session.post \
    (
        url    = url,
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data

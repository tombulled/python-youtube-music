from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def search(self, query=None, params=None, continuation=None):
    url = self._url_api(ytm_constants.ENDPOINT_YTM_API_SEARCH)

    url_params = ytm_constants.URL_PARAMS
    payload    = ytm_constants.PAYLOAD

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

    resp = self.session.post(url, params=url_params, json=payload)

    data = resp.json()

    return data

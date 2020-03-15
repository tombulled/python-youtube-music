from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def browse(self, browse_id=None, page_type=None, continuation=None):
    url = self._url_api(ytm_constants.ENDPOINT_YTM_API_BROWSE)
    params = ytm_constants.URL_PARAMS

    if continuation:
        params['continuation'] = continuation
        params['ctoken']       = continuation

    payload = ytm_constants.PAYLOAD

    if browse_id:
        payload['browseId'] = browse_id

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
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data

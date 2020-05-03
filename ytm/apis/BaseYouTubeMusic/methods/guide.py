'''
Module containing the method: guide
'''

import copy
from .. import constants
from .. import decorators

@decorators.catch
def guide(self: object) -> dict:
    '''
    Return guide data.

    Guide data returns tab browse id's

    Args:
        self: Class instance

    Returns:
        Guide data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.guide()
        >>>
        >>> pivot_items = data['items'][0]['pivotBarRenderer']['items']
        >>>
        >>> for pivot_item in pivot_items:
            pivot_item = pivot_item['pivotBarItemRenderer']
            print(pivot_item['pivotIdentifier'])

        FEmusic_home
        FEmusic_trending
        FEmusic_liked
        >>>
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_GUIDE)

    params  = copy.deepcopy(constants.URL_PARAMS)
    payload = copy.deepcopy(constants.PAYLOAD)

    resp = self.session.post \
    (
        url    = url,
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data

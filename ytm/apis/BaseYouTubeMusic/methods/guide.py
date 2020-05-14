'''
Module containing the method: guide
'''

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

    resp = self._session.post \
    (
        url    = self._url_api(constants.ENDPOINT_YTM_API_GUIDE),
        params = self._params,
        json   = self._payload,
    )

    data = resp.json()

    return data

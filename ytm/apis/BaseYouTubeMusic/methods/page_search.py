'''
'''

from .. import constants

def page_search(self: object, q: str) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_SEARCH,
        params = \
        {
            'q': q,
        },
    )

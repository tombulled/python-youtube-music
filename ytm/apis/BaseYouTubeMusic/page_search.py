'''
'''

from ... import constants as ytm_constants

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def page_search(self: object, q: str) -> dict:
    '''
    '''
    
    return self._get_page \
    (
        endpoint = ytm_constants.ENDPOINT_YTM_SEARCH,
        params = \
        {
            'q': q,
        },
    )

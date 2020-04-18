'''
'''

from ... import constants as ytm_constants
from . import utils

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def page_watch(self: object, v: str, list: str = None) -> dict:
    '''
    '''

    return self._get_page \
    (
        endpoint = ytm_constants.ENDPOINT_YTM_WATCH,
        params = utils.filter_dict \
        (
            {
                'v':    v,
                'list': list,
            }
        ),
    )

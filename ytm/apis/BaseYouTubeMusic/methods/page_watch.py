'''
'''

from .. import constants
from .. import utils

def page_watch(self: object, v: str, list: str = None) -> dict:
    '''
    '''

    return self._get_page \
    (
        constants.ENDPOINT_YTM_WATCH,
        params = utils.filter \
        (
            {
                'v':    v,
                'list': list,
            }
        ),
    )

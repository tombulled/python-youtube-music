'''
'''

from .. import utils
from .. import constants

@staticmethod
def _url_api(*endpoints: str, params: dict = None) -> str:
    '''
    '''

    return utils.url_ytm \
    (
        constants.ENDPOINT_YTM_API,
        *endpoints,
        params = params,
    )

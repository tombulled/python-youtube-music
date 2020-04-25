'''
'''

from .. import utils

@staticmethod
def _url_yt(*endpoints: str, params: dict = None) -> str:
    '''
    '''

    return utils.url_yt \
    (
        *endpoints,
        params = params,
    )

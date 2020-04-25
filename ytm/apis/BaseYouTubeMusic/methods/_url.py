'''
'''

from .. import utils

@staticmethod
def _url(*endpoints: str, params: dict = None) -> str:
    '''
    '''

    return utils.url_ytm \
    (
        *endpoints,
        params = params,
    )

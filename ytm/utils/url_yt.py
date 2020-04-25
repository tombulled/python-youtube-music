'''
'''

from .. import constants
from ._url import _url

def url_yt(*endpoints: str, params: dict = None) -> str:
    '''
    '''

    return _url \
    (
        protocol  = constants.PROTOCOL_YOUTUBE,
        domain    = constants.DOMAIN_YOUTUBE,
        endpoints = endpoints,
        params    = params,
    )

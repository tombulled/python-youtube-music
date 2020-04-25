'''
'''

from .. import constants
from ._url import _url

def url_ytm(*endpoints: str, params: dict = None) -> str:
    '''
    '''

    return _url \
    (
        protocol  = constants.PROTOCOL_YOUTUBE_MUSIC,
        domain    = constants.DOMAIN_YOUTUBE_MUSIC,
        endpoints = endpoints,
        params    = params,
    )

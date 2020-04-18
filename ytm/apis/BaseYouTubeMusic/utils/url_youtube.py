'''
'''

from .. import constants

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def url_youtube(endpoint:str = None) -> str:
    '''
    '''

    return '{protocol}://{domain}/{endpoint}'.format \
    (
        protocol = constants.PROTOCOL_YOUTUBE,
        domain   = constants.DOMAIN_YOUTUBE,
        endpoint = endpoint or '',
    )

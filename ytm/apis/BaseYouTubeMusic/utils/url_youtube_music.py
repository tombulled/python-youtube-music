'''
'''

from .. import constants

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def url_youtube_music(endpoint: str = None) -> str:
    '''
    '''

    return '{protocol}://{domain}/{endpoint}'.format \
    (
        protocol = constants.PROTOCOL_YOUTUBE_MUSIC,
        domain   = constants.DOMAIN_YOUTUBE_MUSIC,
        endpoint = endpoint or '',
    )

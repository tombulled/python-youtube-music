''' xxx '''

from .. import constants

__all__ = __name__.split('.')[-1:]

def url_youtube_music(endpoint=''):
    url = '{protocol}://{domain}/{endpoint}'.format \
    (
        protocol = constants.PROTOCOL_YOUTUBE_MUSIC,
        domain   = constants.DOMAIN_YOUTUBE_MUSIC,
        endpoint = endpoint,
    )

    return url

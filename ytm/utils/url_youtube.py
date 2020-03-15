''' xxx '''

from .. import constants

__all__ = __name__.split('.')[-1:]

def url_youtube(endpoint=''):
    url = '{protocol}://{domain}/{endpoint}'.format \
    (
        protocol = constants.PROTOCOL_YOUTUBE,
        domain   = constants.DOMAIN_YOUTUBE,
        endpoint = endpoint,
    )

    return url

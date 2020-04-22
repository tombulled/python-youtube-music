from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class ArtistSinglesContinuation(BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            '6gPTAUNwc0JDbndLYlFBQVpXNEFBVWRDQUFGSFFnQUJBRVpGYlhWemFXTmZaR',
            '1YwWVdsc1gyRnlkR2x6ZEFBQkFBQUJBQUFBQVFBQkFBQUJBUW',
            'k4',
            'QXhvWVZVT',
            utils.entropy \
            (
                length = 39,
                name   = 'b64_artist_id',
            ),
            'Z2dFWVZVT',
            utils.group('b64_artist_id'),
            'QUFFU',
            utils.entropy(11),
            'NkFJYUFuZHpHQUFxRDJGeWRHbHpkRjl5Wld4bFlYTmxjekN4MU5EbGxfSEo4',
            'bkE%3D',
        ),
    )

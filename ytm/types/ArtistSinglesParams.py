from . import base
from . import utils

class ArtistSinglesParams(base.BaseType):
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
            utils.entropy(13),
            'FJYUFuZHpHQUFxRDJGeWRHbHpkRjl5Wld4bFlYTmxjekN4MU5EbGxfSEo4',
            'bkE%3D',
        ),
    )

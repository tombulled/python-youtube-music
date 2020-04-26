from . import base
from . import utils

class AlbumPlaylistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional('RDAMPL'),
            'OLAK5uy_',
            utils.entropy(33),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, 'RDAMPL')

        return value

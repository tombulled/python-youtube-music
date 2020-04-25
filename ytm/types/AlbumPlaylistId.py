from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

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

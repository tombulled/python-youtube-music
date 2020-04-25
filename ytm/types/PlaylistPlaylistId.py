from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistPlaylistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional
            (
                'VL',
                'RDAMPL',
            ),
            'RDCLAK5uy_',
            utils.entropy(33),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, 'VL')
        value = utils.lstrip(value, 'RDAMPL')

        return value

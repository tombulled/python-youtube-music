from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistPlaylistId(BaseType):
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
        value = utils.left_strip('VL')
        value = utils.left_strip('RDAMPL')

        return value

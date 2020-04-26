from . import base
from . import utils

class ChartPlaylistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional \
            (
                'VL',
                'RDAMPL',
            ),
            'PL',
            utils.entropy(32),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, 'VL')
        value = utils.lstrip(value, 'RDAMPL')

        return value

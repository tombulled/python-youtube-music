from . import base
from . import utils

class SongId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional('RDAMVM'),
            utils.entropy(11),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, 'RDAMVM')

        return value

from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

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

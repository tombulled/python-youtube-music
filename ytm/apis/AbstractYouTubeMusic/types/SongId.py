from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class SongId(BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.entropy(11),
        ),
    )

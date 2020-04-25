from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class ArtistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'UC',
            utils.entropy(22),
        ),
    )

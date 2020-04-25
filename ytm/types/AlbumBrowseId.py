from . import base
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class AlbumBrowseId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'MPREb_',
            utils.entropy(11),
        ),
    )

from . import base
from . import utils

class AlbumId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'MPREb_',
            utils.entropy(11),
        ),
    )

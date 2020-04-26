from . import base
from . import utils

class ArtistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'UC',
            utils.entropy(22),
        ),
    )

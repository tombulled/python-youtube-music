from . import base
from . import utils

class ArtistRadioId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'RDEM',
            utils.entropy(22),
        ),
    )

from . import base
from . import utils

class ArtistShuffleId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            'RDAO',
            utils.entropy(22),
        ),
    )

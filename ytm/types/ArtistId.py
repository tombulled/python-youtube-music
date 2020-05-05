from . import base
from . import utils
from . import constants

class ArtistId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            constants.PREFIX_ARTIST_ID,
            utils.entropy(constants.LEN_ENTROPY_ARTIST_ID),
        ),
    )

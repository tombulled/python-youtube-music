from . import base
from . import utils
from . import constants

class AlbumId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            constants.PREFIX_ALBUM_ID,
            utils.entropy(constants.LEN_ENTROPY_ALBUM_ID),
        ),
    )

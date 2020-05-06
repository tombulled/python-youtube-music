from .. import base
from .. import constants

class SongId(base.Id):
    _pattern = '^(?P<prefix>{prefixes})?(?P<data>[{chars}]{{{length}}})$'.format \
    (
        prefixes = constants.PREFIX_SONG_RADIO_ID,
        chars    = constants.CHARS_ID,
        length   = constants.LEN_SONG_ID,
    )

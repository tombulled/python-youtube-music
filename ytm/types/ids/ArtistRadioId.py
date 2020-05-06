from .. import base
from .. import constants

class ArtistRadioId(base.Id):
    _pattern = '^(?P<prefix>{prefixes})(?P<data>[{chars}]{{{entropy_length}}})$'.format \
    (
        prefixes       = '|'.join \
        (
            (
                constants.PREFIX_ARTIST_RADIO_ID,
                constants.PREFIX_ARTIST_SHUFFLE_ID,
            ),
        ),
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ARTIST_ID,
    )

    @classmethod
    def _clean(cls, value: str):
        return constants.PREFIX_ARTIST_RADIO_ID + value

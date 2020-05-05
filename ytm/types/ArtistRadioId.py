from . import base
from . import utils
from . import constants

class ArtistRadioId(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            utils.optional \
            (
                constants.PREFIX_ARTIST_RADIO_ID,
                constants.PREFIX_ARTIST_SHUFFLE_ID,
            ),
            utils.entropy(constants.LEN_ENTROPY_ARTIST_ID),
        ),
    )

    @classmethod
    def _clean(cls, value: str):
        value = utils.lstrip(value, constants.PREFIX_ARTIST_RADIO_ID)
        value = utils.lstrip(value, constants.PREFIX_ARTIST_SHUFFLE_ID)

        value = constants.PREFIX_ARTIST_RADIO_ID + value

        return value

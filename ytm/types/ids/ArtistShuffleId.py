from .ArtistRadioId import ArtistRadioId
from .. import constants

class ArtistShuffleId(ArtistRadioId):
    @classmethod
    def _clean(cls: type, value: str) -> str:
        return constants.PREFIX_ARTIST_SHUFFLE_ID + value

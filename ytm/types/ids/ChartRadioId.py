from .ChartPlaylistId import ChartPlaylistId
from .. import constants

class ChartRadioId(ChartPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        return constants.PREFIX_PLAYLIST_RADIO_ID + value

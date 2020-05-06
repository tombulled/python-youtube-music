from .PlaylistId import PlaylistId
from .. import constants

class PlaylistRadioId(PlaylistId):
    @classmethod
    def _clean(cls, value: str):
        return constants.PREFIX_PLAYLIST_RADIO_ID + super()._clean(value)

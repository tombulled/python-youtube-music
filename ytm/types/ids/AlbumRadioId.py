from .AlbumPlaylistId import AlbumPlaylistId
from .. import constants

class AlbumRadioId(AlbumPlaylistId):
    @classmethod
    def _clean(cls: type, value: str) -> dict:
        return constants.PREFIX_PLAYLIST_RADIO_ID + value

from .AlbumPlaylistId import AlbumPlaylistId
from . import constants

class AlbumRadioId(AlbumPlaylistId):
    @classmethod
    def _clean(cls: type, value: str) -> str:
        return constants.PREFIX_ALBUM_RADIO_ID + super()._clean(value)

from .ChartPlaylistId import ChartPlaylistId
from .. import constants

class ChartPlaylistBrowseId(ChartPlaylistId):
    @classmethod
    def _clean(cls: type, value: str) -> str:
        return constants.PREFIX_PLAYLIST_BROWSE_ID + value

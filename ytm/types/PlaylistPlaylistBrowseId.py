from .PlaylistPlaylistId import PlaylistPlaylistId

class PlaylistPlaylistBrowseId(PlaylistPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'VL' + value

        return value

from .PlaylistId import PlaylistId

class PlaylistBrowseId(PlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'VL' + value

        return value

from .ChartPlaylistId import ChartPlaylistId

class ChartPlaylistBrowseId(ChartPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'VL' + value

        return value

from .ChartPlaylistId import ChartPlaylistId

class ChartRadioId(ChartPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMPL' + value

        return value

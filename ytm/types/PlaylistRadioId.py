from .PlaylistId import PlaylistId

class PlaylistRadioId(PlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMPL' + value

        return value

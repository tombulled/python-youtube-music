from .PlaylistPlaylistId import PlaylistPlaylistId

class PlaylistRadioId(PlaylistPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMPL' + value

        return value

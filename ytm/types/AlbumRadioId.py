from .AlbumPlaylistId import AlbumPlaylistId

class AlbumRadioId(AlbumPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMPL' + value

        return value

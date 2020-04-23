from .AlbumPlaylistId import AlbumPlaylistId

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class AlbumRadioId(AlbumPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'RDAMPL' + value

        return value

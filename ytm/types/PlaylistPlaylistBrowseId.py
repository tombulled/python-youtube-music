from .PlaylistPlaylistId import PlaylistPlaylistId

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistPlaylistBrowseId(PlaylistPlaylistId):
    @classmethod
    def _clean(cls, value: str):
        value = super()._clean(value)

        value = 'VL' + value

        return value

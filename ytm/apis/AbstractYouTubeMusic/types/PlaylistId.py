from .BaseType import BaseType

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistId(BaseType):
    _patterns = \
    (
        r'^(VL)?PL[a-zA-Z0-9_-]{32}$', # ChartPlaylistId, ArtistSongsPlaylistId
        r'^(VL)?RDCLAK5uy_[a-zA-Z0-9_-]{33}$', # PlaylistListId
    )

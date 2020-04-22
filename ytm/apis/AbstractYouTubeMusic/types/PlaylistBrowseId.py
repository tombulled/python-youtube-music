from .BaseType import BaseType

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistBrowseId(BaseType):
    _patterns = \
    (
        r'^VLPL[a-zA-Z0-9_-]{32}$',         # ChartPlaylistBrowseId, ArtistSongsPlaylistBrowseId
        r'^VLRDCLAK5uy_[a-zA-Z0-9_-]{33}$', # PlaylistListBrowseId
    )

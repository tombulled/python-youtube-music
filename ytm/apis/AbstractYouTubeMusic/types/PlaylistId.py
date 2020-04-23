from .BaseType import BaseType
from .ChartPlaylistId import ChartPlaylistId
from .ArtistSongsPlaylistId import ArtistSongsPlaylistId
from .PlaylistPlaylistId import PlaylistPlaylistId
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistId(BaseType):
    _patterns = utils.patterns \
    (
        ChartPlaylistId,
        ArtistSongsPlaylistId,
        PlaylistPlaylistId,
    )

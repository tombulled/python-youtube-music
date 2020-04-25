from . import base
from .ChartPlaylistBrowseId import ChartPlaylistBrowseId
from .ArtistSongsPlaylistBrowseId import ArtistSongsPlaylistBrowseId
from .PlaylistPlaylistBrowseId import PlaylistPlaylistBrowseId
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class PlaylistBrowseId(base.BaseType):
    _patterns = utils.patterns \
    (
        ChartPlaylistBrowseId,
        ArtistSongsPlaylistBrowseId,
        PlaylistPlaylistBrowseId,
    )

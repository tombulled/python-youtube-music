from . import base
from .ChartPlaylistBrowseId import ChartPlaylistBrowseId
from .ArtistSongsPlaylistBrowseId import ArtistSongsPlaylistBrowseId
from .PlaylistPlaylistBrowseId import PlaylistPlaylistBrowseId
from . import utils

class PlaylistBrowseId(base.BaseType):
    _patterns = utils.patterns \
    (
        ChartPlaylistBrowseId,
        ArtistSongsPlaylistBrowseId,
        PlaylistPlaylistBrowseId,
    )

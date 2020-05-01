from . import base
from .ChartPlaylistId import ChartPlaylistId
from .ArtistSongsPlaylistId import ArtistSongsPlaylistId
from .PlaylistPlaylistId import PlaylistPlaylistId
from . import utils

class PlaylistId(base.BaseType):
    _patterns = utils.patterns \
    (
        ChartPlaylistId,
        ArtistSongsPlaylistId,
        PlaylistPlaylistId,
    )

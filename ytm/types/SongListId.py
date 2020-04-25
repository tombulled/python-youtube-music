from . import base
from . import utils
from .ChartPlaylistId import ChartPlaylistId
from .ChartRadioId import ChartRadioId
from .ChartShuffleId import ChartShuffleId
from .ArtistSongsPlaylistId import ArtistSongsPlaylistId
from .ArtistSongsRadioId import ArtistSongsRadioId
from .ArtistSongsShuffleId import ArtistSongsShuffleId
from .ArtistRadioId import ArtistRadioId
from .ArtistShuffleId import ArtistShuffleId
from .PlaylistPlaylistId import PlaylistPlaylistId
from .PlaylistRadioId import PlaylistRadioId
from .PlaylistShuffleId import PlaylistShuffleId
from .AlbumPlaylistId import AlbumPlaylistId
from .AlbumRadioId import AlbumRadioId
from .AlbumShuffleId import AlbumShuffleId
from .SongRadioId import SongRadioId
from .SongShuffleId import SongShuffleId

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class SongListId(base.BaseType):
    _patterns = utils.patterns \
    (
        ChartPlaylistId,
        ChartRadioId,
        ChartShuffleId,
        ArtistSongsPlaylistId,
        ArtistSongsRadioId,
        ArtistSongsShuffleId,
        ArtistRadioId,
        ArtistShuffleId,
        PlaylistPlaylistId,
        PlaylistRadioId,
        PlaylistShuffleId,
        AlbumPlaylistId,
        AlbumRadioId,
        AlbumShuffleId,
        SongRadioId,
        SongShuffleId,
    )

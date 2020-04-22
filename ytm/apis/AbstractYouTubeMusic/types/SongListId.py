from .BaseType import BaseType

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class SongListId(BaseType):
    _patterns = \
    (
        r'^(RDAMPL)?PL[a-zA-Z0-9_-]{32}$',         # ChartPlaylistId, ChartRadioPlaylistId, ArtistSongsId, ArtistSongsRadioPlaylistId
        r'^(RDAMPL)?RDCLAK5uy_[a-zA-Z0-9_-]{33}$', # PlaylistListId, PlaylistRadioPlaylistBrowseId
        r'^(RDAMPL)?OLAK5uy_[a-zA-Z0-9_-]{33}$'    # AlbumPlaylistId, AlbumRadioPlaylistBrowseId
        r'^RDAMVM[a-zA-Z0-9_-]{11}$',              # SongRadioPlaylistBrowseId, SongShufflePlaylistBrowseId
        r'^RDAO[a-zA-Z0-9_-]{22}$',                # ArtistShufflePlaylistBrowseId
        r'^RDEM[a-zA-Z0-9_-]{22}$',                # ArtistRadioPlaylistBrowseId
    )

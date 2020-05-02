from .. import decorators
from .... import parsers
from .... import utils
from .... import types
from ....types import \
(
    Union,
    SongId,
    Params,
    WatchContinuation,
    ChartPlaylistId,
    ChartPlaylistBrowseId,
    ChartRadioId,
    ChartShuffleId,
    ArtistSongsPlaylistId,
    ArtistSongsPlaylistBrowseId,
    ArtistSongsRadioId,
    ArtistSongsShuffleId,
    ArtistRadioId,
    ArtistShuffleId,
    PlaylistId,
    PlaylistBrowseId,
    PlaylistRadioId,
    PlaylistShuffleId,
    AlbumPlaylistId,
    AlbumPlaylistBrowseId,
    AlbumRadioId,
    AlbumShuffleId,
    SongRadioId,
)

@decorators.method(parsers.watch)
def watch \
        (
            self:         object,
            song_id:      SongId = None,
            playlist_id: Union \
            (
                ChartPlaylistId,
                ChartPlaylistBrowseId,
                ChartRadioId,
                ChartShuffleId,
                ArtistSongsPlaylistId,
                ArtistSongsPlaylistBrowseId,
                ArtistSongsRadioId,
                ArtistSongsShuffleId,
                ArtistRadioId,
                ArtistShuffleId,
                PlaylistId,
                PlaylistBrowseId,
                PlaylistRadioId,
                PlaylistShuffleId,
                AlbumPlaylistId,
                AlbumPlaylistBrowseId,
                AlbumRadioId,
                AlbumShuffleId,
                SongRadioId,
            ) = None,
            params:       Params            = None, # Is this relevant if radio and shuffle is covered?
            continuation: WatchContinuation = None,
        ) -> dict:
    '''
    '''

    type_map = \
    {
        types.ChartPlaylistBrowseId:       types.ChartPlaylistId,
        types.ArtistSongsPlaylistBrowseId: types.ArtistSongsPlaylistId,
        types.PlaylistBrowseId:            types.PlaylistId,
        types.AlbumPlaylistBrowseId:       types.AlbumPlaylistId,
    }

    for type_src, type_dst in type_map.items():
        if utils.isinstance(playlist_id, type_src):
            playlist_id = type_dst(playlist_id)

            break

    return self._base.next \
    (
        video_id     = song_id,
        playlist_id  = playlist_id,
        params       = params,
        continuation = continuation,
    )

'''
'''

from .. import decorators
from .. import constants
from .... import parsers
from .... import utils
from .... import types
from ....types import \
(
    Union,
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
)

@decorators.method(parsers.watch_shuffle)
def watch_shuffle \
        (
            self: object,
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
            ),
        ) -> dict:
    '''
    '''

    type_map = \
    {
        types.ChartShuffleId: \
        (
            types.ChartPlaylistId,
            types.ChartPlaylistBrowseId,
            types.ChartRadioId,
        ),
        types.ArtistSongsShuffleId: \
        (
            types.ArtistSongsPlaylistId,
            types.ArtistSongsPlaylistBrowseId,
            types.ArtistSongsRadioId,
        ),
        types.ArtistShuffleId: \
        (
            types.ArtistRadioId,
        ),
        types.PlaylistShuffleId: \
        (
            types.PlaylistId,
            types.PlaylistBrowseId,
            types.PlaylistRadioId,
        ),
        types.AlbumShuffleId: \
        (
            types.AlbumPlaylistId,
            types.AlbumPlaylistBrowseId,
            types.AlbumRadioId,
        ),
    }

    for type_target, type_sources in type_map.items():
        for type_source in type_sources:
            if utils.isinstance(playlist_id, type_source):
                playlist_id = type_target(playlist_id)

                break
        else:
            continue

        break

    return self._base.next \
    (
        playlist_id = playlist_id,
        params      = constants.PARAMS_SHUFFLE,
    )

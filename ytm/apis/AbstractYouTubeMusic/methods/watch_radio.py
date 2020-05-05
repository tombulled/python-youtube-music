'''
'''

from .. import decorators
from .... import constants
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
    SongRadioId,
    SongId,
)

@decorators.method(parsers.watch_radio)
def watch_radio \
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
                SongRadioId,
            ) = None,
            song_id: SongId = None,
        ) -> dict:
    '''
    '''

    type_map = \
    {
        types.ChartRadioId: \
        (
            types.ChartPlaylistId,
            types.ChartPlaylistBrowseId,
            types.ChartShuffleId,
        ),
        types.ArtistSongsRadioId: \
        (
            types.ArtistSongsPlaylistId,
            types.ArtistSongsPlaylistBrowseId,
            types.ArtistSongsShuffleId,
        ),
        types.ArtistRadioId: \
        (
            types.ArtistShuffleId,
        ),
        types.PlaylistRadioId: \
        (
            types.PlaylistId,
            types.PlaylistBrowseId,
            types.PlaylistShuffleId,
        ),
        types.AlbumRadioId: \
        (
            types.AlbumPlaylistId,
            types.AlbumPlaylistBrowseId,
            types.AlbumShuffleId,
        ),
    }

    if playlist_id is not None:
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
            params      = constants.PARAMS_RADIO,
        )
    elif song_id is not None:
        return self._base.next \
        (
            video_id      = song_id,
            params        = 'mgMDCNgE', # Make these constants
            player_params = 'igMDCNgE',
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'playlist_id\' or \'song_id\''
        )

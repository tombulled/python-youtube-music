'''
Module containing the method: watch_radio
'''

from .. import decorators
from .... import constants
from .... import parsers
from .... import utils
from .... import types
from ....types import \
(
    Union,
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
            song_id: SongId = None,
            playlist_id: Union \
            (
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
        ) -> dict:
    '''
    Fetch Radio Watch data.

    Use the watch() method to continue data.

    Args:
        self: Class Instance
        song_id: Song Id
            Example: '0nCYgT-rVSo'
        playlist_id: Playlist Id
            Example: 'RDEM8Tjy6KJDUmM5-nJ3baglrQ'

    Returns:
        Radio Watch data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.watch_radio(song_id = '0nCYgT-rVSo')
        >>>
        >>> data['tracks'][0]['name']
        'Cool with You'
        >>>
    '''

    type_map = \
    {
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
            params        = constants.PARAMS_RADIO_SONG,
            player_params = constants.PLAYER_PARAMS_RADIO_SONG,
            # should playlist_id be passed through as well?
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'playlist_id\' or \'song_id\''
        )

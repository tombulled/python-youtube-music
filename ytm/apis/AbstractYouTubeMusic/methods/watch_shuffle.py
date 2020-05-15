'''
Module containing the method: watch_shuffle
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
)

@decorators.method(parsers.watch_shuffle)
def watch_shuffle \
        (
            self: object,
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
            ),
        ) -> dict:
    '''
    Fetch Shuffle Watch data.

    Use the watch() method to continue data.

    Args:
        self: Class Instance
        playlist_id: Playlist Id
            Example: 'RDAODz952MrmDXLULMlo7SEXUw'
        song_id: Song Id
            Example: 'gyOF8CopyGo'

    Returns:
        Shuffle Watch data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.watch_shuffle('OLAK5uy_kEQJGO2SZ0k-vJ8b-F2AJLfKnw0cFydNg')
        >>>
        >>> data['tracks'][0]['name']
        'Come as You Are'
        >>>
    '''

    type_map = \
    {
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

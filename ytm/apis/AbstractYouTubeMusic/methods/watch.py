'''
Module containing the method: watch
'''

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
            playlist_id:  Union \
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
            params:       Params            = None, # Is this relevant if radio and shuffle is covered?
            continuation: WatchContinuation = None,
        ) -> dict:
    '''
    Fetch Watch data.

    Args:
        self: Class Instance
        song_id: Song Id
            Example: '0nCYgT-rVSo'
        playlist_id: Playlist Id
            Example: 'OLAK5uy_kEQJGO2SZ0k-vJ8b-F2AJLfKnw0cFydNg'
        params: Watch Params
            Example: 'wAEB'
        continuation: Watch Continuation
            Example: 'CBkSSBILLUIzOVdoVW5Pc0UiKFJEQU1QTFBMSGNkcGVKUEVJdDlRLX...'

    Returns:
        Watch data

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> data = api.watch('Rf3-KrGyw8U', 'OLAK5uy_le-wYvLezyD8DZ_n99oJJswSaobGTiGgA')
        >>>
        >>> data['tracks'][0]['name']
        'B.I.T.M.'
        >>>
    '''

    type_map = \
    {
        types.PlaylistBrowseId:            types.PlaylistId,
        types.AlbumPlaylistBrowseId:       types.AlbumPlaylistId,
    }

    for type_src, type_dst in type_map.items():
        if utils.isinstance(playlist_id, type_src):
            playlist_id = type_dst(playlist_id)

            break

    if song_id or playlist_id:
        return self._base.next \
        (
            video_id     = song_id,
            playlist_id  = playlist_id,
            params       = params,
        )
    elif continuation:
        return self._base.next \
        (
            continuation = continuation,
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'playlist_id\' or \'song_id\''
        )

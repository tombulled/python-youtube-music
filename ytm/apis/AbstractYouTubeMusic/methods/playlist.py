'''
Module containing the method: playlist
'''

from .. import decorators
from .... import parsers
from .... import types
from .... import utils
from ....types import \
(
    Union,
    PlaylistId,
    PlaylistBrowseId,
    PlaylistContinuation,
)

@decorators.method(parsers.playlist)
def playlist \
        (
            self: object,
            playlist_id: Union \
            (
                PlaylistId,
                PlaylistBrowseId,
            ) = None,
            continuation: PlaylistContinuation = None,
        ) -> dict:
    '''
    Fetch Playlist data.

    Args:
        self: Class Instance
        playlist_id: Playlist Id
            Example: 'RDCLAK5uy_nUi8B-S9ckz5feHM7oMGyQQ_eKW2Zl9aE'
        continuation: Playlist Continuation
            Example: '4qmFsgJbEi1WTFJEQ0xBSzV1eV9uVWk4Qi1TOWNrejVmZUhNN29NR3...'

    Returns:
        Playlist data.

    Raises:
        MethodError: Method encountered an error

    Example:
        >>> api = ytm.AbstractYouTubeMusic()
        >>>
        >>> playlist = api.playlist('RDCLAK5uy_nUi8B-S9ckz5feHM7oMGyQQ_eKW2Zl9aE')
        >>>
        >>> playlist['name']
        '00s Sing-Alongs'
        >>>
        >>> # More playlist data (only if it has 100+ tracks)
        >>> more_playlist = api.playlist(continuation = playlist['continuation'])
        >>>
        >>> more_playlist['tracks'][0]['name']
        'America'
        >>>
    '''

    if playlist_id is not None:
        if utils.isinstance(playlist_id, types.PlaylistId):
            playlist_browse_id = types.PlaylistBrowseId(playlist_id)
        else:
            playlist_browse_id = playlist_id

        return self._base.browse_playlist \
        (
            browse_id = playlist_browse_id,
        )
    elif continuation is not None:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        raise Exception \
        (
            'Missing 1 required argument: \'playlist_id\' or \'continuation\''
        )

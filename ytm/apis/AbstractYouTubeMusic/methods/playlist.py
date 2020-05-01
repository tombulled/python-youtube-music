# from .. import constants
from .. import decorators
from .... import parsers
# from .... import utils
from .... import types
# from ....types import PlaylistId, PlaylistContinuation
from ....types import \
(
    ChartPlaylistId,
    ChartPlaylistBrowseId,
    ArtistSongsPlaylistId,
    ArtistSongsPlaylistBrowseId,
    PlaylistId,
    PlaylistBrowseId,
    PlaylistContinuation,
)

@decorators.method(parsers.playlist)
def playlist \
        (
            self:         object,
            playlist_id:  PlaylistId           = None,
            continuation: PlaylistContinuation = None,
        ) -> dict:
    '''
    '''

    if playlist_id is not None:
        playlist_browse_id = types.PlaylistBrowseId(playlist_id)

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

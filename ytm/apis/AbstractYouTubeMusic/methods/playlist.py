from .. import decorators
from .... import parsers
from .... import types
from .... import utils
from ....types import \
(
    Union,
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
            self: object,
            playlist_id: Union \
            (
                ChartPlaylistId,
                ChartPlaylistBrowseId,
                ArtistSongsPlaylistId,
                ArtistSongsPlaylistBrowseId,
                PlaylistId,
                PlaylistBrowseId,
            ) = None,
            continuation: PlaylistContinuation = None,
        ) -> dict:
    '''
    '''

    if playlist_id is not None:
        if utils.isinstance(playlist_id, types.ChartPlaylistId):
            playlist_browse_id = types.ChartPlaylistBrowseId(playlist_id)
        elif utils.isinstance(playlist_id, types.ArtistSongsPlaylistId):
            playlist_browse_id = types.ArtistSongsPlaylistBrowseId(playlist_id)
        elif utils.isinstance(playlist_id, types.PlaylistId):
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

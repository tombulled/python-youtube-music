# from . import parser
from .. import parsers
from .. import constants
from .. import decorators
from .. import utils
from .. import types
from ..types import PlaylistId, PlaylistContinuation

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.playlist)
def playlist \
        (
            self:         object,
            playlist_id:  PlaylistId           = None,
            continuation: PlaylistContinuation = None,
        ) -> dict:
    '''
    '''

    assert any((playlist_id, continuation)), f'Missing 1 required argument: \'playlist_id\' or \'continuation\''

    if playlist_id is not None:
        if utils.isinstance(playlist_id, types.PlaylistBrowseId):
            prefix = ''
        else:
            prefix = constants.PREFIX_PLAYLIST

        browse_id = types.PlaylistBrowseId(f'{prefix}{playlist_id}')

        return self._base.browse_playlist \
        (
            browse_id = browse_id,
        )
    elif continuation is not None:
        return self._base.browse \
        (
            continuation = continuation,
        )

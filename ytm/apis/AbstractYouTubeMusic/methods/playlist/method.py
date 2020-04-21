from . import parser
from ... import constants
from ... import decorators
from ... import types
from ...types import PlaylistId, PlaylistContinuation

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method \
        (
            self:         object,
            playlist_id:  PlaylistId           = None,
            continuation: PlaylistContinuation = None,
        ) -> dict:
    '''
    '''

    assert any((playlist_id, continuation)), f'Missing 1 required argument: \'playlist_id\' or \'continuation\''

    if playlist_id is not None:
        if types.isinstance(playlist_id, types.PlaylistBrowseId):
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

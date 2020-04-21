from . import parser
from ... import utils
from ... import decorators
from ... import types
from ...types import AlbumId

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, id: AlbumId) -> dict:
    '''
    '''

    if types.isinstance(id, types.AlbumPlaylistId):
        page = self._base.page_playlist \
        (
            list = id,
        )

        browse_id = utils.get_nested \
        (
            page,
            'INITIAL_ENDPOINT',
            'browseEndpoint',
            'browseId',
        )
    elif types.isinstance(id, types.AlbumBrowseId):
        browse_id = id
    else:
        raise Exception(f'Invalid album id: {repr(id)}')

    browse_id = types.AlbumBrowseId(browse_id)

    return self._base.browse_album \
    (
        browse_id = browse_id,
    )

# from . import parser
from .. import parsers
from .. import utils
from .. import decorators
from .. import types
from ..types import AlbumId

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.album)
def album(self: object, id: AlbumId) -> dict:
    '''
    '''

    if utils.isinstance(id, types.AlbumPlaylistId):
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
    elif utils.isinstance(id, types.AlbumBrowseId):
        browse_id = id
    else:
        raise Exception(f'Invalid album id: {repr(id)}')

    browse_id = types.AlbumBrowseId(browse_id)

    return self._base.browse_album \
    (
        browse_id = browse_id,
    )

from .. import parsers
from .. import utils
from .. import decorators
from .. import types
from ..types import AlbumId

@decorators.method(parsers.album)
def album(self: object, album_id: AlbumId) -> dict:
    '''
    '''

    if utils.isinstance(album_id, types.AlbumPlaylistId):
        page = self._base.page_playlist \
        (
            list = album_id,
        )

        browse_id = utils.get \
        (
            page,
            'INITIAL_ENDPOINT',
            'browseEndpoint',
            'browseId',
        )
    elif utils.isinstance(album_id, types.AlbumBrowseId):
        browse_id = album_id
    else:
        raise Exception(f'Invalid album id: {repr(album_id)}')

    browse_id = types.AlbumBrowseId(browse_id)

    return self._base.browse_album \
    (
        browse_id = browse_id,
    )

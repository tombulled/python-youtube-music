from . import parser
from ... import utils
from ... import types
from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

AlbumId = types.AlbumId

@decorators.enforce()
@decorators.rename(__method__)
def method(self: object, id: AlbumId) -> dict:
    '''
    '''

    # id = types.AlbumId(id)

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

    browse_id = types.AlbumBrowseId(browse_id)

    data = self._base.browse_album \
    (
        browse_id = browse_id,
    )

    parsed_data = parser.parse(data)

    return parsed_data

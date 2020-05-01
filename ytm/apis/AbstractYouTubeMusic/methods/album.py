from .. import decorators
from .... import parsers
from .... import utils
from .... import types
from ....types import \
(
    # AlbumId,
    Union,
    AlbumPlaylistId,
    AlbumPlaylistBrowseId,
    AlbumBrowseId,
    AlbumId,
    AlbumRadioId,
    AlbumShuffleId,
)

@decorators.method(parsers.album)
# def album(self: object, album_id: AlbumId) -> dict:
def album \
        (
            self:     object,
            album_id: Union
            (
                AlbumPlaylistId,
                AlbumPlaylistBrowseId,
                AlbumBrowseId,
                AlbumId,
            ),
        ) -> dict:
    '''
    '''

    # if utils.isinstance(album_id, types.AlbumPlaylistId):
    #     page = self._base.page_playlist \
    #     (
    #         list = album_id,
    #     )
    #
    #     browse_id = utils.get \
    #     (
    #         page,
    #         'INITIAL_ENDPOINT',
    #         'browseEndpoint',
    #         'browseId',
    #     )
    # else:
    #     browse_id = album_id
    #
    # browse_id = types.AlbumBrowseId(browse_id)

    if utils.isinstance(album_id, types.AlbumBrowseId):
        browse_id = album_id
    else:
        album_id = types.AlbumPlaylistId(album_id)

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

        browse_id = types.AlbumBrowseId(browse_id)

    return self._base.browse_album \
    (
        browse_id = browse_id,
    )

from . import base
from .AlbumPlaylistId import AlbumPlaylistId
from .AlbumBrowseId import AlbumBrowseId
from . import utils

class AlbumId(base.BaseType):
    _patterns = utils.patterns \
    (
        AlbumPlaylistId,
        AlbumBrowseId,
    )

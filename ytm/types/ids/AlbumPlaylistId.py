'''
Module containing the Id type: AlbumPlaylistId
'''

from .. import base
from .. import constants

class AlbumPlaylistId(base.Id):
    '''
    Id class: AlbumPlaylistId

    Example:
        >>> id = AlbumPlaylistId('OLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ')
        >>>
        >>> id
        <AlbumPlaylistId('OLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ')>
        >>>
        >>> str(id)
        'OLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ'
        >>>
    '''

    _pattern = '^(?P<prefix>{prefixes})?(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefixes       = constants.PREFIX_PLAYLIST_RADIO_ID,
        prefix         = constants.PREFIX_ALBUM_PLAYLIST_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ALBUM_PLAYLIST_ID,
    )

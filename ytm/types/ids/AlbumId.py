'''
Module containing the Id type: AlbumId
'''

from .. import base
from .. import constants

class AlbumId(base.Id):
    '''
    Id class: AlbumId

    Example:
        >>> id = AlbumId('MPREb_K8qWMWVqXGi')
        >>>
        >>> id
        <AlbumId('MPREb_K8qWMWVqXGi')>
        >>>
        >>> str(id)
        'MPREb_K8qWMWVqXGi'
        >>>
    '''

    _pattern: str = '^(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefix         = constants.PREFIX_ALBUM_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ALBUM_ID,
    )

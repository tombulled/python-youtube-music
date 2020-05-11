'''
'''

from .. import base
from .. import constants

class AlbumId(base.Id):
    '''
    '''
    
    _pattern = '^(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefix         = constants.PREFIX_ALBUM_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ALBUM_ID,
    )

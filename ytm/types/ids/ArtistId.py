'''
'''

from .. import base
from .. import constants

class ArtistId(base.Id):
    '''
    '''
    
    _pattern = '^(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefix         = constants.PREFIX_ARTIST_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ARTIST_ID,
    )

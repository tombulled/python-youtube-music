'''
Module containing the Id type: SongId
'''

from .. import base
from .. import constants

class SongId(base.Id):
    '''
    Id class: SongId

    Example:
        >>> id = SongId('XnwpXfwXp6w')
        >>>
        >>> id
        <SongId('XnwpXfwXp6w')>
        >>>
        >>> str(id)
        'XnwpXfwXp6w'
        >>>
    '''

    _pattern = '^(?P<prefix>{prefixes})?(?P<data>[{chars}]{{{length}}})$'.format \
    (
        prefixes = constants.PREFIX_SONG_RADIO_ID,
        chars    = constants.CHARS_ID,
        length   = constants.LEN_SONG_ID,
    )

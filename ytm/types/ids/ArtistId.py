'''
Module containing the Id type: ArtistId
'''

from .. import base
from .. import constants

class ArtistId(base.Id):
    '''
    Id class: ArtistId

    Example:
        >>> id = ArtistId('UCRr1xG_2WIDs18a6cIiCxeA')
        >>>
        >>> id
        <ArtistId('UCRr1xG_2WIDs18a6cIiCxeA')>
        >>>
        >>> str(id)
        'UCRr1xG_2WIDs18a6cIiCxeA'
        >>>
    '''

    _pattern: str = '^(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefix         = constants.PREFIX_ARTIST_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_ARTIST_ID,
    )

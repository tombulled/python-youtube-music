'''
Module containing the Id type: ChartPlaylistId
'''

from .. import base
from .. import constants

class ChartPlaylistId(base.Id):
    '''
    Id class: ChartPlaylistId

    Example:
        >>> id = ChartPlaylistId('PL4fGSI1pDJn688ebB8czINn0_nov50e3A')
        >>>
        >>> id
        <ChartPlaylistId('PL4fGSI1pDJn688ebB8czINn0_nov50e3A')>
        >>>
        >>> str(id)
        'PL4fGSI1pDJn688ebB8czINn0_nov50e3A'
        >>>
    '''

    _pattern: str = '^(?P<prefix>{prefixes})?(?P<data>{prefix}[{chars}]{{{entropy_length}}})$'.format \
    (
        prefixes       = '|'.join \
        (
            (
                constants.PREFIX_PLAYLIST_BROWSE_ID,
                constants.PREFIX_PLAYLIST_RADIO_ID,
            )
        ),
        prefix         = constants.PREFIX_CHART_PLAYLIST_ID,
        chars          = constants.CHARS_ID,
        entropy_length = constants.LEN_ENTROPY_CHART_PLAYLIST_ID,
    )

'''
Module containing the Id type: PlaylistId
'''

from .. import base
from .. import constants

class PlaylistId(base.Id):
    '''
    Id class: PlaylistId

    Example:
        >>> id = PlaylistId('RDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')
        >>>
        >>> id
        <PlaylistId('RDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')>
        >>>
        >>> str(id)
        'RDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc'
        >>>
    '''

    _pattern: str = \
    (
        '^(?P<prefix>{prefixes})?(?P<data>{patterns})$'
    ).format \
    (
        prefixes = '|'.join \
        (
            (
                constants.PREFIX_PLAYLIST_BROWSE_ID,
                constants.PREFIX_PLAYLIST_RADIO_ID,
            ),
        ),
        patterns = '|'.join \
        (
            '(?:{prefix}[{chars}]{{{entropy_length}}})'.format(**data)
             for data in \
            (
                {
                    'prefix':         constants.PREFIX_PLAYLIST_ID,
                    'chars':          constants.CHARS_ID,
                    'entropy_length': constants.LEN_ENTROPY_PLAYLIST_ID,
                },
                {
                    'prefix':         constants.PREFIX_CHART_PLAYLIST_ID,
                    'chars':          constants.CHARS_ID,
                    'entropy_length': constants.LEN_ENTROPY_CHART_PLAYLIST_ID,
                },
            )
        ),
    )

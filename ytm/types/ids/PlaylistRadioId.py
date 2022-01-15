'''
Module containing the Id type: PlaylistRadioId
'''

from .PlaylistId import PlaylistId
from .. import constants

class PlaylistRadioId(PlaylistId):
    '''
    Id class: PlaylistRadioId

    Example:
        >>> id = PlaylistRadioId('RDAMPLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')
        >>>
        >>> id
        <PlaylistRadioId('RDAMPLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')>
        >>>
        >>> str(id)
        'RDAMPLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc'
        >>>
    '''

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the extracted data value.

        Append the playlist radio prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> PlaylistRadioId._clean('RDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')
            'RDAMPLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc'
            >>>
        '''

        return constants.PREFIX_PLAYLIST_RADIO_ID + super()._clean(value)

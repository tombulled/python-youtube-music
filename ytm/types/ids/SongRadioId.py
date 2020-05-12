'''
Module containing the Id type: SongRadioId
'''

from .SongId import SongId
from .. import constants

class SongRadioId(SongId):
    '''
    Id class: SongRadioId

    Example:
        >>> id = SongRadioId('RDAMVMXnwpXfwXp6w')
        >>>
        >>> id
        <SongRadioId('RDAMVMXnwpXfwXp6w')>
        >>>
        >>> str(id)
        'RDAMVMXnwpXfwXp6w'
        >>>
    '''

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the extracted data value.

        Append the song radio prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> SongRadioId._clean('XnwpXfwXp6w')
            'RDAMVMXnwpXfwXp6w'
            >>>
        '''

        return constants.PREFIX_SONG_RADIO_ID + super()._clean(value)

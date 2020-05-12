'''
Module containing the Id type: ChartRadioId
'''

from .ChartPlaylistId import ChartPlaylistId
from .. import constants

class ChartRadioId(ChartPlaylistId):
    '''
    Id class: ChartRadioId

    Example:
        >>> id = ChartRadioId('RDAMPLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')
        >>>
        >>> id
        <ChartRadioId('RDAMPLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')>
        >>>
        >>> str(id)
        'RDAMPLPL4fGSI1pDJn688ebB8czINn0_nov50e3A'
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
            >>> ChartRadioId._clean('PL4fGSI1pDJn688ebB8czINn0_nov50e3A')
            'RDAMPLPL4fGSI1pDJn688ebB8czINn0_nov50e3A'
            >>>
        '''

        return constants.PREFIX_PLAYLIST_RADIO_ID + value

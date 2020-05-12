'''
Module containing the Id type: ChartPlaylistBrowseId
'''

from .ChartPlaylistId import ChartPlaylistId
from .. import constants

class ChartPlaylistBrowseId(ChartPlaylistId):
    '''
    Id class: ChartPlaylistBrowseId

    Example:
        >>> id = ChartPlaylistBrowseId('VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')
        >>>
        >>> id
        <ChartPlaylistBrowseId('VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A')>
        >>>
        >>> str(id)
        'VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A'
        >>>
    '''

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the extracted data value.

        Append the playlist browse id prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> ChartPlaylistBrowseId._clean('PL4fGSI1pDJn688ebB8czINn0_nov50e3A')
            'VLPL4fGSI1pDJn688ebB8czINn0_nov50e3A'
            >>>
        '''

        return constants.PREFIX_PLAYLIST_BROWSE_ID + value

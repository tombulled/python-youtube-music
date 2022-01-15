'''
Module containing the Id type: ArtistShuffleId
'''

from .ArtistRadioId import ArtistRadioId
from .. import constants

class ArtistShuffleId(ArtistRadioId):
    '''
    Id class: ArtistShuffleId

    Example:
        >>> id = ArtistShuffleId('RDAOHSpo_Uv9STIRtF73zMywLg')
        >>>
        >>> id
        <ArtistShuffleId('RDAOHSpo_Uv9STIRtF73zMywLg')>
        >>>
        >>> str(id)
        'RDAOHSpo_Uv9STIRtF73zMywLg'
        >>>
    '''

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the extracted data value.

        Append the artist shuffle prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> ArtistShuffleId._clean('HSpo_Uv9STIRtF73zMywLg')
            'RDAOHSpo_Uv9STIRtF73zMywLg'
            >>>
        '''

        return constants.PREFIX_ARTIST_SHUFFLE_ID + value

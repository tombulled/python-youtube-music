'''
Module containing the Id type: AlbumRadioId
'''

from .AlbumPlaylistId import AlbumPlaylistId
from .. import constants

class AlbumRadioId(AlbumPlaylistId):
    '''
    Id class: AlbumRadioId

    Example:
        >>> id = AlbumRadioId('RDAMPLOLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ')
        >>>
        >>> id
        <AlbumRadioId('RDAMPLOLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ')>
        >>>
        >>> str(id)
        'RDAMPLOLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ'
        >>>
    '''

    @classmethod
    def _clean(cls: type, value: str) -> dict:
        '''
        Clean the extracted data value.

        Append the playlist radio prefix to the value.

        Args:
            cls: This class
            value: The extracted data value to clean

        Returns:
            Cleaned value

        Example:
            >>> AlbumRadioId._clean('OLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ')
            'RDAMPLOLAK5uy_nZZjkBu_E4olFSb5Ey-fQ-4a0ZCqJICdQ'
            >>>
        '''

        return constants.PREFIX_PLAYLIST_RADIO_ID + value

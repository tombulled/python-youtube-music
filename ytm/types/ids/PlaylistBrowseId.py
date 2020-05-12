'''
Module containing the Id type: PlaylistBrowseId
'''

from .PlaylistId import PlaylistId
from .. import constants

class PlaylistBrowseId(PlaylistId):
    '''
    Id class: PlaylistBrowseId

    Example:
        >>> id = PlaylistBrowseId('VLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')
        >>>
        >>> id
        <PlaylistBrowseId('VLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')>
        >>>
        >>> str(id)
        'VLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc'
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
            >>> PlaylistBrowseId._clean('RDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc')
            'VLRDCLAK5uy_kqSXUdZBZlDrNwxWgVm3xlQ7q0I6h9Zsc'
            >>>
        '''

        return constants.PREFIX_PLAYLIST_BROWSE_ID + super()._clean(value)

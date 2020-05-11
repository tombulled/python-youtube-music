'''
'''

from .PlaylistId import PlaylistId
from .. import constants

class PlaylistBrowseId(PlaylistId):
    '''
    '''

    @classmethod
    def _clean(cls, value: str):
        '''
        '''
        
        return constants.PREFIX_PLAYLIST_BROWSE_ID + super()._clean(value)

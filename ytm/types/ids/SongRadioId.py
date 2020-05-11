'''
'''

from .SongId import SongId
from .. import constants

class SongRadioId(SongId):
    '''
    '''

    @classmethod
    def _clean(cls, value: str):
        '''
        '''
        
        return constants.PREFIX_SONG_RADIO_ID + super()._clean(value)

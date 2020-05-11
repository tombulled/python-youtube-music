'''
'''

from .TypeB64 import TypeB64
from .. import constants

class Params(TypeB64):
    '''
    '''
    
    _pattern = f'^(?P<data>[{constants.CHARS_PARAMS}]*)$'

'''
'''

from .TypeStr import TypeStr
from .. import constants

class Id(TypeStr):
    '''
    '''
    
    _pattern = f'^(?P<data>[{constants.CHARS_ID}]*)$'

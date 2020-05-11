'''
Module containing the base type: Params
'''

from .TypeB64 import TypeB64
from .. import constants

class Params(TypeB64):
    '''
    Base Type: Params.

    Attributes:
        _pattern: Regular expression pattern used to extract data
    '''

    _pattern: str = f'^(?P<data>[{constants.CHARS_PARAMS}]*)$'

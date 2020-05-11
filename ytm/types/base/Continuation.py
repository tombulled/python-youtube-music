'''
Module containing the base type: Continuation
'''

from .TypeB64 import TypeB64
from .. import constants

class Continuation(TypeB64):
    '''
    Base Type: Continuation.

    Attributes:
        _pattern: Regular expression pattern used to extract data
    '''

    _pattern: str = f'^(?P<data>[{constants.CHARS_CONTINUATION}]*)$'

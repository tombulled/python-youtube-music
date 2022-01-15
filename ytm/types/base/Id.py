'''
Module containing the base type: Id
'''

from .TypeStr import TypeStr
from .. import constants

class Id(TypeStr):
    '''
    Base Type: Id.

    Attributes:
        _pattern: Regular expression pattern used to extract data
    '''

    _pattern: str = f'^(?P<data>[{constants.CHARS_ID}]*)$'

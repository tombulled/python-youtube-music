'''
'''

from ... import classes
from .. import utils

class BaseUnion(tuple, metaclass = classes.BuiltinMeta):
    '''
    '''

    def __new__(cls: type, *types) -> object:
        '''
        '''

        return super().__new__(cls, types)

    def __repr__(self: object) -> str:
        '''
        '''

        return '{class_name}({types})'.format \
        (
            class_name = self.__class__.__name__,
            types      = ', '.join(type.__name__ for type in self)
        )

    def _isinstance(self: object, value: object) -> bool:
        '''
        '''

        for type in self:
            if utils.isinstance(value, type):
                return True

        return False

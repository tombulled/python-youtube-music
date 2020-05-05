'''
'''

from ... import classes

import re

class BaseType(str, metaclass = classes.BuiltinMeta):
    '''
    '''

    _patterns = ()
    _pattern = None

    def __new__(cls: type, value: str) -> object:
        '''
        '''

        if not cls._match(value):
            raise TypeError \
            (
                'Invalid {class_name}: {value}'.format \
                (
                    class_name = cls.__name__,
                    value      = repr(str(value)),
                )
            )

        value = cls._clean(value)

        return super().__new__(cls, value)

    def __repr__(self: object) -> str:
        '''
        '''

        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value      = super().__repr__(),
        )

    @classmethod
    def _match(cls: type, value: str) -> bool:
        '''
        '''

        if not isinstance(value, str):
            return False

        if isinstance(value, cls):
            return True

        if cls._pattern:
            patterns = (cls._pattern,)
        else:
            patterns = cls._patterns

        if not patterns:
            return True

        for pattern in patterns:
            match = re.match \
            (
                pattern = pattern,
                string  = value,
                flags   = re.DOTALL,
            )

            if match is not None:
                break
        else:
            return False

        return True

    @classmethod
    def _isinstance(cls: type, value: str) -> bool:
        '''
        '''

        return cls._match(value) and cls._clean(value) == value

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        '''

        return value

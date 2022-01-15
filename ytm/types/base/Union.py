'''
Module containing the base type: Union
'''

from ... import classes
from .. import utils

class Union(tuple, metaclass = classes.BuiltinMeta):
    '''
    Base Type: Union.

    A Union is a collection of other types. Its main purpose is for docstrings.

    Example:
        >>> def foo(value: Union(Continuation, Id, Params)):
        	""" Returns 'some value' """
        	return 'some value'

        >>>
        >>> help(foo)
        Help on function foo in module __main__:

        foo(value: Union(Continuation, Id, Params))
            Returns 'some value'

        >>>
    '''

    def __new__(cls: type, *types: type) -> object:
        '''
        Create a new class instance.

        Args:
            cls: This class
            *types: Types for the Union

        Returns:
            New class instance
        '''

        for item_type in types:
            if not isinstance(item_type, type):
                raise TypeError \
                (
                    'Invalid {class_name} type: {value}'.format \
                    (
                        class_name = cls.__name__,
                        value      = repr(str(item_type)),
                    )
                )

        return super().__new__(cls, types)

    def __repr__(self: object) -> str:
        '''
        Create a string representation of the class.

        The representation is of the form: <{class_name}({types})>

        Args:
            self: Class instance

        Returns:
            String representation of the class

        Example:
            >>> my_union = Union(str, int, bool)
            >>>
            >>> my_union
            Union(str, int, bool)
            >>>
        '''

        return '{class_name}({types})'.format \
        (
            class_name = self.__class__.__name__,
            types      = ', '.join(type.__name__ for type in self)
        )

    def _isinstance(self: object, value: object) -> bool:
        '''
        Check whether a value is an instance of any of the types in this union.

        Args:
            self: Class instance
            value: Value to check

        Returns:
            Whether the value is an instance of any of the types in the union

        Example:
            >>> my_union = Union(str, int, bool)
            >>>
            >>> my_union
            Union(str, int, bool)
            >>>
            >>> my_union._isinstance(43)
            True
            >>> my_union._isinstance(b'foo')
            False
            >>>
        '''

        for type in self:
            if utils.isinstance(value, type):
                return True

        return False

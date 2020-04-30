'''
Module containing the meta class: BuiltinMeta
'''

class BuiltinMeta(type):
    '''
    Meta class to allow a class to pretend to be a builtin class

    Example:
        Without meta class:
            >>> class Foo():
            	pass

            >>> Foo
            <class '__main__.Foo'>
            >>>

        With meta class:
            >>> class Foo(metaclass=BuiltinMeta):
            	pass

            >>> Foo
            <class 'Foo'>
            >>>
    '''

    def __new__(cls: type, name: str, bases: tuple, attrs: dict) -> object:
        '''
        Return a new class instance.

        Args:
            cls: Class type
            name: Class name
            bases: Class bases
            attrs: Class attributes

        Returns:
            New class instance
        '''

        return super().__new__ \
        (
            cls,
            name,
            bases,
            {
                **attrs,
                '__module__': 'builtins',
            },
        )

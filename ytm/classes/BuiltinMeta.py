'''
'''

class BuiltinMeta(type):
    '''
    '''

    def __new__(cls: type, name: str, bases: tuple, attrs: dict) -> object:
        '''
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

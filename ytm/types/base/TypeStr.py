'''
'''

from ... import classes

import re

class TypeStr(str, metaclass = classes.BuiltinMeta):
    '''
    '''

    _pattern = '^(?P<data>.*)$'

    def __new__(cls: type, value: str) -> object:
        '''
        '''

        parsed = cls._parse(value)
        data   = parsed.get('data')

        if not parsed:
            raise TypeError \
            (
                'Invalid {class_name}: {value}'.format \
                (
                    class_name = cls.__name__,
                    value      = repr(str(value)),
                )
            )

        return super().__new__(cls, data)

    def __repr__(self: object) -> str:
        '''
        '''

        # Make utility: snip? shorten? to 'some long sen...' <--- utility adds ellipsis

        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value      = super().__repr__(),
        )

    @classmethod
    def _parse(cls: type, value: str) -> bool:
        '''
        '''

        parsed = {}
        groups = {}

        if not isinstance(value, str) or not cls._pattern:
            return parsed

        match = re.match \
        (
            pattern = cls._pattern,
            string  = value,
            flags   = re.DOTALL,
        )

        if match:
            groups = match.groupdict()

            data = groups.get('data')

            if data:
                groups['data'] = cls._clean(data)

        return groups

    @classmethod
    def _isinstance(cls: type, value: str) -> bool:
        '''
        '''

        parsed = cls._parse(value)
        data   = parsed.get('data')

        return data and data == value

    @classmethod
    def _clean(cls: type, value: str) -> str:
        return value

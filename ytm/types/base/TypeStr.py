'''
Module containing the base type: TypeStr
'''

from ... import classes
from .. import utils

import re

class TypeStr(str, metaclass = classes.BuiltinMeta):
    '''
    Base Type: TypeStr.

    Base string type.

    Attributes:
        _pattern: Regular expression pattern used to extract data
    '''

    _pattern: str = '^(?P<data>.*)$'

    def __new__(cls: type, value: str) -> object:
        '''
        Create a new class instance.

        Args:
            cls: This class
            value: Value to initialise class with

        Returns:
            New class instance
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
        Create a string representation of the class.

        The representation is of the form: <{class_name}({value})>

        Args:
            self: Class instance

        Returns:
            String representation of the class
        '''

        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value      = repr(utils.truncate(str(self))),
        )

    @classmethod
    def _parse(cls: type, value: str) -> bool:
        '''
        Parse a string value to extract data.

        In no data is extracted, the value is not a valid instance of this type.

        Args:
            cls: This class
            value: String value to parse

        Returns:
            Values extracted during parsing

        Example:
            >>> TypeStr._parse('foo bar')
            {'data': 'foo bar'}
            >>>
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
        Check whether a string value is a valid instance of this type.

        Args:
            cls: This class
            value: String value to check

        Returns:
            Whether the value is a valid instance of this type

        Example:
            >>> class MyStrType(TypeStr):
            	_pattern = '^(?P<data>ABC.{3})$'

            >>>
            >>> MyStrType._isinstance('AAAfoo')
            False
            >>> MyStrType._isinstance('ABCfoo')
            True
            >>>
        '''

        parsed = cls._parse(value)
        data   = parsed.get('data')

        return bool(data) and data == value

    @classmethod
    def _clean(cls: type, value: str) -> str:
        '''
        Clean the data after it has been extracted.

        Args:
            cls: This class
            value: Data value to clean

        Returns:
            Cleaned data value

        Example:
            >>> class MyStrType(TypeStr):
            	_pattern = '^original-prefix(?P<data>.{3})$'

            	@classmethod
            	def _clean(cls, value):
            		return 'new-prefix' + value

            >>>
            >>> my_str = MyStrType('original-prefixABC')
            >>> my_str
            <MyStrType('new-prefixABC')>
            >>>
        '''

        return value

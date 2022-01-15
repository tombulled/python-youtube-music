'''
Module containing the base type: TypeB64
'''

from .TypeStr import TypeStr
from .. import utils

import urllib.parse
import base64
import re
from typing import Any

class TypeB64(TypeStr):
    '''
    Base Type: TypeB64.

    This type contains a series of base64 encoded strings and byte sequences.

    Attributes:
        _pattern: Regular expression pattern used to extract data
    '''

    _pattern: bytes = b'^(?P<data>.*)$'

    @classmethod
    def _parse(cls: type, value: str, pattern: bytes = None) -> dict:
        '''
        Parse a string value to extract data.

        In no data is extracted, the value is not a valid instance of this type.
        The data contained in the value will have been url-encoded, then
        base64-encoded.

        Args:
            cls: This class
            value: String value to parse
            pattern: Pattern used to extract data from the value

        Returns:
            Values extracted during parsing

        Example:
            >>> TypeB64._parse('Zm9vIGJhci4gMSArIDEgPSAyIQ%3D%3D')
            {'data': 'Zm9vIGJhci4gMSArIDEgPSAyIQ%3D%3D', 'parsed': b'foo bar. 1 + 1 = 2!'}
            >>>
        '''

        value = str(value)

        if pattern is None:
            pattern = cls._pattern

        parsed = {}

        url_decoded = urllib.parse.unquote(value)

        # Replacing - with + has been checked and is correct.
        # Is replacing _ with + correct?
        url_decoded = url_decoded.replace('-', '+').replace('_', '+')

        if not utils.is_base64(url_decoded):
            return parsed

        b64_decoded = base64.b64decode(url_decoded)

        match = re.match \
        (
            pattern = pattern,
            string  = b64_decoded,
            flags   = re.DOTALL,
        )

        if match:
            parsed = match.groupdict()

            parsed.update \
            (
                {
                    'parsed': parsed.get('data'),
                    'data': value,
                }
            )

        return parsed

    @staticmethod
    def _get(groups: dict, type: type, key: str) -> Any:
        '''
        Retrieve an extracted value and decode it appropriately.

        Args:
            groups: Extracted groups
            type: Type of the target data
            key: Key of the target data

        Returns:
            The value from <groups> specified by <key> appropriately decoded
            or None if there is no value in <groups>

        Example:
            >>> import re
            >>>
            >>> pattern = b'^(?P<str>.{3})(?P<int>.)(?P<bool>.)(?P<bytes>.{2})$'
            >>> string  = b'foo\x3d\x01\xaf\xbc'
            >>>
            >>> match = re.match(pattern, string, flags=re.DOTALL)
            >>> groups = match.groupdict()
            >>>
            >>> groups
            {'str': b'foo', 'int': b'=', 'bool': b'\x01', 'bytes': b'\xaf\xbc'}
            >>>
            >>> TypeB64._get(groups, str, 'str')
            'foo'
            >>> TypeB64._get(groups, int, 'int')
            61
            >>> TypeB64._get(groups, bool, 'bool')
            True
            >>> TypeB64._get(groups, bytes, 'bytes')
            b'\xaf\xbc'
            >>>
        '''

        if type is str:
            return (groups.get(key) or b'').decode() or None
        elif type is bytes:
            return (groups.get(key) or b'') or None
        elif type is int:
            return ord(groups.get(key) or b'\x00') or None
        elif type is bool:
            return bool(ord(groups.get(key) or b'\x00'))

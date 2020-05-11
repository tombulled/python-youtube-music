'''
'''

from .TypeStr import TypeStr
from .. import utils

import urllib.parse
import base64
import re
from typing import Any

class TypeB64(TypeStr):
    '''
    '''

    _pattern = f'^(?P<data>.*)$'.encode()

    @classmethod
    def _parse(cls: type, value: str, pattern: bytes = None) -> dict:
        '''
        '''

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

        return parsed

    @staticmethod
    def _get(groups: dict, type: type, key: str) -> Any:
        '''
        '''

        if type is str:
            return (groups.get(key) or b'').decode() or None
        elif type is bytes:
            return (groups.get(key) or b'') or None
        elif type is int:
            return ord(groups.get(key) or b'\x00') or None
        elif type is bool:
            return bool(ord(groups.get(key) or b'\x00'))

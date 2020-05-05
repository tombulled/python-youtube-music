from . import base
from . import utils
from . import constants
import urllib.parse
import base64
import re

class SearchContinuation(base.BaseType):
    _pattern = utils.pattern \
    (
        b'\x12',
        utils.entropy \
        (
            length = 2,
            chars  = '.',
        ).encode(),
        b'\x12',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'query_len',
        ).encode(),
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'query',
            repeat = '+',
        ).encode(),
        b'\x1a',
        utils.entropy \
        (
            length = 2,
            chars  = '.',
        ).encode(),
        b'Eg-KAQwIA',
        utils.optional \
        (
            *constants.SEARCH_PARAMS_MAP_REV,
            required = True,
            group    = 'param',
        ).encode(),
        b'MABI',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
        ).encode(),
        b'GoKEA',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
        ).encode(),
        b'QBBA',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
        ).encode(),
        b'EA',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
        ).encode(),
        b'QBYIB',
        utils.entropy \
        (
            name   = 'ids_data',
            repeat = '+',
            chars  = constants.CHARS_CONTINUATION,
        ).encode(),
        b'\x18\xf1\xea\xd0',
        b'\.',
    )

    @classmethod
    def _match(cls, value: str) -> bool:
        continuation_url_decoded = urllib.parse.unquote(value)

        if not utils.is_base64(continuation_url_decoded):
            return False

        continuation_base64_decoded = base64.b64decode(continuation_url_decoded)

        match = re.match(cls._pattern, continuation_base64_decoded)

        if match is None:
            return False

        data_url_encoded = match.group('ids_data').decode()
        data_url_decoded = urllib.parse.unquote(data_url_encoded).replace('-', '+')

        if not utils.is_base64(data_url_decoded):
            return False

        data_b64_decoded = base64.b64decode(data_url_decoded)

        ids = []

        for segment in data_b64_decoded.split(b'\x82\x01'):
            id_len = segment[0]
            id     = segment[1:].decode()

            if len(segment) != id_len + 1:
                return False

            ids.append(id)

        return True

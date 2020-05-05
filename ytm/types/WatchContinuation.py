from . import base
from . import utils
import urllib.parse
import base64
import re

class WatchContinuation(base.BaseType):
    _pattern = utils.pattern \
    (
        b'\x08\x19\x12',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
        ).encode(),
        b'\x12',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'len_video_id',
        ).encode(),
        utils.entropy \
        (
            length = 11,
            name   = 'video_id',
        ).encode(),
        b'"',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'len_playlist_id',
        ).encode(),
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'playlist_id',
            repeat = '+',
        ).encode(),
        b'2',
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'len_params',
        ).encode(),
        utils.entropy \
        (
            length = 1,
            chars  = '.',
            name   = 'params',
            repeat = '+',
        ).encode(),
        b'8',
        b'\x18\xb8\x01\x02\xd0\x01\x01\xf0\x01\x01\x18\n',
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

        len_video_id    = ord(match.group('len_video_id'))
        len_playlist_id = ord(match.group('len_playlist_id'))
        len_params      = ord(match.group('len_params'))

        video_id    = match.group('video_id').decode()
        playlist_id = match.group('playlist_id').decode()
        params      = match.group('params').decode()

        length_map = \
        {
            video_id:    len_video_id,
            playlist_id: len_playlist_id,
            params:      len_params
        }

        for value, length in length_map.items():
            if len(value) != length:
                return False

        return True

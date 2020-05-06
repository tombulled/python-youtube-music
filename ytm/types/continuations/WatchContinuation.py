from .. import base

class WatchContinuation(base.Continuation):
    @classmethod
    def _parse(cls: type, value: str) -> dict:
        value = str(value)

        pattern = \
        (
            b'\x08\x19\x12'
            b'.'
            b'\x12'
            b'(?P<len_video_id>.)'
            b'(?P<video_id>.{11})'
            b'"'
            b'(?P<len_playlist_id>.)'
            b'(?P<playlist_id>.+)'
            b'2'
            b'(?P<len_params>.)'
            b'(?P<params>.+)'
            b'8'
            b'\x18\xb8\x01\x02\xd0\x01\x01\xf0\x01\x01\x18\n'
        )

        data = {}

        parsed = super()._parse(value, pattern)

        if not parsed:
            return data

        len_video_id    = cls._get(parsed, int, 'len_video_id')
        len_playlist_id = cls._get(parsed, int, 'len_playlist_id')
        len_params      = cls._get(parsed, int, 'len_params')
        video_id        = cls._get(parsed, str, 'video_id')
        playlist_id     = cls._get(parsed, str, 'playlist_id')
        params          = cls._get(parsed, str, 'params')

        lengths = \
        (
            (video_id,    len_video_id),
            (playlist_id, len_playlist_id),
            (params,      len_params),
        )

        for item, length in lengths:
            if not item or len(item) != length:
                return data

        data = \
        {
            'video_id':    video_id,    # Check format
            'playlist_id': playlist_id, # Check format
            'params':      params,      # Check format
            'data':        value,
        }

        return data

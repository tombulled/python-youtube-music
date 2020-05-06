from .. import base

class PlaylistContinuation(base.Continuation):
    @classmethod
    def _parse(cls: type, value: str) -> dict:
        value = str(value)

        pattern_1 = \
        (
            b'^'
            b'\xe2\xa9\x85\xb2\x02\[\x12'
            b'(?P<len_playlist_browse_id>.)'
            b'(?P<playlist_browse_id>.{45})'
            b'\x1a\*'
            b'(?P<suffix>.+)'
            b'$'
        )
        pattern_2 = \
        (
            b'^'
            b'z'
            b'(?P<len_params>.)'
            b'(?P<params>.{21})' # Note If you b64 decode this left-stripped of 'PT:' it yields a song_id ?
            b'\x92\x01\x03\x08\xba\x04'
        )

        data = {}

        parsed_1 = super()._parse(value, pattern_1)

        if not parsed_1:
            return data

        len_playlist_browse_id = cls._get(parsed_1, int, 'len_playlist_browse_id')
        playlist_browse_id     = cls._get(parsed_1, str, 'playlist_browse_id')
        suffix                 = cls._get(parsed_1, str, 'suffix')

        if not playlist_browse_id or len(playlist_browse_id) != len_playlist_browse_id:
            return data

        parsed_2 = super()._parse(suffix, pattern_2)

        if not parsed_2:
            return data

        len_params = cls._get(parsed_2, int, 'len_params')
        params     = cls._get(parsed_2, str, 'params')

        if not params or len(params) != len_params:
            return data

        data = \
        {
            'playlist_browse_id': playlist_browse_id,
            'params': params,
            'data': value,
        }

        return data

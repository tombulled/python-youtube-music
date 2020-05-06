from .. import base

class ArtistAlbumsParams(base.Params):
    @classmethod
    def _parse(cls: type, value: str) -> dict:
        value = str(value)

        pattern_1 = \
        (
            b'^'
            b'\xea\x03'
            b'(?P<len_suffix>.)'
            b'\x01'
            b'(?P<suffix>.+)'
            b'$'
        )
        pattern_2 = \
        (
            b'^'
            b'\n\x9c\x01\n\}\nn\x00\x00'
            b'(?P<language>.+)'
            b'\x00\x01'
            b'(?P<region_1>.+)'
            b'\x00\x01'
            b'(?P<region_2>.+)'
            b'\x00\x01\x00'
            b'(?P<browse_id>.+)' # FEmusic_detail_artist
            b'\x00\x01\x00\x00\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x01\x01\x08'
            b'.'
            b'\x03\x1a'
            b'(?P<len_artist_id_1>.)'
            b'(?P<artist_id_1>.+)'
            b'\x82\x01'
            b'(?P<len_artist_id_2>.)'
            b'(?P<artist_id_2>.+)'
            b'\x00\x01\x10'
            b'.{6}'
            b'\xe9\x02\x1a\x02ws\x18\x00\*'
            b'(?P<len_target>.)'
            b'(?P<target>.+)' # artist_releases
            b'0\xb1\xd4\xd0\xe5\x97\xf1\xc9\xf2p'
            b'$'
        )

        data = {}

        parsed_1 = super()._parse(value, pattern_1)

        len_suffix = cls._get(parsed_1, int, 'len_suffix')
        suffix     = cls._get(parsed_1, str, 'suffix')

        if not suffix or len(suffix) != len_suffix:
            return data

        parsed_2 = super()._parse(suffix, pattern_2)

        language        = cls._get(parsed_2, str, 'language')
        region_1        = cls._get(parsed_2, str, 'region_1')
        region_2        = cls._get(parsed_2, str, 'region_2')
        browse_id       = cls._get(parsed_2, str, 'browse_id')
        len_artist_id_1 = cls._get(parsed_2, int, 'len_artist_id_1')
        len_artist_id_2 = cls._get(parsed_2, int, 'len_artist_id_2')
        artist_id_1     = cls._get(parsed_2, str, 'artist_id_1')
        artist_id_2     = cls._get(parsed_2, str, 'artist_id_2')
        len_target      = cls._get(parsed_2, int, 'len_target')
        target          = cls._get(parsed_2, str, 'target')

        lengths_1 = \
        (
            (artist_id_1, len_artist_id_1),
            (artist_id_2, len_artist_id_2),
            (target,      len_target),
        )

        for item, length in lengths_1:
            if not item or len(item) != length:
                return data

        data = \
        {
            'language':    language,
            'region_1':    region_1,
            'region_2':    region_2,
            'artist_id_1': artist_id_1, # Check format
            'artist_id_2': artist_id_2, # Check format
            'target':      target,
            'data':        value,
            'browse_id':   browse_id,
        }

        return data

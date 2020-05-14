'''
Module containing the continuation type: HomeContinuation
'''

from .. import base
from .. import utils

class HomeContinuation(base.Continuation):
    '''
    Continuation class: HomeContinuation.

    Example:
        >>> api = ytm.YouTubeMusic()
        >>>
        >>> home = api.home()
        >>>
        >>> continuation = ytm.types.HomeContinuation(home['continuation'])
        >>>
        >>> continuation
        <HomeContinuation('4qmFsgKIARIMRkVtdXNpY19ob21lGnhDQU42VmtOcVJVRkJ...')>
        >>>
    '''

    @classmethod
    def _parse(cls: type, value: str) -> dict:
        '''
        Parse a continuation string.

        Args:
            cls: This class
            value: Value to parse

        Returns:
            Values extracted during parsing

        Example:
            >>> api = ytm.YouTubeMusic()
            >>>
            >>> home = api.home()
            >>>
            >>> continuation = ytm.types.HomeContinuation(home['continuation'])
            >>>
            >>> from pprint import pprint
            >>>
            >>> parsed = continuation._parse(continuation)
            >>>
            >>> pprint(parsed)
            {'browse_id': 'FEmusic_home',
             'data': '4qmFsgKIARIMRkVtdXNpY19ob21lGnhDQU42VmtOcVJVRkJSMVoxUVV...',
             'flag_continuation': False,
             'language': 'en',
             'playlist_id': None,
             'region_1': 'GB',
             'region_2': 'GB',
             'total_shelves': 3}
            >>>
        '''

        value = str(value)

        pattern_1 = \
        (
            b'^'
            b'\xe2\xa9\x85\xb2\x02'
            b'.'
            b'\x01\x12'
            b'(?P<len_browse_id>.)'
            b'(?P<browse_id>.{12})' # Use constant
            b'\x1a'
            b'(?P<len_suffix>.)'
            b'\x01?'
            b'(?P<suffix>.+)'
            b'$'
        )
        pattern_2 = \
        (
            b'^'
            b'\x08'
            b'(?P<total_shelves>.)'
            b'z'
            b'(?P<len_suffix>.)'
            b'(?P<flag_continuation>\x01)?'
            b'(?P<suffix>.+)'
            b'$'
        )
        pattern_3 = \
        (
            b'^'
            b'\n1\x00\x00'
            b'(?P<language>.+)'
            b'\x00\x01'
            b'(?P<region_1>.+)'
            b'\x00\x01'
            b'(?P<region_2>.+)'
            b'\x00\x01\x00'
            b'(?P<browse_id>.+)'
            b'\x00\x01\x00\x00\x01\x01'
            b'C'
            b'\x00\x00\x00\x01\x00\x01\x00\x00\x01\x01\x04\x01\x94'
            b'.{2}'
            b'\x10'
            b'.'
            b'\x18'
            b'.{6}'
            b'\xe9\x022'
            b'(?:\x00|.\x1a.(?P<playlist_id>.+))'
            b'$'
        )

        data = {}

        parsed_1 = super()._parse(value, pattern_1)

        len_browse_id_1 = cls._get(parsed_1, int, 'len_browse_id')
        len_suffix_1    = cls._get(parsed_1, int, 'len_suffix')
        browse_id_1     = cls._get(parsed_1, str, 'browse_id')
        suffix_1        = cls._get(parsed_1, str, 'suffix')

        lengths_1 = \
        (
            (browse_id_1, len_browse_id_1),
            (suffix_1,    len_suffix_1),
        )

        for item, length in lengths_1:
            if not item or len(item) != length:
                return data

        parsed_2 = super()._parse(suffix_1, pattern_2)

        len_suffix_2      = cls._get(parsed_2, int,  'len_suffix')
        total_shelves     = cls._get(parsed_2, int,  'total_shelves')
        flag_continuation = cls._get(parsed_2, bool, 'flag_continuation')
        suffix_2          = cls._get(parsed_2, str,  'suffix')

        if not suffix_2 or len(suffix_2) != len_suffix_2:
            return data

        suffix_2 = utils.pad_base64(suffix_2)

        parsed_3 = super()._parse(suffix_2, pattern_3)

        language     = cls._get(parsed_3, str, 'language')
        region_1     = cls._get(parsed_3, str, 'region_1')
        region_2     = cls._get(parsed_3, str, 'region_2')
        browse_id_2  = cls._get(parsed_3, str, 'browse_id')
        playlist_id  = cls._get(parsed_3, str, 'playlist_id')

        if browse_id_1 != browse_id_2:
            return data

        data = \
        {
            'browse_id':         browse_id_1,
            'total_shelves':     total_shelves,
            'flag_continuation': flag_continuation,
            'language':          language,
            'region_1':          region_1,
            'region_2':          region_2,
            'playlist_id':       playlist_id, # Check the format of this
            'data':              value,
        }

        return data

'''
Module containing the continuation type: PlaylistContinuation
'''

from .. import base

class PlaylistContinuation(base.Continuation):
    '''
    Continuation class: PlaylistContinuation.

    Example:
        >>> api = ytm.YouTubeMusic()
        >>>
        >>> playlist = api.playlist('RDCLAK5uy_lXWhlJsihey6xq1b50d7Uv93NLqle8TSc')
        >>>
        >>> continuation = ytm.types.PlaylistContinuation(playlist['continuation'])
        >>>
        >>> continuation
        <PlaylistContinuation('4qmFsgJbEi1WTFJEQ0xBSzV1eV9sWFdobEpzaWhleTZ4cTF...')>
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
            >>> playlist = api.playlist('RDCLAK5uy_lXWhlJsihey6xq1b50d7Uv93NLqle8TSc')
            >>>
            >>> continuation = ytm.types.PlaylistContinuation(playlist['continuation'])
            >>>
            >>> from pprint import pprint
            >>>
            >>> parsed = continuation._parse(continuation)
            >>>
            >>> pprint(parsed)
            {'data': '4qmFsgJbEi1WTFJEQ0xBSzV1eV9sWFdobEpzaWhleTZ4cTFiNTBkN1...',
             'params': 'PT:EgtyS1RLVGEzU1o3UQ',
             'playlist_browse_id': 'VLRDCLAK5uy_lXWhlJsihey6xq1b50d7Uv93NLqle8TSc'}
            >>>
        '''

        value = str(value)

        pattern_1 = \
        (
            b'^'
            b'\xe2\xa9\x85\xb2\x02'
            b'.'
            b'\x12'
            b'(?P<len_playlist_browse_id>.)'
            b'(?P<playlist_browse_id>.+)'
            b'\x1a'
            b'(?P<len_suffix>.)'
            b'(?P<suffix>.+)'
            b'$'
        )
        pattern_2 = \
        (
            b'^'
            b'z'
            b'(?P<len_params>.)'
            b'(?P<params>.+)'
            b'\x92\x01\x03\x08\xba\x04'
        )

        data = {}

        parsed_1 = super()._parse(value, pattern_1)

        if not parsed_1:
            return data

        len_playlist_browse_id = cls._get(parsed_1, int, 'len_playlist_browse_id')
        playlist_browse_id     = cls._get(parsed_1, str, 'playlist_browse_id')
        len_suffix             = cls._get(parsed_1, int, 'len_suffix')
        suffix                 = cls._get(parsed_1, str, 'suffix')

        lengths_1 = \
        (
            (playlist_browse_id, len_playlist_browse_id),
            (suffix,             len_suffix),
        )

        for item, length in lengths_1:
            if not item or len(item) != length:
                return data

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

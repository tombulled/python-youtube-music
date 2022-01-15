'''
Module containing the continuation type: SearchContinuation
'''

from .. import base
from .. import constants

class SearchContinuation(base.Continuation):
    '''
    Continuation class: SearchContinuation.

    Example:
        >>> api = ytm.YouTubeMusic()
        >>>
        >>> albums = api.search_albums('strange trails')
        >>>
        >>> continuation = ytm.types.SearchContinuation(albums['continuation'])
        >>>
        >>> continuation
        <SearchContinuation('EpMGEg5zdHJhbmdlIHRyYWlscxqABkVnLUtBUXdJQUJBQUd...')>
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
            >>> albums = api.search_albums('strange trails')
            >>>
            >>> continuation = ytm.types.SearchContinuation(albums['continuation'])
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

        pattern_1 = b''.join \
        (
            (
                b'^'
                b'\x12'
                b'.{2}'
                b'\x12'
                b'(?P<len_query>.)'
                b'(?P<query>.+)'
                b'\x1a'
                b'.{2}'
                b'Eg-KAQwIA',
                f'(?P<param>{"|".join(constants.SEARCH_PARAMS_MAP_REV)})'.encode(),
                b'MABI'
                b'.'
                b'GoKEA'
                b'.'
                b'QBBA'
                b'.'
                b'EA'
                b'.'
                b'QBYIB'
                b'(?P<suffix>.+)'
                b'\x18\xf1\xea\xd0'
                b'\.'
                b'$'
            )
        )
        pattern_2 = b'^(?P<entropy>.*)$'

        data = {}

        parsed_1 = super()._parse(value, pattern_1)

        if not parsed_1:
            return data

        len_query = cls._get(parsed_1, int, 'len_query')
        query     = cls._get(parsed_1, str, 'query')
        param     = cls._get(parsed_1, str, 'param')
        suffix    = cls._get(parsed_1, str, 'suffix')

        if not query or len(query) != len_query:
            return data

        filter = constants.SEARCH_PARAMS_MAP_REV.get(param)

        parsed_2 = super()._parse(suffix, pattern_2)

        if not parsed_2:
            return data

        entropy = cls._get(parsed_2, bytes, 'entropy')

        ids = []

        for segment in entropy.split(b'\x82\x01'):
            id_len = segment[0]
            id     = segment[1:].decode()

            if len(segment) != id_len + 1:
                return False

            # Check ID is valid format here

            ids.append(id)

        data = \
        {
            'query':  query,
            'param':  param,
            'filter': filter,
            'ids':    ids,
            'data':   value,
        }

        return data

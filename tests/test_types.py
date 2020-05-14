import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent))

import pytest
import ytm.types

data = \
{
    ytm.types.Continuation: \
    {
        True: \
        (
            'U29tZSBjb250aW51YXRpb24gZGF0YS4uLg%3D%3D',
            'QWEtOV8%3D',
        ),
        False: \
        (
            '😄',
            'Aa-9_%',
            b'foo',
        ),
    },
    ytm.types.Id: \
    {
        True: \
        (
            'foo',
            'Aa-9_',
        ),
        False: \
        (
            '😄',
            '.',
        ),
    },
    ytm.types.Params: \
    {
        True: \
        (
            'U29tZSBjb250aW51YXRpb24gZGF0YS4uLg%3D%3D',
            'QWEtOV8%3D',
        ),
        False: \
        (
            '😄',
            'Aa-9_%',
            b'foo',
        ),
    },
    ytm.types.TypeB64: \
    {
        True: \
        (
            'U29tZSBjb250aW51YXRpb24gZGF0YS4uLg%3D%3D',
            'QWEtOV8%3D',
        ),
        False: \
        (
            '😄',
            'Aa-9_%',
            b'foo',
        ),
    },
    ytm.types.TypeStr: \
    {
        True: \
        (
            'foo',
            'Aa-9_',
        ),
        False: \
        (
        ),
    },
    ytm.types.Union: \
    {
        True: \
        (
            str,
            ytm.types.TypeStr,
        ),
        False: \
        (
            'foo',
            ytm.types.TypeStr('foo'),
        ),
    },
    ytm.types.HomeContinuation: \
    {
        True: \
        (
            '4qmFsgKIARIMRkVtdXNpY19ob21lGnhDQU42VmtOcVJVRkJSMVoxUVVGR1NGRm5RVUpTTUVsQlFWRkNSMUpYTVRGak1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUZCVVVGQ1FVRkJRa0ZSVVVKc1JHbEVSVUZCV1c4M2RtbDFZa3Q2TmxGSmVVRkI%3D',
            '4qmFsgKIARIMRkVtdXNpY19ob21lGnhDQU42VmtOcVJVRkJSMVoxUVVGR1NGRm5RVUpTTUVsQlFWRkNSMUpYTVRGak1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUZCVVVGQ1FVRkJRa0ZSVVVKc1JHcE1SVUZCV1RWbGNubDNPRXQ2TmxGSmVVRkI%3D',
            '4qmFsgLhARIMRkVtdXNpY19ob21lGtABQ0FaNmtnRkRha1ZCUVVkV2RVRkJSa2hSWjBGQ1VqQkpRVUZSUWtkU1Z6RXhZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQlFWRkJRa0ZCUVVKQlVWRkNiRVJxVEVWQlRWazFaWEo1ZHpoTGVqWlJTWGxNVW05eVZXdFNSRlJGUmt4T1dGWTFXREozTkZveFNtMU1WbU16VTFad2VFMUlSa2xXVjNSS1lWWlNjRlJZV2paa1IzUnRZVEZKZEZWVVJuTldVUSUzRCUzRA%3D%3D',
            '4qmFsgLhARIMRkVtdXNpY19ob21lGtABQ0FsNmtnRkRha1ZCUVVkV2RVRkJSa2hSWjBGQ1VqQkpRVUZSUWtkU1Z6RXhZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQlFWRkJRa0ZCUVVKQlVWRkNiRVJxVEVWQldWazFaWEo1ZHpoTGVqWlJTWGxNVW05eVZXdFNSRlJGUmt4T1dGWTFXREp6ZVU0elZqRk1WVll3VlZZNWFVNVdWWGxqYWtreVVrVTFSVmRyT1hSVWJrWklXa2RPYWxaVmJFaFZVUSUzRCUzRA%3D%3D',
        ),
        False: \
        (
            'foo',
            'ABCD',
            '.',
        ),
    },
    ytm.types.PlaylistContinuation: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.SearchContinuation: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.WatchContinuation: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumPlaylistBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumPlaylistId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.AlbumShuffleId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistShuffleId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistSongsPlaylistBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistSongsPlaylistId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistSongsRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistSongsShuffleId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ChartPlaylistBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ChartPlaylistId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ChartRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ChartShuffleId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.PlaylistBrowseId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.PlaylistId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.PlaylistRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.PlaylistShuffleId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.SongId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.SongRadioId: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistAlbumsParams: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
    ytm.types.ArtistSinglesParams: \
    {
        True: \
        (
        ),
        False: \
        (
        ),
    },
}

for type, type_data in data.items():
    def _test(type, data):
        for valid, cases in data.items():
            for case_index, case_data in enumerate(cases):
                if valid:
                    type(case_data)
                else:
                    with pytest.raises(TypeError):
                        type(case_data)

    test_name     = f'test_{type.__name__}'
    _test_wrapper = lambda type=type, data=type_data, test=_test: test(type, data)

    locals()[test_name] = _test_wrapper

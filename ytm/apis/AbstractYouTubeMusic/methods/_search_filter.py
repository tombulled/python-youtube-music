from .. import constants
from .. import decorators
from .. import parsers

@decorators.method()
def _search_filter(self: object, query: str, filter: str) -> list:
    filter = filter.strip().lower()
    query  = query.strip()

    param_map = \
    {
        'albums':    constants.SEARCH_PARAM_ALBUMS,
        'artists':   constants.SEARCH_PARAM_ARTISTS,
        'playlists': constants.SEARCH_PARAM_PLAYLISTS,
        'songs':     constants.SEARCH_PARAM_SONGS,
        'videos':    constants.SEARCH_PARAM_VIDEOS,
    }

    param = param_map.get(filter)

    assert query, 'No search query provided'
    assert param, f'Invalid search filter: {repr(filter)}'

    data = self._base.search \
    (
        query  = query,
        params = ''.join \
        (
            (
                constants.SEARCH_PARAM_PREFIX,
                param,
                constants.SEARCH_PARAM_SUFFIX,
            ),
        ),
    )

    # parsed_data = parser.parse(data, filter)
    parsed_data = parsers._search_filter(data, filter)

    return parsed_data

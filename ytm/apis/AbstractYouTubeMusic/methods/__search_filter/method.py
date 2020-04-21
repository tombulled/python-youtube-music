from . import parser
from ... import constants
from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__)
def method(self: object, query: str, filter: str) -> list:
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

    parsed_data = parser.parse(data, filter)

    return parsed_data

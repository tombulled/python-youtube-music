from . import parser
from ... import constants

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

def method(self, query, filter):
    filter = filter.strip().lower()
    query  = query.strip()

    if not query:
        return # No point

    param_map = \
    {
        'albums':    constants.SEARCH_PARAM_ALBUMS,
        'artists':   constants.SEARCH_PARAM_ARTISTS,
        'playlists': constants.SEARCH_PARAM_PLAYLISTS,
        'songs':     constants.SEARCH_PARAM_SONGS,
        'videos':    constants.SEARCH_PARAM_VIDEOS,
    }

    param = param_map.get(filter)

    if not param:
        return

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

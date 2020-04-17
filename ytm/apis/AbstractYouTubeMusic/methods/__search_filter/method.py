from . import parser
from ..... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def method(self, query, filter):
    param_map = \
    {
        'albums':    ytm_constants.SEARCH_PARAM_ALBUMS,
        'artists':   ytm_constants.SEARCH_PARAM_ARTISTS,
        'playlists': ytm_constants.SEARCH_PARAM_PLAYLISTS,
        'songs':     ytm_constants.SEARCH_PARAM_SONGS,
        'videos':    ytm_constants.SEARCH_PARAM_VIDEOS,
    }

    param = param_map[filter]

    data = self._base.search \
    (
        query  = query,
        params = ''.join \
        (
            (
                ytm_constants.SEARCH_PARAM_PREFIX,
                param,
                ytm_constants.SEARCH_PARAM_SUFFIX,
            ),
        ),
    )

    parsed_data = parser.parse(data, filter)

    return parsed_data

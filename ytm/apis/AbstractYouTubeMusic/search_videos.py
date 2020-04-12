from . import parsers
from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def search_videos(self, query):
    data = self.base.search \
    (
        query = query,
        params = ''.join \
        (
            (
                ytm_constants.SEARCH_PARAM_PREFIX,
                ytm_constants.SEARCH_PARAM_VIDEOS,
                ytm_constants.SEARCH_PARAM_SUFFIX,
            ),
        ),
    )

    parsed = parsers.search_videos(data)

    return parsed

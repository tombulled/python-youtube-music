from . import parser
from ..... import constants as ytm_constants
from ... import decorators

__all__ = __name__.split('.')[-1:]

@decorators.parse(parser.parse)
def method(self, query):
    return self._base.search \
    (
        query = query,
        params = ''.join \
        (
            (
                ytm_constants.SEARCH_PARAM_PREFIX,
                ytm_constants.SEARCH_PARAM_ARTISTS,
                ytm_constants.SEARCH_PARAM_SUFFIX,
            ),
        ),
    )

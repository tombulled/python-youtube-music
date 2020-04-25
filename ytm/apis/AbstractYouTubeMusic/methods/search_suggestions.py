# from . import parser
from .. import parsers
from .. import decorators

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.search_suggestions)
def search_suggestions(self: object, query: str) -> list:
    return self._base.search_suggestions \
    (
        query = query
    )

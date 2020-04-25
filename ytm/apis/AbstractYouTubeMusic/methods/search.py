# from . import parser
from .. import parsers
from .. import decorators

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.search)
def search(self: object, query: str) -> dict:
    return self._base.search \
    (
        query = query,
    )

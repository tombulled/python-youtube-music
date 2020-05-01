from .. import decorators
from .... import parsers

@decorators.method(parsers.search_suggestions)
def search_suggestions(self: object, query: str) -> list:
    return self._base.search_suggestions \
    (
        query = query
    )

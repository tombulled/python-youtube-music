from .. import decorators
from .... import parsers

@decorators.method(parsers.search)
def search(self: object, query: str) -> dict:
    return self._base.search \
    (
        query = query,
    )

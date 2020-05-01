from .. import decorators

@decorators.method()
def search_albums(self: object, query: str) -> list:
    return self._search_filter(query, 'albums')

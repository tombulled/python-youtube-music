from . import containers

__all__ = __name__.split('.')[-1:]

def search_suggestions(self, query):
    data = self.base.search_suggestions \
    (
        query = query
    )

    container = containers.SearchSuggestions \
    (
        api = self,
        data = data,
    )

    return container

from . import parsers

__all__ = __name__.split('.')[-1:]

def suggest(self, query):
    data = self.base.search_suggestions \
    (
        query = query
    )

    parsed_data = parsers.search_suggestions(data)

    return parsed_data

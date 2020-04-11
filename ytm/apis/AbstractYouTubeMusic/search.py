from . import parsers

__all__ = __name__.split('.')[-1:]

def search(self, query):
    data = self.base.search \
    (
        query = query,
    )

    parsed = parsers.search(data)

    return parsed

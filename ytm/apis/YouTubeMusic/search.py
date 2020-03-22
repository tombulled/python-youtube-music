from . import containers

__all__ = __name__.split('.')[-1:]

def search(self, query):
    data = self.base.search \
    (
        query = query,
    )

    container = containers.Search \
    (
        api = self,
        data = data,
    )

    return container

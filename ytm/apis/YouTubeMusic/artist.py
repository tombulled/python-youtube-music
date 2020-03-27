from . import containers

__all__ = __name__.split('.')[-1:]

def artist(self, artist_id):
    data = self.base.browse_artist \
    (
        browse_id = artist_id,
    )

    container = containers.Artist \
    (
        api = self,
        data = data,
    )

    return container

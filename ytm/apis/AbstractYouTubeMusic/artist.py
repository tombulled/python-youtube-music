from . import parsers

__all__ = __name__.split('.')[-1:]

def artist(self, artist_id):
    data = self.base.browse_artist \
    (
        browse_id = artist_id,
    )

    parsed_data = parsers.browse_artist(data)

    return parsed_data

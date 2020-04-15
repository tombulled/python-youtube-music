from . import parsers

__all__ = __name__.split('.')[-1:]

def artist_singles(self, artist_id, params):
    data = self.base.browse \
    (
        browse_id = artist_id,
        params    = params,
    )

    parsed_data = parsers.artist_singles(data)

    return parsed_data

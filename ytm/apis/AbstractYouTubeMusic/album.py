from . import parsers
from ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

# Note: alum_id can also be a browse_id
def album(self, id):
    if id.startswith('OLAK5uy'): # playlist_id
        page = self.base.page_playlist \
        (
            list = id,
        )

        browse_id = ytm_utils.get_nested \
        (
            page,
            'INITIAL_ENDPOINT',
            'browseEndpoint',
            'browseId',
        )

        if not browse_id:
            return # raise
    elif id.startswith('MPREb'): # browse_id
        browse_id = id
    else:
        # Make decorator?
        raise ValueError(f'Invalid album id: {repr(id)}')

    data = self.base.browse_album \
    (
        browse_id = browse_id, # check browse_id is correct format?
    )

    parsed_data = parsers.browse_album(data)

    return parsed_data

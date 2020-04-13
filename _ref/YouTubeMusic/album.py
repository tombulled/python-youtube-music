from . import containers
from  ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]


def album(self, album_id=None, browse_id=None):
    if not any((album_id, browse_id)): return # raise?

    if not browse_id:
        page = self.base.page_playlist \
        (
            list = album_id,
        )

        browse_id = ytm_utils.get_nested(page, 'INITIAL_ENDPOINT', 'browseEndpoint', 'browseId')

        if not browse_id:
            return # raise

    data = self.base.browse_album \
    (
        browse_id = browse_id, # check browse if is correct format
    )

    container = containers.Album \
    (
        api = self,
        data = data,
    )

    return container

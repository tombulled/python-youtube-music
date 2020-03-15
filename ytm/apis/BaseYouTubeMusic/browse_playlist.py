from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def browse_playlist(self, browse_id):
    return self.browse \
    (
        browse_id = browse_id,
        page_type = ytm_constants.PAGE_TYPE_PLAYLIST,
    )

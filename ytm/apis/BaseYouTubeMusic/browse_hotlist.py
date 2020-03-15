from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def browse_hotlist(self):
    return self.browse \
    (
        browse_id = ytm_constants.BROWSE_ID_HOTLIST,
    )

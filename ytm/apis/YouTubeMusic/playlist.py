from . import containers
from  ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def playlist(self, playlist_id=None, browse_id=None):
    if not any((playlist_id, browse_id)): return # raise

    if not browse_id:
        if any(playlist_id.startswith(prefix) for prefix in ('RDAO', 'RDEM', 'RDAM', ytm_constants.PREFIX_PLAYLIST)):
            prefix = ''
        else:
            prefix = ytm_constants.PREFIX_PLAYLIST

        browse_id = f'{prefix}{playlist_id}'

    data = self.base.browse_playlist \
    (
        browse_id = browse_id,
    )

    container = containers.Playlist \
    (
        api = self,
        data = data,
    )

    return container

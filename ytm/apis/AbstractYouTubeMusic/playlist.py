from . import parsers
from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def playlist(self, playlist_id=None, continuation=None):
    if playlist_id is not None:
        if any(playlist_id.startswith(prefix) for prefix in ('RDAO', 'RDEM', 'RDAM', ytm_constants.PREFIX_PLAYLIST)):
            prefix = ''
        else:
            prefix = ytm_constants.PREFIX_PLAYLIST

        browse_id = f'{prefix}{playlist_id}'

        data = self.base.browse_playlist \
        (
            browse_id = browse_id,
        )
    elif continuation is not None:
        data = self.base.browse \
        (
            continuation = continuation,
        )
    else:
        # Make this a decorator
        raise TypeError('playlist() missing 1 required argument: \'playlist_id\' or \'continuation\'')

    parsed_data = parsers.browse_playlist(data)

    return parsed_data

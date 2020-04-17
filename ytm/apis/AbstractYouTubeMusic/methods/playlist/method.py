from . import parser
from ..... import constants as ytm_constants
from ... import decorators

__all__ = __name__.split('.')[-1:]

@decorators.parse(parser.parse)
def method(self, playlist_id=None, continuation=None):
    if playlist_id is not None:
        if any(playlist_id.startswith(prefix) for prefix in ('RDAO', 'RDEM', 'RDAM', ytm_constants.PREFIX_PLAYLIST)):
            prefix = ''
        else:
            prefix = ytm_constants.PREFIX_PLAYLIST

        browse_id = f'{prefix}{playlist_id}'

        return self._base.browse_playlist \
        (
            browse_id = browse_id,
        )
    elif continuation is not None:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        # Make this a decorator
        raise TypeError('playlist() missing 1 required argument: \'playlist_id\' or \'continuation\'')

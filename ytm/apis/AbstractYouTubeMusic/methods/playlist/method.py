from . import parser
from ... import constants
from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, playlist_id=None, continuation=None) -> dict:
    if playlist_id is not None:
        if any(playlist_id.startswith(prefix) for prefix in ('RDAO', 'RDEM', 'RDAM', constants.PREFIX_PLAYLIST)):
            prefix = ''
        else:
            prefix = constants.PREFIX_PLAYLIST

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

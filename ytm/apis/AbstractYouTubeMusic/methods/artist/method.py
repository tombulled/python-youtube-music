from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

@decorators.parse(parser.parse)
def method(self, artist_id):
    if len(artist_id) != 24 or not artist_id.startswith('UC'):
        raise ValueError(f'Invalid artist id: {repr(artist_id)}')

    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

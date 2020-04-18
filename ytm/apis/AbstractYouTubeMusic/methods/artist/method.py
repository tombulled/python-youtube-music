from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

@decorators.parse(parser.parse)
def method(self, artist_id):
    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

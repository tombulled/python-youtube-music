from . import parser
from ... import decorators

__all__ = __name__.split('.')[-1:]

@decorators.parse(parser.parse)
def method(self, artist_id):
    return self._base.browse_artist \
    (
        browse_id = artist_id,
    )

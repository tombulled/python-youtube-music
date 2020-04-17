from . import parser
from ... import decorators

__all__ = __name__.split('.')[-1:]

@decorators.parse(parser.parse)
def method(self, continuation=None):
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

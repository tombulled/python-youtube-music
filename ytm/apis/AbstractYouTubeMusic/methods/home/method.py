from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

@decorators.parse(parser.parse)
def method(self, continuation=None):
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

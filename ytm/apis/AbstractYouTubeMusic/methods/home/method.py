from . import parser
from ... import decorators
from ... import types

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

Continuation = types.Continuation

@decorators.parse(parser.parse)
def method(self, continuation: Continuation=None):
    continuation = Continuation(continuation)
    
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

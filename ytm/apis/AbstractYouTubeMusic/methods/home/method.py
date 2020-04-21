from . import parser
from ... import decorators
from ...types import HomeContinuation

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, continuation: HomeContinuation = None) -> dict:
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

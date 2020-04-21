from . import parser
from ... import decorators
from ... import types

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

Continuation = types.Continuation

@decorators.enforce(parameters=False, return_value=True)
@decorators.parse(parser.parse)
@decorators.enforce(parameters=True, return_value=False)
@decorators.rename(__method__)
def method(self: object, continuation: Continuation=None) -> dict:
    # continuation = Continuation(continuation)

    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

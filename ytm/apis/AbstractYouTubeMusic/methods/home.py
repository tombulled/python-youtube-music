from .. import decorators
from .... import parsers
from ....types import HomeContinuation

@decorators.method(parsers.home)
def home(self: object, continuation: HomeContinuation = None) -> dict:
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

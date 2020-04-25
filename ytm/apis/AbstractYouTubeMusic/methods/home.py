# from . import parser
from .. import parsers
from .. import decorators
from ..types import HomeContinuation

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.home)
def home(self: object, continuation: HomeContinuation = None) -> dict:
    if continuation:
        return self._base.browse \
        (
            continuation = continuation,
        )
    else:
        return self._base.browse_home()

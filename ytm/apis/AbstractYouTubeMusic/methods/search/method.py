from . import parser
from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__all__      = (__function__,)

@decorators.method(__method__, parser.parse)
def method(self: object, query: str) -> dict:
    return self._base.search \
    (
        query = query,
    )

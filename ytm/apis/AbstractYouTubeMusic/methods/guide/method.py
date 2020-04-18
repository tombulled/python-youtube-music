from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__ = (__method__,)

@decorators.parse(parser.parse)
def method(self):
    return self._base.guide()
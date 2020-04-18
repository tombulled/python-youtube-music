from . import parser
from ... import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.parse(parser.parse)
def method(self, query):
    return self._base.search_suggestions \
    (
        query = query
    )

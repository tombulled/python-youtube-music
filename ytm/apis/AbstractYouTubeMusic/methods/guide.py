# from . import parser
from .. import parsers
from .. import decorators

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.guide)
def guide(self: object) -> dict:
    return self._base.guide()

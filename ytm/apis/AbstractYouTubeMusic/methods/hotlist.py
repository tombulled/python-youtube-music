# from . import parser
from .. import parsers
from .. import decorators

# @decorators.method(__method__, parser.parse)
@decorators.method(parsers.hotlist)
def hotlist(self: object):
    return self._base.browse_hotlist()

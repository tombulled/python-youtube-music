from .. import decorators
from .... import parsers

@decorators.method(parsers.hotlist)
def hotlist(self: object):
    return self._base.browse_hotlist()

from .. import decorators
from .... import parsers

@decorators.method(parsers.guide)
def guide(self: object) -> dict:
    return self._base.guide()

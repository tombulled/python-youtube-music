from .. import decorators
from ....types import SearchContinuation

@decorators.method()
def search_artists \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._search_filter \
    (
        filter       = 'artists',
        query        = query,
        continuation = continuation,
    )

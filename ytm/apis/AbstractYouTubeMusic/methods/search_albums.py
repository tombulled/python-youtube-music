from .. import decorators
from ....types import SearchContinuation

@decorators.method()
def search_albums \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._search_filter \
    (
        filter       = 'albums',
        query        = query,
        continuation = continuation,
    )

from .. import decorators
from ....types import SearchContinuation

@decorators.method()
def search_songs \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._search_filter \
    (
        filter       = 'songs',
        query        = query,
        continuation = continuation,
    )

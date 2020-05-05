from .. import decorators
from ....types import SearchContinuation

@decorators.method()
def search_playlists \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._search_filter \
    (
        filter       = 'playlists',
        query        = query,
        continuation = continuation,
    )

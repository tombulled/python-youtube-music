from .. import decorators
from ....types import SearchContinuation

@decorators.method()
def search_videos \
        (
            self:         object,
            query:        str                = None,
            continuation: SearchContinuation = None,
        ) -> dict:
    '''
    '''

    return self._search_filter \
    (
        filter       = 'videos',
        query        = query,
        continuation = continuation,
    )

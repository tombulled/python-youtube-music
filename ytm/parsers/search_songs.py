from ._search_filter import _search_filter as parse_search_filter
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search_songs(data: dict):
    return parse_search_filter \
    (
        data   = data,
        filter = 'songs',
    )

from .. import decorators

@decorators.method()
def search_videos(self: object, query: str) -> list:
    return self._search_filter(query, 'videos')

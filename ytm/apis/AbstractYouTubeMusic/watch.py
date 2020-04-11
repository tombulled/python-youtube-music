from . import parsers

__all__ = __name__.split('.')[-1:]

def watch(self, song_id=None, playlist_id=None, params=None, continuation=None):
    data = self.base.next \
    (
        video_id     = song_id,
        playlist_id  = playlist_id,
        params       = params,
        continuation = continuation,
    )

    parsed_data = parsers.next(data)

    return parsed_data

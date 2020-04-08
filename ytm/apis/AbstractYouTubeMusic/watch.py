from . import parsers

__all__ = __name__.split('.')[-1:]

def watch(self, song_id, playlist_id=None, params=None):
    # Watch has a continuation!

    data = self.base.next \
    (
        video_id = song_id,
        playlist_id = playlist_id,
        params = params,
    )

    parsed_data = parsers.next(data)

    return parsed_data

from . import containers

__all__ = __name__.split('.')[-1:]

def song_info(self, song_id):
    data = self.base.video_info \
    (
        video_id = song_id,
    )

    container = containers.SongInfo \
    (
        api = self,
        data = data,
    )

    return container

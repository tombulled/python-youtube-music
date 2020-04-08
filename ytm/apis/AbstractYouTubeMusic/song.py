from . import parsers

__all__ = __name__.split('.')[-1:]

def song(self, song_id):
    data = self.base.video_info \
    (
        video_id = song_id,
    )

    parsed_data = parsers.video_info(data)

    return parsed_data

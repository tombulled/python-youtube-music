from ... import constants as ytm_constants
from ... import utils     as ytm_utils

# NOTE: Merge me with _test/test-1.py

class YouTubeMusicDL(object):
    def __init__(self):
        # Module is heavy
        import youtube_dl

        self.ytdl = youtube_dl.YoutubeDL \
        (
            params = \
            {
                'format': 'bestaudio',
                'quiet': True,
            }
        )

    def info(self, video_id):
        info = self._video_info \
        (
            video_id = video_id,
        )

        return info

    def download(self, video_id):
        info = self._video_info \
        (
            video_id = video_id,
            download = True,
        )

        return info

    def _video_info(self, video_id, download=False):
        info = self.ytdl.extract_info \
        (
            url      = ytm_utils.url_youtube(f'watch/?v={video_id}'),
            ie_key   = 'Youtube',
            download = download,
        )

        return info

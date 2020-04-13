import pathlib
import os

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
                'outtmpl': '%(title)s.%(ext)s',
            }
        )

        self._format_selector = self.ytdl.build_format_selector('bestaudio')

    def info(self, video_id):
        info = self._video_info \
        (
            video_id = video_id,
        )

        return info

    def download(self, video_id, file_name=None, file_path=None):
        if not file_path:
            file_path = os.getcwd()

        if not file_name:
            file_name = '%(title)s'

        if '.' not in file_name:
            file_name += '.%(ext)s'

        path_directory = pathlib.Path(file_path)

        path_file = path_directory.joinpath(file_name)

        _param_outtmpl = self.ytdl.params.get('outtmpl', None)

        self.ytdl.params['outtmpl'] = str(path_file)

        info = self._video_info \
        (
            video_id = video_id,
            download = True,
        )

        format = next(self._format_selector(info))

        file_name = file_name % \
        {
            'title': info['title'],
            'ext': format['ext'],
        }

        path_file = path_directory.joinpath(file_name)

        if _param_outtmpl:
            self.ytdl.params['outtmpl'] = _param_outtmpl

        success = not self.ytdl._download_retcode

        if success:
            return str(path_file)

    def _video_info(self, video_id, download=False):
        info = self.ytdl.extract_info \
        (
            url = f'https://www.youtube.com/watch?v={video_id}',
            ie_key = 'Youtube',
            download = download,
        )

        return info

dl = YouTubeMusicDL()

x = dl.download('8zZHAfq0gls', file_name='Aquilo - Sober', file_path='C:/Users/Admin/Desktop')

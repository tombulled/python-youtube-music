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
                'format':  'bestaudio',
                'quiet':   True,
                'outtmpl': '%(title)s.%(ext)s',
            }
        )

    def info(self, video_id):
        info = self._info \
        (
            video_id = video_id,
        )

        return info

    def download_audio(self, video_id, file_name=None, file_path=None):
        return self.download \
        (
            video_id  = video_id,
            file_name = file_name,
            file_path = file_path,
            format    = 'bestaudio',
        )

    def download_video(self, video_id, file_name=None, file_path=None):
        return self.download \
        (
            video_id  = video_id,
            file_name = file_name,
            file_path = file_path,
            format    = 'bestvideo+bestaudio/best',
        )

    def download(self, video_id, file_name=None, file_path=None, format=None):
        if not file_path:
            file_path = os.getcwd()

        if not file_name:
            file_name = '%(title)s'

        if '.' not in file_name:
            file_name += '.%(ext)s'

        if format is None:
            format = 'bestaudio'

        path_directory = pathlib.Path(file_path)

        path_file = path_directory.joinpath(file_name)

        _param_outtmpl = self.ytdl.params.get('outtmpl', None)
        _param_format = self.ytdl.params.get('format', None)

        self.ytdl.params['outtmpl'] = str(path_file)
        self.ytdl.params['format'] = format

        info = self._info \
        (
            video_id = video_id,
            download = True,
        )

        format_selector = self.ytdl.build_format_selector(format)

        format = next(format_selector(info))

        file_name = file_name % \
        {
            'title': info['title'],
            'ext': format['ext'],
        }

        path_file = path_directory.joinpath(file_name)

        if _param_outtmpl:
            self.ytdl.params['outtmpl'] = _param_outtmpl

        if _param_format:
            self.ytdl.params['format'] = _param_format

        success = not self.ytdl._download_retcode

        if success:
            return str(path_file)

    def _info(self, video_id, download=False):
        info = self.ytdl.extract_info \
        (
            url = f'https://www.youtube.com/watch?v={video_id}',
            ie_key = 'Youtube',
            download = download,
        )

        return info

dl = YouTubeMusicDL()

x = dl.download_audio('8zZHAfq0gls', file_name='Aquilo - Sober', file_path='C:/Users/Admin/Desktop')

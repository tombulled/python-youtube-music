from ..YouTubeMusic import YouTubeMusic
from ... import utils

import pathlib
import os
import io
import requests

# https://github.com/tombulled/python-youtube-music/issues/5
# The issue above highlighted that creationflags is specific to Windows only
# As CMD opening is a very Windows specific issue and is not super important
# the code below has been left commented-out for now until a working
# platform independent solution is found

# Monkey patch ffmpeg's popen:
# import subprocess
# import functools
# subprocess._Popen = subprocess.Popen
# subprocess.Popen  = functools.partial \
# (
#     subprocess._Popen,
#     creationflags = 0x08000000,
# )

class BaseYouTubeMusicDL(object):
    def __init__(self, youtube_downloader=None):
        if not youtube_downloader:
            import youtube_dl
            youtube_downloader = youtube_dl.YoutubeDL
        self._yt_dl = youtube_downloader

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}()>'
        
    def _download \
            (
                self,
                song_id,
                metadata  = None,
                thumbnail = None,
                directory = None,
                video     = False,
            ):
        '''
        '''

        import mutagen.easyid3
        import mutagen.id3
        import mutagen.mp4
        import mutagen.easymp4

        file_name_format = '%(title)s.%(ext)s'

        if not metadata:
            metadata = {}

        if directory:
            path_directory = pathlib.Path(directory)
        else:
            path_directory = pathlib.Path(os.getcwd())

        path_file = path_directory.joinpath(file_name_format)

        post_processors = []

        if video:
            format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
            to_ext = 'mp4'
        else:
            format = 'bestaudio'
            to_ext = 'mp3'

            post_processors.append \
            (
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': to_ext,
                }
            )

        ytdl = self._yt_dl \
        (
            params = \
            {
                'quiet':          True,
                'outtmpl':        str(path_file),
                'postprocessors': post_processors,
                'format':         format,
            }
        )

        url = utils.url_yt \
        (
            'watch',
            params = {'v': song_id},
        )

        info = ytdl.extract_info \
        (
            url      = url,
            ie_key   = 'Youtube',
            download = True,
        )

        any_title = info.get('track', info.get('title'))
        metadata = utils.filter \
        (
            {
                'title':       any_title,
                'artist':      info.get('artist'),
                'album':       info.get('album'),
                'albumartist': info.get('artist'),
                'discnumber':  '1',
                'tracknumber': '1',
                'date':        str(info.get('release_year')),
                **metadata,
            }
        )
        info.setdefault('track', any_title)

        sanitized_name = info['title']
        illegal_chars = ['\\', '/', ':', '*', '?', '<', '>', '|', '"']
        for char in illegal_chars:
            sanitized_name = sanitized_name.replace(char, '_')
        file_path_src = self._get_file_path \
        (
            info,
            file_name_format % \
            {
                'title': sanitized_name,
                'ext': to_ext,
            },
            directory,
        )

        file_path_dst = file_path_src.parent.joinpath \
        (
            file_name_format % \
            {
                'title': sanitized_name,
                'ext':   to_ext,
            }
        )

        if not thumbnail:
            thumbnail = self._get_album_art(info['thumbnails'][0]['url'], crop=True)

        if video:
            mp4 = mutagen.mp4.MP4(file_path_dst)

            cover = mutagen.mp4.MP4Cover \
            (
                thumbnail,
                imageformat = mutagen.mp4.AtomDataType.PNG,
            )

            mp4['covr'] = (cover,)

            mp4.save()

            easymp4 = mutagen.easymp4.EasyMP4(file_path_dst)

            easymp4.update(metadata)

            easymp4.save()
        else:
            id3 = mutagen.id3.ID3(file_path_dst)

            ENCODING_UTF8 = 3
            MIME_PNG  = 'image/png'
            IMAGE_TYPE_COVER = 3
            IMAGE_DESCRIPTION_COVER = 'Cover'

            id3.add \
            (
                mutagen.id3.APIC
                (
                    encoding = ENCODING_UTF8,
                    mime     = MIME_PNG,
                    type     = IMAGE_TYPE_COVER,
                    desc     = IMAGE_DESCRIPTION_COVER,
                    data     = thumbnail,
                )
            )

            id3.save(v2_version = 3)

            easyid3 = mutagen.easyid3.EasyID3(file_path_dst)

            easyid3.update(metadata)

            easyid3.save(v2_version = 3)

        # Rename to {track}.{ext} here?

        success = not ytdl._download_retcode

        if success:
            return info

    def _get_file_path(self, info, template, directory=None):
        if not directory:
            directory = os.getcwd()

        path_directory = pathlib.Path(directory)

        file_name = template % \
        {
            'track': info['track'],
            'ext':   info['ext'],
        }

        path_file = path_directory.joinpath(file_name)

        return path_file

    def _get_album_art(self, url, crop=True):
        from PIL import Image

        resp   = requests.get(url) # Use _api's session
        buffer = io.BytesIO(resp.content)
        image  = Image.open(buffer)

        if crop:
            buffer = io.BytesIO()

            image_size = image.size

            region = \
            (
                (image_size[0] - image_size[1]) // 2,
                0,
                image_size[1] + ((image_size[0] - image_size[1]) // 2),
                image_size[1],
            )

            image_cropped = image.crop(region)

            image_cropped.save(buffer, format='PNG')

        buffer.seek(0)

        return buffer.read()

class AbstractYouTubeMusicDL(object):
    def __init__(self: object, api: object = None):
        if api is None:
            api = YouTubeMusic()

        self._base = BaseYouTubeMusicDL()
        self._api = api

    def download_song(self, song_id, directory=None):
        return self._base._download \
        (
            song_id   = song_id,
            directory = directory,
            video     = False,
        )

    def download_video(self, song_id, directory=None):
        return self._base._download \
        (
            song_id   = song_id,
            directory = directory,
            video     = True,
        )

    def download_album(self, album_id, directory=None):
        album = self._api.album(album_id)

        album_thumbnail_url = album['thumbnail']['url']
        album_artist        = album['artists'][0]['name']
        album_name          = album['name']
        album_year          = album['date']['year']
        album_tracks        = album['tracks']

        thumbnail = self._base._get_album_art \
        (
            url  = album_thumbnail_url,
            crop = False,
        )

        metadata = utils.filter \
        (
            {
                'artist':      album_artist,
                'album':       album_name,
                'albumartist': album_artist,
                'date':        str(album_year),
            }
        )

        # Create album directory

        for index, track in enumerate(album_tracks, start = 1):
            track_id    = track['id']
            track_name  = track['name']
            track_index = str(index)

            track_metadata = \
            {
                **metadata,
                'title': track_name,
                'tracknumber': track_index,

            }

            downloaded = self._base._download \
            (
                song_id   = track_id,
                metadata  = track_metadata,
                thumbnail = thumbnail,
                directory = directory, # CHANGE THIS
                video     = False,
            )

        return album

    def download_playlist(self, playlist_id, directory=None):
        playlist = self._api.playlist(playlist_id)

        playlist_name          = playlist['name']
        playlist_year          = str(playlist['year'])
        playlist_thumbnail_url = playlist['thumbnail']['url']
        playlist_tracks        = playlist['tracks']
        playlist_continuation  = playlist['continuation']
        playlist_artist_name   = playlist['artist']['name']

        thumbnail = self._base._get_album_art \
        (
            url  = playlist_thumbnail_url,
            crop = False,
        )

        metadata = utils.filter \
        (
            {
                'album':       playlist_name,
                'albumartist': playlist_artist_name,
                'date':        playlist_year,
            }
        )

        while playlist_continuation:
            data = self._api.playlist(continuation = playlist_continuation)

            playlist_tracks.append(data['tracks'])

        # Create playlist directory

        for track_index, track in enumerate(playlist_tracks, start = 1):
            track_artist_name = track['artist']['name']
            track_name        = track['name']
            track_id          = track['id']
            track_index       = str(track_index)

            track_metadata = \
            {
                **metadata,
                'title': track_name,
                'tracknumber': track_index,
                'artist': track_artist_name,
            }

            downloaded = self._base._download \
            (
                song_id   = track_id,
                metadata  = track_metadata,
                thumbnail = thumbnail,
                directory = directory, # CHANGE THIS
                video     = False,
            )

        return playlist

class YouTubeMusicDL(AbstractYouTubeMusicDL):
    pass

import time
t1=time.time()
import youtube_dl
t2=time.time()
print('Imported in:', t2-t1)
# exit()
from pprint import pprint as pp

def get_video_info(video_id):
    opts = \
    {
        'quiet': True,
    }

    with youtube_dl.YoutubeDL(opts) as ydl:
        info = ydl.extract_info \
        (
            url = f'https://www.youtube.com/watch?v={video_id}',
            download = False,
            ie_key = 'Youtube',
        )

    return info

def download(video_id):
    opts = \
    {
        'format': 'bestaudio',
        'quiet': True,
    }

    with youtube_dl.YoutubeDL(opts) as ydl:
        info = ydl.extract_info \
        (
            url = f'https://www.youtube.com/watch?v={video_id}',
            download = True,
            ie_key = 'Youtube',
        )

        print('Return code:', ydl._download_retcode)

    return info

def time_it(func, *args, **kwargs):
    time_start = time.time()
    response = func(*args, **kwargs)
    time_stop = time.time()
    print(f'Executed in: {time_stop - time_start}')

    return response

# info  = time_it(get_video_info, 'mG2WyysmHF8')
info2 = time_it(download, 'mG2WyysmHF8')

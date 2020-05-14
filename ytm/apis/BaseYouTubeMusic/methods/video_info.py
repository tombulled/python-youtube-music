'''
Module containing the method: video_info
'''

from .. import constants
from .. import utils
from .. import decorators

import urllib
import base64
import json
import requests

@decorators.catch
def video_info(self: object, video_id: str) -> dict:
    '''
    Retrieve video info data.

    Unlike other methods, this relies on YouTube instead of YouTube Music.
    YouTube Music itself uses this to get further information about videos.

    Args:
        self: Class instance
        video_id: Video id
            Example: 'CkOP828oL30'

    Returns:
        Video info data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.video_info('CkOP828oL30')
        >>>
        >>> data['player_response']['videoDetails']['title']
        'Passenger | Bullets (Official Album Audio)'
        >>>
    '''

    video_id = str(video_id)

    resp = requests.get \
    (
        url = self._url_yt(constants.ENDPOINT_YT_VIDEO_INFO),
        params = \
        {
            'video_id': video_id,
            'el': 'detailpage',
            'ps': 'default',
            'hl': 'en',
            'gl': 'US',
            'eurl': f'https://youtube.googleapis.com/v/{video_id}', # Make this use a url util
        }
    )

    data = dict(urllib.parse.parse_qsl(resp.text))

    # Offload this to /parsers/song?
    parsers = \
    {
        'fexp': lambda data:  \
            list(map(int, data.split(','))),
        'fflags': lambda data: \
            utils.parse_fflags(dict(urllib.parse.parse_qsl(data))),
        'account_playback_token': lambda data: \
            base64.b64decode(data.encode()).decode(),
        'timestamp': lambda data: \
            int(data),
        'enablecsi': lambda data: \
            bool(int(data)),
        'use_miniplayer_ui': lambda data: \
            bool(int(data)),
        'autoplay_count': lambda data: \
            int(data),
        'player_response': lambda data: \
            json.loads(data),
        'watch_next_response': lambda data: \
            json.loads(data),
        'watermark': lambda data: \
            data.strip(',').split(','),
        'rvs': lambda data: \
            dict(urllib.parse.parse_qsl(data)),
    }

    for key, val in data.items():
        if key in parsers:
            data[key] = parsers[key](val)

    return data

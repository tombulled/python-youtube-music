'''
'''

from .. import constants
from .. import utils
from .. import decorators

import urllib
import base64
import json

@decorators.catch
def video_info(self: object, video_id: str) -> dict:
    '''
    '''

    resp = self.session.get \
    (
        url = self._url_yt(constants.ENDPOINT_YT_VIDEO_INFO),
        params = \
        {
            'video_id': video_id,
            'el': 'detailpage',
            'ps': 'default',
            'hl': 'en',
            'gl': 'US',
            'eurl': f'https://youtube.googleapis.com/v/{video_id}',
        }
    )

    data = dict(urllib.parse.parse_qsl(resp.text))

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

from ... import constants as ytm_constants

from . import utils

import urllib
import base64
import json

__all__ = __name__.split('.')[-1:]

def video_info(self, video_id):
    resp = self.session.get \
    (
        url = self._url_yt(ytm_constants.ENDPOINT_YT_VIDEO_INFO),
        params = \
        {
            'video_id': video_id,
            'el': 'detailpage',
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
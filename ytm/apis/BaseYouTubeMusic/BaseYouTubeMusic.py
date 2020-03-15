''' xxx '''

import requests
import re
import json
import base64
import urllib

from . import utils

from ... import constants as ytm_constants
from ... import utils     as ytm_utils

__all__ = __name__.split('.')[-1:]

class BaseYouTubeMusic(object):
    def __init__(self):
        self.session = requests.Session()

        self.domain       = ytm_constants.DOMAIN_YOUTUBE_MUSIC
        self.protocol     = ytm_constants.PROTOCOL_HTTPS
        self.api_endpoint = ytm_constants.ENDPOINT_YTM_API

        self.session.headers.update \
        (
            {
                'User-Agent'       : ytm_utils.random_user_agent(),
                'X-Goog-Visitor-Id': ytm_constants.HEADER_VISITOR_ID,
                'Referer'          : self._url(),
            }
        )

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

    def page_home(self):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_HOME,
        )

    def page_hotlist(self):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_HOTLIST,
        )

    def page_search(self, q):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_SEARCH,
            params = \
            {
                'q': q,
            },
        )

    def page_playlist(self, list):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_PLAYLIST,
            params = \
            {
                'list': list,
            },
        )

    def page_channel(self, channel):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_CHANNEL + channel,
        )

    def page_watch(self, v, list=None):
        return self._get_page \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_WATCH,
            params = ytm_utils.filter_dict \
            (
                {
                    'v': v,
                    'list': list,
                }
            ),
        )

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

    def search(self, query=None, params=None, continuation=None):
        url = self._url_api(ytm_constants.ENDPOINT_YTM_API_SEARCH)

        url_params = ytm_constants.URL_PARAMS
        payload    = ytm_constants.PAYLOAD

        if continuation:
            url_params['continuation'] = continuation

        if not query:
            query = ''

        payload['query'] = query

        if params:
            payload['params'] = params
        else:
            payload['suggestStats'] = \
            {
                'clientName': 'youtube-music',
                'inputMethod': 'KEYBOARD',
                'originalQuery': query,
                'parameterValidationStatus': 'VALID_PARAMETERS',
                'searchMethod': 'ENTER_KEY',
                'validationStatus': 'VALID',
                'zeroPrefixEnabled': True,
            }

        resp = self.session.post(url, params=url_params, json=payload)

        data = resp.json()

        return data

    def browse_album(self, browse_id):
        return self.browse \
        (
            browse_id = browse_id,
            page_type = ytm_constants.PAGE_TYPE_ALBUM,
        )

    def browse_artist(self, browse_id):
        return self.browse \
        (
            browse_id = browse_id,
            page_type = ytm_constants.PAGE_TYPE_ARTIST,
        )

    def browse_playlist(self, browse_id):
        return self.browse \
        (
            browse_id = browse_id,
            page_type = ytm_constants.PAGE_TYPE_PLAYLIST,
        )

    def browse_home(self):
        return self.browse \
        (
            browse_id = ytm_constants.BROWSE_ID_HOME,
        )

    def browse_hotlist(self):
        return self.browse \
        (
            browse_id = ytm_constants.BROWSE_ID_HOTLIST,
        )

    def browse(self, browse_id=None, page_type=None, continuation=None):
        url = self._url_api(ytm_constants.ENDPOINT_YTM_API_BROWSE)
        params = ytm_constants.URL_PARAMS

        if continuation:
            params['continuation'] = continuation
            params['ctoken']       = continuation

        payload = ytm_constants.PAYLOAD

        if browse_id:
            payload['browseId'] = browse_id

        if page_type:
            payload['browseEndpointContextSupportedConfigs'] = \
            {
                'browseEndpointContextMusicConfig': \
                {
                    'pageType': page_type,
                }
            }

        resp = self.session.post \
        (
            url    = url,
            params = params,
            json   = payload,
        )

        data = resp.json()

        return data

    def next \
            (
                self,
                playlist_id         = None,
                video_id            = None,
                index               = None,
                music_video_type    = None,
                params              = None,
                tuner_setting_value = None,
                player_params       = None,
            ):
        url = self._url_api(ytm_constants.ENDPOINT_YTM_API_NEXT)

        url_params = ytm_constants.URL_PARAMS

        payload = ytm_constants.PAYLOAD

        payload.update \
        (
            {
                'enablePersistentPlaylistPanel': True,
                'isAudioOnly': True,
                'params': params or 'wAEB',
                'tunerSettingValue': tuner_setting_value or 'AUTOMIX_SETTING_NORMAL',
            }
        )

        if playlist_id:
            payload['playlistId'] = playlist_id

        if video_id:
            payload.update \
            (
                {
                    'videoId': video_id,
                    'watchEndpointMusicSupportedConfigs': \
                    {
                        'watchEndpointMusicConfig': \
                        {
                            'hasPersistentPlaylistPanel': True,
                            'musicVideoType': music_video_type or 'MUSIC_VIDEO_TYPE_OMV',
                        },
                    },
                }
            )

        if index:
            payload['index'] = index

        if player_params:
            payload['playerParams'] = player_params

        resp = self.session.post \
        (
            url    = url,
            params = url_params,
            json   = payload,
        )

        data = resp.json()

        return data

    def guide(self):
        url = self._url_api(ytm_constants.ENDPOINT_YTM_API_GUIDE)

        params  = ytm_constants.URL_PARAMS
        payload = ytm_constants.PAYLOAD

        resp = self.session.post \
        (
            url    = url,
            params = params,
            json   = payload,
        )

        data = resp.json()

        return data

    def search_suggestions(self, query=None):
        url = self._url_api(ytm_constants.ENDPOINT_YTM_API_SEARCH_SUGGESTIONS)

        params  = ytm_constants.URL_PARAMS
        payload = ytm_constants.PAYLOAD

        payload['input'] = query or ''

        resp = self.session.post \
        (
            url    = url,
            params = params,
            json   = payload,
        )

        data = resp.json()

        return data

    def _get_page(self, endpoint, *args, **kwargs):
        url = self._url(endpoint)

        resp = self.session.get(url, *args, **kwargs)

        config_data = re.search(r'ytcfg\.set\((?P<data>.*)\);', resp.text)

        if config_data is None: return

        config_data = config_data.group('data')

        config = json.loads(config_data)

        for key, val in config.items():
            if isinstance(val, str) and val.startswith('{'):
                config[key] = json.loads(val)

        return config

    @staticmethod
    def _url(endpoint=None):
        return ytm_utils.url_youtube_music \
        (
            endpoint = endpoint or '',
        )

    @staticmethod
    def _url_yt(endpoint=None):
        return ytm_utils.url_youtube \
        (
            endpoint = endpoint or '',
        )

    @staticmethod
    def _url_api(endpoint=None):
        return ytm_utils.url_youtube_music \
        (
            endpoint = ytm_constants.ENDPOINT_YTM_API + (endpoint or ''),
        )

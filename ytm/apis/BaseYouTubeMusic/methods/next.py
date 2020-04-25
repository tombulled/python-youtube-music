'''
'''

from .. import constants
from .. import decorators

@decorators.catch
def next \
        (
            self:                object,
            video_id:            str    = None,
            playlist_id:         str    = None,
            index:               int    = None,
            music_video_type:    str    = None,
            params:              str    = None,
            tuner_setting_value: str    = None,
            player_params:       str    = None,
            continuation:        str    = None,
        ) -> dict:
    '''
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_NEXT)

    url_params = constants.URL_PARAMS

    payload = constants.PAYLOAD

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

    if continuation:
        payload['continuation'] = continuation

    resp = self.session.post \
    (
        url    = url,
        params = url_params,
        json   = payload,
    )

    data = resp.json()

    return data

'''
Module containing the method: next
'''

import copy
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
    Return next data.

    Next data is used when listening to a song/playlist and returns the
    tracks in the queue

    Args:
        self: Class instance
        video_id: Video Id
            Example: '-yDWjtrgkb0'
        playlist_id: Playlist Id
            Example: 'PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM'
            Note: This is *not* a browse id
        index: Video index
            Example: 1
            Note: This is zero-based
        music_video_type: Music video type
            Example: 'MUSIC_VIDEO_TYPE_OMV'
        params: Params
            Example: 'OAHyAQIIAQ%3D%3D'
        tuner_setting_value: Tuner settings value
            Example: 'AUTOMIX_SETTING_NORMAL'
        player_params: Player params
            Example: 'igMDCNgE'
        continuation: Continuation
            Example: 'CDISPBILdUxIcXBqVzNhRHMiIlBMNGZHU0kxcERKbjVrSTgxSjFmWV...'

    Returns:
        Next data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.next \
        (
        	video_id = 'l0U7SxXHkPY',
        	playlist_id = 'PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM',
        	tuner_setting_value = 'AUTOMIX_SETTING_NORMAL',
        	music_video_type = 'MUSIC_VIDEO_TYPE_OMV',
        )
        >>>
        >>> data['currentVideoEndpoint']['watchEndpoint']
        {'videoId': 'l0U7SxXHkPY', 'playlistId': 'PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM', 'index': 0}
        >>>
    '''

    url = self._url_api(constants.ENDPOINT_YTM_API_NEXT)

    url_params = copy.deepcopy(self._params)
    payload    = copy.deepcopy(self._payload)

    payload.update \
    (
        {
            'enablePersistentPlaylistPanel': True,
            'isAudioOnly': True,
            'params': params or constants.PARAMS_WATCH,
            'tunerSettingValue': tuner_setting_value or constants.AUTOMIX_SETTING_NORMAL,
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
                        'musicVideoType': music_video_type or constants.MUSIC_VIDEO_TYPE_OMV,
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

    resp = self._session.post \
    (
        url    = url,
        params = url_params,
        json   = payload,
    )

    data = resp.json()

    return data

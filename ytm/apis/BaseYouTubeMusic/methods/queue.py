'''
Module containing the method: queue
'''

from .. import constants

import copy

def queue(self: object, *video_ids: str, playlist_id: str = None) -> dict:
    '''
    Return queue data.

    Enqueues the specified video_id's or playlist_id and returns their songs data.
    The playlist_id argument should not be a browse id.

    Args:
         self: Class instance
        *video_ids: Video Ids to enqueue
         playlist_video: Playlist Id to enqueue

    Returns:
        Queue data

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.queue('Gz3-4UuMWjQ', 'Ye8Er8MtiLk')
        >>>
        >>> for song in data['queueDatas']:
        	song = song['content']['playlistPanelVideoRenderer']

        	print(song['title'])

        {'runs': [{'text': 'Amen'}]}
        {'runs': [{'text': 'Kites'}]}
        >>>
    '''

    url_params = copy.deepcopy(self._params)
    payload    = copy.deepcopy(self._payload)

    if playlist_id:
        payload['playlistId'] = playlist_id

        video_ids = (None,)

    payload['videoIds'] = video_ids

    resp = self._session.post \
    (
        url    = self._url_api(constants.ENDPOINT_YTM_API_GET_QUEUE),
        params = url_params,
        json   = payload,
    )

    data = resp.json()

    return data

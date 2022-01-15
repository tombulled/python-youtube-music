'''
Module containing the parser: queue
'''

from .. import utils
from . import decorators
from . import constants
from . import formatters
from . import cleansers

@decorators.enforce_parameters
@decorators.catch
def queue(data: dict) -> list:
    '''
    Parse data: Queue.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.queue('Gz3-4UuMWjQ')
        >>>
        >>> parsed_data = ytm.parsers.queue(data)
        >>>
        >>> parsed_data[0]['name']
        'Amen'
        >>>
    '''

    assert data, 'No data to parse'

    queue_items = utils.get(data, 'queueDatas', default=())

    assert queue_items, 'No queded items'

    songs = []

    for queue_item in queue_items:
        queue_item_content = utils.get(queue_item, 'content')
        panel_video        = utils.first(queue_item_content)
        panel_video_menu   = utils.get(panel_video, *constants.MENU_ITEMS, func = formatters.menu_items)

        video_title             = utils.get(panel_video, 'title', *constants.RUN_TEXT)
        video_thumbnail         = utils.get(panel_video, *constants.THUMBNAIL)
        video_duration          = utils.get(panel_video, 'lengthText', *constants.RUN_TEXT, func = cleansers.iso_time)
        video_selected          = utils.get(panel_video, 'selected')
        video_params            = utils.get(panel_video, 'navigationEndpoint', 'watchEndpoint', 'params')
        video_type              = utils.get(panel_video, 'navigationEndpoint', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType', func = cleansers.type)
        video_id                = utils.get(panel_video, 'videoId')
        video_artist_name       = utils.get(panel_video, 'shortBylineText', *constants.RUN_TEXT)
        video_artist_id         = utils.get(panel_video_menu, 'goToArtist', 'endpoint', *constants.BROWSE_ENDPOINT_ID)
        video_album_id          = utils.get(panel_video_menu, 'goToAlbum', 'endpoint', *constants.BROWSE_ENDPOINT_ID)
        video_album_type        = utils.get(panel_video_menu, 'goToAlbum', 'endpoint', *constants.BROWSE_ENDPOINT_PAGE_TYPE, func = cleansers.type)
        video_radio_params      = utils.get(panel_video_menu, 'startRadio', 'endpoint', 'watchEndpoint', 'params')
        video_radio_playlist_id = utils.get(panel_video_menu, 'startRadio', 'endpoint', 'watchEndpoint', 'playlistId')

        video_data = \
        {
            'id':        video_id,
            'name':      video_title,
            'thumbnail': video_thumbnail,
            'duration':  video_duration,
            'type':      video_type,
            'artist': \
            {
                'id':   video_artist_id,
                'name': video_artist_name,
            },
            'album': \
            {
                'id': video_album_id,
            },
            'radio': \
            {
                'params':      video_radio_params,
                'playlist_id': video_radio_playlist_id,
            },
        }

        songs.append(video_data)

    return songs

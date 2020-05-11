'''
Module containing the parser: song
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def song(data: dict) -> dict:
    '''
    Parse data: Song.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.video_info('8gYfvzGqcbY')
        >>>
        >>> parsed_data = ytm.parsers.song(data)
        >>>
        >>> parsed_data['name']
        'Above The Clouds Of Pompeii'
        >>>
    '''

    assert data, 'No data to parse'

    player_response = utils.get \
    (
        data,
        'player_response',
    )
    video_details = utils.get \
    (
        player_response,
        'videoDetails',
    )
    secondary_info = utils.get \
    (
        data,
        'watch_next_response',
        'contents',
        'twoColumnWatchNextResults',
        'results',
        'results',
        'contents',
        1,
        'videoSecondaryInfoRenderer',
    )
    microformat = utils.get \
    (
        player_response,
        'microformat',
        'playerMicroformatRenderer',
    )
    video_owner_renderer = utils.get \
    (
        secondary_info,
        'owner',
        'videoOwnerRenderer',
    )
    video_owner_thumbnail = utils.get \
    (
        video_owner_renderer,
        'thumbnail',
        'thumbnails',
        -1,
    )
    raw_meta_rows = utils.get \
    (
        secondary_info,
        'metadataRowContainer',
        'metadataRowContainerRenderer',
        'rows',
        default = (),
    )

    assert player_response
    assert video_details
    assert secondary_info
    assert microformat
    assert video_owner_renderer
    assert video_owner_thumbnail
    assert raw_meta_rows

    meta_rows = []

    for meta_row in raw_meta_rows:
        meta_row = utils.first(meta_row)

        meta_row_title = utils.get \
        (
            meta_row,
            'title',
            'simpleText',
            func = lambda title: title.lower().replace(' ', '_'),
        )

        meta_rows.append(meta_row_title)

    video_title = utils.get \
    (
        video_details,
        'title',
    )
    video_id = utils.get \
    (
        video_details,
        'videoId',
    )
    video_views = utils.get \
    (
        video_details,
        'viewCount',
        func = int,
    )
    video_owner_id = utils.get \
    (
        video_owner_renderer,
        'navigationEndpoint',
        'browseEndpoint',
        'browseId',
    )
    video_owner_subscribers = utils.get \
    (
        video_owner_renderer,
        'subscriberCountText',
        'runs',
        0,
        'text',
        func = lambda data: data.strip().split(' ')[0],
    )
    video_owner_thumbnail_height = utils.get \
    (
        video_owner_thumbnail,
        'height',
    )
    video_owner_thumbnail_width = utils.get \
    (
        video_owner_thumbnail,
        'width',
    )
    video_owner_thumbnail_url = utils.get \
    (
        video_owner_thumbnail,
        'url',
        func = lambda data: 'https:' + data,
    )
    video_owner_name = utils.get \
    (
        video_owner_renderer,
        'title',
        'runs',
        0,
        'text',
    )
    video_description = utils.get \
    (
        secondary_info,
        'description',
        'runs',
        0,
        'text',
    )
    video_artist_name = utils.get \
    (
        video_details,
        'author',
    )
    video_artist_id = utils.get \
    (
        video_details,
        'channelId',
    )
    video_date_year = utils.get \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[0]),
    )
    video_date_month = utils.get \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[1]),
    )
    video_date_day = utils.get \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[2]),
    )
    video_rating = utils.get \
    (
        video_details,
        'averageRating',
    )
    video_duration = utils.get \
    (
        video_details,
        'lengthSeconds',
        func = int,
    )
    video_thumbnail = utils.get \
    (
        video_details,
        'thumbnail',
        'thumbnails',
        -1,
    )
    video_explicit = 'parental_warning' in meta_rows

    scraped = \
    {
        'id':          video_id,
        'name':        video_title,
        'views':       video_views,
        'rating':      video_rating,
        'duration':    video_duration,
        'explicit':    video_explicit,
        'description': video_description,
        'thumbnail':   video_thumbnail,
        'owner': \
        {
            'id':          video_owner_id,
            'name':        video_owner_name,
            'subscribers': video_owner_subscribers,
            'thumbnail': \
            {
                'height': video_owner_thumbnail_height,
                'width':  video_owner_thumbnail_width,
                'url':    video_owner_thumbnail_url,
            },
        },
        'artist': \
        {
            'name': video_artist_name,
            'id':   video_artist_id,
        },
        'date': \
        {
            'year':  video_date_year,
            'month': video_date_month,
            'day':   video_date_day,
        },
    }

    return scraped

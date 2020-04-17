from ... import utils

__all__ = __name__.split('.')[-1:]

def parse(data):
    player_response = utils.get_nested \
    (
        data,
        'player_response',
    )
    video_details = utils.get_nested \
    (
        player_response,
        'videoDetails',
    )
    secondary_info = utils.get_nested \
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
    microformat = utils.get_nested \
    (
        player_response,
        'microformat',
        'playerMicroformatRenderer',
    )
    video_owner_renderer = utils.get_nested \
    (
        secondary_info,
        'owner',
        'videoOwnerRenderer',
    )
    video_owner_thumbnail = utils.get_nested \
    (
        video_owner_renderer,
        'thumbnail',
        'thumbnails',
        -1,
    )
    raw_meta_rows = utils.get_nested \
    (
        secondary_info,
        'metadataRowContainer',
        'metadataRowContainerRenderer',
        'rows',
        default = (),
    )

    meta_rows = []

    for meta_row in raw_meta_rows:
        meta_row = utils.first_key(meta_row)

        meta_row_title = utils.get_nested \
        (
            meta_row,
            'title',
            'simpleText',
            func = lambda title: title.lower().replace(' ', '_'),
        )

        meta_rows.append(meta_row_title)

    video_title = utils.get_nested \
    (
        video_details,
        'title',
    )
    video_id = utils.get_nested \
    (
        video_details,
        'videoId',
    )
    video_views = utils.get_nested \
    (
        video_details,
        'viewCount',
        func = int,
    )
    video_owner_id = utils.get_nested \
    (
        video_owner_renderer,
        'navigationEndpoint',
        'browseEndpoint',
        'browseId',
    )
    video_owner_subscribers = utils.get_nested \
    (
        video_owner_renderer,
        'subscriberCountText',
        'runs',
        0,
        'text',
        func = lambda data: data.strip().split(' ')[0],
    )
    video_owner_thumbnail_height = utils.get_nested \
    (
        video_owner_thumbnail,
        'height',
    )
    video_owner_thumbnail_width = utils.get_nested \
    (
        video_owner_thumbnail,
        'width',
    )
    video_owner_thumbnail_url = utils.get_nested \
    (
        video_owner_thumbnail,
        'url',
        func = lambda data: 'https:' + data,
    )
    video_owner_name = utils.get_nested \
    (
        video_owner_renderer,
        'title',
        'runs',
        0,
        'text',
    )
    video_description = utils.get_nested \
    (
        secondary_info,
        'description',
        'runs',
        0,
        'text',
    )
    video_artist_name = utils.get_nested \
    (
        video_details,
        'author',
    )
    video_artist_id = utils.get_nested \
    (
        video_details,
        'channelId',
    )
    video_date_year = utils.get_nested \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[0]),
    )
    video_date_month = utils.get_nested \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[1]),
    )
    video_date_day = utils.get_nested \
    (
        microformat,
        'publishDate',
        func = lambda date: int(date.strip().split('-')[2]),
    )
    video_rating = utils.get_nested \
    (
        video_details,
        'averageRating',
    )
    video_duration = utils.get_nested \
    (
        video_details,
        'lengthSeconds',
        func = int,
    )
    video_thumbnail = utils.get_nested \
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

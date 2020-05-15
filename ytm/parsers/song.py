'''
Module containing the parser: song
'''

from .. import utils
from . import decorators
from . import cleansers

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

    player_response     = utils.get(data, 'player_response')
    watch_next_response = utils.get(data, 'watch_next_response')

    assert player_response,     'No player response'
    assert watch_next_response, 'No watch next response'

    # Player Response
    streaming_data = utils.get(player_response, 'streamingData')
    video_details  = utils.get(player_response, 'videoDetails')
    microformat    = utils.get(player_response, 'microformat', 'playerMicroformatRenderer')

    watch_next_contents = utils.get \
    (
        watch_next_response,
        'contents',
        'twoColumnWatchNextResults',
    )
    watch_next_player_overlay_results = utils.get \
    (
        watch_next_response,
        'playerOverlays',
        'playerOverlayRenderer',
        'endScreen',
        'watchNextEndScreenRenderer',
        'results',
    )

    watch_next_results = utils.get \
    (
        watch_next_contents,
        'results',
        'results',
        'contents',
    )
    watch_next_secondary_results = utils.get \
    (
        watch_next_contents,
        'secondaryResults',
        'secondaryResults',
        'results',
    )

    watch_next_autoplay_videos = utils.get \
    (
        watch_next_secondary_results,
        0,
        'compactAutoplayRenderer',
        'contents',
        default = [],
    )

    watch_next_videos = watch_next_autoplay_videos + watch_next_secondary_results[1:]

    video_metadata_renderer = utils.get \
    (
        watch_next_results,
        0,
        'itemSectionRenderer',
        'contents',
        0,
        'videoMetadataRenderer',
    )
    video_description_renderer = utils.get \
    (
        watch_next_results,
        1,
        'itemSectionRenderer',
        'contents',
        0,
        'videoDescriptionRenderer',
    )

    video_description_runs  = utils.get(video_description_renderer, 'description', 'runs')
    video_like_button       = utils.get(video_metadata_renderer, 'likeButton', 'likeButtonRenderer')
    video_owner_renderer    = utils.get(video_metadata_renderer, 'owner', 'videoOwnerRenderer')
    video_subscribe_button  = utils.get(video_owner_renderer, 'subscribeButton', 'subscribeButtonRenderer')
    video_owner_thumbnail   = utils.get(video_owner_renderer, 'thumbnail', 'thumbnails', -1)
    raw_video_metadata_rows = utils.get(video_description_renderer, 'metadataRowContainer', 'metadataRowContainerRenderer', 'rows', default=())

    video_metadata_rows = []

    for video_metadata_row in raw_video_metadata_rows:
        video_metadata_row = utils.first(video_metadata_row)

        video_metadata_row_name = utils.get(video_metadata_row, 'title', 'simpleText')

        if video_metadata_row_name:
            video_metadata_row_key = video_metadata_row_name.strip().lower().replace(' ', '_')

            video_metadata_rows.append(video_metadata_row_key)

    video_publish_date = utils.get(microformat, 'publishDate', func = lambda date: tuple(map(int, date.strip().split('-'))), default=())
    video_upload_date  = utils.get(microformat, 'uploadDate',  func = lambda date: tuple(map(int, date.strip().split('-'))), default=())

    video_description_run_texts = []

    for video_description_run in video_description_runs:
        video_description_run_text = utils.get(video_description_run, 'text')

        if video_description_run_text:
            video_description_run_texts.append(video_description_run_text)

    # Video Details
    song_author_name       = utils.get(video_details, 'author')
    song_author_id         = utils.get(video_details, 'channelId')
    song_rating            = utils.get(video_details, 'averageRating')
    song_keywords          = utils.get(video_details, 'keywords')
    song_duration          = utils.get(video_details, 'lengthSeconds', func = int)
    song_description_short = utils.get(video_details, 'shortDescription')
    song_thumbnail         = utils.get(video_details, 'thumbnail', 'thumbnails', -1)
    song_name              = utils.get(video_details, 'title')
    song_id                = utils.get(video_details, 'videoId')
    song_views             = utils.get(video_details, 'viewCount', func = int)

    # Microformat
    song_family_safe        = utils.get(microformat, 'isFamilySafe')
    song_publish_date_year  = utils.get(video_publish_date, 0)
    song_publish_date_month = utils.get(video_publish_date, 1)
    song_publish_date_day   = utils.get(video_publish_date, 2)
    song_upload_date_year   = utils.get(video_upload_date, 0)
    song_upload_date_month  = utils.get(video_upload_date, 1)
    song_upload_date_day    = utils.get(video_upload_date, 2)

    # Video Metadata
    song_date                   = utils.get(video_metadata_renderer, 'dateText', 'simpleText')
    song_description_long       = utils.get(video_metadata_renderer, 'description', 'runs', 0, 'text')
    song_dislikes               = utils.get(video_like_button, 'dislikeCount')
    song_likes                  = utils.get(video_like_button, 'likeCount')
    song_owner_id               = utils.get(video_subscribe_button, 'channelId')
    song_owner_subscribers      = utils.get(video_subscribe_button, 'subscriberCountText', 'simpleText')
    song_owner_thumbnail_height = utils.get(video_owner_thumbnail, 'height')
    song_owner_thumbnail_width  = utils.get(video_owner_thumbnail, 'width')
    song_owner_thumbnail_url    = utils.get(video_owner_thumbnail, 'url', func = 'https:'.__add__)
    song_owner_name             = utils.get(video_owner_renderer, 'title', 'runs', 0, 'text')

    # Video Description
    song_explicit    = 'parental_warning' in video_metadata_rows
    song_description = ''.join(video_description_run_texts)

    # Watch Next
    song_recommended_videos = []

    for watch_next_video in watch_next_videos:
        watch_next_video = utils.first(watch_next_video)

        watch_next_video_long_byline_text = utils.get(watch_next_video, 'longBylineText', 'runs', 0)

        watch_next_video_artist_thumbnail = utils.get(watch_next_video, 'channelThumbnail', 'thumbnails', 0)
        watch_next_video_duration = utils.get(watch_next_video, 'lengthText', 'simpleText', func = cleansers.iso_time)
        watch_next_video_artist_id = utils.get(watch_next_video_long_byline_text, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        watch_next_video_artist_name = utils.get(watch_next_video_long_byline_text, 'text')
        watch_next_video_published_time = utils.get(watch_next_video, 'publishedTimeText', 'simpleText')
        watch_next_video_views_count = utils.get(watch_next_video, 'viewCountText', 'simpleText', func = lambda views: int(views.strip().split(' ')[0].replace(',', '')))
        watch_next_video_thumbnail = utils.get(watch_next_video, 'thumbnail', 'thumbnails', -1)
        watch_next_video_title = utils.get(watch_next_video, 'title', 'simpleText')
        watch_next_video_id = utils.get(watch_next_video, 'videoId')

        watch_next_video_data = \
        {
            'artist': \
            {
                'thumbnail': watch_next_video_artist_thumbnail,
                'id':        watch_next_video_artist_id,
                'name':      watch_next_video_artist_name,
            },
            'duration':  watch_next_video_duration,
            'published': watch_next_video_published_time,
            'views':     watch_next_video_views_count,
            'thumbnail': watch_next_video_thumbnail,
            'name':      watch_next_video_title,
            'id':        watch_next_video_id,
        }

        song_recommended_videos.append(watch_next_video_data)

    parsed = \
    {
        'rating':      song_rating,
        'duration':    song_duration,
        'description': song_description,
        'thumbnail':   song_thumbnail,
        'name':        song_name,
        'id':          song_id,
        'views':       song_views,
        'dislikes':    song_dislikes,
        'likes':       song_likes,
        'explicit':    song_explicit,
        'recommended': song_recommended_videos,
        'date': \
        {
            'year':  song_publish_date_year,
            'month': song_publish_date_month,
            'day':   song_publish_date_day,
        },
        'artist': \
        {
            'id':          song_owner_id,
            'name':        song_owner_name,
            'subscribers': song_owner_subscribers,
            'thumbnail': \
            {
                'height': song_owner_thumbnail_height,
                'width':  song_owner_thumbnail_width,
                'url':    song_owner_thumbnail_url,
            },
        },
    }

    return parsed

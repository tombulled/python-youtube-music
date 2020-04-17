from ..... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def parse(data):
    video_meta_rows = \
    [
        ytm_utils.get_nested(row, 'metadataRowRenderer', 'title', 'simpleText', func=lambda title: title.lower().replace(' ', '_'))
        for row in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'metadataRowContainer', 'metadataRowContainerRenderer', 'rows', default = ())
    ]

    video_title = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'title')
    video_views = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount', func=int)
    video_owner_id = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
    video_owner_subscribers = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'subscriberCountText', 'runs', 0, 'text', func=lambda data: data.strip().split(' ')[0])
    video_owner_thumbnail_height = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'height')
    video_owner_thumbnail_width = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'width')
    video_owner_thumbnail_url = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'url', func=lambda data: 'https:' + data)
    video_owner_name = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text')
    video_artist_name = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'author')
    video_artist_id = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'channelId')
    video_date_year = ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[0]))
    video_date_month = ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[1]))
    video_date_day = ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[2]))
    video_explicit = 'parental_warning' in video_meta_rows
    video_rating = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating')
    video_duration = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds', func = int)
    video_thumbnail = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', -1)
    video_id = ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'videoId')
    video_description = ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text')

    scraped = \
    {
        'id': video_id,
        'name': video_title,
        'views': video_views,
        'rating': video_rating,
        'duration': video_duration,
        'thumbnail': video_thumbnail,
        'description': video_description,
        'owner': \
        {
            'id': video_owner_id,
            'name': video_owner_name,
            'subscribers': video_owner_subscribers,
            'thumbnail': \
            {
                'height': video_owner_thumbnail_height,
                'width': video_owner_thumbnail_width,
                'url': video_owner_thumbnail_url,
            },
        },
        'explicit': video_explicit,
        'artist': \
        {
            'name': video_artist_name,
            'id': video_artist_id,
        },
        'date': \
        {
            'year': video_date_year,
            'month': video_date_month,
            'day': video_date_day,
        },
    }

    return scraped

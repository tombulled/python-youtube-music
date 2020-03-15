from ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def song_info(self, song_id):
    data = self.base.video_info \
    (
        video_id = song_id,
    )

    scraped = \
    {
        'title': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'title'),
        'view_count': \
        {
            'short': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'viewCount', 'simpleText'),
            'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'shortViewCount', 'simpleText'),
            'actual': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount', func=int),
        },
        'owner': \
        {
            'id': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
            'subscriber_count': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'subscriberCountText', 'runs', 0, 'text'),
            'thumbnails': \
            [
                {
                    'height': ytm_utils.get_nested(thumbnail, 'height'),
                    'width': ytm_utils.get_nested(thumbnail, 'width'),
                    'url': 'https:' + ytm_utils.get_nested(thumbnail, 'url'),
                }
                for thumbnail in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', default = [])
            ],
            'name': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text'),
        },
        'description': \
        {
            'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text'),
            'short': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'shortDescription'),
        },
        'explicit': 'Parental warning' in \
        [
            ytm_utils.get_nested(row, 'metadataRowRenderer', 'title', 'simpleText')
            for row in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'metadataRowContainer', 'metadataRowContainerRenderer', 'rows', default = [])
        ],
        'channel': \
        {
            'name': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'author'),
            'id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'channelId'),
        },
        'average_rating': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating'),
        'length_seconds': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds', func = int),
        'thumbnails': \
        [
            {
                'height': ytm_utils.get_nested(thumbnail, 'height'),
                'width': ytm_utils.get_nested(thumbnail, 'width'),
                'url': ytm_utils.get_nested(thumbnail, 'url'),
            }
            for thumbnail in ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', default = [])
        ],
        'video_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'videoId'),
        'date': \
        {
            'short': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate'),
            'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'dateText', 'simpleText'),
        },
    }

    return scraped

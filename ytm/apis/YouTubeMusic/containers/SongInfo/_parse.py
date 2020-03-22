from ..... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def _parse(self):
    scraped = \
    {
        'title': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'title'),
        # 'view_count': \
        # {
        #     'short': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'viewCount', 'simpleText'),
        #     'long': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'shortViewCount', 'simpleText'),
        #     'actual': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'viewCount', func=int),
        # },
        'views': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'viewCount', func=int),
        'owner': \
        {
            'id': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
            'subscribers': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'subscriberCountText', 'runs', 0, 'text', func=lambda data: data.strip().split(' ')[0]),
            # 'thumbnails': \
            # [
            #     {
            #         'height': ytm_utils.get_nested(thumbnail, 'height'),
            #         'width': ytm_utils.get_nested(thumbnail, 'width'),
            #         'url': 'https:' + ytm_utils.get_nested(thumbnail, 'url'),
            #     }
            #     for thumbnail in ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', default = [])
            # ],
            'thumbnail': \
            {
                'height': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'height'),
                'width': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'width'),
                'url': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', -1, 'url', func=lambda data: 'https:' + data),
            },
            'name': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text'),
        },
        # 'description': \
        # {
        #     'long': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text'),
        #     'short': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'shortDescription'),
        # },
        'description': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text'),
        'explicit': 'Parental warning' in \
        [
            ytm_utils.get_nested(row, 'metaself.raw_dataRowRenderer', 'title', 'simpleText')
            for row in ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'metaself.raw_dataRowContainer', 'metaself.raw_dataRowContainerRenderer', 'rows', default = [])
        ],
        'channel': \
        {
            'name': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'author'),
            'id': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'channelId'),
        },
        'average_rating': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'averageRating'),
        'duration': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'lengthSeconds', func = int),
        # 'thumbnails': \
        # [
        #     {
        #         'height': ytm_utils.get_nested(thumbnail, 'height'),
        #         'width': ytm_utils.get_nested(thumbnail, 'width'),
        #         'url': ytm_utils.get_nested(thumbnail, 'url'),
        #     }
        #     for thumbnail in ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', default = [])
        # ],
        'thumbnail': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', -1),
        'video_id': ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'videoId'),
        'date': \
        {
            # 'short': ytm_utils.get_nested(self.raw_data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate'),
            # 'long': ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'dateText', 'simpleText'),
            'year': ytm_utils.get_nested(self.raw_data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[0])),
            'month': ytm_utils.get_nested(self.raw_data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[1])),
            'day': ytm_utils.get_nested(self.raw_data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate', func = lambda date: int(date.strip().split('-')[2])),
        },
    }

    # scraped = {}
    #
    # title = ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'title')
    # view_count_short = ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'viewCount', 'simpleText')
    # view_count_long = ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'shortViewCount', 'simpleText')
    # view_count_actual = ytm_utils.get_nested(self.raw_data, 'player_response', 'videoDetails', 'viewCount', func=int)
    # owner_id = ytm_utils.get_nested(self.raw_data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')


    return scraped

from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    scraped = \
    {
        'playlist': None,
        'tracks': [],
    }

    if 'continuationContents' in data:
        self._continuation = ytm_utils.get_nested(data, 'continuationContents', 'musicPlaylistShelfContinuation', 'continuations', 0, 'nextContinuationData', 'continuation')

        data = ytm_utils.get_nested(data, 'continuationContents', 'musicPlaylistShelfContinuation')

    else:
        scraped['playlist'] = \
        {
            'title': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'title', 'runs', 0, 'text'),
            'type': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'subtitle', 'runs', 0, 'text'),
            'subtitle': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'subtitle', 'runs', 2, 'text'),
            'year': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'subtitle', 'runs', 4, 'text', func=int),
            'thubnail': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'thumbnail', 'croppedSquareThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
            'duration': ytm_utils.get_nested(data, 'header', 'musicDetailHeaderRenderer', 'secondSubtitle', 'runs', 2, 'text'),
            'id': ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer', 'playlistId'),
            'track_count': ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer', 'collapsedItemCount'),
            # 'continuation': ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer', 'continuations', 0, 'nextContinuationData', 'continuation'),
        }

        self._continuation = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer', 'continuations', 0, 'nextContinuationData', 'continuation')

        data = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer')

    tracks = ytm_utils.get_nested(data, 'contents', default=[])

    for track in tracks:
        track_data = \
        {
            'id': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId'),
            'title': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
            'music_video_type': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType'),
            'duration': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'fixedColumns', 0, 'musicResponsiveListItemFixedColumnRenderer', 'text', 'simpleText'),
            'thumbnail': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
            'artist': \
            {
                'name': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text'),
                'id': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId'),
            },
            'explicit': ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer', 'badges', 0, 'musicInlineBadgeRenderer', 'accessibilityData', 'accessibilityData', 'label', func=str.lower) == 'explicit',
        }

        track_obj = containers.PlaylistTrack(self.api, track_data)

        # scraped['tracks'].append(track_data)
        scraped['tracks'].append(track_obj)

    return scraped

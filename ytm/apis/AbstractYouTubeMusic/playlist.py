from ... import utils as ytm_utils
from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def playlist(self, playlist_id=None, continuation=None, make_radio=False):
    scraped = {}

    if continuation:
        data = self.base.browse \
        (
            continuation = continuation,
        )

        data = ytm_utils.get_nested(data, 'continuationContents', 'musicPlaylistShelfContinuation')
    elif playlist_id:
        # Do appropriate playlist checks
        if make_radio:
            prefix = ytm_constants.PREFIX_RADIO
        else:
            prefix = ytm_constants.PREFIX_PLAYLIST

        data = self.base.browse_playlist \
        (
            browse_id = f'{prefix}{playlist_id}', # Check this
        )

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
            'continuation': ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer', 'continuations', 0, 'nextContinuationData', 'continuation'),
        }

        data = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicPlaylistShelfRenderer')
    else:
        return None # raise?

    scraped['tracks'] = \
    [
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
        for index, track in enumerate(ytm_utils.get_nested(data, 'contents', default=[]))
    ]

    # from pprint import pprint as pp
    # pp(ytm_utils.get_nested(data, 'contents')[11])

    return scraped

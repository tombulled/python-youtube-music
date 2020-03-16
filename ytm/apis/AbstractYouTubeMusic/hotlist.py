from ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def hotlist(self):
    data = self.base.browse_hotlist()

    scraped = \
    [
        {
            'title': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'title', 'runs', 0, 'text'),
            'views': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'subtitle', 'runs', -1, 'text'),
            'artists': \
            [
                ytm_utils.get_nested(run, 'text')
                for run in ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'subtitle', 'runs', default=[])[:-1:2]
            ],
            'artist_id': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'menu', 'menuRenderer', 'items', 5, 'menuNavigationItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
            'thumbnail': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'backgroundImage', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1),
            'id': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'onTap', 'watchEndpoint', 'videoId'),
            'music_video_type': ytm_utils.get_nested(track, 'musicFullBleedItemRenderer', 'onTap', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType'),
        }
        for track in ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'gridRenderer', 'items', default=[])
    ]

    return scraped

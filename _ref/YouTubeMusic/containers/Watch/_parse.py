from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    playlist_tracks = []

    tracks = ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'contents', default=[])

    for track in tracks:
        track_data = \
        {
            # 'index': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'navigationEndpoint', 'watchEndpoint', 'index'),
            'title': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'title', 'runs', 0, 'text'),
            'thumbnail': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'thumbnail', 'thumbnails', -1),
            'duration': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'lengthText', 'runs', 0, 'text'),
            'selected': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'selected'),
            'playlist_id': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
            'params': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
            'music_video_type': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'navigationEndpoint', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType'),
            'song_id': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'videoId'),
            'radio': \
            {
                'playlist_id': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'menu', 'menuRenderer', 'items', 6, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId'),
                'params': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'menu', 'menuRenderer', 'items', 6, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params'),
            },
            'artist': \
            {
                'id': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'menu', 'menuRenderer', 'items', 7, 'menuNavigationItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                'title': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'shortBylineText', 'runs', 0, 'text'),
            },
            'album_id': ytm_utils.get_nested(track, 'playlistPanelVideoRenderer', 'menu', 'menuRenderer', 'items', 8, 'menuNavigationItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
        }

        track_obj = containers.WatchPlaylistTrack(self.api, track_data)

        playlist_tracks.append(track_obj)

        # playlist_tracks.append(track_data)

    playlist_data = \
    {
        # 'title': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'title'),
        # 'artist': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'shortBylineText', 'runs', 0, 'text'),
        # 'current_index': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'currentIndex'),
        'playlist_id': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'playlistId'),
        'continuation': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'continuations', 0, 'nextRadioContinuationData', 'continuation'),
        'total_videos': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'playlist', 'playlistPanelRenderer', 'totalVideosText', 'runs', 0, 'text', func=lambda total: int(total.strip().split(' ')[0])),
        'tracks': playlist_tracks,
    }

    playlist_obj = containers.WatchPlaylist(self.api, playlist_data)

    current_data = \
    {
        # 'playlist_id': ytm_utils.get_nested(data, 'currentVideoEndpoint', 'watchEndpoint', 'playlistId'),
        'index': ytm_utils.get_nested(data, 'currentVideoEndpoint', 'watchEndpoint', 'index'),
        'artist': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'byline', 'runs', 0, 'text'),
        'year': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'byline', 'runs', 4, 'text', func=int),
        'album': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'albumName', 'runs', 0, 'text'),
        'song': \
        {
            'id': ytm_utils.get_nested(data, 'currentVideoEndpoint', 'watchEndpoint', 'videoId'),
            'title': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'title', 'runs', 0, 'text'),
            # 'title': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'secondaryTitle', 'runs', 0, 'text'),
        },
        'total': \
        {
            'views': ytm_utils.get_nested(data, 'contents', 'singleColumnMusicWatchNextResultsRenderer', 'metadataScreen', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', 0, 'musicWatchMetadataRenderer', 'viewCountText', 'runs', 0, 'text', func=lambda views: int(views.strip().split(' ')[0].replace(',', ''))),
            'likes': ytm_utils.get_nested(data, 'playerOverlays', 'playerOverlayRenderer', 'actions', 0, 'likeButtonRenderer', 'likeCount'),
            'dislikes': ytm_utils.get_nested(data, 'playerOverlays', 'playerOverlayRenderer', 'actions', 0, 'likeButtonRenderer', 'dislikeCount'),
        },
    }

    current_obj = containers.WatchCurrentSong(self.api, current_data)

    scraped = \
    {
        'playlist': playlist_obj,
        'current': current_obj,
    }

    return scraped

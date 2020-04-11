from .... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def browse_playlist(data):
    scraped = \
    {
        'playlist': None,
        'tracks': [],
        'continuation': None,
    }

    if 'continuationContents' in data:
        data = ytm_utils.get_nested \
        (
            data,
            'continuationContents',
            'musicPlaylistShelfContinuation',
        )

        continuation = ytm_utils.get_nested \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )
    else:
        music_detail_header_renderer = ytm_utils.get_nested \
        (
            data,
            'header',
            'musicDetailHeaderRenderer',
        )
        music_playlist_shelf_renderer = ytm_utils.get_nested \
        (
            data,
            'contents',
            'singleColumnBrowseResultsRenderer',
            'tabs',
            0,
            'tabRenderer',
            'content',
            'sectionListRenderer',
            'contents',
            0,
            'musicPlaylistShelfRenderer',
        )

        playlist_title = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'title',
            'runs',
            0,
            'text',
        )
        playlist_type = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            0,
            'text',
        )
        playlist_subtitle = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            2,
            'text',
        )
        playlist_year = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            4,
            'text',
            func = int,
        )
        playlist_thumbnail = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'thumbnail',
            'croppedSquareThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        playlist_duration = ytm_utils.get_nested \
        (
            music_detail_header_renderer,
            'secondSubtitle',
            'runs',
            2,
            'text',
        )
        playlist_id = ytm_utils.get_nested \
        (
            music_playlist_shelf_renderer,
            'playlistId',
        )
        playlist_track_count = ytm_utils.get_nested \
        (
            music_playlist_shelf_renderer,
            'collapsedItemCount',
        )

        scraped['playlist'] = \
        {
            'title':       playlist_title,
            'type':        playlist_type,
            'subtitle':    playlist_subtitle,
            'year':        playlist_year,
            'thubnail':    playlist_thumbnail,
            'duration':    playlist_duration,
            'id':          playlist_id,
            'track_count': playlist_track_count,
        }

        data = ytm_utils.get_nested \
        (
            data,
            'contents',
            'singleColumnBrowseResultsRenderer',
            'tabs',
            0,
            'tabRenderer',
            'content',
            'sectionListRenderer',
            'contents',
            0,
            'musicPlaylistShelfRenderer',
        )

        continuation = ytm_utils.get_nested \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )

    scraped['continuation'] = continuation

    tracks = ytm_utils.get_nested(data, 'contents', default=())

    for track in tracks:
        track = ytm_utils.get_nested(track, 'musicResponsiveListItemRenderer')

        track_watch_endpoint = ytm_utils.get_nested \
        (
            track,
            'overlay',
            'musicItemThumbnailOverlayRenderer',
            'content',
            'musicPlayButtonRenderer',
            'playNavigationEndpoint',
            'watchEndpoint',
        )

        track_music_video_type = ytm_utils.get_nested \
        (
            track_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        track_id = ytm_utils.get_nested \
        (
            track_watch_endpoint,
            'videoId',
        )
        track_title = ytm_utils.get_nested \
        (
            track,
            'flexColumns',
            0,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )
        track_duration = ytm_utils.get_nested \
        (
            track,
            'fixedColumns',
            0,
            'musicResponsiveListItemFixedColumnRenderer',
            'text',
            'simpleText',
        )
        track_thumbnail = ytm_utils.get_nested \
        (
            track,
            'thumbnail',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_explicit = ytm_utils.get_nested \
        (
            track,
            'badges',
            0,
            'musicInlineBadgeRenderer',
            'accessibilityData',
            'accessibilityData',
            'label',
            func = str.lower
        ) == 'explicit'
        track_artist_id = ytm_utils.get_nested \
        (
            track,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        track_artist_name = ytm_utils.get_nested \
        (
            track,
            'flexColumns',
            1,
            'musicResponsiveListItemFlexColumnRenderer',
            'text',
            'runs',
            0,
            'text',
        )

        track_data = \
        {
            'id':        track_id,
            'title':     track_title,
            'duration':  track_duration,
            'thumbnail': track_thumbnail,
            'explicit':  track_explicit,
            'artist': \
            {
                'id':   track_artist_id,
                'name': track_artist_name,
            },
        }

        scraped['tracks'].append(track_data)

    return scraped

from ... import utils

__parser__ = __name__.split('.')[-1]
__all__ = (__parser__,)

def parse(data):
    if 'continuationContents' in data:
        playlist_data = None

        data = utils.get_nested \
        (
            data,
            'continuationContents',
            'musicPlaylistShelfContinuation',
        )

        continuation = utils.get_nested \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )
    else:
        music_detail_header_renderer = utils.get_nested \
        (
            data,
            'header',
            'musicDetailHeaderRenderer',
        )
        music_playlist_shelf_renderer = utils.get_nested \
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

        playlist_title = utils.get_nested \
        (
            music_detail_header_renderer,
            'title',
            'runs',
            0,
            'text',
        )
        playlist_type = utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            0,
            'text',
        )
        playlist_subtitle = utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            2,
            'text',
        )
        playlist_year = utils.get_nested \
        (
            music_detail_header_renderer,
            'subtitle',
            'runs',
            4,
            'text',
            func = int,
        )
        playlist_thumbnail = utils.get_nested \
        (
            music_detail_header_renderer,
            'thumbnail',
            'croppedSquareThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        playlist_duration = utils.get_nested \
        (
            music_detail_header_renderer,
            'secondSubtitle',
            'runs',
            2,
            'text',
        )
        playlist_id = utils.get_nested \
        (
            music_playlist_shelf_renderer,
            'playlistId',
        )
        playlist_track_count = utils.get_nested \
        (
            music_playlist_shelf_renderer,
            'collapsedItemCount',
        )

        playlist_data = \
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

        data = utils.get_nested \
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

        continuation = utils.get_nested \
        (
            data,
            'continuations',
            0,
            'nextContinuationData',
            'continuation',
        )

    raw_tracks = utils.get_nested \
    (
        data,
        'contents',
        default = (),
    )

    tracks = []

    for track in raw_tracks:
        track = utils.first_key(track)

        track_watch_endpoint = utils.get_nested \
        (
            track,
            'overlay',
            'musicItemThumbnailOverlayRenderer',
            'content',
            'musicPlayButtonRenderer',
            'playNavigationEndpoint',
            'watchEndpoint',
        )

        track_music_video_type = utils.get_nested \
        (
            track_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        track_id = utils.get_nested \
        (
            track_watch_endpoint,
            'videoId',
        )
        track_title = utils.get_nested \
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
        track_artist_id = utils.get_nested \
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
        track_artist_name = utils.get_nested \
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
        track_duration = utils.get_nested \
        (
            track,
            'fixedColumns',
            0,
            'musicResponsiveListItemFixedColumnRenderer',
            'text',
            'simpleText',
        )
        track_thumbnail = utils.get_nested \
        (
            track,
            'thumbnail',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_explicit = utils.get_nested \
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

        tracks.append(track_data)

    scraped = \
    {
        'playlist':     playlist_data,
        'tracks':       tracks,
        'continuation': continuation,
    }

    return scraped

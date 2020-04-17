# from ..... import utils as utils
from ... import utils

__all__ = __name__.split('.')[-1:]

def parse(data):
    if 'continuationContents' in data:
        playlist_renderer = utils.get_nested \
        (
            data,
            'continuationContents',
            'playlistPanelContinuation',
        )
    else:
        playlist_renderer = utils.get_nested \
        (
            data,
            'contents',
            'singleColumnMusicWatchNextResultsRenderer',
            'playlist',
            'playlistPanelRenderer',
        )

    tracks = utils.get_nested \
    (
        playlist_renderer,
        'contents',
        default = (),
    )

    playlist_tracks = []

    for track in tracks:
        track = utils.first_key(track)

        track_watch_endpoint = utils.get_nested \
        (
            track,
            'navigationEndpoint',
            'watchEndpoint',
        )
        track_radio_watch_endpoint = utils.get_nested \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            6,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'watchEndpoint',
        )
        track_artist_browse_endpoint = utils.get_nested \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            7,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'browseEndpoint',
        )
        track_album_browse_endpoint = utils.get_nested \
        (
            track,
            'menu',
            'menuRenderer',
            'items',
            8,
            'menuNavigationItemRenderer',
            'navigationEndpoint',
            'browseEndpoint',
        )

        track_selected = utils.get_nested \
        (
            track,
            'selected',
        )
        track_music_video_type = utils.get_nested \
        (
            track_watch_endpoint,
            'watchEndpointMusicSupportedConfigs',
            'watchEndpointMusicConfig',
            'musicVideoType',
        )
        track_index = utils.get_nested \
        (
            track_watch_endpoint,
            'index',
        )
        track_playlist_id = utils.get_nested \
        (
            track_watch_endpoint,
            'playlistId',
        )
        track_params = utils.get_nested \
        (
            track_watch_endpoint,
            'params',
        )
        track_id = utils.get_nested \
        (
            track,
            'videoId',
        )
        track_name = utils.get_nested \
        (
            track,
            'title',
            'runs',
            0,
            'text',
        )
        track_duration = utils.get_nested \
        (
            track,
            'lengthText',
            'runs',
            0,
            'text',
        )
        track_artist_name = utils.get_nested \
        (
            track,
            'shortBylineText',
            'runs',
            0,
            'text',
        )
        track_thumbnail = utils.get_nested \
        (
            track,
            'thumbnail',
            'thumbnails',
            -1,
        )
        track_radio_playlist_id = utils.get_nested \
        (
            track_radio_watch_endpoint,
            'playlistId',
        )
        track_radio_params = utils.get_nested \
        (
            track_radio_watch_endpoint,
            'params',
        )
        track_artist_id = utils.get_nested \
        (
            track_artist_browse_endpoint,
            'browseId',
        )
        track_album_id = utils.get_nested \
        (
            track_album_browse_endpoint,
            'browseId',
        )

        track_data = \
        {
            'name':      track_name,
            'duration':  track_duration,
            'params':    track_params, # Same for all
            'id':        track_id,
            'album_id':  track_album_id,
            'thumbnail': track_thumbnail,
            'radio': \
            {
                'playlist_id': track_radio_playlist_id,
                'params':      track_radio_params, # Same for all
            },
            'artist': \
            {
                'id':   track_artist_id,
                'name': track_artist_name,
            },
        }

        playlist_tracks.append(track_data)

    playlist_name  = utils.get_nested \
    (
        playlist_renderer,
        'title',
    )
    playlist_radio = utils.get_nested \
    (
        playlist_renderer,
        'isInfinite',
    )
    playlist_id = utils.get_nested \
    (
        playlist_renderer,
        'playlistId',
    )
    playlist_continuation = utils.get_nested \
    (
        playlist_renderer,
        'continuations',
        0,
        'nextRadioContinuationData',
        'continuation',
    )
    playlist_total = utils.get_nested \
    (
        playlist_renderer,
        'totalVideosText',
        'runs',
        0,
        'text',
        func = lambda total: int(total.strip().split(' ')[0]),
    )

    playlist_data = \
    {
        'id':           playlist_id,
        'continuation': playlist_continuation,
        'total':        playlist_total,
        'tracks':       playlist_tracks,
        'radio':        playlist_radio,
    }

    current_watch_endpoint = utils.get_nested \
    (
        data,
        'currentVideoEndpoint',
        'watchEndpoint',
    )
    current_metadata_renderer = utils.get_nested \
    (
        data,
        'contents',
        'singleColumnMusicWatchNextResultsRenderer',
        'metadataScreen',
        'sectionListRenderer',
        'contents',
        0,
        'itemSectionRenderer',
        'contents',
        0,
        'musicWatchMetadataRenderer',
    )
    current_like_button_renderer = utils.get_nested \
    (
        data,
        'playerOverlays',
        'playerOverlayRenderer',
        'actions',
        0,
        'likeButtonRenderer',
    )

    current_index = utils.get_nested \
    (
        current_watch_endpoint,
        'index',
    )
    current_song_id = utils.get_nested \
    (
        current_watch_endpoint,
        'videoId',
    )
    current_artist_name = utils.get_nested \
    (
        current_metadata_renderer,
        'byline',
        'runs',
        0,
        'text',
    )
    current_year = utils.get_nested \
    (
        current_metadata_renderer,
        'byline',
        'runs',
        4,
        'text',
        func = int,
    )
    current_album_name = utils.get_nested \
    (
        current_metadata_renderer,
        'albumName',
        'runs',
        0,
        'text',
    )
    current_song_name = utils.get_nested \
    (
        current_metadata_renderer,
        'title',
        'runs',
        0,
        'text',
    )
    current_views = utils.get_nested \
    (
        current_metadata_renderer,
        'viewCountText',
        'runs',
        0,
        'text',
        func = lambda views: int(views.strip().split(' ')[0].replace(',', '')),
    )
    current_likes = utils.get_nested \
    (
        current_like_button_renderer,
        'likeCount',
    )
    current_dislikes = utils.get_nested \
    (
        current_like_button_renderer,
        'dislikeCount',
    )

    # Make this None if its a continuation
    current_data = \
    {
        'index':       current_index,
        'artist_name': current_artist_name,
        'album_name':  current_album_name,
        'year':        current_year,
        'song': \
        {
            'id':   current_song_id,
            'name': current_song_name,
        },
        'views':    current_views,
        'likes':    current_likes,
        'dislikes': current_dislikes,
    }

    scraped = \
    {
        'playlist': playlist_data,
        'current':  current_data,
    }

    return scraped

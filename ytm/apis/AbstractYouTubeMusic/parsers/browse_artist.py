from .... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def browse_artist(data):
    contents = ytm_utils.get_nested \
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
        default = (),
    )

    shelves = {}

    for content in contents:
        content_key = list(content)[0]
        content = content[content_key]

        if content_key in shelves:
            shelves[content_key].append(content)
        else:
            shelves[content_key] = [content]

    artist_playlist_id = ytm_utils.get_nested(shelves, 'musicShelfRenderer', 0, 'bottomEndpoint', 'browseEndpoint', 'browseId')
    artist_name = ytm_utils.get_nested(data, 'header', 'musicImmersiveHeaderRenderer', 'title', 'runs', 0, 'text')
    artist_id = ytm_utils.get_nested(data, 'header', 'musicImmersiveHeaderRenderer', 'subscriptionButton', 'subscribeButtonRenderer', 'channelId')
    artist_subscribers = ytm_utils.get_nested(data, 'header', 'musicImmersiveHeaderRenderer', 'subscriptionButton', 'subscribeButtonRenderer', 'subscriberCountText', 'runs', 0, 'text')
    artist_playlist_params = ytm_utils.get_nested(shelves, 'musicShelfRenderer', 0, 'bottomEndpoint', 'browseEndpoint', 'params')
    artist_views = ytm_utils.get_nested(shelves, 'musicDescriptionShelfRenderer', 0, 'subheader', 'runs', 0, 'text', func=lambda views:int(views.strip().split(' ')[0].replace(',', '')))
    artist_description = ytm_utils.get_nested(shelves, 'musicDescriptionShelfRenderer', 0, 'description', 'runs', 0, 'text')

    songs = []

    shelf_songs = ytm_utils.get_nested(shelves, 'musicShelfRenderer', 0, 'contents', default=[])

    for song in shelf_songs:
        song = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer')

        song_overlay_watch_endpoint = ytm_utils.get_nested(song, 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint')
        song_menu_watch_endpoint = ytm_utils.get_nested(song, 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint')
        song_flex_column_0_run = ytm_utils.get_nested(song, 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0)
        song_flex_column_1_run = ytm_utils.get_nested(song, 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0)
        song_flex_column_2_run = ytm_utils.get_nested(song, 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0)

        song_playlist_params = ytm_utils.get_nested(song_overlay_watch_endpoint, 'params')
        song_playlist_id = ytm_utils.get_nested(song_overlay_watch_endpoint, 'playlistId')
        song_video_id = ytm_utils.get_nested(song_overlay_watch_endpoint, 'videoId')
        song_music_video_type = ytm_utils.get_nested(song_overlay_watch_endpoint, 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType')
        song_thumbnail = ytm_utils.get_nested(song, 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
        song_title = ytm_utils.get_nested(song_flex_column_0_run, 'text')
        song_artist_title = ytm_utils.get_nested(song_flex_column_1_run, 'text')
        song_artist_browse_id = ytm_utils.get_nested(song_flex_column_1_run, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        song_album_title = ytm_utils.get_nested(song_flex_column_2_run, 'text')
        song_album_browse_id = ytm_utils.get_nested(song_flex_column_2_run, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        song_radio_params = ytm_utils.get_nested(song_menu_watch_endpoint, 'params')
        song_radio_playlist_id = ytm_utils.get_nested(song_menu_watch_endpoint, 'playlistId')

        song_data = \
        {
            'id': song_video_id,
            'title': song_title,
            # 'video_type': song_music_video_type,
            'thumbnail': song_thumbnail,
            # 'playlist': \
            # {
            #     'params': song_playlist_params,
            #     'id': song_playlist_id,
            # },
            'artist': \
            {
                'title': song_artist_title,
                'id': song_artist_browse_id,
            },
            'album': \
            {
                'title': song_album_title,
                'id': song_album_browse_id,
            },
            'radio': \
            {
                'params': song_radio_params,
                'playlist_id': song_radio_playlist_id,
            },
        }

        songs.append(song_data)

    shelves = ytm_utils.get_nested(shelves, 'musicCarouselShelfRenderer', default=())

    shelves_data = {}

    fields = \
    (
        'albums',
        'singles',
        'videos',
        'songs',
        'playlists',
        'similar_artists',
    )

    for field in fields:
        shelves_data.setdefault(field, None)

    for shelf in shelves:
        shelf_title = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'title', 'runs', 0, 'text')
        shelf_browse_id = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'endIcons', 0, 'iconLinkRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
        shelf_params = ytm_utils.get_nested(shelf, 'header', 'musicCarouselShelfBasicHeaderRenderer', 'endIcons', 0, 'iconLinkRenderer', 'navigationEndpoint', 'browseEndpoint', 'params')

        shelf_identifier = shelf_title.strip().lower().replace(' ', '_') if shelf_title else None

        shelf_items = ytm_utils.get_nested(shelf, 'contents', default=[])

        items = []

        for item in shelf_items:
            if shelf_identifier == 'albums':
                shelf_item_icon_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitleBadges', 0, 'musicInlineBadgeRenderer', 'icon', 'iconType')

                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_browse_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
                shelf_item_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'params')
                shelf_item_page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
                shelf_item_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text')
                shelf_item_year = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text', func=int)
                shelf_item_explicit = shelf_item_icon_type == 'MUSIC_EXPLICIT_BADGE'
                shelf_item_shuffle_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_shuffle_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

                item_data = \
                {
                    'name': shelf_item_title,
                    'id': shelf_item_browse_id,
                    'type': shelf_item_type,
                    'year': shelf_item_year,
                    'explicit': shelf_item_explicit,
                    'params': shelf_item_params,
                    'thumbnail': shelf_item_thumbnail,
                    'shuffle': \
                    {
                        'params': shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params': shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'singles':
                shelf_item_icon_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitleBadges', 0, 'musicInlineBadgeRenderer', 'icon', 'iconType')

                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_browse_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
                shelf_item_playlist_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'params')
                shelf_item_page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
                shelf_item_year = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text', func=int)
                shelf_item_explicit = shelf_item_icon_type == 'MUSIC_EXPLICIT_BADGE'
                shelf_item_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailOverlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_shuffle_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_shuffle_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'title': shelf_item_title,
                    'album_id': shelf_item_browse_id,
                    'playlist': \
                    {
                        'params': shelf_item_playlist_params,
                        'id': shelf_item_playlist_id,
                    },
                    'year': shelf_item_year,
                    'explicit': shelf_item_explicit,
                    'shuffle': \
                    {
                        'params': shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params': shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'videos':
                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_video_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'videoId')
                shelf_item_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId')
                shelf_item_music_video_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'title': shelf_item_title,
                    'id': shelf_item_video_id,
                    # 'playlist_id': shelf_item_playlist_id,
                    # 'video_type': shelf_item_music_video_type,
                    'radio': \
                    {
                        'params': shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'featured_on':
                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_playlist_browse_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
                shelf_item_page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
                shelf_item_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text')
                shelf_item_artist = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 2, 'text')
                shelf_item_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailOverlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_shuffle_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_shuffle_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'title': shelf_item_title,
                    'artist': shelf_item_artist,
                    # 'playlist': \
                    # {
                    #     'browse_id': shelf_item_playlist_browse_id,
                    'id': shelf_item_playlist_id,
                    # },
                    'shuffle': \
                    {
                        'params': shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params': shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }
            elif shelf_identifier == 'fans_might_also_like':
                shelf_item_page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_browse_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
                shelf_item_subscribers = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text', func=lambda subscribers: subscribers.split(' ')[0])
                shelf_item_shuffle_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_shuffle_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'title': shelf_item_title,
                    'id': shelf_item_browse_id,
                    # 'page_type': shelf_item_page_type,
                    'subscribers': shelf_item_subscribers,
                    'shuffle': \
                    {
                        'params': shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                    'radio': \
                    {
                        'params': shelf_item_shuffle_params,
                        'playlist_id': shelf_item_shuffle_playlist_id,
                    },
                }
            else:
                return # raise

            items.append(item_data)

        if shelf_identifier == 'albums':
            shelf_data = \
            {
                'title': shelf_title,
                # 'artist_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            # Update to correct artist id
            artist_id = shelf_browse_id
        elif shelf_identifier == 'singles':
            shelf_data = \
            {
                'title': shelf_title,
                # 'artist_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            # Update to correct artist id
            artist_id = shelf_browse_id
        elif shelf_identifier == 'videos':
            if shelf_browse_id and shelf_browse_id.startswith('VL'):
                shelf_browse_id = shelf_browse_id[2:]

            shelf_data = \
            {
                'title': shelf_title,
                'playlist_id': shelf_browse_id, # left-strip 'VL'
                # 'params': shelf_params, # Needed?
                'items': items,
            }
        elif shelf_identifier == 'featured_on':
            shelf_data = \
            {
                'title': shelf_title,
                # 'browse_id': shelf_browse_id,
                # 'params': shelf_params,
                'items': items,
            }

            shelf_identifier = 'playlists'
        elif shelf_identifier == 'fans_might_also_like':
            shelf_data = \
            {
                'title': shelf_title,
                # 'browse_id': shelf_browse_id,
                # 'params': shelf_params,
                'items': items,
            }

            shelf_identifier = 'similar_artists'
        else:
            return # raise

        shelves_data[shelf_identifier] = shelf_data

    if artist_playlist_id and artist_playlist_id.startswith('VL'):
        artist_playlist_id = artist_playlist_id[2:]

    shelves_data['songs'] = \
    {
        'title': 'Songs',
        'playlist_id': artist_playlist_id, # Left-strip 'VL'
        # 'params': artist_playlist_params, # Needed?
        'items': songs,
    }

    scraped = \
    {
        'name': artist_name,
        'id': artist_id,
        'subscribers': artist_subscribers,
        'views': artist_views,
        'description': artist_description,
        # 'shelves': shelves_data,
        **shelves_data,
    }

    return scraped

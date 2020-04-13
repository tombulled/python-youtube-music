from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    # return data
    contents = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', default=())

    shelves = {}

    for content in contents:
        content_key = list(content)[0]
        content = content[content_key]

        if content_key in shelves:
            shelves[content_key].append(content)
        else:
            shelves[content_key] = [content]

    # return shelves

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
        song_playlist_params = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'params')
        song_playlist_id = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'playlistId')
        song_video_id = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'videoId')
        song_title = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
        song_music_video_type = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'overlay', 'musicItemThumbnailOverlayRenderer', 'content', 'musicPlayButtonRenderer', 'playNavigationEndpoint', 'watchEndpoint', 'watchEndpointMusicSupportedConfigs', 'watchEndpointMusicConfig', 'musicVideoType')
        song_thumbnail = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
        song_artist_title = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
        song_artist_browse_id = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        song_album_title = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
        song_album_browse_id = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'flexColumns', 2, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        song_radio_params = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'params')
        song_radio_playlist_id = ytm_utils.get_nested(song, 'musicResponsiveListItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchEndpoint', 'playlistId')

        song_data = \
        {
            'id': song_video_id,
            'title': song_title,
            'video_type': song_music_video_type,
            'thumbnail': song_thumbnail,
            'playlist': \
            {
                'params': song_playlist_params,
                'id': song_playlist_id,
            },
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

        song_obj = containers.ArtistSong(self.api, song_data)

        songs.append(song_obj)

    songs_obj = containers.ArtistSongs(self.api, songs)

    shelves = ytm_utils.get_nested(shelves, 'musicCarouselShelfRenderer', default=[])

    shelves_data = {}

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

                item_obj = containers.ArtistAlbum(self.api, item_data)
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

                item_obj = containers.ArtistSingle(self.api, item_data)
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
                    'song_id': shelf_item_video_id,
                    'playlist_id': shelf_item_playlist_id,
                    'video_type': shelf_item_music_video_type,
                    'radio': \
                    {
                        'params': shelf_item_radio_params,
                        'playlist_id': shelf_item_radio_playlist_id,
                    },
                }

                item_obj = containers.ArtistVideo(self.api, item_data)
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
                    'playlist': \
                    {
                        'browse_id': shelf_item_playlist_browse_id,
                        'id': shelf_item_playlist_id,
                    },
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

                item_obj = containers.ArtistPlaylist(self.api, item_data)
            elif shelf_identifier == 'fans_might_also_like':
                shelf_item_thumbnail = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'thumbnailRenderer', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)
                shelf_item_title = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'title', 'runs', 0, 'text')
                shelf_item_browse_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId')
                shelf_item_page_type = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
                shelf_item_subscribers = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'subtitle', 'runs', 0, 'text', func=lambda subscribers: subscribers.split(' ')[0])
                shelf_item_shuffle_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_shuffle_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 0, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')
                shelf_item_radio_params = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
                shelf_item_radio_playlist_id = ytm_utils.get_nested(item, 'musicTwoRowItemRenderer', 'menu', 'menuRenderer', 'items', 1, 'menuNavigationItemRenderer', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

                item_data = \
                {
                    'thumbnail': shelf_item_thumbnail,
                    'title': shelf_item_title,
                    'artist_id': shelf_item_browse_id,
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

                item_obj = containers.ArtistSimilarArtist(self.api, item_data)
            else:
                return # raise

            items.append(item_obj)

        if shelf_identifier == 'albums':
            shelf_data = \
            {
                'title': shelf_title,
                'browse_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            shelf_obj = containers.ArtistAlbums(self.api, shelf_data)
        elif shelf_identifier == 'singles':
            shelf_data = \
            {
                'title': shelf_title,
                'browse_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            shelf_obj = containers.ArtistSingles(self.api, shelf_data)
        elif shelf_identifier == 'videos':
            shelf_data = \
            {
                'title': shelf_title,
                'browse_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            shelf_obj = containers.ArtistVideos(self.api, shelf_data)
        elif shelf_identifier == 'featured_on':
            shelf_data = \
            {
                'title': shelf_title,
                'browse_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            shelf_identifier = 'playlists'

            shelf_obj = containers.ArtistPlaylists(self.api, shelf_data)
        elif shelf_identifier == 'fans_might_also_like':
            shelf_data = \
            {
                'title': shelf_title,
                'browse_id': shelf_browse_id,
                'params': shelf_params,
                'items': items,
            }

            shelf_identifier = 'similar_artists'

            shelf_obj = containers.ArtistSimilarArtists(self.api, shelf_data)
        else:
            return # raise

        shelves_data[shelf_identifier] = shelf_obj

    scraped = \
    {
        'name': artist_name,
        'id': artist_id,
        'subscribers': artist_subscribers,
        'views': artist_views,
        'description': artist_description,
        'shelves': shelves_data,
        'playlist': \
        {
            'id': artist_playlist_id,
            'params': artist_playlist_params,
        },
        'songs': songs_obj,
    }

    return scraped

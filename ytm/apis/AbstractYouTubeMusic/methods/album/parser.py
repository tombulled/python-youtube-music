from ..... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def parse(data):
    scraped = {}

    # Better way of doing this?
    raw_mutations = ytm_utils.get_nested \
    (
        data,
        'frameworkUpdates',
        'entityBatchUpdate',
        'mutations',
        default = (),
    )

    mutations = {}

    for mutation in raw_mutations:
        payload = ytm_utils.get_nested(mutation, 'payload', default={})

        # Use utils.first_key ?
        payload_type = ytm_utils.get_nested(list(payload.keys()), 0)

        payload = ytm_utils.get_nested(payload, payload_type)

        if not payload:
            continue

        mutations.setdefault(payload_type, []).append(payload)

    other_versions_contents = ytm_utils.get_nested \
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
        1,
        'musicCarouselShelfRenderer',
        'contents',
        default=(),
    )

    other_versions = []

    for album in other_versions_contents:
        album = ytm_utils.get_nested(album, 'musicTwoRowItemRenderer')

        album_menu_items = ytm_utils.get_nested \
        (
            album,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )

        album_menu = {}

        for menu_item in album_menu_items:
            menu_item = ytm_utils.first_key(menu_item)

            for key, val in menu_item.copy().items():
                if not key.startswith('default'):
                    continue

                new_key = key.replace('default', '')
                new_key = new_key[0].lower() + new_key[1:]

                menu_item[new_key] = menu_item.pop(key)

            menu_text = ytm_utils.get_nested \
            (
                menu_item,
                'text',
                'runs',
                0,
                'text',
            )
            menu_icon = ytm_utils.get_nested \
            (
                menu_item,
                'icon',
                'iconType',
            )
            menu_endpoint = ytm_utils.get_nested \
            (
                menu_item,
                'navigationEndpoint',
            )

            if not menu_endpoint:
                continue

            menu_identifier = menu_text[0].lower() + menu_text.title()[1:].replace(' ', '') if menu_text else None

            menu_item_data = \
            {
                'text':     menu_text,
                'icon':     menu_icon,
                'endpoint': menu_endpoint,
            }

            album_menu[menu_identifier] = menu_item_data

        album_thumbnail = ytm_utils.get_nested \
        (
            album,
            'thumbnailRenderer',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        album_name = ytm_utils.get_nested \
        (
            album,
            'title',
            'runs',
            0,
            'text',
        )
        album_type = ytm_utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            0,
            'text',
        )
        album_artist_name = ytm_utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            2,
            'text',
        )
        album_artist_id = ytm_utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            2,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        album_page_type = ytm_utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseEndpointContextSupportedConfigs',
            'browseEndpointContextMusicConfig',
            'pageType',
        )
        album_id = ytm_utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        album_params = ytm_utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'params',
        )
        album_radio_id = ytm_utils.get_nested \
        (
            album_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        album_radio_params = ytm_utils.get_nested \
        (
            album_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'params',
        )


        album_data = \
        {
            'name':      album_name,
            'id':        album_id,
            'params':    album_params,
            'thumbnail': album_thumbnail,
            'type':      album_type,
            'radio': \
            {
                'id':     album_radio_id,
                'params': album_radio_params,
            },
            'artist': \
            {
                'name': album_artist_name,
                'id':   album_artist_id,
            },
        }

        other_versions.append(album_data)

    tracks = ytm_utils.get_nested(mutations, 'musicTrack', default=())

    tracks_data = []

    for track in tracks:
        track_index = ytm_utils.get_nested \
        (
            track,
            'albumTrackIndex',
            func = int,
        )
        track_artists = ytm_utils.get_nested \
        (
            track,
            'artistNames',
            func = lambda names: list(map(str.strip, names.split(','))),
        )
        track_explicit = ytm_utils.get_nested \
        (
            track,
            'contentRating',
            'explicitType',
        ) == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT'
        track_length = ytm_utils.get_nested \
        (
            track,
            'lengthMs',
            func = int,
        ) # round(int(track.get('lengthMs'))/60*10**-3, 2)
        track_thumbnail = ytm_utils.get_nested \
        (
            track,
            'thumbnailDetails',
            'thumbnails',
            -1,
        )
        track_title = ytm_utils.get_nested \
        (
            track,
            'title',
        )
        track_id = ytm_utils.get_nested \
        (
            track,
            'videoId',
        )

        track_data = \
        {
            'index':     track_index,
            'artists':   track_artists,
            'explicit':  track_explicit,
            'length':    track_length,
            'thumbnail': track_thumbnail,
            'title':     track_title,
            'video_id':  track_id,
        }

        tracks_data.append(track_data)

    artists_data = []

    for artist in ytm_utils.get_nested(mutations, 'musicArtist'):
        artist_id        = ytm_utils.get_nested(artist, 'externalChannelId')
        artist_name      = ytm_utils.get_nested(artist, 'name')
        artist_thumbnail = ytm_utils.get_nested(artist, 'thumbnailDetails', 'thumbnails', -1)

        artist_data = \
        {
            'id':        artist_id,
            'name':      artist_name,
            'thumbnail': artist_thumbnail,
        }

        artists_data.append(artist_data)

    album_data = \
    {
        'track_count': int(ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'trackCount')),
        'radio_id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'radioAutomixPlaylistId'),
        'id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'audioPlaylistId'),
        'artist_name': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'artistDisplayName'),
        'explicit': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType') == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT',
        'duration': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'durationMs', func=int), # /60*10**-3
        'primary_artist_ids': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'primaryArtists'),
        'release_date': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseDate'),
        'release_type': \
        {
            'MUSIC_RELEASE_TYPE_ALBUM': 'Album',
            'MUSIC_RELEASE_TYPE_EP': 'EP',
        }[ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseType')],
        'thumbnail': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'thumbnailDetails', 'thumbnails', -1),
        'title': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'title'),
        'description': ytm_utils.get_nested(mutations, 'musicAlbumReleaseDetail', 0, 'description'),
    }

    scraped = \
    {
        'artists': artists_data,
        'album': album_data,
        'tracks': tracks_data,
        'variants': other_versions,
    }

    return scraped

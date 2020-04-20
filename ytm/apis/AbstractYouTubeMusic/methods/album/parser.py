from ... import utils
from ... import decorators

__parser__ = __name__.split('.')[-1]
__method__ = __name__.split('.')[-2]
__all__ = (__parser__,)

@decorators.catch(__method__)
def parse(data):
    assert data

    scraped = {}

    raw_mutations = utils.get_nested \
    (
        data,
        'frameworkUpdates',
        'entityBatchUpdate',
        'mutations',
        default = (),
    )

    assert raw_mutations

    mutations = {}

    for mutation in raw_mutations:
        payload = utils.get_nested \
        (
            mutation,
            'payload',
            default = {},
        )

        payload_type = utils.get_nested(list(payload.keys()), 0)

        payload = utils.get_nested(payload, payload_type)

        if not payload:
            continue

        mutations.setdefault(payload_type, []).append(payload)

    other_versions_contents = utils.get_nested \
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
        default = (),
    )

    other_versions = []

    for album in other_versions_contents:
        album = utils.get_nested \
        (
            album,
            'musicTwoRowItemRenderer',
        )

        album_menu_items = utils.get_nested \
        (
            album,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )

        album_menu = {}

        for menu_item in album_menu_items:
            menu_item = utils.first_key(menu_item)

            for key, val in menu_item.copy().items():
                if not key.startswith('default'):
                    continue

                new_key = key.replace('default', '')
                new_key = new_key[0].lower() + new_key[1:]

                menu_item[new_key] = menu_item.pop(key)

            menu_text = utils.get_nested \
            (
                menu_item,
                'text',
                'runs',
                0,
                'text',
            )
            menu_icon = utils.get_nested \
            (
                menu_item,
                'icon',
                'iconType',
            )
            menu_endpoint = utils.get_nested \
            (
                menu_item,
                'navigationEndpoint',
            )

            if not menu_endpoint:
                continue

            menu_identifier = menu_text[0].lower() + menu_text.title()[1:].replace(' ', '') \
                if menu_text else None

            menu_item_data = \
            {
                'text':     menu_text,
                'icon':     menu_icon,
                'endpoint': menu_endpoint,
            }

            album_menu[menu_identifier] = menu_item_data

        album_thumbnail = utils.get_nested \
        (
            album,
            'thumbnailRenderer',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        album_name = utils.get_nested \
        (
            album,
            'title',
            'runs',
            0,
            'text',
        )
        album_type = utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            0,
            'text',
        )
        album_artist_name = utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            2,
            'text',
        )
        album_artist_id = utils.get_nested \
        (
            album,
            'subtitle',
            'runs',
            2,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        album_page_type = utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseEndpointContextSupportedConfigs',
            'browseEndpointContextMusicConfig',
            'pageType',
        )
        album_id = utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        album_params = utils.get_nested \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'params',
        )
        album_radio_id = utils.get_nested \
        (
            album_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        album_radio_params = utils.get_nested \
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

    tracks = utils.get_nested \
    (
        mutations,
        'musicTrack',
        default = (),
    )

    tracks_data = []

    for track in tracks:
        track_index = utils.get_nested \
        (
            track,
            'albumTrackIndex',
            func = int,
        )
        track_artists = utils.get_nested \
        (
            track,
            'artistNames',
            func = lambda names: list(map(str.strip, names.split(','))),
        )
        track_explicit = utils.get_nested \
        (
            track,
            'contentRating',
            'explicitType',
        ) == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT'
        track_length = utils.get_nested \
        (
            track,
            'lengthMs',
            func = int,
        ) # round(int(track.get('lengthMs'))/60*10**-3, 2)
        track_thumbnail = utils.get_nested \
        (
            track,
            'thumbnailDetails',
            'thumbnails',
            -1,
        )
        track_title = utils.get_nested \
        (
            track,
            'title',
        )
        track_id = utils.get_nested \
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

    music_artist = utils.get_nested(mutations, 'musicArtist', default=())

    for artist in music_artist:
        artist_id = utils.get_nested \
        (
            artist,
            'externalChannelId',
        )
        artist_name = utils.get_nested \
        (
            artist,
            'name',
        )
        artist_thumbnail = utils.get_nested \
        (
            artist,
            'thumbnailDetails',
            'thumbnails',
            -1,
        )

        artist_data = \
        {
            'id':        artist_id,
            'name':      artist_name,
            'thumbnail': artist_thumbnail,
        }

        artists_data.append(artist_data)

    album_release = utils.get_nested \
    (
        mutations,
        'musicAlbumRelease',
        0,
    )
    album_release_detail = utils.get_nested \
    (
        mutations,
        'musicAlbumReleaseDetail',
        0,
    )

    album_track_count = utils.get_nested \
    (
        album_release,
        'trackCount',
        func = int,
    )
    album_radio_id = utils.get_nested \
    (
        album_release,
        'radioAutomixPlaylistId',
    )
    album_id = utils.get_nested \
    (
        album_release,
        'audioPlaylistId',
    )
    album_artist_name = utils.get_nested \
    (
        album_release,
        'artistDisplayName',
    )
    album_explicit = utils.get_nested \
    (
        album_release,
        'contentRating',
        'explicitType',
    ) == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT'
    album_duration = utils.get_nested \
    (
        album_release,
        'durationMs',
        func = int,
    ) # /60*10**-3
    album_primary_artist_ids = utils.get_nested \
    (
        album_release,
        'primaryArtists',
    )
    album_release_date = utils.get_nested \
    (
        album_release,
        'releaseDate',
    )
    album_release_type = utils.get_nested \
    (
        album_release,
        'releaseType',
        func = lambda type: type.split('_')[-1].title(),
    )
    album_thumbnail = utils.get_nested \
    (
        album_release,
        'thumbnailDetails',
        'thumbnails',
        -1,
    )
    album_title = utils.get_nested \
    (
        album_release,
        'title',
    )
    album_description = utils.get_nested \
    (
        album_release_detail,
        'description',
    )

    album_data = \
    {
        'name':               album_title,
        'id':                 album_id,
        'track_count':        album_track_count,
        'radio_id':           album_radio_id,
        'artist_name':        album_artist_name,
        'explicit':           album_explicit,
        'duration':           album_duration,
        'primary_artist_ids': album_primary_artist_ids,
        'release_date':       album_release_date,
        'release_type':       album_release_type,
        'thumbnail':          album_thumbnail,
        'description':        album_description,
    }

    scraped = \
    {
        'artists':  artists_data,
        'album':    album_data,
        'tracks':   tracks_data,
        'variants': other_versions,
    }

    return scraped

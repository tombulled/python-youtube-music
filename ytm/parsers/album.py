'''
Module containing the parser: album
'''

from .. import utils
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def album(data: dict) -> dict:
    '''
    Parse album data.

    Args:
        data: Data to parse

    Returns:
        Parsed data

    Raises:
        ParserError: The parser encountered an error

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api.browse_album('MPREb_ij6eHbvH9FF')
        >>>
        >>> parsed_data['name']
        'Why Are You OK'
        >>>
    '''

    assert data, 'No data to parse'

    scraped = {}

    raw_mutations = utils.get \
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
        payload = utils.get \
        (
            mutation,
            'payload',
            default = {},
        )

        payload_type = utils.get(list(payload.keys()), 0)

        payload = utils.get(payload, payload_type)

        if not payload:
            continue

        mutations.setdefault(payload_type, []).append(payload)

    other_versions_contents = utils.get \
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
        album = utils.get \
        (
            album,
            'musicTwoRowItemRenderer',
        )

        album_menu_items = utils.get \
        (
            album,
            'menu',
            'menuRenderer',
            'items',
            default = (),
        )

        album_menu = {}

        for menu_item in album_menu_items:
            menu_item = utils.first(menu_item)

            for key, val in menu_item.copy().items():
                if not key.startswith('default'):
                    continue

                new_key = key.replace('default', '')
                new_key = new_key[0].lower() + new_key[1:]

                menu_item[new_key] = menu_item.pop(key)

            menu_text = utils.get \
            (
                menu_item,
                'text',
                'runs',
                0,
                'text',
            )
            menu_icon = utils.get \
            (
                menu_item,
                'icon',
                'iconType',
            )
            menu_endpoint = utils.get \
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

        # return album_menu ###
        # return album
        # return utils.get \
        # (
        #     album,
        #     'subtitle')

        album_subtitle_runs = utils.get \
        (
            album,
            'subtitle',
            'runs',
            default = (),
        )

        album_thumbnail = utils.get \
        (
            album,
            'thumbnailRenderer',
            'musicThumbnailRenderer',
            'thumbnail',
            'thumbnails',
            -1,
        )
        album_name = utils.get \
        (
            album,
            'title',
            'runs',
            0,
            'text',
        )
        album_type = utils.get \
        (
            album_subtitle_runs,
            0,
            'text',
        )
        # album_artist_name = utils.get \
        # (
        #     album,
        #     'subtitle',
        #     'runs',
        #     2,
        #     'text',
        # )
        # album_artist_id = utils.get \
        # (
        #     album,
        #     'subtitle',
        #     'runs',
        #     2,
        #     'navigationEndpoint',
        #     'browseEndpoint',
        #     'browseId',
        # )
        album_page_type = utils.get \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseEndpointContextSupportedConfigs',
            'browseEndpointContextMusicConfig',
            'pageType',
        )
        album_id = utils.get \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'browseId',
        )
        album_params = utils.get \
        (
            album,
            'navigationEndpoint',
            'browseEndpoint',
            'params',
        )
        album_radio_id = utils.get \
        (
            album_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        album_radio_params = utils.get \
        (
            album_menu,
            'startRadio',
            'endpoint',
            'watchPlaylistEndpoint',
            'params',
        )
        album_shuffle_id = utils.get \
        (
            album_menu,
            'shufflePlay',
            'endpoint',
            'watchPlaylistEndpoint',
            'playlistId',
        )
        album_shuffle_params = utils.get \
        (
            album_menu,
            'shufflePlay',
            'endpoint',
            'watchPlaylistEndpoint',
            'params',
        )

        album_artists = []

        for album_artist in album_subtitle_runs[2::2]:
            album_artist_name = utils.get \
            (
                album_artist,
                'text',
            )
            album_artist_id = utils.get \
            (
                album_artist,
                'navigationEndpoint',
                'browseEndpoint',
                'browseId',
            )

            album_artist_data = \
            {
                'name': album_artist_name,
                'id':   album_artist_id,
            }

            album_artists.append(album_artist_data)

        album_data = \
        {
            'name':      album_name,
            'id':        album_id,
            # 'params':    album_params,
            'thumbnail': album_thumbnail,
            'type':      album_type,
            'artists':   album_artists,
            'radio': \
            {
                'id':     album_radio_id,
                'params': album_radio_params,
            },
            'shuffle': \
            {
                'id':     album_shuffle_id,
                'params': album_shuffle_params,
            },
            # 'artist': \
            # {
            #     'name': album_artist_name,
            #     'id':   album_artist_id,
            # },
        }

        other_versions.append(album_data)

    tracks = utils.get \
    (
        mutations,
        'musicTrack',
        default = (),
    )

    tracks_data = []

    for track in tracks:
        # return track ###

        track_index = utils.get \
        (
            track,
            'albumTrackIndex',
            func = int,
        )
        track_artists = utils.get \
        (
            track,
            'artistNames',
            func = lambda names: list(map(str.strip, names.split(','))),
        )
        track_explicit = utils.get \
        (
            track,
            'contentRating',
            'explicitType',
        ) == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT'
        track_length = utils.get \
        (
            track,
            'lengthMs',
            func = int,
        ) # round(int(track.get('lengthMs'))/60*10**-3, 2)
        track_thumbnail = utils.get \
        (
            track,
            'thumbnailDetails',
            'thumbnails',
            -1,
        )
        track_title = utils.get \
        (
            track,
            'title',
        )
        track_id = utils.get \
        (
            track,
            'videoId',
        )

        track_data = \
        {
            'index':     track_index,
            'explicit':  track_explicit,
            'length':    track_length,
            'thumbnail': track_thumbnail,
            'name':     track_title,
            'id':        track_id,
        }

        tracks_data.append(track_data)

    tracks_data = sorted(tracks_data, key=lambda track: track.pop('index'))

    artists_data = []

    music_artist = utils.get(mutations, 'musicArtist', default=())

    for artist in music_artist:
        artist_id = utils.get \
        (
            artist,
            'externalChannelId',
        )
        artist_name = utils.get \
        (
            artist,
            'name',
        )
        artist_thumbnail = utils.get \
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

    # return mutations ###

    album_release = utils.get \
    (
        mutations,
        'musicAlbumRelease',
        0,
    )
    album_release_detail = utils.get \
    (
        mutations,
        'musicAlbumReleaseDetail',
        0,
    )

    album_track_count = utils.get \
    (
        album_release,
        'trackCount',
        func = int,
    )
    album_radio_id = utils.get \
    (
        album_release,
        'radioAutomixPlaylistId',
    )
    album_shuffle_id = utils.get \
    (
        album_release,
        'radioPlaylistMixPlaylistId', # These may be the wrong way around?
    )
    album_id = utils.get \
    (
        album_release,
        'audioPlaylistId',
    )
    album_artist_name = utils.get \
    (
        album_release,
        'artistDisplayName',
    )
    album_explicit = utils.get \
    (
        album_release,
        'contentRating',
        'explicitType',
    ) == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT'
    album_duration = utils.get \
    (
        album_release,
        'durationMs',
        func = int,
    ) # /60*10**-3
    album_primary_artist_ids = utils.get \
    (
        album_release,
        'primaryArtists',
    )
    album_release_date = utils.get \
    (
        album_release,
        'releaseDate',
    )
    album_release_type = utils.get \
    (
        album_release,
        'releaseType',
        func = lambda type: type.split('_')[-1].title(),
    )
    album_thumbnail = utils.get \
    (
        album_release,
        'thumbnailDetails',
        'thumbnails',
        -1,
    )
    album_title = utils.get \
    (
        album_release,
        'title',
    )
    album_description = utils.get \
    (
        album_release_detail,
        'description',
    )

    album_radio_data = None
    album_shuffle_data = None

    if album_radio_id:
        album_radio_data = \
        {
            'playlist_id': album_radio_id,
        }
    if album_shuffle_id:
        album_shuffle_data = \
        {
            'playlist_id': album_shuffle_id,
        }

    album_data = \
    {
        'name':          album_title,
        'id':            album_id,
        'total_tracks':  album_track_count,
        'radio':         album_radio_data,
        'shuffle':       album_shuffle_data,
        'explicit':      album_explicit,
        'duration':      album_duration,
        'date':          album_release_date,
        'type':          album_release_type,
        'thumbnail':     album_thumbnail,
        'description':   album_description,
    }

    scraped = \
    {
        **album_data,
        'artists':  artists_data,
        # 'album':    album_data,
        'tracks':   tracks_data,
        'variants': other_versions,
    }

    return scraped

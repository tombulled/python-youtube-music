from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    scraped = {}

    # Better way of doing this?
    raw_mutations = ytm_utils.get_nested(data, 'frameworkUpdates', 'entityBatchUpdate', 'mutations', default=[])
    mutations = {}

    for mutation in raw_mutations:
        payload = mutation['payload']
        payload_type = list(payload.keys())[0]

        payload = payload[payload_type]

        if payload_type in mutations:
            mutations[payload_type].append(payload)
        else:
            mutations[payload_type] = [payload]

    tracks = mutations.get('musicTrack', [])
    tracks_data = []

    for track in tracks:
        track_data = \
        {
            # 'index': int(track.get('albumTrackIndex')),
            'index': ytm_utils.get_nested(track, 'albumTrackIndex', func=int),
            'artist_names': track.get('artistNames'),
            'explicit': ytm_utils.get_nested(track, 'contentRating', 'explicitType') == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT',
            # '_explicit_type': ytm_utils.get_nested(track, 'contentRating', 'explicitType'),
            # '_explicit': {'MUSIC_ENTITY_EXPLICIT_TYPE_NOT_EXPLICIT': False, 'MUSIC_ENTITY_EXPLICIT_TYPE_EDITED': False}[ytm_utils.get_nested(track, 'contentRating', 'explicitType')],
            #'details': track.get('details'),
            #'id': track.get('id'),
            # 'length': round(int(track.get('lengthMs'))/60*10**-3, 2), # parse me
            'length': ytm_utils.get_nested(track, 'lengthMs', func=int),
            #'like_state': track.get('likeState'),
            #'tracking_params': ytm_utils.get_nested(track, 'loggingDirectives', 'trackingParams'),
            #'share': track.get('share'),
            'thumbnail': ytm_utils.get_nested(track, 'thumbnailDetails', 'thumbnails', -1),
            'title': track.get('title'),
            'video_id': track.get('videoId'),
            #'video_mode_version': track.'videoModeVersion'),
        }

        track_obj = containers.AlbumTrack(self.api, track_data)

        # tracks_data.append(track_data)
        tracks_data.append(track_obj)

    artist_data = \
    {
        'id': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'externalChannelId'),
        'name': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'name'),
        'thumbnail': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'thumbnailDetails', 'thumbnails', -1),
    }

    artist_obj = containers.AlbumArtist(self.api, artist_data)

    album_data = \
    {
        'artist_name': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'artistDisplayName'),
        #'audio_playlist_id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'audioPlaylistId'),
        'explicit': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType') == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT',
        # '_explicit_type': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType'),
        # 'explicit': {'MUSIC_ENTITY_EXPLICIT_TYPE_NOT_EXPLICIT': False, 'MUSIC_ENTITY_EXPLICIT_TYPE_EDITED': False}[ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType')],
        # '_details': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'details'),
        # 'duration': round(int(ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'durationMs'))/60*10**-3, 2),
        'duration': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'durationMs', func=int),
        #'id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'id'),
        #'tracking_params': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'loggingDirectives', 'trackingParams'),
        'primary_artist_ids': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'primaryArtists'),
        #'radio_automix_playlist_id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'radioAutomixPlaylistId'),
        'release_date': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseDate'),
        'release_type': \
        {
            'MUSIC_RELEASE_TYPE_ALBUM': 'Album',
            'MUSIC_RELEASE_TYPE_EP': 'EP',
            # ep...
        }[ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseType')],
        #'share': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'share'),
        #'thumbnails': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'thumbnailDetails', 'thumbnails'),
        'thumbnail': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'thumbnailDetails', 'thumbnails', -1),
        'title': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'title'),
        # 'track_count': int(ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'trackCount')),
        # '_user_details': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'userDetails'),
        'description': ytm_utils.get_nested(mutations, 'musicAlbumReleaseDetail', 0, 'description'),
        # '_tracks': ytm_utils.get_nested(mutations, 'musicAlbumReleaseDetail', 0, 'tracks'),
        #'in_library': ytm_utils.get_nested(mutations, 'musicAlbumReleaseUserDetail', 0, 'in_library'),
    }

    scraped = \
    {
        # 'artist': artist_data,
        'artist': artist_obj,
        'album': album_data,
        'tracks': tracks_data,
    }

    return scraped

    # scraped = \
    # {
    #     'artist': \
    #     {
    #         'channel_id': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'externalChannelId'),
    #         'name': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'name'),
    #         'thumbnail': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'thumbnailDetails', 'thumbnails', -1),
    #         # '_id': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'id'),
    #         # '_details': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'details'),
    #         # '_user_details': ytm_utils.get_nested(mutations, 'musicArtist', 0, 'userDetails'),
    #     },
    #     'tracks': \
    #     [
    #         {
    #             # 'index': int(track.get('albumTrackIndex')),
    #             'index': ytm_utils.get_nested(track, 'albumTrackIndex', func=int),
    #             'artist_names': track.get('artistNames'),
    #             'explicit': ytm_utils.get_nested(track, 'contentRating', 'explicitType') == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT',
    #             # '_explicit_type': ytm_utils.get_nested(track, 'contentRating', 'explicitType'),
    #             # '_explicit': {'MUSIC_ENTITY_EXPLICIT_TYPE_NOT_EXPLICIT': False, 'MUSIC_ENTITY_EXPLICIT_TYPE_EDITED': False}[ytm_utils.get_nested(track, 'contentRating', 'explicitType')],
    #             #'details': track.get('details'),
    #             #'id': track.get('id'),
    #             # 'length': round(int(track.get('lengthMs'))/60*10**-3, 2), # parse me
    #             'length': ytm_utils.get_nested(track, 'lengthMs', func=int),
    #             #'like_state': track.get('likeState'),
    #             #'tracking_params': ytm_utils.get_nested(track, 'loggingDirectives', 'trackingParams'),
    #             #'share': track.get('share'),
    #             'thumbnail': ytm_utils.get_nested(track, 'thumbnailDetails', 'thumbnails', -1),
    #             'title': track.get('title'),
    #             'video_id': track.get('videoId'),
    #             #'video_mode_version': track.'videoModeVersion'),
    #         }
    #         for track in mutations.get('musicTrack', [])
    #     ],
    #     'album': \
    #     {
    #         'artist_name': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'artistDisplayName'),
    #         #'audio_playlist_id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'audioPlaylistId'),
    #         'explicit': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType') == 'MUSIC_ENTITY_EXPLICIT_TYPE_EXPLICIT',
    #         # '_explicit_type': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType'),
    #         # 'explicit': {'MUSIC_ENTITY_EXPLICIT_TYPE_NOT_EXPLICIT': False, 'MUSIC_ENTITY_EXPLICIT_TYPE_EDITED': False}[ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'contentRating', 'explicitType')],
    #         # '_details': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'details'),
    #         # 'duration': round(int(ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'durationMs'))/60*10**-3, 2),
    #         'duration': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'durationMs', func=int),
    #         #'id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'id'),
    #         #'tracking_params': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'loggingDirectives', 'trackingParams'),
    #         'primary_artist_ids': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'primaryArtists'),
    #         #'radio_automix_playlist_id': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'radioAutomixPlaylistId'),
    #         'release_date': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseDate'),
    #         'release_type': \
    #         {
    #             'MUSIC_RELEASE_TYPE_ALBUM': 'Album',
    #             'MUSIC_RELEASE_TYPE_EP': 'EP',
    #             # ep...
    #         }[ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'releaseType')],
    #         #'share': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'share'),
    #         #'thumbnails': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'thumbnailDetails', 'thumbnails'),
    #         'thumbnail': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'thumbnailDetails', 'thumbnails', -1),
    #         'title': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'title'),
    #         # 'track_count': int(ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'trackCount')),
    #         # '_user_details': ytm_utils.get_nested(mutations, 'musicAlbumRelease', 0, 'userDetails'),
    #         'description': ytm_utils.get_nested(mutations, 'musicAlbumReleaseDetail', 0, 'description'),
    #         # '_tracks': ytm_utils.get_nested(mutations, 'musicAlbumReleaseDetail', 0, 'tracks'),
    #         #'in_library': ytm_utils.get_nested(mutations, 'musicAlbumReleaseUserDetail', 0, 'in_library'),
    #     },
    # }

    # return scraped

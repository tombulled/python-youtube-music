''' xxx '''

from ..BaseYouTubeMusic import BaseYouTubeMusic

# from . import utils

# from ... import constants as ytm_constants
from ... import utils     as ytm_utils

__all__ = __name__.split('.')[-1:]

class YouTubeMusic(object):
    def __init__(self):
        self.base = BaseYouTubeMusic()

    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

    def home(self):
        ...

    def hotlist(self):
        ...

    def search(self):
        ...

    def playlist(self):
        ...

    def artist(self):
        ...

    def song(self):
        ...

    def album(self):
        ...

    def guide(self):
        ...

    def song_info(self, song_id):
        data = self.base.video_info \
        (
            video_id = song_id,
        )

        for k, v in data.items():
            print(k.ljust(35), str(type(v)).ljust(10), repr(v)[:100])

        # enable_csi = data['enablecsi'] # True
        # ps = data['ps'] # 'desktop-polymer'
        # watermark = data['watermark'] # ['https://s.ytimg.com/yts/img/watermark/youtube_watermark-vflHX6b6E.png', 'https://s.ytimg.com/yts/img/watermark/youtube_hd_watermark-vflAzLcD6.png']
        # innertube_api_version = data['innertube_api_version'] # 'v1'
        # csi_page_type = data['csi_page_type'] # 'watch'
        # cver = data['cver'] # '2.20200312.05.00'
        # use_miniplayer_ui = data['use_miniplayer_ui']
        # watch_next_response = data['watch_next_response']
        # fflags = data['fflags'] # ...
        # hl = data['hl'] # ...
        # innertube_api_key = data['innertube_api_key'] # AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8
        # cr = data['cr'] # 'GB'
        # player_response = data['player_response'] # ...

        # scraped = \
        # {
        #     'enable_csi': ytm_utils.get_nested(data, 'enablecsi'),
        #     'ps': ytm_utils.get_nested(data, 'ps'),
        #     'watermarks': ytm_utils.get_nested(data, 'watermark'),
        #     'innertube': \
        #     {
        #         'api': \
        #         {
        #             'version': ytm_utils.get_nested(data, 'innertube_api_version'),
        #             'key': ytm_utils.get_nested(data, 'innertube_api_key'),
        #         },
        #         'context_client_version': ytm_utils.get_nested(data, 'innertube_context_client_version'),
        #     },
        #     'csi_page_type': ytm_utils.get_nested(data, 'csi_page_type'),
        #     'use_miniplayer_ui': ytm_utils.get_nested(data, 'use_miniplayer_ui'),
        #     'fflags': ytm_utils.get_nested(data, 'fflags'),
        #     'host_language': ytm_utils.get_nested(data, 'hl'),
        #     'fexp': ytm_utils.get_nested(data, 'fexp'),
        #     'gapi_hint_params': ytm_utils.get_nested(data, 'gapi_hint_params'),
        #     'client': \
        #     {
        #         'name': ytm_utils.get_nested(data, 'c'),
        #         'version': ytm_utils.get_nested(data, 'cver'),
        #         'os': \
        #         {
        #             'name': ytm_utils.get_nested(data, 'cos'),
        #             'version': ytm_utils.get_nested(data, 'cosver'),
        #         },
        #         'browser': \
        #         {
        #             'name': ytm_utils.get_nested(data, 'cbr'),
        #             'version': ytm_utils.get_nested(data, 'cbrver'),
        #         },
        #     },
        #     'vss_host': ytm_utils.get_nested(data, 'vss_host'),
        #     'autoplay_count': ytm_utils.get_nested(data, 'autoplay_count'),
        #     'status': ytm_utils.get_nested(data, 'status'),
        #
        #     'rvs': ytm_utils.get_nested(data, 'rvs'),
        #     'watch_next': ytm_utils.get_nested(data, 'watch_next_response'),
        #     'player': ytm_utils.get_nested(data, 'player_response'),
        # }

        # return scraped

        scraped = \
        {
            'recommended_song': \
            {
                'aria_label': ytm_utils.get_nested(data, 'rvs', 'aria_label'),
                'author': ytm_utils.get_nested(data, 'rvs', 'author'),
                # 'endscreen_autoplay_session_data': ytm_utils.get_nested(data, 'rvs', 'endscreen_autoplay_session_data'),
                'song_id': ytm_utils.get_nested(data, 'rvs', 'id'),
                'image_url': ytm_utils.get_nested(data, 'rvs', 'iurlhq'),
                # 'iurlmq': ytm_utils.get_nested(data, 'rvs', 'iurlmq'),
                'length_seconds': ytm_utils.get_nested(data, 'rvs', 'length_seconds'),
                'list': ytm_utils.get_nested(data, 'rvs', 'list'),
                'playlist': \
                {
                    'image_url': ytm_utils.get_nested(data, 'rvs', 'playlist_iurlhq') or \
                        ytm_utils.get_nested(data, 'rvs', 'playlist_iurlmq'),
                    # 'playlist_iurlmq': ytm_utils.get_nested(data, 'rvs', 'playlist_iurlmq'),
                    'title': ytm_utils.get_nested(data, 'rvs', 'playlist_title'),
                    'length': ytm_utils.get_nested(data, 'rvs', 'playlist_length'),
                },
                # 'session_data': ytm_utils.get_nested(data, 'rvs', 'session_data'),
                'short_view_count_text': ytm_utils.get_nested(data, 'rvs', 'short_view_count_text'),
                'thumbnail_ids': ytm_utils.get_nested(data, 'rvs', 'thumbnail_ids'),
                'title': ytm_utils.get_nested(data, 'rvs', 'title'),
                # 'video_id': ytm_utils.get_nested(data, 'rvs', 'video_id'),
            },
            'watch_next': \
            {
                # '': \
                'title': ''.join \
                (
                    run['text']
                    for run in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'title', 'runs')
                ),
                'view_count': \
                {
                    'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'viewCount', 'simpleText'),
                    'short': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'shortViewCount', 'simpleText'),
                },
                'date': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'dateText', 'simpleText'),
                'owner': \
                {
                    'browse_id': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                    'subscriber_count': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'subscriberCountText', 'runs', 0, 'text'),
                    'thumbnails': \
                    [
                        {
                            'height': ytm_utils.get_nested(thumbnail, 'height'),
                            'width': ytm_utils.get_nested(thumbnail, 'width'),
                            'url': 'https:' + ytm_utils.get_nested(thumbnail, 'url'),
                        }
                        for thumbnail in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', default=[])
                    ],
                    'title': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text'),
                },
                'description': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text'),
                'explicit': 'Parental warning' in \
                [
                    ytm_utils.get_nested(row, 'metadataRowRenderer', 'title', 'simpleText')
                    for row in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'metadataRowContainer', 'metadataRowContainerRenderer', 'rows', default = [])
                ],



                # '': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoSecondaryInfoRenderer', ''),
                # }
                #     for result in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', default = []),
                # ]
                # '': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'secondaryResults'),
                # watch_next_response > contents, playerOverlays,

            },
            'player': \
            {
                # '': ytm_utils.get_nested(data, 'player_response', 'streamingData', ''),# cant use
                'channel_name': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'author'),# ...
                'average_rating': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating'),# ...
                'channel_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'channelId'),# ...
                'length_seconds': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds'),# ...
                'description': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'shortDescription'),# ...
                'thumbnails': \
                [
                    {
                        'height': ytm_utils.get_nested(thumbnail, 'height'),
                        'width': ytm_utils.get_nested(thumbnail, 'width'),
                        'url': ytm_utils.get_nested(thumbnail, 'url'),
                    }
                    for thumbnail in ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', default = [])
                ],
                'title': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'title'),# ...
                'video_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'videoId'),# ...
                'view_count': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount'),# ...
                # 'description': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'description', 'simpleText'),# ...
                # 'external_channel_id': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'externalChannelId'),# ...
                # 'micro_length_seconds': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'lengthSeconds'),# ...
                # 'owner_channel_name': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'ownerChannelName'),# ...
                'publish_date': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate'),# ...
                # 'thumbnail': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'thumbnail', 'thumbnails', 0),# ...
                # 'micro_title': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'title', 'simpleText'),# ...
                'upload_date': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'uploadDate'),# ...
                # 'micro_view_count': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'viewCount'),# ...
                # '': ytm_utils.get_nested(data, 'player_response', 'microformat', ''),# ...
                # no: playabilityStatus, playerAds, playbackTracking, captions, storyboards, adPlacements, attestation, messages
                # yes: streamingData, videoDetails, microformat
                # maybe: playerConfig, (loadness)
                # '': ytm_utils.get_nested(data, 'player_response', '')
            },
        }

        scraped = \
        {
            # 'title': ''.join \
            # (
            #     run['text']
            #     for run in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'title', 'runs')
            # ),
            'title': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'title'),# ...
            'view_count': \
            {
                'short': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'viewCount', 'simpleText'),
                'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'viewCount', 'videoViewCountRenderer', 'shortViewCount', 'simpleText'),
                'actual': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount', func=int),# ...
            },
            'owner': \
            {
                'id': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'navigationEndpoint', 'browseEndpoint', 'browseId'),
                'subscriber_count': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'subscriberCountText', 'runs', 0, 'text'),
                'thumbnails': \
                [
                    {
                        'height': ytm_utils.get_nested(thumbnail, 'height'),
                        'width': ytm_utils.get_nested(thumbnail, 'width'),
                        'url': 'https:' + ytm_utils.get_nested(thumbnail, 'url'),
                    }
                    for thumbnail in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails', default=[])
                ],
                'name': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'owner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text'),
            },
            'description': \
            {
                'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'description', 'runs', 0, 'text'),
                'short': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'shortDescription'),# ...
            },
            'explicit': 'Parental warning' in \
            [
                ytm_utils.get_nested(row, 'metadataRowRenderer', 'title', 'simpleText')
                for row in ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 1, 'videoSecondaryInfoRenderer', 'metadataRowContainer', 'metadataRowContainerRenderer', 'rows', default = [])
            ],
            'channel': \
            {
                'name': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'author'),# ...
                'id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'channelId'),# ...
            },
            'average_rating': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating'),# ...
            'length_seconds': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds', func=int),# ...
            'thumbnails': \
            [
                {
                    'height': ytm_utils.get_nested(thumbnail, 'height'),
                    'width': ytm_utils.get_nested(thumbnail, 'width'),
                    'url': ytm_utils.get_nested(thumbnail, 'url'),
                }
                for thumbnail in ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', default = [])
            ],
            'video_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'videoId'),# ...
            'date': \
            {
                'short': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'publishDate'),# ...
                # 'upload_date': ytm_utils.get_nested(data, 'player_response', 'microformat', 'playerMicroformatRenderer', 'uploadDate'),# ...
                'long': ytm_utils.get_nested(data, 'watch_next_response', 'contents', 'twoColumnWatchNextResults', 'results', 'results', 'contents', 0, 'videoPrimaryInfoRenderer', 'dateText', 'simpleText'),
            },
        }

        from pprint import pprint
        pprint(scraped)

        # scraped['_x'] = data['watch_next_response']

        # return scraped
        return data

        scraped = \
        {
            'api': \
            {
                'key':  ytm_utils.get_nested(data, 'innertube_api_key'),
                'version': ytm_utils.get_nested(data, 'innertube_api_version'),
            },
            'client': \
            {
                'name':  ytm_utils.get_nested(data, 'c'),
                'version': ytm_utils.get_nested(data, 'cver'),
            },
            'config': \
            {
                'region': ytm_utils.get_nested(data, 'cr'),
                'playback_token': ytm_utils.get_nested(data, 'account_playback_token'),
                'language': ytm_utils.get_nested(data, 'hl'),
                # 'page_type': ytm_utils.get_nested(data, 'csi_page_type'),
                # 'format': ytm_utils.parse_format_list(ytm_utils.get_nested(data, 'fmt_list')),
            },
            'expires_in_seconds': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'expiresInSeconds'),
            'family_safe': ytm_utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'familySafe'),
            'category': ytm_utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'category'),
            'thumbnail': ytm_utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'thumbnail', 'thumbnails', -1),
            'title': ytm_utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'title'),
            'publish_date': ytm_utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'publishDate'),
            'stream': \
            {
                'approx_duration_ms': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'approxDurationMs'),
                'audio_channels': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'audioChannels'),
                'audio_quality': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'audioQuality'),
                'audio_sample_rate': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'audioSampleRate'),
                'average_bitrate': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'averageBitrate'),
                'bitrate': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'bitrate'),
                'cipher': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'cipher'),
                'content_length': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'contentLength'),
                'height': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'height'),
                'itag': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'itag'),
                'last_modified': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'lastModified'),
                'mime_type': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'mimeType'),
                'projection_type': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'projectionType'),
                'quality': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'quality'),
                'quality_label': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'qualityLabel'),
                'width': ytm_utils.get_nested(data, 'player_response', 'streamingData', 'formats', 0, 'width'),

                # 'itag': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 'itag'),
                # 'quality': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 'quality'),
                's': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 's'),
                'sp': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 'sp'),
                # 'type': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 'type'),
                'url': ytm_utils.get_nested(data, 'fmt_stream_map', 0, 'url'),
            },
            'streams': \
            [
                {
                    'approx_duration_ms': ytm_utils.get_nested(adaptive_format, 'approxDurationMs'),
                    'audio_channels': ytm_utils.get_nested(adaptive_format, 'audioChannels'),
                    'audio_quality': ytm_utils.get_nested(adaptive_format, 'audioQuality'),
                    'audio_sample_rate': ytm_utils.get_nested(adaptive_format, 'audioSampleRate'),
                    'average_bitrate': ytm_utils.get_nested(adaptive_format, 'averageBitrate'),
                    'bitrate': ytm_utils.get_nested(adaptive_format, 'bitrate'),
                    #'cipher': ytm_utils.get_nested(adaptive_format, 'cipher'),
                    'content_length': ytm_utils.get_nested(adaptive_format, 'contentLength'),
                    'index_range': \
                    {
                        'end': ytm_utils.get_nested(adaptive_format, 'initRange', 'end'),
                        'start': ytm_utils.get_nested(adaptive_format, 'initRange', 'start'),
                    },
                    'init_range': \
                    {
                        'end': ytm_utils.get_nested(adaptive_format, 'indexRange', 'end'),
                        'start': ytm_utils.get_nested(adaptive_format, 'indexRange', 'start'),
                    },
                    'itag': ytm_utils.get_nested(adaptive_format, 'itag'),
                    'last_modified': ytm_utils.get_nested(adaptive_format, 'lastModified'),
                    'mime_type': ytm_utils.get_nested(adaptive_format, 'mimeType'),
                    'projection_type': ytm_utils.get_nested(adaptive_format, 'projectionType'),
                    'quality': ytm_utils.get_nested(adaptive_format, 'quality'),

                    #'bitrate': ytm_utils.get_nested(stream, 'bitrate'),
                    #'clen': ytm_utils.get_nested(stream, 'clen'),
                    'eotf': ytm_utils.get_nested(stream, 'eotf'),
                    'fps': ytm_utils.get_nested(stream, 'fps'),
                    #'index': ytm_utils.get_nested(stream, 'index'),
                    #'init': ytm_utils.get_nested(stream, 'init'),
                    #'itag': ytm_utils.get_nested(stream, 'itag'),
                    #'lmt': ytm_utils.get_nested(stream, 'lmt'),
                    'primaries': ytm_utils.get_nested(stream, 'primaries'),
                    'projection_type_int': ytm_utils.get_nested(stream, 'projection_type'),
                    'quality_label': ytm_utils.get_nested(stream, 'quality_label'),
                    's': ytm_utils.get_nested(stream, 's'),
                    'size': ytm_utils.get_nested(stream, 'size'),
                    'sp': ytm_utils.get_nested(stream, 'sp'),
                    #'type': ytm_utils.get_nested(stream, 'type'),
                    'url': ytm_utils.get_nested(stream, 'url'),
                }
                for adaptive_format, stream in zip \
                (
                    ytm_utils.get_nested(data, 'player_response', 'streamingData', 'adaptiveFormats', default=[]),
                    ytm_utils.get_nested(data, 'adaptive_fmts', default=[]),
                )
            ],
            'video_details': \
            {
                'author': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'author'),
                'average_rating': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating'),
                'channel_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'channelId'),
                # 'is_crawlable': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isCrawlable'),
                # 'is_live_content': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isLiveContent'),
                # 'is_low_latency_live_stream': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isLowLatencyLiveStream'),
                # 'is_owner_viewing': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isOwnerViewing'),
                # 'is_private': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isPrivate'),
                # 'is_unplugged_corpus': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'isUnpluggedCorpus'),
                'keywords': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'keywords'),
                #'latency_class': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'latencyClass'),
                'duration': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds'),
                'music_video_type': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'musicVideoType'),
                'description': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'shortDescription'),
                #'thumbnail': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', -1),
                'title': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'title'),
                'video_id': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'videoId'),
                'views': ytm_utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount'),
            },
            # 'format_stream': \
            # {
            #     'itag': utils.get_nested(data, 'fmt_stream_map', 0, 'itag'),
            #     'quality': utils.get_nested(data, 'fmt_stream_map', 0, 'quality'),
            #     's': utils.get_nested(data, 'fmt_stream_map', 0, 's'),
            #     'sp': utils.get_nested(data, 'fmt_stream_map', 0, 'sp'),
            #     'type': utils.get_nested(data, 'fmt_stream_map', 0, 'type'),
            #     'url': utils.get_nested(data, 'fmt_stream_map', 0, 'url'),
            # },
            # 'streams': \
            # [
            #     {
            #         'bitrate': utils.get_nested(stream, 'bitrate'),
            #         'clen': utils.get_nested(stream, 'clen'),
            #         'eotf': utils.get_nested(stream, 'eotf'),
            #         'fps': utils.get_nested(stream, 'fps'),
            #         'index': utils.get_nested(stream, 'index'),
            #         'init': utils.get_nested(stream, 'init'),
            #         'itag': utils.get_nested(stream, 'itag'),
            #         'lmt': utils.get_nested(stream, 'lmt'),
            #         'primaries': utils.get_nested(stream, 'primaries'),
            #         'projection_type': utils.get_nested(stream, 'projection_type'),
            #         'quality_label': utils.get_nested(stream, 'quality_label'),
            #         's': utils.get_nested(stream, 's'),
            #         'size': utils.get_nested(stream, 'size'),
            #         'sp': utils.get_nested(stream, 'sp'),
            #         'type': utils.get_nested(stream, 'type'),
            #         'url': utils.get_nested(stream, 'url'),
            #     }
            #     for stream in utils.get_nested(data, 'adaptive_fmts', default=[])
            # ],

            # 'annotations': utils.get_nested(data, 'player_response', 'annotations', 0, 'playerAnnotationsUrlsRenderer', 'invideoUrl'),
            # 'captions': \
            # [
            #     {
            #         'url': utils.get_nested(captions, 'baseUrl'),
            #         'is_translatable': utils.get_nested(captions, 'isTranslatable'),
            #         'language_code': utils.get_nested(captions, 'languageCode'),
            #         'name': utils.get_nested(captions, 'name', 'runs', 0, 'text'),
            #         'vss_id': utils.get_nested(captions, 'vssId'),
            #     }
            #     for captions in utils.get_nested(data, 'player_response', 'captions', 'playerCaptionsTracklistRenderer', 'captionTracks', default=[])
            # ],

            #'description': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'description'),
            # 'og_type': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'ogType'),
            # 'page_owner_details': \
            # {
            #     'external_channel_id': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'externalChannelId'),
            #     'name': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'name'),
            # },
            #'tags': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'tags'),
            # 'video_details': \
            # {
            #     'duration_iso_8601': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'durationIso8601'),
            #     'duration_seconds': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'durationSeconds'),
            #     'external_video_id': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'externalVideoId'),
            # },
            #'view_count': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'viewCount'),



            # 'fflags': utils.get_nested(data, 'fflags'),
            # 'api_key': utils.get_nested(data, 'innertube_api_key'),
            #'client_name': utils.get_nested(data, 'c'),
            #'region': utils.get_nested(data, 'cr'),
            #'playback_token': utils.get_nested(data, 'account_playback_token'),
            # 'browser_name': utils.get_nested(data, 'cbr'),
            # 'browser_version': utils.get_nested(data, 'cbrver'),
            # 'api_version': utils.get_nested(data, 'innertube_api_version'),
            #'client_version': utils.get_nested(data, 'cver'),
            #'language': utils.get_nested(data, 'hl'),
            #'page_type': utils.get_nested(data, 'csi_page_type'),
            # 'status': utils.get_nested(data, 'status'),
            # 'os_version': utils.get_nested(data, 'cosver'),
            # 'os_name': utils.get_nested(data, 'cos'),
            # 'timestamp': utils.get_nested(data, 'timestamp'),
            # 'vss_host': utils.get_nested(data, 'vss_host'),
            # 'experiment_flags': utils.get_nested(data, 'fexp'),
            # 'watermarks': utils.get_nested(data, 'watermarks'),
            #'format': utils.parse_format_list(utils.get_nested(data, 'fmt_list')),
            #'format_stream': utils.get_nested(data, 'fmt_stream_map', 0),
            #'streams': utils.get_nested(data, 'adaptive_fmts'),

            # 'player_response': \
            # {
            #     'live_stream': \
            #     {
            #         'display_endscreen': utils.get_nested(data, 'player_response', 'playabilityStatus', 'liveStreamability', 'liveStreamabilityRenderer', 'displayEndscreen'),
            #         'poll_delay': utils.get_nested(data, 'player_response', 'playabilityStatus', 'liveStreamability', 'liveStreamabilityRenderer', 'pollDelayMs'),
            #         'video_id': utils.get_nested(data, 'player_response', 'playabilityStatus', 'liveStreamability', 'liveStreamabilityRenderer', 'videoId'),
            #     },
            #     'playable_in_embed': utils.get_nested(data, 'player_response', 'playabilityStatus', 'playableInEmbed'),
            #     'playability_status': utils.get_nested(data, 'player_response', 'playabilityStatus', 'status'),
            #     'formats': utils.get_nested(data, 'player_response', 'streamingData', 'formats'),
            #     'adaptive_formats': utils.get_nested(data, 'player_response', 'streamingData', 'adaptiveFormats'), # These (^) need to be parsed
            #     'expires_in_seconds': utils.get_nested(data, 'player_response', 'streamingData', 'expiresInSeconds'),
            #     'captions': \
            #     [
            #         {
            #             'url': utils.get_nested(captions, 'baseUrl'),
            #             'is_translatable': utils.get_nested(captions, 'isTranslatable'),
            #             'language_code': utils.get_nested(captions, 'languageCode'),
            #             'name': utils.get_nested(captions, 'name', 'runs', 0, 'text'),
            #             'vss_id': utils.get_nested(captions, 'vssId'),
            #         }
            #         for captions in utils.get_nested(data, 'player_response', 'captions', 'playerCaptionsTracklistRenderer', 'captionTracks', default=[])
            #     ],
            #     'video_details': \
            #     {
            #         'allow_ratings': utils.get_nested(data, 'player_response', 'videoDetails', 'allowRatings'),
            #         'author': utils.get_nested(data, 'player_response', 'videoDetails', 'author'),
            #         'average_rating': utils.get_nested(data, 'player_response', 'videoDetails', 'averageRating'),
            #         'channel_id': utils.get_nested(data, 'player_response', 'videoDetails', 'channelId'),
            #         'is_crawlable': utils.get_nested(data, 'player_response', 'videoDetails', 'isCrawlable'),
            #         'is_live_content': utils.get_nested(data, 'player_response', 'videoDetails', 'isLiveContent'),
            #         'is_low_latency_live_stream': utils.get_nested(data, 'player_response', 'videoDetails', 'isLowLatencyLiveStream'),
            #         'is_owner_viewing': utils.get_nested(data, 'player_response', 'videoDetails', 'isOwnerViewing'),
            #         'is_private': utils.get_nested(data, 'player_response', 'videoDetails', 'isPrivate'),
            #         'is_unplugged_corpus': utils.get_nested(data, 'player_response', 'videoDetails', 'isUnpluggedCorpus'),
            #         'keywords': utils.get_nested(data, 'player_response', 'videoDetails', 'keywords'),
            #         'latency_class': utils.get_nested(data, 'player_response', 'videoDetails', 'latencyClass'),
            #         'duration': utils.get_nested(data, 'player_response', 'videoDetails', 'lengthSeconds'),
            #         'music_video_type': utils.get_nested(data, 'player_response', 'videoDetails', 'musicVideoType'),
            #         'short_description': utils.get_nested(data, 'player_response', 'videoDetails', 'shortDescription'),
            #         'thumbnail': utils.get_nested(data, 'player_response', 'videoDetails', 'thumbnail', 'thumbnails', -1),
            #         'title': utils.get_nested(data, 'player_response', 'videoDetails', 'title'),
            #         'video_id': utils.get_nested(data, 'player_response', 'videoDetails', 'videoId'),
            #         'views': utils.get_nested(data, 'player_response', 'videoDetails', 'viewCount'),
            #     },
            #     'annotations': utils.get_nested(data, 'player_response', 'annotations', 0, 'playerAnnotationsUrlsRenderer', 'invideoUrl'),
            #     'player_config': \
            #     {
            #         'audio': \
            #         {
            #             'enable_per_format_loudness':  utils.get_nested(data, 'player_response', 'playerConfig', 'audioConfig', 'enablePerFormatLoudness'),
            #             'loudness_db':  utils.get_nested(data, 'player_response', 'playerConfig', 'audioConfig', 'loudnessDb'),
            #             'perceptual_loudness_db':  utils.get_nested(data, 'player_response', 'playerConfig', 'audioConfig', 'perceptualLoudnessDb'),
            #         },
            #         'media': \
            #         {
            #             'max_read_ahead_media_time_ms':  utils.get_nested(data, 'player_response', 'playerConfig', 'mediaCommonConfig', 'dynamicReadaheadConfig', 'maxReadAheadMediaTimeMs'),
            #             'min_read_ahead_media_time_ms':  utils.get_nested(data, 'player_response', 'playerConfig', 'mediaCommonConfig', 'dynamicReadaheadConfig', 'minReadAheadMediaTimeMs'),
            #             'read_ahead_growth_rate_ms':  utils.get_nested(data, 'player_response', 'playerConfig', 'mediaCommonConfig', 'dynamicReadaheadConfig', 'readAheadGrowthRateMs'),
            #         },
            #         'stream': \
            #         {
            #             'max_bitrate':  utils.get_nested(data, 'player_response', 'playerConfig', 'streamSelectionConfig', 'maxBitrate'),
            #         },
            #     },
            #     'storyboards_spec': utils.get_nested(data, 'player_response', 'storyboards', 'playerStoryboardSpecRenderer', 'spec'),
            #     'microformat': \
            #     {
            #         'android_package': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'androidPackage'),
            #         'app_name': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'appName'),
            #         'available_countries': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'availableCountries'),
            #         'category': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'category'),
            #         'description': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'description'),
            #         'family_safe': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'familySafe'),
            #         'ios_app_arguments': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'iosAppArguments'),
            #         'ios_app_store_id': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'iosAppStoreId'),
            #         'alternative_links': \
            #         [
            #             {
            #                 'type': utils.get_nested(link, 'alternateType'),
            #                 'url': utils.get_nested(link, 'hrefUrl'),
            #                 'title': utils.get_nested(link, 'title'),
            #             }
            #             for link in utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'linkAlternates', default=[])
            #         ],
            #         'noindex': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'noindex'),
            #         'og_type': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'ogType'),
            #         'page_owner_details': \
            #         {
            #             'external_channel_id': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'externalChannelId'),
            #             'name': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'name'),
            #             'url_google_plus_profile': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'urlGooglePlusProfile'),
            #             'youtube_profile_url': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'pageOwnerDetails', 'youtubeProfileUrl'),
            #         },
            #         'paid': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'paid'),
            #         'publish_date': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'publishDate'),
            #         'schema_dot_org_type': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'schemaDotOrgType'),
            #         'site_name': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'siteName'),
            #         'tags': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'tags'),
            #         'thumbnail': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'thumbnail', 'thumbnails', -1),
            #         'title': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'title'),
            #         'twitter_card_type': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'twitterCardType'),
            #         'twitter_site_handle': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'twitterSiteHandle'),
            #         'unlisted': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'unlisted'),
            #         'upload_date': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'uploadDate'),
            #         'url_applinks_android': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'urlApplinksAndroid'),
            #         'url_applinks_ios': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'urlApplinksIos'),
            #         'url_canonical': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'urlCanonical'),
            #         'url_twitter_android': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'urlTwitterAndroid'),
            #         'url_twitter_ios': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'urlTwitterIos'),
            #         'video_details': \
            #         {
            #             'duration_iso_8601': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'durationIso8601'),
            #             'duration_seconds': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'durationSeconds'),
            #             'external_video_id': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'videoDetails', 'externalVideoId'),
            #         },
            #         'view_count': utils.get_nested(data, 'player_response', 'microformat', 'microformatDataRenderer', 'viewCount'),
            #     },
            #     'tracking_params': utils.get_nested(data, 'player_response', 'trackingParams'),
            #     'attestation': \
            #     {
            #         'bot_guard': \
            #         {
            #             'interpreter_url': utils.get_nested(data, 'player_response', 'attestation', 'playerAttestationRenderer', 'botguardData', 'interpreterUrl'),
            #             'program': utils.get_nested(data, 'player_response', 'attestation', 'playerAttestationRenderer', 'botguardData', 'program'),
            #         },
            #         'challenge': utils.get_nested(data, 'player_response', 'attestation', 'playerAttestationRenderer', 'challenge'),
            #     },
            #     'ad_placements': \
            #     [
            #         {
            #             'config': \
            #             {
            #                 'time_offset': \
            #                 {
            #                     'offset_end_milliseconds': utils.get_nested(ad_placement, 'adPlacementRenderer', 'config', 'adPlacementConfig', 'adTimeOffset', 'offsetEndMilliseconds'),
            #                     'offset_start_milliseconds': utils.get_nested(ad_placement, 'adPlacementRenderer', 'config', 'adPlacementConfig', 'adTimeOffset', 'offsetStartMilliseconds'),
            #                 },
            #                 'hide_cue_range_marker': utils.get_nested(ad_placement, 'adPlacementRenderer', 'config', 'adPlacementConfig', 'hideCueRangeMarker'),
            #                 'kind': utils.get_nested(ad_placement, 'adPlacementRenderer', 'config', 'adPlacementConfig', 'kind'),
            #             },
            #             'ad_break_url': utils.get_nested(ad_placement, 'adPlacementRenderer', 'renderer', 'adBreakServiceRenderer', 'getAdBreakUrl'),
            #             'prefetch_milliseconds': utils.get_nested(ad_placement, 'adPlacementRenderer', 'renderer', 'adBreakServiceRenderer', 'prefetchMilliseconds'),
            #             'tracking_params': utils.get_nested(ad_placement, 'adPlacementRenderer', 'trackingParams'),
            #         }
            #         for ad_placement in utils.get_nested(data, 'player_response', 'adPlacements', default=[])
            #     ],
            #     'ad_safety_readon': \
            #     {
            #         'is_foc_enabled': utils.get_nested(data, 'player_response', 'adSafetyReason', 'isFocEnabled'),
            #         'is_remarketing_enabled': utils.get_nested(data, 'player_response', 'adSafetyReason', 'isRemarketingEnabled'),
            #     },
            # },
        }

        return scraped

    def search_suggestions(self, query):
        data = self.base.search_suggestions \
        (
            query = query
        )

        suggestions = \
        [
            ''.join \
            (
                run['text']
                for run in ytm_utils.get_nested \
                (
                    item,
                    'searchSuggestionRenderer',
                    'suggestion',
                    'runs',
                )
            )
            for item in ytm_utils.get_nested \
            (
                data,
                'contents',
                0,
                'searchSuggestionsSectionRenderer',
                'contents',
                default = [],
            )
        ]

        return suggestions

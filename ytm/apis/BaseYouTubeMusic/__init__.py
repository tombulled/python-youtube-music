''' xxx '''

from ...utils import _import

import requests

from ... import constants as ytm_constants
from ... import utils     as ytm_utils

_import(locals())

class BaseYouTubeMusic(object):
    def __init__(self):
        methods = \
        (
        _get_page,
        _url_api,
        _url_yt,
        _url,
        browse_album,
        browse_artist,
        browse_home,
        browse_hotlist,
        browse_playlist,
        browse,
        guide,
        next,
        page_channel,
        page_home,
        page_hotlist,
        page_playlist,
        page_search,
        page_watch,
        search_suggestions,
        video_info,
        )

        for method in methods:
            setattr(self.__class__, method.__name__.split('.')[-1], method)

        self.session = requests.Session()

        self.domain       = ytm_constants.DOMAIN_YOUTUBE_MUSIC
        self.protocol     = ytm_constants.PROTOCOL_HTTPS
        self.api_endpoint = ytm_constants.ENDPOINT_YTM_API

        self.session.headers.update \
        (
            {
                'User-Agent'       : ytm_utils.random_user_agent(),
                'X-Goog-Visitor-Id': ytm_constants.HEADER_VISITOR_ID,
                'Referer'          : self._url(),
            }
        )


    def __repr__(self):
        representation = '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

        return representation

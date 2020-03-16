from ... import utils as ytm_utils
from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def _url_api(self, endpoint=None):
    return ytm_utils.url_youtube_music \
    (
        endpoint = ytm_constants.ENDPOINT_YTM_API + (endpoint or ''),
    )

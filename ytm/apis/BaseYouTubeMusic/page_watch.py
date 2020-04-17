from ... import constants as ytm_constants
from . import utils

__all__ = __name__.split('.')[-1:]

def page_watch(self, v, list=None):
    return self._get_page \
    (
        endpoint = ytm_constants.ENDPOINT_YTM_WATCH,
        params = utils.filter_dict \
        (
            {
                'v': v,
                'list': list,
            }
        ),
    )

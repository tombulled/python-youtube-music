from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def page_search(self, q):
    return self._get_page \
    (
        endpoint = ytm_constants.ENDPOINT_YTM_SEARCH,
        params = \
        {
            'q': q,
        },
    )

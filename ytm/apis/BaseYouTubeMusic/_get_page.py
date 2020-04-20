'''
'''

import re
import json
from . import utils
from . import constants
from . import exceptions
from . import decorators

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

@decorators.catch
def _get_page(self: object, endpoint: str, params: dict=None) -> dict:
    '''
    Return a page's configuration data.

    Fetches the page at https://music.youtube.com/{endpoint} and
    extracts the configuration dictionary

    Parameters:
        self:
            <BaseYouTubeMusic> class instance
        endpoint:
            Page endpoint
            E.g. 'hotlist', 'playlist'
        params:
            Params to be used for the GET request
            E.g. {'q': 'search query'}

    Returns:
        dict:
            Page configuration dictionary

    Example:
        >>> api = ytm.BaseYouTubeMusic()
        >>>
        >>> data = api._get_page \
        (
            endpoint = 'search',
            params   = {'q': 'foo fighters'},
        )
        >>>
        >>> data.get('YTFE_BUILD_TIMESTAMP')
        'Thu Apr 16 21:13:20 2020 (1587096800)'
        >>>

    Raises:
        InvalidPageConfigurationError:
            Page has no configuration data
        PageNotFoundError:
            Page not found
    '''

    endpoint = endpoint.strip().lower()

    url = self._url(endpoint)

    resp = self.session.get \
    (
        url    = url,
        params = params,
    )

    config_match = re.search \
    (
        pattern = r'ytcfg\.set\((?P<data>.*)\);',
        string  = resp.text,
    )

    if config_match is None:
        raise exceptions.InvalidPageConfigurationError \
        (
            'Page has no configuration data',
        )

    config_data = config_match.group('data')
    config      = json.loads(config_data)

    for key, val in config.items():
        if isinstance(val, str):
            val = val.strip()

            json_match = re.match \
            (
                pattern = r'\{(.*)\}',
                string  = val,
            )

            if json_match is not None:
                config[key] = json.loads(val)

    initial_browse_id = utils.get_nested \
    (
        config,
        'INITIAL_ENDPOINT',
        'browseEndpoint',
        'browseId',
    )

    if endpoint and initial_browse_id == constants.BROWSE_ID_HOME:
        raise exceptions.PageNotFoundError \
        (
            'Page not found',
        )

    return config

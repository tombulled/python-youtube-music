'''
'''

import re
import json

__method__ = __name__.split('.')[-1]
__all__    = (__method__,)

def _get_page(self: object, endpoint: str, *args, **kwargs) -> dict:
    '''
    '''

    url = self._url(endpoint)

    resp = self.session.get(url, *args, **kwargs)

    config_match = re.search(r'ytcfg\.set\((?P<data>.*)\);', resp.text)

    if config_match is None:
        config = {}
    else:
        config_data = config_match.group('data')
        config      = json.loads(config_data)

    for key, val in config.items():
        if isinstance(val, str):
            val = val.strip()

            if re.match(r'\{(.*)\}', val) is not None:
                config[key] = json.loads(val)

    return config

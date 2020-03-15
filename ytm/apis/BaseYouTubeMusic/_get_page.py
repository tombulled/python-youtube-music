import re
import json

__all__ = __name__.split('.')[-1:]

def _get_page(self, endpoint, *args, **kwargs):
    url = self._url(endpoint)

    resp = self.session.get(url, *args, **kwargs)

    config_data = re.search(r'ytcfg\.set\((?P<data>.*)\);', resp.text)

    if config_data is None: return

    config_data = config_data.group('data')

    config = json.loads(config_data)

    for key, val in config.items():
        if isinstance(val, str) and val.startswith('{'):
            config[key] = json.loads(val)

    return config

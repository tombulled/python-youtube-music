from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def next(self, update=True):
    if not self._continuation: return # raise

    data = self.api.base.browse \
    (
        continuation = self._continuation,
    )

    parsed_data = self._parse(data)

    if update:
        self['tracks'].extend(parsed_data['tracks'])

    return parsed_data

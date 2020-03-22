from ..... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def next(self):
    if not self._continuation: return # raise

    data = self.api.base.search \
    (
        continuation = self._continuation,
    )

    parsed_data = self._parse(data)

    continuation = ytm_utils.get_nested(parsed_data, 'continuation')
    items = ytm_utils.get_nested(parsed_data, 'items', default=[])

    # parsed_data.pop('continuation')

    # if update:
    self._continuation = continuation
    self.extend(items)

    # set continuation
    # return items

    # if update:
    #     self.extend(parsed_data['items'])

        # self['']

    return items

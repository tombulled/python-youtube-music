# from ..... import utils as ytm_utils
# from ... import containers

__all__ = __name__.split('.')[-1:]

def next(self):
    browse_id = self['browse_id']
    params = self['params']

    if not all((browse_id, params)):
        return # raise

    data = self.api.base.browse \
    (
        browse_id = browse_id,
        params = params,
    )

    parsed_data = self._parse(data)

    # get new bits to return, update class

    return parsed_data

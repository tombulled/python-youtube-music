from ._search import _search as parse_search
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def search(data: dict):
    parsed = parse_search(data)

    for shelf_name, shelf in parsed.items():
        if 'items' in shelf:
            parsed[shelf_name] = shelf.get('items')

    return parsed

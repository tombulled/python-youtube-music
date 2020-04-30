'''
Module containing the utility function: get
'''

from typing import Any, Callable, Iterable

def get \
        (
            iterable: Iterable,
            *keys:    Any,
            default:  Any      = None,
            func:     Callable = None,
        ) -> Any:
    '''
    Get a value from a multi-dimensional iterable.

    Get a value by specifying all of the keys needed to extract it

    Args:
        iterable: An iterable to retrieve a value from
            Example: ['a', ['b']]
        keys: The keys or indexes needed to access the desired item
            Example: [1, 0] or ['a', 'b', 0]
        default: The value to return if the item doesn't exist
            at the specified location
            Example: 'Default Value'
        func: Function to clean the retrieved item if it existed
            Example: int

    Returns:
        The retrieved item, parsed using func, or the default value

    Example:
        Item exists, no parsing:
            >>> data = ['Nope', ['Nope', {'key': 'Yes!'}]]
            >>> ytm.utils.get(data, 1, 1, 'key')
            'Yes!'
            >>>
        Item exists, parsing:
            >>> data = ['Nope', ['Nope', {'key': 'Yes!'}]]
            >>> ytm.utils.get(data, 1, 1, 'key', func = lambda item: item + ' :)')
            'Yes! :)'
            >>>
        Item doesn't exist:
            >>> data = ['Nope', ['Nope', {'key': 'Yes!'}]]
            >>> ytm.utils.get(data, 1, 1, 'invalid_key', default = 'Not there :(')
            'Not there :('
            >>>
    '''

    if not isinstance(iterable, Iterable) \
            or not iterable \
            or not keys:
        return default

    item = iterable

    for key in keys:
        if not isinstance(item, dict):
            if isinstance(key, int) and key < 0:
                key += len(item)

            item = dict(enumerate(item))

        if key not in item:
            return default

        item = item[key]

    if func:
        try:
            item = func(item)
        except:
            item = default

    return item

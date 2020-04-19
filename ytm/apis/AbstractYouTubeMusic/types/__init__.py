'''
'''

import re
from .. import exceptions
import types

def new_id(name, patterns=None):
    def __init__(self, id: str):
        id.__init__(self)

        if not patterns:
            return

        for pattern in patterns:
            match = re.match \
            (
                pattern = pattern,
                string  = self,
                flags   = re.DOTALL,
            )

            if match is not None:
                break
        else:
            raise exceptions.InvalidIdError \
            (
                'Invalid {class_name}: {value}'.format \
                (
                    class_name = self.__class__.__name__,
                    value      = str.__repr__(self),
                )
            )

    def __repr__(self):
        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value = str.__repr__(self),
        )

    methods = \
    (
        __init__,
        __repr__,
    )

    def construct(namespace):
        for method in methods:
            namespace[method.__name__] = method

        namespace['__module__'] = __builtins__['__name__']

    class_ = types.new_class \
    (
        name  = name,
        bases = (str,),
        exec_body = construct,
    )

    return class_

def isinstance(object, class_):
    try:
        class_(str(object))

        return True
    except:
        raise
        return False

custom_types  = \
(
    {
        'name': 'BrowseId',
        'patterns': \
        (
            r'^[a-zA-Z0-9_-]+$',
        ),
    },
    {
        'name': 'AlbumId',
        'patterns': \
        (
            r'^OLAK5uy_[a-zA-Z0-9_-]{33}$',
            r'^MPREb_[a-zA-Z0-9_-]{11}$',
        ),
    },
    {
        'name': 'AlbumPlaylistId',
        'patterns': \
        (
            r'^OLAK5uy_[a-zA-Z0-9_-]{33}$',
        ),
    },
    {
        'name': 'AlbumBrowseId',
        'patterns': \
        (
            r'^MPREb_[a-zA-Z0-9_-]{11}$',
        ),
    },
    {
        'name': 'ArtistId',
        'patterns': \
        (
            r'^UC[a-zA-Z0-9_-]{22}$',
        ),
    },
)

__all__ = \
[
    'isinstance',
]

for custom_type in custom_types:
    type = new_id(**custom_type)

    locals()[type.__name__] = type

    __all__.append(type.__name__)

'''
'''

import re
from .. import exceptions
import types
import builtins

def new_id(name, patterns=None):
    def __init__(self, id: str):
        id.__init__(self)

        if not patterns:
            return

        for pattern in patterns:
            # print(pattern, str(self))
            match = re.match \
            (
                pattern = pattern,
                string  = str(self),
                flags   = re.DOTALL,
            )

            # print(match)

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

        namespace['__module__'] = builtins.__name__

    class_ = types.new_class \
    (
        name  = name,
        bases = (str,),
        exec_body = construct,
    )

    return class_

def isinstance(object, class_):
    custom_type_names = [custom_type['name'] for custom_type in custom_types]

    class_name = getattr(class_, '__name__', None) \
        or getattr(class_.__class__, '__name__')

    # print(class_name, custom_type_names)

    if class_name in custom_type_names:
        try:
            class_(str(object))

            # print('Created:', class_, 'with', str(object))

            return True
        except:
            return False
    else:
        # return builtins.isinstance(object, class_)
        # print(object) #, type(object))
        # print(class_, type(class_))
        # print(class_, class_.__mro__)
        # object_name = getattr(object, '__name__', None) \
        #     or getattr(object.__class__, '__name__')
        # print(object.__mro__)
        mro = getattr(object, '__mro__', None) \
            or getattr(object.__class__, '__mro__')
        # print(object, mro)
        # print(object_name, [resolution.__name__ for resolution in class_.__mro__] + [class_.__name__])
        # print(object, type(object), class_.__mro__, [resolution.__name__ for resolution in class_.__mro__] + [class_.__name__])
        # return type(object) in [resolution.__name__ for resolution in class_.__mro__] + [class_.__name__]
        return class_ in mro

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
        'name': 'Continuation',
        'patterns': \
        (
            r'^[a-zA-Z0-9_%-]+$',
        ),
    },
    {
        'name': 'Params',
        'patterns': \
        (
            r'^[a-zA-Z0-9_%-]+$',
        ),
    },
    {
        'name': 'HomeContinuation',
        'patterns': \
        (
            (
                r'^'
                r'4qmFsg'
                r'KM'
                r'ARIMRkVtdXNpY19ob21lG'
                r'nxDQU42VkVOcVFVRkJSMVoxUVVGR1NGRm5RVUpTTUVsQlFWRkNSMUpYTVRGak'
                r'1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUpCUVVWQlFVRkZRa0pCUjFSMV'
                r'[a-zA-Z0-9_%-]{4}'
                r'JRVUp'
                r'[a-zA-Z0-9_%-]{15}'
                r'p2UVdwSlFRJTNEJTNE'
                r'$'
            ),
            (
                r'^'
                r'4qmFsg'
                r'Lb'
                r'ARIMRkVtdXNpY19ob21lG'
                r'soBQ0F'
                r'[a-zA-Z0-9_-]{1}'
                r'NmtBRkRha0ZCUVVkV2RVRkJSa2hSWjBGQ1VqQkpRVUZSUWtkU1Z6RX'
                r'hZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQ1FVRkZRVUZCUlVKQ1FVZFVk'
                r'[a-zA-Z0-9_-]{4}'
                r'VVV'
                r'[a-zA-Z0-9_-]{18}'
                r'WIwRnFTWFJIYVhSVFVrVk9UVkZWY3pGa1dHeG1Z'
                r'[a-zA-Z0-9_-]{77}'
                r'SUzRA%3D%3D'
                r'$'
            ),
        ),
    },
    {
        'name': 'WatchContinuation',
        'patterns': \
        {
            (
                r'^'
                r'CBkSMRIL'
                r'[a-zA-Z0-9_-]{15}'
                r'iEVJEQU1WT'
                r'[a-zA-Z0-9_-]{15}'
                r'MgR3QUVCOBi4AQLQAQHwAQEYCg%3D%3D'
                r'$'
            ),
        },
    },
    {
        'name': 'ArtistSinglesContinuation',
        'patterns': \
        (
            (
                r'^'
                r'6gPTAUNwc0JDbndLYlFBQVpXNEFBVWRDQUFGSFFnQUJBRVpGYlhWemFXTmZaR'
                r'1YwWVdsc1gyRnlkR2x6ZEFBQkFBQUJBQUFBQVFBQkFBQUJBUW'
                r'k4'
                r'QXhvWVZVT'
                r'(?P<b64_artist_id>[a-zA-Z0-9_-]{39})'
                r'Z2dFWVZVT'
                r'(?P=b64_artist_id)'
                r'QUFFU'
                r'[a-zA-Z0-9_-]{11}'
                r'NkFJYUFuZHpHQUFxRDJGeWRHbHpkRjl5Wld4bFlYTmxjekN4MU5EbGxfSEo4'
                r'bkE%3D'
                r'$'
            ),
        ),
    },
    {
        'name': 'ArtistAlbumsContinuation',
        'patterns': \
        (
            (
                r'^'
                r'6gPTAUNwc0JDbndLYlFBQVpXNEFBVWRDQUFGSFFnQUJBRVpGYlhWemFXTmZaR'
                r'1YwWVdsc1gyRnlkR2x6ZEFBQkFBQUJBQUFBQVFBQkFBQUJBUW'
                r'lY'
                r'QXhvWVZVT'
                r'(?P<b64_artist_id>[a-zA-Z0-9_-]{39})'
                r'Z2dFWVZVT'
                r'(?P=b64_artist_id)'
                r'QUFFU'
                r'[a-zA-Z0-9_-]{11}'
                r'NkFJYUFuZHpHQUFxRDJGeWRHbHpkRjl5Wld4bFlYTmxjekN4MU5EbGxfSEo4'
                r'bkE%3D'
                r'$'
            ),
        ),
    },
    {
        'name': 'PlaylistContinuation',
        'patterns': \
        (
            (
                r'^'
                r'4qmFsgJbEi1WTFJEQ0xBSzV1eV9'
                r'[a-zA-Z0-9_-]{45}'
                r'KmVoVlFWRHBGWjN'
                r'[a-zA-Z0-9_-]{28}'
                r'TQVFNSXVnUSUzRA%3D%3D'
                r'$'
            ),
        ),
    },
    {
        'name': 'PlaylistId',
        'patterns': \
        (
            r'^(VL)?PL[a-zA-Z0-9_-]{32}$',
            r'^(VL)?RDCLAK5uy_[a-zA-Z0-9_-]{33}$',
        ),
    },
    {
        'name': 'PlaylistBrowseId',
        'patterns': \
        (
            r'^VLPL[a-zA-Z0-9_-]{32}$',
            r'^VLRDCLAK5uy_[a-zA-Z0-9_-]{33}$',
        ),
    },
    {
        'name': 'SongListId',
        'patterns': \
        (
            r'^(RDAMPL)?PL[a-zA-Z0-9_-]{32}$', # Chart or Artist Songs. RDAMPL means its a radio
            r'^(RDAMPL)?RDCLAK5uy_[a-zA-Z0-9_-]{33}$', # Playlist. RDAMPL means its a radio
            r'^(RDAMPL)?OLAK5uy_[a-zA-Z0-9_-]{33}$' # Album. RDAMPL means its a radio
            r'^RDAMVM[a-zA-Z0-9_-]{11}$', # Song radio/shuffle
            r'^RDAO[a-zA-Z0-9_-]{22}$', # Artist Shuffle
            r'^RDEM[a-zA-Z0-9_-]{22}$', # Artist Radio
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
        'name': 'SongId',
        'patterns': \
        (
            r'^[a-zA-Z0-9_-]{11}$',
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

for custom_type_spec in custom_types:
    custom_type = new_id(**custom_type_spec)

    locals()[custom_type.__name__] = custom_type

    __all__.append(custom_type.__name__)

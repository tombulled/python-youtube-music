from . import base
from . import utils

class HomeContinuation(base.BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            '4qmFsg',
            'KM',
            'ARIMRkVtdXNpY19ob21lG',
            'nxDQU42VkVOcVFVRkJSMVoxUVVGR1NGRm5RVUp',
            utils.entropy(5), # VYTNk or TTUVs ?
            'QlFWRkNSMUpYTVRGak',
            '1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUpCUVVWQlFVRkZRa0pCUjF',
            utils.entropy(7),
            'JRVUp',
            utils.entropy(17),
            'UVdwSlFRJTNEJTNE',
        ),
        # This needs more reverse engineering
        utils.pattern \
        (
            '4qmFsg',
            'KZ',
            'ARIMRkVtdXNpY19ob21lG',
            'ogBQ0FsNllrTnFRVUZCUjFaMVFVRkdTRkZuUVVKVWEzZEJRVkZDUjFKWE1URmpNbXh',
            'xV0RKb2RtSlhWVUZCVVVGQlFWRkdSRUZCUVVKQlFVVkJRVUZGUWtKQlIxUXRi',
            utils.entropy(23),
            'ad1FXcEpTME5OYmxkb1gxZDNNWEZIWjFWMw%3D%3D',
        ),
        utils.pattern \
        (
            '4qmFsg',
            'Lb',
            'ARIMRkVtdXNpY19ob21lG',
            'soBQ0F',
            utils.entropy(1),
            'NmtBRkRha0ZCUVVkV2RVRkJSa2hSWjBGQ1',
            utils.entropy(5), # VqQkp or ZHdDN ?
            'RVUZSUWtkU1Z6RX',
            'hZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQ1FVRkZRVUZCUlVKQ1FVZFV',
            utils.entropy(5),
            'VVV',
            utils.entropy(21),
            'RnFTWFJIYVhSVFVrVk9UVkZWY3pGa1dHeG1Z',
            utils.entropy(78),
            'UzRA%3D%3D',
        ),
    )

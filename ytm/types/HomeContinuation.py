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
            'nxDQU42VkVOcVFVRkJSMVoxUVVGR1NGRm5RVUpTTUVsQlFWRkNSMUpYTVRGak',
            '1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUpCUVVWQlFVRkZRa0pCUjF',
            utils.entropy(7),
            'JRVUp',
            utils.entropy(17),
            'UVdwSlFRJTNEJTNE',
        ),
        utils.pattern \
        (
            '4qmFsg',
            'Lb',
            'ARIMRkVtdXNpY19ob21lG',
            'soBQ0F',
            utils.entropy(1),
            'NmtBRkRha0ZCUVVkV2RVRkJSa2hSWjBGQ1VqQkpRVUZSUWtkU1Z6RX',
            'hZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQ1FVRkZRVUZCUlVKQ1FVZFV',
            utils.entropy(5),
            'VVV',
            utils.entropy(21),
            'RnFTWFJIYVhSVFVrVk9UVkZWY3pGa1dHeG1Z',
            utils.entropy(78),
            'UzRA%3D%3D',
        ),
    )
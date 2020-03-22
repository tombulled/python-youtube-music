''' xxx '''

from .....utils import _import
from ..... import utils as ytm_utils


_import(locals())

locals()['__all__'] = __name__.split('.')[-1:]

class SearchVideos(list):
    def __init__(self, api, data):
        methods = \
        (
            '_parse',
            'next',
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

        # self._continuation = ytm_utils.get_nested(data, 'continuation')
        self._continuation = None

        self.api = api

        super().__init__(data)

    # def __repr__(self):
    #     representation = '<{api_name}:{class_name}({data})>'.format \
    #     (
    #         api_name = self.api.__class__.__name__,
    #         class_name = self.__class__.__name__,
    #         data = self.data,
    #     )
    #
    #     return representation

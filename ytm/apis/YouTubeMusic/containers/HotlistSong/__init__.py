''' xxx '''

from .....utils import _import

_import(locals())

locals()['__all__'] = __name__.split('.')[-1:]

class HotlistSong(dict):
    def __init__(self, api, data):
        methods = \
        (
            'artist',
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

        self.api = api
        self.raw_data = data
        self.data = data

        super().__init__(self.data)

    # def __repr__(self):
    #     representation = '<{api_name}:{class_name}({data})>'.format \
    #     (
    #         api_name = self.api.__class__.__name__,
    #         class_name = self.__class__.__name__,
    #         data = self.data,
    #     )
    #
    #     return representation

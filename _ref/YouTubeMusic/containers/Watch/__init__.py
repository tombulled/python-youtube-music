''' xxx '''

from .....utils import _import

_import(locals())

locals()['__all__'] = __name__.split('.')[-1:]

class Watch(dict):
    def __init__(self, api, data):
        methods = \
        (
            '_parse',
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

        self.api = api
        # self.raw_data = data
        # self.data = self._parse()
        parsed_data = self._parse(data)

        # super().__init__(self.data)
        super().__init__(parsed_data)

    # def __repr__(self):
    #     representation = '<{api_name}:{class_name}({data})>'.format \
    #     (
    #         api_name = self.api.__class__.__name__,
    #         class_name = self.__class__.__name__,
    #         data = self.data,
    #     )
    #
    #     return representation

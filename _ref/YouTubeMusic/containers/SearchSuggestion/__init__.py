''' xxx '''

from .....utils import _import

_import(locals())

locals()['__all__'] = __name__.split('.')[-1:]

# def search_suggestion(api, data):
#     obj = SearchSuggestion()
#
#     obj.api = api
#     obj.raw_data = data
#     obj.data =

class SearchSuggestion(str):
    # def __init__(self, api, data):
    def __init__(self, data):
        # print('SearchSuggestion:', api, repr(data))
        methods = \
        (
            'search',
            'search_suggestions',
        )

        for method in methods:
            setattr(self.__class__, method, globals()[method])

        # self.api = api
        # self.raw_data = data
        # self.data = data
        #
        # print(self.raw_data, self.data)
        #
        # super().__init__(*args, **kwargs)
        data.__init__(self)

    # def __repr__(self):
    #     representation = '<{api_name}:{class_name}({data})>'.format \
    #     (
    #         api_name = self.api.__class__.__name__,
    #         class_name = self.__class__.__name__,
    #         data = repr(self.data),
    #     )
    #
    #     return representation

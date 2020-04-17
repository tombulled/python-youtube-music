__all__ = __name__.split('.')[-1:]

__filter__ = __name__.split('.')[-2].split('_', 1)[-1]

def method(self, query):
    return self.__search_filter(query, __filter__)

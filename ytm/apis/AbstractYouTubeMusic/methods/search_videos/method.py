from ... import decorators

__function__ = __name__.split('.')[-1]
__method__   = __name__.split('.')[-2]
__filter__ = __method__.split('_', 1)[-1]
__all__    = (__method__,)

@decorators.enforce()
@decorators.rename(__method__)
def method(self: object, query: str) -> list:
    return self.__search_filter(query, __filter__)

# from . import base
# from .. import utils
#
# class Union():
#     def __init__(self: object, *types: type) -> None:
#         self._types = types
#
#     def __repr__(self: object) -> str:
#         return '<{class_name}({types})>'.format \
#         (
#             class_name = self.__class__.__name__,
#             types      = ', '.join(type.__name__ for type in self._types)
#         )
#
#     def _validate(self: object, value: object) -> bool:
#         for type in self._types:
#             if utils.isinstance(value, type):
#                 return True
#
#         return False

from . import base

class Union(base.BaseUnion):
    pass

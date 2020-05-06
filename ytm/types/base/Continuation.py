from .TypeB64 import TypeB64
from .. import constants

class Continuation(TypeB64):
    _pattern = f'^(?P<data>[{constants.CHARS_CONTINUATION}]*)$'

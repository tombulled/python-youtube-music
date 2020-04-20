from .. import utils

utils._import(locals())

# This should not be repeated
class BaseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__class__.__module__ = __builtins__['__name__']

# class InvalidAlbumIdError(BaseException): pass
# class InvalidArtistIdError(BaseException): pass
# class InvalidBrowseIdError(BaseException): pass
class InvalidIdError(BaseException): pass
class InvalidResponseError(BaseException): pass

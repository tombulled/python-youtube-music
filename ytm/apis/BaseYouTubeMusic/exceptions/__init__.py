from .. import utils

utils._import(locals())

class BaseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__class__.__module__ = __builtins__['__name__']

class InvalidPageConfigurationError(BaseException): pass
class PageNotFoundError(BaseException): pass

class YouTubeMusicApiError(BaseException):
    def __init__(self, data):
        super().__init__()

        self.data = utils.get_nested(data, 'error')

        self.code = utils.get_nested(self.data, 'code')
        self.errors = utils.get_nested(self.data, 'errors', default=())
        self.message = utils.get_nested(self.data, 'message')
        self.status = utils.get_nested(self.data, 'status')

    def __str__(self):
        return '[{code}] {status} - {message} ({domains})'.format \
        (
            code = self.code,
            status = self.status,
            message = self.message,
            domains = ', '.join \
            (
                utils.get_nested(error, 'domain')
                for error in self.errors
            ),
        )

class YouTubeApiError(BaseException):
    def __init__(self, data):
        super().__init__()

        self.data = data

        self.code = utils.get_nested(self.data, 'errorcode')
        self.message = utils.get_nested(self.data, 'reason')
        self.status = utils.get_nested(self.data, 'status')

    def __str__(self):
        return '[{code}] {status} - {message}'.format \
        (
            code = self.code,
            status = self.status,
            message = self.message,
        )

from . import base

class YouTubeMusicApiError(base.BaseException):
    def __init__(self, data):
        super().__init__()

        self.data = data.get('error')

        self.code = self.data.get('code')
        self.errors = self.data.get('errors', ())
        self.message = self.data.get('message')
        self.status = self.data.get('status')

    def __str__(self):
        return '[{code}] {status} - {message} ({domains})'.format \
        (
            code = self.code,
            status = self.status,
            message = self.message,
            domains = ', '.join \
            (
                error.get('domain')
                for error in self.errors
            ),
        )

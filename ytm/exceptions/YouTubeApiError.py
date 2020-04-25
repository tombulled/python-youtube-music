from . import base

class YouTubeApiError(base.BaseException):
    def __init__(self, data):
        super().__init__()

        self.data = data

        self.code = self.data.get('errorcode')
        self.message = self.data.get('reason')
        self.status = self.data.get('status')

    def __str__(self):
        return '[{code}] {status} - {message}'.format \
        (
            code = self.code,
            status = self.status,
            message = self.message,
        )

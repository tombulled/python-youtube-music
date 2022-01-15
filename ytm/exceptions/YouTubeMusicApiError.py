'''
Module containing the exception: YouTubeMusicApiError
'''

from . import base

class YouTubeMusicApiError(base.BaseException):
    '''
    Exception raised when the YouTube Api reports an error

    Attributes:
        data: YouTube Music Api error data
        code: Error code
            Example: 500
        errors: Errors
            Example: [{'domain': 'global',
                        'message': 'Unknown Error.',
                        'reason': 'backendError'}]
        message: Error message
            Example: 'Unknown Error.'
        status: Error status
            Example: 'UNKNOWN'
    '''

    data:    dict = None
    code:    int  = None
    errors:  list = None
    message: str  = None
    status:  str  = None

    def __init__(self: object, data: dict) -> None:
        '''
        Initialise the exception class.

        Args:
            self: Class instance
            data: YouTube Music Api error data
        '''

        super().__init__()

        self.data = data.get('error')

        self.code    = self.data.get('code')
        self.errors  = self.data.get('errors', ())
        self.message = self.data.get('message')
        self.status  = self.data.get('status')

    def __str__(self: object) -> str:
        '''
        Returns a string representation of the class.

        Args:
            self: Class instance

        Returns:
            String representation of the form:
                [{code}] {status} - {message} ({domains})
        '''

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

'''
Module containing the exception: YouTubeApiError
'''

from . import base

class YouTubeApiError(base.BaseException):
    '''
    Exception raised when the YouTube Api reports an error

    Attributes:
        data: YouTube Api error data
        code: Error code
        message: Error message
        status: Error status
    '''

    data:    dict = None
    code:    int  = None
    message: str  = None
    status:  str  = None

    def __init__(self: object, data: dict) -> None:
        '''
        Initialise the exception class.

        Args:
            self: Class instance
            data: YouTube Api error data
        '''

        super().__init__()

        self.data = data

        self.code    = self.data.get('errorcode')
        self.message = self.data.get('reason')
        self.status  = self.data.get('status')

    def __str__(self: object) -> str:
        '''
        Returns a string representation of the class.

        Args:
            self: Class instance

        Returns:
            String representation of the form:
                [{code}] {status} - {message}
        '''

        return '[{code}] {status} - {message}'.format \
        (
            code    = self.code,
            status  = self.status,
            message = self.message,
        )

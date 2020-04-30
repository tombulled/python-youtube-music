'''
Module containing the exception: ParserError
'''

from . import base

class ParserError(base.BaseException):
    '''
    Exception raised when a parser encounters an error

    Attributes:
        parser: Name of the parser function which encountered an error
        message: Exception message
    '''

    parser:  str = None
    message: str = None

    def __init__(self: object, parser: str, message: str):
        '''
        Initialise the exception class.

        Args:
            self: Class instance
            parser: The name of the parser function which encountered an error
        '''

        self.parser = parser
        self.message = message

        super().__init__(f'{self.parser}() encountered an error: {self.message}')

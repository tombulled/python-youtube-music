from . import base

class ParserError(base.BaseException):
    def __init__(self, parser: str, message: str):
        self.parser = parser
        self.message = message

        super().__init__(f'{self.parser}() encountered an error: {self.message}')

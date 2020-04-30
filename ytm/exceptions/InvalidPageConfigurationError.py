'''
Module containing the exception: InvalidPageConfigurationError
'''

from . import base

class InvalidPageConfigurationError(base.BaseException):
    '''
    Exception raised when a page contains invalid configuration data
    '''

    pass

'''
'''

import requests

from . import constants
from . import utils

imported = utils._import(locals())

methods = \
{
    func.__name__: func
    for func in imported
    if callable(func)
}

__class__ = __name__.split('.')[-1]
__all__   = (__class__,)

class BaseYouTubeMusic(object):
    '''
    '''

    def __init__(self: object):
        '''
        '''

        self.__methods = []

        for method_name, method in methods.items():
            setattr(self.__class__, method_name, method)

            self.__methods.append(method_name)

        self.session = requests.Session()

        self.session.headers.update \
        (
            {
                'User-Agent'       : utils.random_user_agent(),
                'X-Goog-Visitor-Id': constants.HEADER_VISITOR_ID,
                'Referer'          : self._url(),
            }
        )

    def __repr__(self: object) -> str:
        '''
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

    def __dir__(self: object) -> list:
        '''
        '''

        return self.__methods

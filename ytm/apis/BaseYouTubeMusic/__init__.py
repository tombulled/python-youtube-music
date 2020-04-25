'''
'''

import requests

from . import constants
from . import utils
from . import methods

class BaseYouTubeMusic(object):
    '''
    '''

    def __init__(self: object):
        '''
        '''

        # self.__methods = []

        for method_name in methods.__all__:
            method = getattr(methods, method_name)

            # print(method_name, method)

            setattr(self.__class__, method_name, method)

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

    # def __dir__(self: object) -> list:
    #     '''
    #     '''
    #
    #     return self.__methods

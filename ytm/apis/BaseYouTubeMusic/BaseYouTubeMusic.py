'''
Module containing the Api class: BaseYouTubeMusic
'''

import requests

from . import constants
from . import utils
from . import methods

class BaseYouTubeMusic(object):
    '''
    Base YouTube Music class.

    Lowest level interactions with YouTube Music are achieved using this class

    Attributes:
        session: Requests session for sending requests
    '''

    session: requests.Session = None

    def __init__(self: object) -> None:
        '''
        Initialise class.

        Args:
            self: Class instance

        Returns:
            None

        Example:
            >>> api = BaseYouTubeMusic()
        '''

        for method_name in methods.__all__:
            method = getattr(methods, method_name)

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
        Return a string representation of the object.

        Returns a string in the format <{class_name}()>

        Args:
            self: Class instance

        Returns:
            String representation of the object

        Example:
            >>> api = BaseYouTubeMusic()
            >>>
            >>> api
            <BaseYouTubeMusic()>
            >>> 
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

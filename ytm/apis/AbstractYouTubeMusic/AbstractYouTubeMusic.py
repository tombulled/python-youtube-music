'''
'''

from ..BaseYouTubeMusic import BaseYouTubeMusic
from . import methods

class AbstractYouTubeMusic(object):
    '''
    '''

    def __init__(self: object):
        '''
        '''

        self._base = BaseYouTubeMusic()

        for method_name in methods.__all__:
            method = getattr(methods, method_name)

            setattr(self.__class__, method_name, method)

    def __repr__(self: object) -> str:
        '''
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

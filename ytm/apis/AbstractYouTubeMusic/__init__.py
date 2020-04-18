'''
'''

from ..BaseYouTubeMusic import BaseYouTubeMusic
from .methods import methods

__all__ = __name__.split('.')[-1:]

class AbstractYouTubeMusic(object):
    '''
    '''

    def __init__(self: object):
        '''
        '''

        # This should be _base or __base
        # ... so not confused with a method when dir(...)
        # ... Note: Has to be removed from all methods aswell
        self._base = BaseYouTubeMusic()

        for method_name, method in methods.items():
            setattr(self.__class__, method_name, method)

    def __repr__(self: object) -> str:
        '''
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

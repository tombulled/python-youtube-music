'''
Module containing the Api class: AbstractYouTubeMusic
'''

from ..BaseYouTubeMusic import BaseYouTubeMusic
from . import methods

class AbstractYouTubeMusic(object):
    '''
    Abstract YouTube Music class.

    Base methods get abstracted and parsed.

    Attributes:
        _base: Base class reference
        _methods: API Methods
    '''

    _base:    BaseYouTubeMusic = None
    _methods: list             = {}

    def __init__(self: object) -> None:
        '''
        Initialise class.

        Args:
            self: Class instance

        Returns:
            None

        Example:
            >>> api = AbstractYouTubeMusic()
        '''

        self._base    = BaseYouTubeMusic()

        for method_name in methods.__all__:
            method = getattr(methods, method_name)

            setattr(self.__class__, method_name, method)

            if not method_name.startswith('_'):
                self._methods[method_name] = method

    def __repr__(self: object) -> str:
        '''
        Return a string representation of the object.

        Returns a string in the format <{class_name}()>

        Args:
            self: Class instance

        Returns:
            String representation of the object

        Example:
            >>> api = AbstractYouTubeMusic()
            >>>
            >>> api
            <AbstractYouTubeMusic()>
            >>>
        '''

        return '<{class_name}()>'.format \
        (
            class_name = self.__class__.__name__,
        )

'''
Module containing the Api class: YouTubeMusic
'''

from ..AbstractYouTubeMusic import AbstractYouTubeMusic

class YouTubeMusic(AbstractYouTubeMusic):
    '''
    Highest level YouTubeMusic Api class.

    When using an Api class, if low-level interactions are not required, this
    is the class to use. Lower-level Api classes will be available through
    attributes.

    For now this class only inherits from AbstractYouTubeMusic as this achieves
    very high-level Api interactions.
    '''

    pass

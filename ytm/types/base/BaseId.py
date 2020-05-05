'''
'''

from .BaseType import BaseType
from .. import utils
from .. import constants

class BaseId(BaseType):
    '''
    '''

    _patterns = \
    (
        utils.pattern \
        (
            utils.entropy \
            (
                chars  = constants.CHARS_ID,
                repeat = '+',
            ),
        ),
    )

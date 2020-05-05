'''
'''

from .BaseType import BaseType
from .. import utils
from .. import constants

class BaseParam(BaseType):
    '''
    '''

    _patterns = \
    (
        utils.pattern \
        (
            utils.entropy \
            (
                chars  = constants.CHARS_PARAM,
                repeat = '+',
            ),
        ),
    )

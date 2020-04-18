'''
'''

import random
from .. import constants

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def random_user_agent() -> str:
    '''
    '''

    return random.choice(constants.USER_AGENTS)

'''
'''

import random
from .. import constants

def random_user_agent() -> str:
    '''
    '''

    return random.choice(constants.USER_AGENTS)

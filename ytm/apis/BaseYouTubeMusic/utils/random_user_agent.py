''' xxx '''

import random
from .... import constants

__all__ = __name__.split('.')[-1:]

def random_user_agent():
    return random.choice(constants.USER_AGENTS)

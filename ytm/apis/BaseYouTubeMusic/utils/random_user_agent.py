'''
Module containing the utility function: random_user_agent
'''

import random
from .. import constants

def random_user_agent() -> str:
    '''
    Returns a random user agent.

    Returns:
        A random user agent

    Example:
        >>> random_user_agent()
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
        >>>
    '''

    return random.choice(constants.USER_AGENTS)

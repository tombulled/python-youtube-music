from .watch import watch as parse_watch
from . import decorators

@decorators.enforce_parameters
@decorators.catch
def watch_shuffle(data: dict):
    return parse_watch(data)

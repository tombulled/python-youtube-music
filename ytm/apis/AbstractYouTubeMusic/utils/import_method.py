'''
'''

import importlib
import sys

__util__ = __name__.split('.')[-1]
__all__  = (__util__,)

def import_method(locals: dict) -> dict:
    '''
    '''

    package = locals.get('__package__')
    spec    = locals.get('__spec__')

    module = importlib.util.module_from_spec(spec)
    module = sys.modules[module.__name__]

    if not hasattr(module, '__all__'):
        module.__all__ = []

    try:
        sub_module = importlib.import_module(f'.method', package=package)

        method = getattr(sub_module, 'method')

        method_name = module.__name__.split('.')[-1]

        method.__name__ = method_name

        module.__all__.append(method_name)

        setattr(module, method_name, method)

        return \
        {
            method.__name__: method
        }
    except ModuleNotFoundError:
        pass

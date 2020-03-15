import pkgutil
import importlib
import sys

__all__ = __name__.split('.')[-1:]

def _import(locals):
    path    = locals.get('__path__')
    package = locals.get('__package__')
    spec    = locals.get('__spec__')

    module = importlib.util.module_from_spec(spec)
    module = sys.modules[module.__name__]

    if not hasattr(module, '__all__'):
        module.__all__ = []

    sub_modules = pkgutil.iter_modules(path)

    imported = []

    for sub_module in sub_modules:
        sub_module_name = sub_module.name

        sub_module = importlib.import_module(f'.{sub_module_name}', package=package)

        object = getattr(sub_module, sub_module_name, None) or sub_module

        setattr(module, sub_module_name, object)

        imported.append(object)
        module.__all__.append(sub_module_name)

    return imported

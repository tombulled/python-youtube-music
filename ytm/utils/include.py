import pkgutil
import importlib
import sys

def include(spec, callback=None):
    '''
    '''

    if not callback:
        callback = lambda module_name: True

    importlib.util.module_from_spec(spec)

    module = sys.modules[spec.name]

    sub_modules = pkgutil.iter_modules(spec.submodule_search_locations)

    imported = {}

    for sub_module in sub_modules:
        sub_module_name = sub_module.name
        
        if not callback(sub_module_name): continue

        sub_module = importlib.import_module \
        (
            name    = f'.{sub_module_name}',
            package = spec.name,
        )

        object = getattr(sub_module, sub_module_name, None) or sub_module

        setattr(module, sub_module_name, object)

        imported[sub_module_name] = object

    return imported

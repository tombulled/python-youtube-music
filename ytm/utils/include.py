'''
Module containing the utility function: include
'''

import pkgutil
import importlib
import sys
from typing import Callable
from _frozen_importlib import ModuleSpec

def include(spec: ModuleSpec, func: Callable = None) -> dict:
    '''
    Include relative libraries, or an object they contain.

    If a relative library exists with an object of the same name inside,
    it returns that object, otherwise, it returns the library. Libraries
    or objects are only returned if func(library or object) is true.

    Args:
        spec: The specification of the module to import from
            Example: utils.__spec__
        func: A function to filter items by
            Example: lambda object: object.__name__ in ('foo',)

    Returns:
        A dictionary of imported libraries or objects

    Example:
        Package named utils containing foo.py, with a function inside named foo:
            >>> include(utils.__spec__)
            {'foo': <function foo at 0x0000027A533CE790>}
            >>>
        Package named utils containing foo.py with a function inside named bar:
            >>> include(utils.__spec__)
            <module 'utils.foo' from '/path/to/utils/foo.py'>
            >>>
    '''

    if not func:
        func = lambda module_name: True

    importlib.util.module_from_spec(spec)

    module = sys.modules[spec.name]

    sub_modules = pkgutil.iter_modules(spec.submodule_search_locations)

    imported = {}

    for sub_module in sub_modules:
        sub_module_name = sub_module.name

        sub_module = importlib.import_module \
        (
            name    = f'.{sub_module_name}',
            package = spec.name,
        )


        object = getattr(sub_module, sub_module_name, None) or sub_module

        if not func(object): continue

        setattr(module, sub_module_name, object)

        imported[sub_module_name] = object

    return imported

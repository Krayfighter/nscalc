from importlib import import_module
from os import getcwd, listdir


# !!!!!   The stack overflow guy said that this was dangerous
for item in listdir(getcwd()+'/extensions'):
    if item.endswith('.py') and item != '__init__.py':
        item = item[:-3]
        module = import_module('extensions.'+item).__dict__
        try:
            to_import = module.__all__
        except AttributeError:
            to_import = [name for name in module if not name.startswith('_')]
        globals().update({name: module[name] for name in to_import})\

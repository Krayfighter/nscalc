from importlib import import_module
from os import getcwd, listdir


for item in listdir(getcwd()+'/extensions'):
    if item.endswith('.py') and item != '__init__.py':
        globals()[item[:-3]] = import_module('extensions.'+item[:-3])


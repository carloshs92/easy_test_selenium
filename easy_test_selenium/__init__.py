import os, sys, inspect

cmd_folder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

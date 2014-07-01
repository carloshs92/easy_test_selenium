import sys
from importlib import import_module

def get_command(cmd):
    return import_module('commands.%s'%cmd)

def execute(argv=None, settings=None):
    # Get arguments
    if argv is None:
        argv = sys.argv

    # Execute command
    cmd = get_command(argv[1])
    cmd.run_command(argv[2])
    print 'OK'

if __name__ == '__main__':
    execute()

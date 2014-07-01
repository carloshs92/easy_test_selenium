import string
import re, sys
from os.path import exists, join
#from _pathconf import addPath
#addPath()
import easy_test_selenium
from easy_test_selenium import utils
import shutil
from shutil import copytree, ignore_patterns

TEMPLATES_PATH = join(easy_test_selenium.__path__[0], 'templates', 'project')
TEMPLATES_TO_RENDER = (
    ('${project_name}', 'settings.py'),
)
IGNORE = ignore_patterns('*.pyc', '.svn')

def run_command(name):
    if not re.search(r'^[_a-zA-Z]\w*$', name):
        print('Error: Project names must begin with a letter and contain only\n' \
            'letters, numbers and underscores')
        sys.exit(1)
    elif exists(name):
        print("Error: directory %r already exists" % name)
        sys.exit(1)
    moduletpl = TEMPLATES_PATH
    copytree(moduletpl, join(name, name), ignore=IGNORE)
    shutil.copy(join(TEMPLATES_PATH, 'settings.py'), name)

    for paths in TEMPLATES_TO_RENDER:
        path = join(*paths)
        tplfile = join(name, string.Template(path).substitute(project_name=name))
        utils.render_templatefile(tplfile, project_name=name, ProjectName=utils.string_camelcase(name))
    print 'ok'
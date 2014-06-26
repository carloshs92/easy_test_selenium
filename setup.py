from distutils.core import setup
setup(
  name = 'easy_test_selenium',
  packages = ['easy_test_selenium', 'command'], # this must be the same as the name above
  version = '0.0.1',
  include_package_data=True,
  description = 'A python mini framework for tests that use Selenium',
  scripts=['command/admin.py'],
  author = 'Carlos Huamani',
  author_email = 'carlos.hs.92@gmail.com',
  url = 'https://github.com/carloshs92/easy_test_selenium', # use the URL to the github repo
  download_url = 'https://github.com/carloshs92/easy_test_selenium/archive/master.zip', # I'll explain this in a second
  keywords = ['test', 'functional test', 'selenium'], # arbitrary keywords
  classifiers = [],
)


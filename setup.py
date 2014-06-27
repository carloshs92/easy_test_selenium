from distutils.core import setup
setup(
    name='easyTestSelenium',
    packages=['easy_test_selenium'],
    version='0.0.1',
    include_package_data=True,
    description='A python mini framework for tests that use Selenium',
    scripts=['bin/admin.py'],
    author='Carlos Huamani',
    author_email='carlos.hs.92@gmail.com',
    url='https://github.com/carloshs92/easy_test_selenium',
    download_url='https://github.com/carloshs92/easy_test_selenium/archive/master.zip',
    keywords=['test', 'functional test', 'selenium'],
    classifiers=[],
)


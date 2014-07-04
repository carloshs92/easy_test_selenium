from importlib import import_module
from easy_test_selenium.test_case_principal import TestCasePrincipal
from easy_test_selenium.configuration import Settings


def run_command(name=None):
    test = TestCasePrincipal()
    settings = Settings()
    conf = settings.getConfiguration()
    for app in conf.TEST_APPS:
        test_case = import_module('%s.test_case'%app)
        setattr(test, 'test_%s'%app, test_case.main)
    for driver in conf.WEB_DRIVERS:
        test.runTest(driver)
    print 'Test Finished'
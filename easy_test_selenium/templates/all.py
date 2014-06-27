# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest

class PruebasDeRegistro(unittest.TestCase):
    def setUp(self):
        self.binary = FirefoxBinary('/usr/bin/firefox/firefox')
        self.driver = webdriver.Firefox(firefox_binary=self.binary)
        self.driver.implicitly_wait(30)
        # url basic
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = False
        self.debug = True

    def printText(self, text):
        if self.debug:
            print text

    def waitFor(self, seconds):
        i = 0
        while seconds > i:
            i += 1
            print u'--> Esperando %d segundo(s)...' % i
            sleep(1)

    #Registre aqui los tests
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

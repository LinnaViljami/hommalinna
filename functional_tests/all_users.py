# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import warnings
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'/usr/bin/firefox')
        self.browser.implicitly_wait(3)

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
 
    def tearDown(self):
        self.browser.quit()
 
if __name__=="__main__":
    unittest.main()

import os

from datetime import datetime

import sys
from selenium import webdriver

import start_settings


def check_failed(f):
    def wrapper(*args):
        try:
            return f(*args)
        except Exception as e:
            print e
            args[0].make_report()
            raise e
    return wrapper


class BaseTest(object):

    def setup(self):
        self.select_driver(start_settings.browser)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def make_report(self):
        print '-----------------------------------------'
        print "FAILED LINK:  " + self.driver.current_url
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.get_screenshot_as_file('screenshot-%s.png' % now)
        print '-----------------------------------------'

    def teardown(self):
        if sys.exc_info()[0]:
            self.make_report()
        self.driver.quit()

    def select_driver(self, driver='chrome'):
        dir = os.path.dirname(__file__)
        if driver == 'chrome':
            self.driver = webdriver.Chrome(executable_path=dir + '/drivers/chromedriver')
        if driver == 'firefox':
            self.driver = webdriver.Firefox(executable_path=dir + '/drivers/geckodriver')
            # solution for older versions of firefox
            # self.driver = webdriver.Firefox()



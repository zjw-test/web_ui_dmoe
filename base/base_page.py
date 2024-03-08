import logging

from selenium.webdriver.support.wait import WebDriverWait
from common.utils import DriverUtil


class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_web_driver()
        logging.info("获取web_driver")

    def find_element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def find_el(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))


class BaseHandle:
    def input(self, el, info):
        el.clear()
        el.send_keys(info)

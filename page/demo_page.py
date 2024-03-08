import logging
import time

import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
from common.utils import DriverUtil


class DemoPage(BasePage):
    """对象库层"""

    def __init__(self):
        super().__init__()
        self.user_management = (By.XPATH, '//*[contains(text(),"用户管理")]')
        self.search = (By.XPATH, '//*[@id="keyword"]')

    def find_user_management(self):
        logging.info("这是一条日志信息")
        return self.find_element(self.user_management)

    def find_search(self):
        return self.find_element(self.search)


class DemoHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.demo_page = DemoPage()

    def click_user_management(self):
        self.demo_page.find_user_management().click()

    def click_search(self):
        self.demo_page.find_search().click()


class DemoProxy:
    """业务层"""

    def __init__(self):
        self.demo_handler = DemoHandle()

    def user_management(self):
        time.sleep(1)
        allure.attach(DriverUtil.get_web_driver().get_screenshot_as_png(), "首页截图", allure.attachment_type.PNG)
        self.demo_handler.click_user_management()
        self.demo_handler.click_search()

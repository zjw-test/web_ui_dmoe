import time

import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
from common.utils import DriverUtil


class DemoPage(BasePage):
    """对象库层"""

    def __init__(self):
        super().__init__()
        self.login = (By.XPATH, '//*[@id="btnSubmit"]')
        self.user_management = (By.XPATH, '//*[contains(text(),"用户管理")]')
        self.search = (By.XPATH, '//*[@id="keyword"]')
        self.immediately_search = (By.XPATH, '//*[contains(text(),"立即搜索")]')

    def find_login(self):
        return self.find_element(self.login)

    def find_user_management(self):
        return self.find_element(self.user_management)

    def find_search(self):
        return self.find_element(self.search)

    def find_immediately_search(self):
        return self.find_element(self.immediately_search)


class DemoHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.demo_page = DemoPage()

    def click_login(self):
        self.demo_page.find_login().click()

    def click_user_management(self):
        self.demo_page.find_user_management().click()

    def click_search(self):
        self.demo_page.find_search().click()

    def input_search(self, keyword):
        self.input(self.demo_page.find_search(), keyword)

    def click_immediately_search(self):
        self.demo_page.find_immediately_search().click()


class DemoProxy:
    """业务层"""

    def __init__(self):
        self.demo_handler = DemoHandle()
        self.driver = DriverUtil.get_web_driver()

    def user_login(self):
        allure.attach(DriverUtil.get_web_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        self.demo_handler.click_login()

    def user_home(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        scroll_height = self.driver.execute_script("return window.innerHeight")
        scroll_times = 0
        while total_height > 0:
            self.driver.execute_script(f"window.scrollTo(0, {scroll_height * scroll_times})")
            time.sleep(1)
            allure.attach(DriverUtil.get_web_driver().get_screenshot_as_png(), f"首页_{scroll_times}",
                          allure.attachment_type.PNG)
            total_height -= scroll_height
            scroll_times += 1

    def user_management(self, keyword):
        time.sleep(2)
        self.demo_handler.click_user_management()
        allure.attach(DriverUtil.get_web_driver().get_screenshot_as_png(), "用户页截图", allure.attachment_type.PNG)
        time.sleep(3)
        self.demo_handler.click_search()
        self.demo_handler.input_search(keyword)
        self.demo_handler.click_immediately_search()
        allure.attach(DriverUtil.get_web_driver().get_screenshot_as_png(), "搜索", allure.attachment_type.PNG)

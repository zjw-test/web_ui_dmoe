# -*- coding: UTF-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.utils import DriverUtil


class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_web_driver()
        logging.info("Web driver 初始化成功")

    def find_element(self, loc, timeout=10, poll_frequency=0.5):
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
            logging.info(f"找到元素: {loc}")
            return element
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"查找元素失败: {loc}, 原因: {e}")

    def find_elements(self, loc, timeout=10, poll_frequency=0.5):
        try:
            elements = WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
            if elements:
                logging.info(f"找到多个元素: {loc}")
            else:
                logging.info(f"未找到匹配元素，但未抛出异常: {loc}")
            return elements
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"查找多个元素失败: {loc}, 原因: {e}")


class BaseHandle:
    def input(self, el, info):
        logging.info(f"开始输入信息到元素: {el}, 输入内容: {info}")
        el.clear()
        el.send_keys(info)
        logging.info(f"输入完成: {info} 到元素: {el}")
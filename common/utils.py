import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import config_log, FILE_LOCATION
import ddddocr

new_path = FILE_LOCATION + os.sep + "scripts" + os.sep + 'captcha.png'
config_log()


class DriverUtil:
    __web_driver = None

    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.implicitly_wait(5)
            cls.__web_driver.get("https://dugusoft.com/erp/index.jsp")
            cls.__web_driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys("demo")
            logging.info("hello ni ni")
            cls.__web_driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys("123")
            captcha_element = cls.__web_driver.find_element(By.XPATH,
                                                            '//*[@id="account"]/ul/li[3]/div/table/tbody/tr/td[2]/img')
            captcha_element.screenshot('captcha.png')
            ocr = ddddocr.DdddOcr()
            with open(new_path, 'rb') as f:
                img_bytes = f.read()
            res = ocr.classification(img_bytes)
            logging.info("识别出的验证码为" + res)
            time.sleep(3)
            cls.__web_driver.find_element(By.XPATH, '//*[@id="txt_check"]').send_keys(res)
            cls.__web_driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click()
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            cls.__web_driver = None

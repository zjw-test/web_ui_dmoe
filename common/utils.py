import logging
import os
import platform
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config.confRead import Config

from global_config import FILE_LOCATION
import ddddocr

config_instance = Config()
host_address = config_instance.read_host()["host_address"]
account = config_instance.read_user()["account"]
password = config_instance.read_user()["password"]

FILE_LOCATION = FILE_LOCATION + os.sep + "scripts"


class DriverUtil:
    __web_driver = None

    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            chrome_options = Options()

            # 根据操作系统选择性地添加参数
            os_name = platform.system().lower()
            if os_name == 'linux':
                # 针对Linux环境的配置
                # 禁止沙箱，稳定浏览器正常工作
                chrome_options.add_argument('--no-sandbox')
                # 不使用临时文件系统，转为常规文件存储，稳定运行，避免内存不足而出错
                chrome_options.add_argument('--disable-dev-shm-usage')
                # 无界面模式在Linux环境下开启
                chrome_options.add_argument('--headless')
            elif os_name == 'windows':
                # 如果有针对Windows的特定配置，可以在这里添加
                # 如果Windows也需要无界面模式，可以取消下面这行注释
                # chrome_options.add_argument('--headless')
                pass

            # 初始化WebDriver实例
            cls.__web_driver = webdriver.Chrome(options=chrome_options)
            # 由于是无界面模式，不能使用maximize_window()，改为设置固定窗口大小
            # cls.__web_driver.maximize_window()
            cls.__web_driver.set_window_size(1920, 1080)

            cls.__web_driver.get(host_address)
            cls.__web_driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(account)
            cls.__web_driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(password)
            captcha_element = cls.__web_driver.find_element(By.XPATH,
                                                            '//*[@id="account"]/ul/li[3]/div/table/tbody/tr/td[2]/img')
            thread_id = threading.get_ident()
            captcha_path = f"{FILE_LOCATION}/captcha_{thread_id}.png"
            captcha_element.screenshot(captcha_path)
            ocr = ddddocr.DdddOcr()
            with open(captcha_path, 'rb') as f:
                img_bytes = f.read()
            res = ocr.classification(img_bytes)
            logging.info("识别出的验证码为" + res)
            cls.__web_driver.find_element(By.XPATH, '//*[@id="txt_check"]').send_keys(res)
            os.remove(captcha_path)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            cls.__web_driver = None

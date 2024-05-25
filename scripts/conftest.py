# -*- coding: UTF-8 -*-
import logging
import os
import shutil

import pytest

from common.utils import DriverUtil
from global_config import FILE_LOCATION, config_log
from page.demo_page import DemoProxy

config_log()  # 全局配置日志


def is_master():
    """判断当前是否为主节点"""
    return not os.environ.get('PYTEST_XDIST_WORKER', False)


# 钩子函数，在pytest的整个测试会话开始之前执行
def pytest_sessionstart(session):
    """会话开始前执行的代码，仅在主节点上执行清理任务"""
    if is_master():
        tmp_path = FILE_LOCATION + os.sep + "tmp"
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)
        os.makedirs(tmp_path)
        logging.info("主节点会话开始：执行了清理任务")


@pytest.fixture(scope="class")
def demo_user_login():
    DemoProxy().user_login()
    logging.info("test_demo_user_login")


# 钩子函数，在pytest测试会话结束后执行
def pytest_sessionfinish(session, exitstatus):
    """会话结束后执行的代码，仅在主节点上生成Allure测试报告"""
    DriverUtil.quit_web_driver()
    logging.info("会话结束：WebDriver已关闭")
    if is_master():
        tmp_path = FILE_LOCATION + os.sep + "tmp"
        report_path = FILE_LOCATION + os.sep + "report"
        os.system(f"allure generate --clean {tmp_path} -o {report_path}")
        logging.info("会话结束：生成了Allure测试报告")

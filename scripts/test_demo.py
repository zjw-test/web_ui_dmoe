import logging
import os
import shutil

import pytest
from common.utils import DriverUtil
from config import config_log, FILE_LOCATION
from page.demo_page import DemoProxy

config_log()


class TestDemo:
    def test_check_file(session):
        tmp_path = FILE_LOCATION + os.sep + "tmp"
        if os.path.exists(tmp_path):
            shutil.rmtree(tmp_path)
            os.makedirs(tmp_path)

    def setup_class(self):
        # tmp_path = FILE_LOCATION + os.sep + "tmp"
        # shutil.rmtree(tmp_path)
        self.driver = DriverUtil.get_web_driver()

    @pytest.mark.smoke
    def test_demo_management(self):
        DemoProxy().user_management()
        logging.info("hello test test test")

    @pytest.mark.smoke(order=100)
    def test_execute_cmd_command(self):
        # tmp_path = FILE_LOCATION + os.sep + "tmp"
        # report_path = FILE_LOCATION + os.sep + "report"
        # shutil.rmtree(tmp_path)
        # shutil.rmtree(report_path)
        os.system("allure generate --clean ../tmp -o ../report")

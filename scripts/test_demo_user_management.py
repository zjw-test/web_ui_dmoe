# -*- coding: UTF-8 -*-
import logging
import pytest
from common.read_json import read_json, read_json_title
from page.demo_page import DemoProxy


# @pytest.mark.usefixtures("demo_user_login")
class TestDemoUserManagement:

    @pytest.mark.smoke
    @pytest.mark.parametrize("keyword", read_json("user_management.json", "user"),
                             ids=read_json_title("user_management.json", "user"))
    def test_demo_user_management(self, keyword):
        logging.info(f"开始搜索{keyword}")
        DemoProxy().user_management(keyword)
        logging.info("test_demo_management")

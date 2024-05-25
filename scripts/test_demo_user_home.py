# -*- coding: UTF-8 -*-
import logging
import pytest
from page.demo_page import DemoProxy


@pytest.mark.usefixtures("demo_user_login")
class TestDemoUserHome:

    @pytest.mark.smoke
    def test_user_home(self):
        DemoProxy().user_home()
        logging.info("test_user_home")

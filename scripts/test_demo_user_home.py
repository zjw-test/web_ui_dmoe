import logging
import pytest
from global_config import config_log
from page.demo_page import DemoProxy

config_log()


@pytest.mark.usefixtures("demo_user_login")
class TestDemoUserHome:

    @pytest.mark.smoke
    def test_user_home(self):
        DemoProxy().user_home()
        logging.info("test_user_home")

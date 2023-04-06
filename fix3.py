from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver


# Fixture for Chrome

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        self.driver.get("https://google.com/")
        print(self.driver.title)
        sleep(5)

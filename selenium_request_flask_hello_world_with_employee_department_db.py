# Import the 'modules' that are required for execution
import pytest, requests
from seleniumwire import webdriver
from assertpy import assert_that
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


#Fixture for Firefox
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def __int__(self):
        super().__int__()

    def test_open_url(self):
        self.driver.get("http://127.0.0.1:8082/emp")
        self.driver.get_screenshot_as_file('testfile.png')
        print(self.driver.title)
        for request in self.driver.requests:
            if request.response:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.body
                    #request.response.headers['Content-Type']
                )
                assert_that(request.response.status_code).contains(200)
                assert_that(request.response.body).contains("CLERK")
                sleep(5)

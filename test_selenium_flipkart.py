import time,pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from assertpy import *

@pytest.fixture(params=['chrome','firefox'], scope='class')
def driver_init(request):
    web_driver = webdriver.Chrome()
    if request == 'chrome':
        web_driver = webdriver.Chrome()
    if request == 'firefox':
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
        self.driver.get("https://www.flipkart.com/")
        time.sleep(5)
        #self.driver.find_element(By.PARTIAL_LINK_TEXT,"Mobiles & Tablets").click()
        #time.sleep(5)
        self.driver.get_screenshot_as_file('testfile.png')
        print(self.driver.title)
        for request in self.driver.requests:
            if request.response:
                print(
                    request.response.status_code,
                )
                time.sleep(5)




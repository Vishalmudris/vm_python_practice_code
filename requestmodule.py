import requests
from assertpy import *
s = requests.Session()

api_post = s.post("www.flipkart.com",headers="testheader", data="Payload")
api_login = s.get("www.flipkart.com",headers="testheader")

header = f"{"'Accept' = 'application/json' 'CSRFToken'  = "CSRF_TOKEN" 'Authorization' = "Basic Authentication""}"

#######################################
#Selenium#
######################################
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config import *
from assertpy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome()
driver.get("https://app.eu.elastica.net/")
assert_that(driver.title.__contains__("Symantec CloudSOC"))
try:
    element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Skip Broadcom Login'))
    WebDriverWait(driver, delay).until(element_present)

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


driver.find_element(By.PARTIAL_LINK_TEXT, 'Skip Broadcom Login').click()

driver.get_screenshot_as_file('myfirstscreenshot.png')

driver.find_element(By.NAME,'email' ).send_keys(email)
driver.find_element(By.NAME, 'password').send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

select = Select(driver.find_element(By.NAME, 'sex'))
select.select_by_visible_text('Female')

driver.switch_to.frame(driver.find_element(By.ID,"ml-webforms-popup-2207054"))
# First:
closepopup = driver.find_element(By.XPATH,"//div[@class='mailerlite-popup']/a")
print(closepopup.get_attribute("class"))
closepopup.click()

######################################
#Boto3
######################################

import boto3

s3_client = boto3.client('s3', region_name)
create_bucket_response = s3_client.create_bucket(Bucket=str(dest).lower(),
                                                 CreateBucketConfiguration={'LocationConstraint': region_name})

#############################################



import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from assertpy import assert_that
driver = Chrome()
driver.get("https://www.flipkart.com")
title = driver.title
print(title)
assert_that(title).contains("Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More")
#driver.find_element(By.XPATH,'//img[@alt="Mobiles"]').click()

driver.find_element(By.XPATH,'//img[@alt="Grocery"]').click()
time.sleep(5)
'//img[@alt="Mobiles"]'

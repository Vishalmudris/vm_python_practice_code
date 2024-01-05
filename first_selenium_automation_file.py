import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = Chrome()
driver.get("http://theTestingWorld.com/testings")

# Maximize Windows

driver.maximize_window()
driver.find_element(By.NAME, 'fld_username').send_keys('testusernamekirti')
driver.find_element(By.NAME, 'fld_email').send_keys('testusernamekirti@kirti.com')
driver.find_element(By.NAME, 'fld_password').send_keys('ItsPassword@1234')
driver.find_element(By.NAME, 'phone').send_keys('123456789')
driver.find_element(By.NAME, 'address').send_keys('The Address Details')
add_click = driver.find_element(By.XPATH, "//input[@name='add_type' and @value='office']").click()
driver.find_element(By.NAME, 'fld_username').send_keys('testusernamekirti')
select = Select(driver.find_element(By.NAME, 'sex'))
select.select_by_visible_text('Female')
time.sleep(5)
select = Select(driver.find_element(By.ID, 'countryId'))
select.select_by_visible_text('India')
time.sleep(5)
select = Select(driver.find_element(By.ID, 'stateId'))
select.select_by_visible_text('Maharashtra')
time.sleep(5)
select = Select(driver.find_element(By.ID, 'cityId'))
select.select_by_visible_text('Pune')
time.sleep(5)
time.sleep(30)
'''fld_emai
fld_password
phone 
address
add_type
sex
country
state
city
zip'''


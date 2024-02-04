import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config import *
from assertpy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome()
driver.get("https://app.eu.elastica.net/")
print("Title after first login", driver.title)
assert_that(driver.title.__contains__("Symantec CloudSOC"))
# Maximize Windows
driver.maximize_window()
print("Title after maximize window", driver.title)

try:
    element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Skip Broadcom Login'))
    WebDriverWait(driver, delay).until(element_present)

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


driver.find_element(By.PARTIAL_LINK_TEXT, 'Skip Broadcom Login').click()
print("Title after Login window", driver.title)
driver.get_screenshot_as_file('myfirstscreenshot.png')
#driver.find_element(By.CSS_SELECTOR, 'a.herf[ng-click="skipIDPBasedLogin()"]').click()
element = driver.find_element(By.NAME,'email' ).send_keys(email)
driver.find_element(By.NAME, 'password').send_keys(password)
#driver.find_element(By.XPATH, "//button[@type="submit")]").click()
#driver.find_element(By.XPATH, "//button[contains(., 'submit')]").click()
#driver.find_element(By.CSS_SELECTOR("button[type='submit']")).click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#driver.find_element(By.XPATH, "//button[@ng-disabled='isLoginInProgress']").click()



print("Title after CASB main window", driver.title)


'''
#driver.find_element(By.PARTIAL_LINK_TEXT, 'Amazon Web Services').click()
#driver.find_element(By.XPATH, "//*[@id='ui-global-nav-0']/div/nav/ul/casb-side-bar-tile[3]/li/div/ul[4]/li[1]/a/p").click()
#driver.find_element(By.XPATH, "//p[@class='iaas-label']").click()

#driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/casb-ng-side-bar/sym-nav-global/div/div[1]/div/nav/ul/casb-side-bar-tile[3]/li/div/ul[4]/li[1]/a/p[0]").click()
#driver.find_element(By.CLASS_NAME, 'iaas-label').click()
driver.implicitly_wait(10)

driver.get("https://app.eu.elastica.net/ui/iaas/inventory/connections")

driver.get_screenshot_as_file('myfirstscreenshot.jpeg')

try:
    element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Accounts'))
    WebDriverWait(driver, delay).until(element_present)

    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#driver.find_element(By.PARTIAL_LINK_TEXT, 'Connections').click()
print("Title after connection window", driver.title)


#driver.find_element(By.CLASS_NAME, 'ui-menuitem-text').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Accounts').click()
#assert_that(driver.find_element(By.))
accounts = driver.find_element(By.PARTIAL_LINK_TEXT, 'Accounts').text
print(accounts)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Resources').click()

driver.find_element(By.PARTIAL_LINK_TEXT, 'Storage').click()
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Documents').click()
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Activities').click()
time.sleep(10)

'''

# 
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()
import time


# username comes from login_details.txt first line and password comes from the second line
username =  open("login_details.txt").readlines()[0].strip()
password = open("login_details.txt").readlines()[1].strip()

driver.get("https://www.investopedia.com/auth/realms/investopedia/protocol/openid-connect/registrations?client_id=finance-simulator&redirect_uri=https%3A%2F%2Fwww.investopedia.com%2Fsimulator%2Fportfolio&state=3ceeb979-1cc4-4517-84af-0cc4d565a3d2&response_mode=fragment&response_type=code&scope=openid&nonce=bf398b25-4ff2-4087-890f-02c4c75f6a66")


# user agent change
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# click on the a tag with the text "Log in"

driver.find_element(By.LINK_TEXT, "log in").click()

driver.find_element(By.ID, "username").send_keys(username)

driver.find_element(By.ID, "password").send_keys(password)

driver.find_element(By.ID, "login").click()

# then take full a screenshot after 5 seconds 
time.sleep(5)
# get the body element 

badi = driver.find_element(By.TAG_NAME, "body")
# take a screenshot of the body element
badi.screenshot("screenshot.png")


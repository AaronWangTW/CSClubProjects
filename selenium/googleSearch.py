from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
assert "Google" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)

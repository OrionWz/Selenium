from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.scrapethissite.com/pages/forms/?page_num=1"


response = driver.get(url)

buttons = driver.find_elements(By.CLASS_NAME, "pagination")


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


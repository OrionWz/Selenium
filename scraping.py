from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.scrapethissite.com/pages/simple/"

response = driver.get(url)

country_names = driver.find_elements(By.CLASS_NAME,"country-name")


for country_name in country_names:
    print(country_name.text)


country_infos = driver.find_elements(By.CLASS_NAME,"country-info")


for country_info in country_infos:
    print(country_info.text)


driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrap(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe", options=options)
    driver.get(url)

    driver.find_element(By.XPATH,'/html/body/div[3]/div/section/div/div/div/div/div/div/div/div/div/div/p[1]/strong/a[3]').click()
    html = driver.page_source
    return html


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_driver():
    options = Options()
    options.add_argument('--headless')  # delete options=options for open browser when program start
    driver = webdriver.Chrome(options=options, executable_path=".\webdrivers\chromedriver.exe")
    return driver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_driver():
    options = Options()
    options.add_argument('--headless') # commend this for open browser when progarmm start
    driver = webdriver.Chrome(options=options, executable_path="C:\webdrivers\chromedriver.exe")
    return driver
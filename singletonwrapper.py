import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome = driver.get('https://google.com')

class SingletonCaseWrapper:
    __instance = None

    def __new__(cls):
        if(cls.__instance is None):
            cls.__instance = super(SingletonCaseWrapper, cls).__new__(cls)

        return cls.__instance

    def Search(self, search_topic):
        search_box = driver.find_element("name", "q")
        search_box.send_keys(search_topic)


test = SingletonCaseWrapper()
test.Search("bowling balls")
time.sleep(10)
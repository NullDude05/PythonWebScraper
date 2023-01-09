import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Establish chrome web driver and the url
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome = driver.get('https://google.com')

# Singleton Class
class SingletonCaseWrapper:
    __instance = None

    # This method runs everytime the singleton class is used to check if there is another instance of this class
    def __new__(cls):
        if(cls.__instance is None):
            cls.__instance = super(SingletonCaseWrapper, cls).__new__(cls)

        return cls.__instance

    # Search something in Google Search using Selenium
    def Search(self, search_topic, html_attr, name_of_attr):
        search_box = driver.find_element(html_attr, name_of_attr)
        search_box.send_keys(search_topic)

    def GetContentClass(self, class_name, html_tag):
        # Get page source code for bs
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        results = []
        for element in soup.find_all(attrs={'class': class_name}):
            name = element.find(html_tag)
            results.append(name.text)

        return results

    # Click a Button using Selenium
    def Click(self, attr_name, name_of_attr):
        time.sleep(2)
        if attr_name == "id":
            button = driver.find_element(By.ID, name_of_attr)
            button.click()
            print("Clicked Id Button")
        elif attr_name == "name":
            button = driver.find_element(By.NAME, name_of_attr)
            button.click()
            print("Clicked Name Button")
        elif attr_name == "xpath":
            button = driver.find_element(By.XPATH, name_of_attr)
            button.click()
            print("Clicked Xpath Button")
        elif attr_name == "link_text":
            button = driver.find_element(By.LINK_TEXT, name_of_attr)
            button.click()
            print("Clicked Link Text Button")
        elif attr_name == "partial_link_text":
            button = driver.find_element(By.PARTIAL_LINK_TEXT, name_of_attr)
            button.click()
            print("Clicked partial link Button")
        elif attr_name == "tag_name":
            button = driver.find_element(By.TAG_NAME, name_of_attr)
            button.click()
            print("Clicked tag name Button")
        elif attr_name == "class_name":
            button = driver.find_element(By.CLASS_NAME, name_of_attr)
            button.click()
            print("Clicked class name Button")
        elif attr_name == "css_selector":
            button = driver.find_element(By.CSS_SELECTOR, name_of_attr)
            button.click()
            print("Clicked css selector Button")
        else:
            print("could not find button by attribute")

        #implement match case statement
        # match attr_name:
        #     case "id":
        #         button = driver.find_element(By.ID, name_of_id)
        #         button.click()
        #         print("Clicked Id Button")
        #     case _:
        #         print("No attribute given")

    

    



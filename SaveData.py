from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()
FORM_URL = os.getenv("FORM_URL")
class SaveData:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome()
        self.driver.get(FORM_URL)
    def save(self, data_set):
        # inputs = self.driver.find_elements(By.CSS_SELECTOR, value='input')

        for data in data_set:
            print(data['price'], data['link'], data['address'])
            price_input = self.driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input = self.driver.find_element(By.XPATH,
                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

            sleep(1)
            price_input.send_keys(data['price'])
            sleep(1)
            link_input.send_keys(data['link'])
            sleep(1)
            address_input.send_keys(data['address'])
            sleep(1)
            btn_submit = self.driver.find_elements(By.CSS_SELECTOR, "[role='button']")
            print(btn_submit[1].text)
            btn_submit[1].click()
            sleep(2)
            btn_next = self.driver.find_element(By.CSS_SELECTOR, value='a')
            btn_next.click()
            sleep(1)


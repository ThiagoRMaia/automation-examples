from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from util import constants


class Functions:
    def __init__(self):
        pass

    @staticmethod
    def start_selenium():
        chrome_driver = constants.PATHS['chromedriver']
        driver = webdriver.Chrome(chrome_driver)
        return driver

    @staticmethod
    def search_term_wikipedia(driver, term):
        search_field = driver.find_element_by_id('searchInput')
        search_field.send_keys(term)
        search_field.send_keys(Keys.ENTER)

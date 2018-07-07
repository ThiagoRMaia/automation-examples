from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from util import constants
import unittest


class Functions:
    def __init__(self):
        pass

    @staticmethod
    def start_selenium():
        chrome_driver = constants.PATHS['chromedriver']
        driver = webdriver.Chrome(chrome_driver)
        return driver

    @staticmethod
    def search_term(driver, term):
        search_field = driver.find_element_by_id('searchInput')
        search_field.send_keys(term)
        search_field.send_keys(Keys.ENTER)


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = Functions.start_selenium()
        self.driver.get('http://www.wikipedia.org')
        self.elements = constants.ELEMENTS

    def tearDown(self):
        self.driver.close()

    def test_01_check_title(self):
        self.assertEqual(self.driver.title, 'wikipedia', 'Title found: ' + self.driver.title + '\nExpected: wikipedia')

    def test_02_search(self):
        Functions.search_term(self.driver, 'furry rabbits')
        self.assertTrue(self.driver.find_element_by_class_name(self.elements['do_you_mean']))

    def test_03_click_suggestion(self):
        Functions.search_term(self.driver, 'furry rabbits')
        self.driver.find_element_by_id(self.elements['suggestion']).click()
        search_results = self.driver.find_element_by_class_name(self.elements['search_result'])
        children = search_results.find_elements_by_tag_name(self.elements['list_item'])
        self.assertEqual(len(children), 20, 'Elements found: ' + str(len(children)))

    def test_04_check_result_content(self):
        Functions.search_term(self.driver, 'furry rabbits')
        self.driver.find_element_by_id(self.elements['suggestion']).click()
        self.driver.find_element_by_xpath(self.elements['first_result']).click()
        self.assertTrue(self.driver.find_element_by_id(self.elements['title']), 'Title not found')
        self.assertTrue(self.driver.find_element_by_id(self.elements['toc']), 'Table of Contents not found')


if __name__ == '__main__':
    unittest.main()
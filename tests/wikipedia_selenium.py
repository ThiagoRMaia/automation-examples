import sys
import os
import unittest

sys.path.append(os.path.dirname(__file__) + '..')
from util import constants, common_func


class Tests(unittest.TestCase):
    def setUp(self):
        self.elements = constants.WIKIPEDIA_ELEMENTS
        self.functions = common_func.Functions()
        self.driver = self.functions.start_selenium()
        self.driver.get(self.elements['website'])

    def tearDown(self):
        self.driver.close()

    def test_01_check_title(self):
        self.assertEqual(self.driver.title, 'wikipedia', 'Title found: ' + self.driver.title + '\nExpected: wikipedia')

    def test_02_search(self):
        self.functions.search_term_wikipedia(self.driver, 'furry rabbits')
        self.assertTrue(self.driver.find_element_by_class_name(self.elements['do_you_mean']))

    def test_03_click_suggestion(self):
        self.functions.search_term_wikipedia(self.driver, 'furry rabbits')
        self.driver.find_element_by_id(self.elements['suggestion']).click()
        search_results = self.driver.find_element_by_class_name(self.elements['search_result'])
        children = search_results.find_elements_by_tag_name(self.elements['list_item'])
        self.assertEqual(len(children), 20, 'Elements found: ' + str(len(children)))

    def test_04_check_result_content(self):
        self.functions.search_term_wikipedia(self.driver, 'furry rabbits')
        self.driver.find_element_by_id(self.elements['suggestion']).click()
        self.driver.find_element_by_xpath(self.elements['first_result']).click()
        self.assertTrue(self.driver.find_element_by_id(self.elements['title']), 'Title not found')
        self.assertTrue(self.driver.find_element_by_id(self.elements['toc']), 'Table of Contents not found')


if __name__ == '__main__':
    unittest.main()

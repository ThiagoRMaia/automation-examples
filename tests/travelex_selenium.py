import sys
import os
import unittest
from time import sleep

sys.path.append(os.path.dirname(__file__) + '..')
from util import constants, common_func


class Tests(unittest.TestCase):
    def setUp(self):
        self.elements = constants.TRAVELEX_ELEMENTS
        self.functions = common_func.Functions()
        self.driver = self.functions.start_selenium()
        self.driver.get(self.elements['website'])

    def tearDown(self):
        self.driver.close()

    def test_01_check_title(self):
        self.assertIn('Travelex', self.driver.title, 'Title found: ' + self.driver.title)

    def test_02_check_cards(self):
        self.driver.maximize_window()
        self.assertTrue(self.driver.find_element_by_xpath(self.elements['cards']), 'Element not found.')

    def test_03_check_slider(self):
        self.driver.set_window_size(550, 550)
        self.assertTrue(self.driver.find_element_by_xpath(self.elements['slider']), 'Element not found.')

    def test_04_check_third_item(self):
        self.driver.set_window_size(550, 550)
        self.driver.implicitly_wait(10)
        for _ in range(0, 2):
            self.functions.slide_card_travelex(self.driver, self.elements['slider'])
            sleep(0.5)
        find_active_dot = self.functions.find_active_dot_travelex(self.driver, self.elements['dots'],
                                                                  self.elements['dot_item'])
        self.assertEqual(find_active_dot, 2, 'Active card (0 - 3): ' + str(find_active_dot))


if __name__ == '__main__':
    unittest.main()

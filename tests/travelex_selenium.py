from util import constants, common_func
import unittest
from time import sleep


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

    # TODO: Slide left twice and check if third item is displayed


if __name__ == '__main__':
    unittest.main()

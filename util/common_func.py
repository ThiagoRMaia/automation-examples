from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from util import constants
import requests


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

    @staticmethod
    def slide_card_travelex(driver, element):
        slider = driver.find_element_by_xpath(element)
        driver.execute_script("arguments[0].scrollIntoView(true);", slider)
        action = ActionChains(driver)
        action.move_to_element_with_offset(slider, 200, 0).drag_and_drop_by_offset(slider, -200, 0).release().perform()

    @staticmethod
    def find_active_dot_travelex(driver, dots, dot_item):
        dots = driver.find_element_by_class_name(dots)
        children = dots.find_elements_by_tag_name(dot_item)
        for child in children:
            if 'active' in child.get_attribute('class'):
                return children.index(child)

    @staticmethod
    def get_all_posts_from_unique_id(post_type, id_code):
        url = {'posts': 'http://jsonplaceholder.typicode.com/posts?userId={0}'.format(id_code),
               'comments': 'http://jsonplaceholder.typicode.com/comments?postId={0}'.format(id_code)}
        return requests.get(url[post_type]).content

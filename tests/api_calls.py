import sys
import os
import unittest
import requests
import json

sys.path.append(os.path.dirname(__file__) + '..')
from util import constants, common_func


class Tests(unittest.TestCase):
    def setUp(self):
        self.api_data = constants.API_CALLS
        self.functions = common_func.Functions()

    def test_01_check_return_code(self):
        return_code = requests.get('https://jsonplaceholder.typicode.com/posts/1').status_code
        self.assertEqual(return_code, 200, 'Status code found: ' + str(return_code))

    def test_02_check_values(self):
        expected_values = self.api_data['comments']
        return_values = requests.get(expected_values['url']).content
        json_values = json.loads(return_values)

        fields = ['postId', 'id', 'name', 'email', 'body']
        for field in fields:
            received_value = json_values[field]
            expected_value = expected_values[field]
            self.assertEqual(received_value, expected_value,
                             'Received {field_name}: {received}\nExpected {field_name}: {expected}'.format(
                                 field_name=field, received=received_value, expected=expected_value))

    def test_03_check_delete(self):
        test_url = 'https://jsonplaceholder.typicode.com/posts/2'
        return_value = requests.delete(test_url).status_code
        self.assertEqual(return_value, 200, "Couldn't delete data.")
        return_content = requests.get(test_url).text
        self.assertEqual(return_content, '{}', 'Data is not empty: ' + str(return_content))

    def test_04_check_no_content(self):
        test_url = 'https://jsonplaceholder.typicode.com/posts/101'
        return_value = requests.get(test_url).status_code
        self.assertEqual(return_value, 204, "Unexpected return code: " + str(return_value))

    def test_05_get_all_posts_from_userid(self):
        all_posts = self.functions.get_all_posts_from_unique_id('posts', '1')
        all_posts_len = len(json.loads(all_posts))
        self.assertEqual(all_posts_len, 10, 'Unexpected list length: ' + str(all_posts_len))

    def test_06_assert_correct_userid(self):
        requested_id = 50
        all_posts = json.loads(self.functions.get_all_posts_from_unique_id('comments', str(requested_id)))
        ids_collected = []
        for post in all_posts:
            ids_collected.append(post['postId'])
        for found_id in ids_collected:
            self.assertEqual(found_id, requested_id, 'Unexpected postId: '+ str(requested_id))


if __name__ == '__main__':
    unittest.main()

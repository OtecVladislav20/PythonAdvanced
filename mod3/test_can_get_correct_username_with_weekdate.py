import unittest
from mod2.app import app
from freezegun import freeze_time


class TestGetCorrentWeekdate(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("13-03-2023")
    def test_can_get_correct_username_with_weekdate(self):
        name = 'Have a good Wednesday'
        url = self.base_url + name
        response = self.app.get(url)
        response_text = response.data.decode()

        correct_answer = f"Hello, {name}. Have a good Monday"

        self.assertTrue(correct_answer in response_text)

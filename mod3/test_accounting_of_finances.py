import unittest

from mod2.app import app


class TestFinances(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.add_url = '/add/'
        self.calculate_year_url = '/calculate/'

    def test_add(self):
        date = 20001201, 100
        url = self.add_url + '/'.join(str(i) for i in date)
        responce = self.app.get(url)
        responce_text = responce.data.decode()

        self.assertEqual('Ваша дата(2000, 12, 1) и сумма трат за этот день(100) записаны!', responce_text)

    def test_calculate_year(self):
        year = '2000'
        url = self.calculate_year_url + year
        responce = self.app.get(url)
        responce_text = responce.data.decode()

        self.assertEqual(str(700), responce_text)

    def test_calculate_month(self):
        year = '2000'
        month = '/12'
        url = self.calculate_year_url + year + month
        responce = self.app.get(url)
        responce_text = responce.data.decode()

        self.assertEqual(str(300), responce_text)


    'The test breaks when an invalid value is applied'
    def test_bad_add(self):
        date = 200001201, 100
        url = self.add_url + '/'.join(str(i) for i in date)
        responce = self.app.get(url)
        responce_text = responce.data.decode()

        self.assertTrue('Ваша дата(20000, 12, 1) и сумма трат за этот день(100) записаны!' == responce_text)

import unittest

from mod3.work3 import Person


vlad = Person('Vlad', 2003, 'Mendeleeva')
bomj = Person('Vlad', 2003,)


class TestTrustButCheak(unittest.TestCase):
    def test_age(self):
        self.assertTrue(str(20) in str(vlad.get_age()))

    def test_name(self):
        self.assertTrue('Vlad' in str(vlad.get_name()))

    def test_set_name(self):
        vlad.set_name('Vladik')
        self.assertTrue('Vladik' in vlad.get_name())

    def test_get_adress(self):
        self.assertTrue('Mendeleeva' in vlad.get_address())

    def test_set_adress(self):
        vlad.set_address('No')
        self.assertTrue('No' in vlad.get_address())

    def test_homeless(self):
        self.assertTrue('True' in str(vlad.is_homeless()))
        self.assertTrue('False' in str(bomj.is_homeless()))


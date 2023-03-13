import unittest

from mod2.decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def test_get_correct_answer_decrypt(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра........'), '')
        self.assertTrue(decrypt('абр......a.') == 'a')
        self.assertEqual(decrypt('1..2.3'), '23')
        self.assertEqual(decrypt('.'), '')
        self.assertEqual(decrypt('1.......................'), '')
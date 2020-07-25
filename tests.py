from unittest import TestCase
from qazaq_transliterator import translit


class QazaqTransliteratorTestCase(TestCase):
    def test_translit(self):
        self.assertEqual(translit('Қазақ'), 'Qazaq')

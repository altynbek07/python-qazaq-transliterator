from unittest import TestCase
from qazaq_transliterator import translit


class QazaqTransliteratorTestCase(TestCase):
    def test_translit(self):
        self.assertEqual(translit('Қазақстан Республикасы — Шығыс Еуропа мен Орталық Азияда орналасқан мемлекет.'), 'Qazaqstan Respublikasy — Şyğys Europa men Ortalyq Aziiada ornalasqan memleket.')

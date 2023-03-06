import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        with self.assertRaises(ValueError):
            englishToFrench(None)  # test for null input
        # test for the translation of the word 'Hello' and 'Bonjour'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        with self.assertRaises(ValueError):
            frenchToEnglish(None)  # test for null input
        # test for the translation of the word 'Bonjour' and 'Hello'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()

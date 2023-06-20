import unittest
from deep_translator import MyMemoryTranslator

class TranslationTestCase(unittest.TestCase):
   
   
    def test_englishToFrench(self):
        translator = MyMemoryTranslator(source='en', target='fr')

        english_text = "Hello"
        expected_french_text = "Bonjour"
        french_text = translator.translate(english_text)
        self.assertEqual(french_text, expected_french_text)


class TranslationTestCase(unittest.TestCase):
    
    
    def test_frenchToEnglish(self):
        translator = MyMemoryTranslator(source='fr', target='en')
        
        french_text = "Bonjour"
        expected_english_text = "Hello"
        english_text = translator.translate(french_text)
        self.assertEqual(english_text, expected_english_text)


if __name__ == '__main__':
    unittest.main()
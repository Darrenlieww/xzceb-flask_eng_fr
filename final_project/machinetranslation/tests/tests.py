import unittest
from translator import englishToFrench,frenchToEnglish


class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertIsNotNone(englishToFrench("Hello"))
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertIsNotNone(frenchToEnglish("Bonjour"))
        
unittest.main()
import unittest
from translator import english_to_french 
from translator import french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_e2f_hello(self):
        self.assertEqual(english_to_french('What is your name?'),"Quel est votre nom?")
    def test_e2f_hello1(self):
        self.assertNotEqual(english_to_french(0),0)
    def test_e2f_hello2(self):
        self.assertNotEqual(english_to_french('None'),'')

class TestfrenchToEnglish(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e1_hello(self):
        self.assertEqual(french_to_english("Quel est votre nom?"),'What is your name?')
    def test_f2e_hello1(self):
        self.assertNotEqual(french_to_english('None'),'') 
    def test_f2e_hello3(self):
        self.assertNotEqual(french_to_english(0),0) 
unittest.main()  

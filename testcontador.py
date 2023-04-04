import unittest

from contador import count_word

class TestCountWord(unittest.TestCase):
    def test_palabra_simple(self):
        result = count_word("Hola")
        self.assertEqual(result, {'hola': 1})

    def test_cadena_vacia(self):
        result = count_word("")
        self.assertEqual(result, {})

    def test_mayusculas(self):
        result = count_word("Hola MUNDO. hola")
        self.assertEqual(result, {'hola': 2, 'mundo.': 1})
    
if __name__ == '__main__':
    unittest.main()

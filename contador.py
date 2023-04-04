import unittest

#PARTE DEL CODIGO
def count_word(texto):
    result = {}

    palabras = texto.lower().split()
    for palabra in palabras:
        if palabra in result:
            result[palabra] += 1
        else:
            result[palabra] = 1

    return result

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

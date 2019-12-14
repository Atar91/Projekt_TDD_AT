import unittest
import kalkulator

class testy_kalkulator(unittest.TestCase):

    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik, 2)

    def test_odejmowanie(self):
        wynik = kalkulator.odejmij(10,3)
        self.assertEqual(wynik,7)

    def test_dzielenie(self):
        wynik = kalkulator.podziel(21,7)
        self.assertEqual(wynik,3)

    def test_mnozenie(self):
        wynik = kalkulator.pomnoz(3,4)
        self.assertEqual(wynik,12)

if __name__ == '__main__':
    unittest.main()

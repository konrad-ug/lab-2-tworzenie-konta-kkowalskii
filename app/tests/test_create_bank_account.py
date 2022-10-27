from types import NoneType
import unittest
import re

from ..Konto import Konto



class TestCreateBankAccount(unittest.TestCase):
    
    
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "05526589435", "PROM_xyz")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "05526589435", "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")
        if (pierwsze_konto.kod_rabatowy) == NoneType:
            self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        else:
            self.assertTrue((re.search('^PROM_...$', pierwsze_konto.kod_rabatowy)), "Niepoprawny kod rabatowy!")

        self.assertEqual(((int(pierwsze_konto.pesel[2:4]) > 12 and int(pierwsze_konto.pesel[2:4]) < 81)

                        or (int(pierwsze_konto.pesel[0:2]) >= 61 and int(pierwsze_konto.pesel[2:4]) <= 12
                            and int(pierwsze_konto.pesel[2:4]) > 0)) and (pierwsze_konto.saldo == 50) or not ((int(pierwsze_konto.pesel[2:4]) > 12 and int(pierwsze_konto.pesel[2:4]) < 81)

                        or (int(pierwsze_konto.pesel[0:2]) >= 61 and int(pierwsze_konto.pesel[2:4]) <= 12
                            and int(pierwsze_konto.pesel[2:4]) > 0)) and (pierwsze_konto.saldo == 0), True, "Rok urodzenia musi być większy niż 1960!")
    #przepraszam za commit na main branch, zagapiłem się 

    #tutaj proszę dodawać nowe testy


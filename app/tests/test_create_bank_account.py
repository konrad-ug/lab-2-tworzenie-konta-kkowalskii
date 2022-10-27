from types import NoneType
import unittest
import re

from ..Konto import Konto



class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "32134529423"
    kod_rabatowy = "PROM_xyz"
    
    
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel, eslf.)
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "05526589435", "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Niepoprawny pesel!")
        if (pierwsze_konto.kod_rabatowy) == NoneType:
            self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        else:
            self.assertTrue((re.search('^PROM_...$', pierwsze_konto.kod_rabatowy)), "Niepoprawny kod rabatowy!")

        
     

    #tutaj proszę dodawać nowe testy


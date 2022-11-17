from distutils.log import info
import unittest

from  ..Konto import Konto
from  ..Konto import KontoFirmowe

testmsg = "Wartości nie są sobie równe"

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "05526589435", "kod")
        konto_bez_kodu = Konto("Dariusz", "Januszewski", "05526589435")

        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "05526589435", "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.kod_rabatowy, "kod", "Kod rabatowy nie został zapisany!")
        self.assertEqual(konto_bez_kodu.kod_rabatowy, None, "Niepoprawna wartość w miejscu kodu rabatowego")



    #kod_rabatowy








        
        

        
from ..Konto import Konto
import unittest

class Test_Kod_Rabatowy(unittest.TestCase):

    def test_kod_rabatowy(self):
        # kody które powinny przyznać 50 złotych
        poprawny_litery = Konto("Kosma", "Kowalski", "80042971412", "PROM_XYZ")
        poprawny_cyfry = Konto("Kosma", "Kowalski", "80042971412", "PROM_123")
        poprawny_znaki = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")
        poprawny_rok = Konto("Kosma", "Kowalski", "00602971412", "PROM_!?*")

        self.assertEqual(poprawny_litery.saldo, 50, 'Niepoprawne saldo')
        self.assertEqual(poprawny_cyfry.saldo, 50, 'Niepoprawne saldo')
        self.assertEqual(poprawny_znaki.saldo, 50, 'Niepoprawne saldo')
        self.assertEqual(poprawny_rok.saldo, 50, 'Niepoprawne saldo')

        # kody które nie powinny przyznać 50 złotych
        za_dlugi_pesel = Konto("Kosma", "Kowalski", "0552658943321")
        bez_kodu_rabatowego = Konto("Kosma", "Kowalski", "0552658943")
        poprawny_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ")
        zly_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM")
        za_dlugi_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ1")
        za_krotki_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XY")
        kod_rabatowy_male_litery = Konto("Kosma", "Kowalski", "0552658943", "prom_XYZ")
        urodzony_w_1960 = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")

        self.assertEqual(za_dlugi_pesel.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(bez_kodu_rabatowego.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(poprawny_kod_rabatowy.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(zly_kod_rabatowy.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(za_dlugi_kod_rabatowy.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(za_krotki_kod_rabatowy.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(kod_rabatowy_male_litery.saldo, 0, 'Niepoprawne saldo')
        self.assertEqual(urodzony_w_1960.saldo, 0, 'Niepoprawne saldo')
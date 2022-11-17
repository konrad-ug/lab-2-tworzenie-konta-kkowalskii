from ..Konto import Konto
import unittest

class Test_Kredyt(unittest.TestCase):

    def test_kredyt(self):
        konto_na_kredyt = Konto("Kosma", "Kowalski", "012034432653")
        konto_z_50pln_z_kodu = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")

        konto_na_kredyt.zaciagnij_kredyt(1000)
        self.assertEqual(konto_na_kredyt.saldo, 0, "kredyt zostal udzielony mimo za krotkiej historii przelewow")

        #uzupelniamy historie przelewow konta
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_na_kredyt, 5)
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_na_kredyt, 5)
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_na_kredyt, 5)

        konto_na_kredyt.zaciagnij_kredyt(1000)
        self.assertEqual(konto_na_kredyt.saldo, 1015, "kredyt nie zostal udzielony mimo spelnionych wymagan")




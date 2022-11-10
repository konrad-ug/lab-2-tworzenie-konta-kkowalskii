import unittest

from  ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    def test_historia(self):
        konto_z_50pln_z_kodu = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")
        konto_puste = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)
        self.assertEqual(konto_z_50pln_z_kodu.historia_przelewow[0], -30, "historia przelewów nie zapisuje się prawidłowo")
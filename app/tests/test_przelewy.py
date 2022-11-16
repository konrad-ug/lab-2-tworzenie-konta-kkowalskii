from ..Konto import Konto
import unittest

class Test_Przelewy(unittest.TestCase):
    def test_przelewy(self):
        konto_z_50pln_z_kodu = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")
        konto_puste = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")

        fakeKonto = {}
        fakeKonto['pesel'] = "1112223334"
        fakeKonto['imie'] = "fake"
        fakeKonto['nazwisko'] = "Konto"
        fakeKonto['historia_przelewow'] = []

        # proba przelewu na zly obiekt
        konto_z_50pln_z_kodu.przelew_wychodzacy(fakeKonto, 60101866617, 30)
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 50, "Przelew przeszedł mimo obiektu nienalezacego do klasy Konto")

        # przelew wychodzący o kwocie 30 pln
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)

        self.assertEqual(konto_puste.saldo, 30, "Przelew nie dodał pieniędzy na konto docelowe")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 20, "Przelew nie odjął pieniędzy nadawcy przelewu")

        # przelew wychodzący (ekspresowy) o kwocie 10 pln
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 20, True)
        self.assertEqual(konto_z_50pln_z_kodu.saldo, -1, "Przelew odjął niepoprawną wartość")

        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)

        self.assertEqual(konto_z_50pln_z_kodu.historia_przelewow[1], -20,"historia przelewów nie zapisuje się prawidłowo")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, -1, "Przelew odjął pieniądze z konta mimo niewystarczających środków")


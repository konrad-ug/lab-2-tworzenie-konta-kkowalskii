import unittest
from ..Konto import KontoFirmowe

class TestNIP(unittest.TestCase):
    def test_konto_firmowe(self):
        kfirmowe1 = KontoFirmowe('hello', "0234563452")

        self.assertEqual(kfirmowe1.saldo, 1000, "Saldo konta firmowego nie zapisało się poprawnie")
        self.assertEqual(kfirmowe1.historia_przelewow, [], "Historia przelewow nie utworzyła się poprawnie")
        self.assertEqual(kfirmowe1.nazwa, "hello", "Nazwa firmy nie zapisała się poprawnie")
        self.assertEqual(kfirmowe1.NIP, "0234563452", "NIP nie zapisał się poprawnie")



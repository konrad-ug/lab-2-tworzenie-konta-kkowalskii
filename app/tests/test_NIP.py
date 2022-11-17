import unittest
from ..Konto import KontoFirmowe

class TestNIP(unittest.TestCase):

    def test_NIP(self):
        za_krotki_NIP = KontoFirmowe("wiesbud", "044")
        za_dlugi_NIP = KontoFirmowe("wiesbud", "11223344556677")
        niepoprawny_NIP = KontoFirmowe("wiesbud", "01nieNIP05")

        self.assertEqual(za_krotki_NIP.NIP, "Niepoprawny NIP!", "Komunikat o błędzie nie zapisał się poprawnie")
        self.assertEqual(za_dlugi_NIP.NIP, "Niepoprawny NIP!", "Komunikat o błędzie nie zapisał się poprawnie")
        self.assertEqual(niepoprawny_NIP.NIP, "Niepoprawny NIP!", "Komunikat o błędzie nie zapisał się poprawnie")
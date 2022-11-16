from ..Konto import Konto
import unittest

class TestPesel(unittest.TestCase):
    def test_numer_pesel(self):
        za_krotki_pesel = Konto("Kosma", "Kowalski", "0552658943")
        za_dlugi_pesel = Konto("Kosma", "Kowalski", "055265894359")
        pusty_pesel = Konto("Kosma", "Kowalski", "")
        pesel_z_niedozwolonymi_znakami = Konto("Kosma", "Kowalski", "055265io435")
        pesel_nie_isDigit = Konto("Kosma", "Kowalski", "cokolwiek")

        # testy które kończą się niepowodzeniem
        self.assertEqual(za_krotki_pesel.pesel, "Niepoprawny pesel!", "Komunikat nie zapisal sie poprawnie")
        self.assertEqual(za_dlugi_pesel.pesel, "Niepoprawny pesel!", "Komunikat nie zapisal sie poprawnie")
        self.assertEqual(pusty_pesel.pesel, "Niepoprawny pesel!", "Komunikat nie zapisal sie poprawnie")
        self.assertEqual(pesel_z_niedozwolonymi_znakami.pesel, "Niepoprawny pesel!", "Komunikat nie zapisal sie poprawnie")
        self.assertEqual(pesel_nie_isDigit.pesel, "Niepoprawny pesel!", "Komunikat nie zapisal sie poprawnie")
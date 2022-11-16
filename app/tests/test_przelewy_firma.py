from ..Konto import KontoFirmowe
import unittest

class TestCreateBankAccountCompany(unittest.TestCase):

    def test_przelew_firmowy(self):
        kfirmowe1 = KontoFirmowe('hello', "0234563452")
        firmowe = KontoFirmowe("wiesbud", "0443322210")

        # próba wykonania przelewu do obiektu nienależącego do klasy KontoFirmowe lub Konto

        fakeKonto = {}
        fakeKonto['NIP'] = "1112223334"
        fakeKonto['nazwa'] = "fakeKonto"
        fakeKonto['historia_przelewow'] = []

        # przelew na błędny obiekt
        kfirmowe1.przelew_firma(fakeKonto, 200, True)
        self.assertEqual(kfirmowe1.saldo, 1000, "Kwota została odjęta mimo złego odbiorcy")

        kfirmowe1.przelew_firma(firmowe, 500)
        self.assertEqual(kfirmowe1.saldo, 500, "Kwota nie została odjęta prawidłowo")

        kfirmowe1.przelew_firma(firmowe, 500, True)
        self.assertEqual(kfirmowe1.saldo, -5, "Kwota nie została odjęta prawidłowo")
        self.assertEqual(firmowe.saldo, 2000, "Kwota nie została przesłana prawidłowo")
        self.assertEqual(firmowe.historia_przelewow[0], 500, "Historia przelewu nie została zapisana prawidłowo")
        self.assertEqual(kfirmowe1.historia_przelewow[0], -500, "Niepoprawna wiadomosc zostala zapisana do historii przelewow")

        # próba przelewu kiedy saldo jest zbyt małe
        kfirmowe1.przelew_firma(firmowe, 1000)
        self.assertEqual(kfirmowe1.saldo, -5, "Saldo nadawcy zostało zmienione mimo niewystarczających środków do wykonania przelwu")
        self.assertEqual(firmowe.saldo, 2000, "Saldo odbiorcy zostało zmienione mimo niewystarczających środków nadawcy")
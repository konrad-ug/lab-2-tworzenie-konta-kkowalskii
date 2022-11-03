from distutils.log import info
import unittest

from  ..Konto import Konto
from  ..Konto import KontoFirmowe

testmsg = "Wartości nie są sobie równe"

class TestCreateBankAccount(unittest.TestCase):
    
    
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "05526589435")

        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, "05526589435", "Pesel nie został zapisany!")

    def test_numer_pesel(self):
        
        za_krotki_pesel = Konto("Kosma", "Kowalski", "0552658943")
        za_dlugi_pesel = Konto("Kosma", "Kowalski", "055265894359")
        pusty_pesel = Konto("Kosma", "Kowalski", "")
        pesel_z_niedozwolonymi_znakami = Konto("Kosma", "Kowalski", "055265io435")
    
        #testy które kończą się niepowodzeniem
        self.assertEqual(za_krotki_pesel.pesel, "Niepoprawny pesel!", testmsg)
        self.assertEqual(za_dlugi_pesel.pesel, "Niepoprawny pesel!", testmsg)
        self.assertEqual(pusty_pesel.pesel, "Niepoprawny pesel!", testmsg)
        self.assertEqual(pesel_z_niedozwolonymi_znakami.pesel, "Niepoprawny pesel!", testmsg)

    #kod_rabatowy

    def test_kod_rabatowy(self):
        #kody które powinny przyznać 50 złotych
        poprawny_litery =  Konto("Kosma", "Kowalski", "80042971412", "PROM_XYZ")
        poprawny_cyfry = Konto("Kosma", "Kowalski", "80042971412", "PROM_123")
        poprawny_znaki = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")

        self.assertEqual(poprawny_litery.saldo, 50, testmsg)
        self.assertEqual(poprawny_cyfry.saldo, 50, testmsg)
        self.assertEqual(poprawny_znaki.saldo, 50, testmsg)

        #kody które nie powinny przyznać 50 złotych
        poprawny_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ")
        zly_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM")
        za_dlugi_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ1")
        za_krotki_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XY")
        kod_rabatowy_male_litery = Konto("Kosma", "Kowalski", "0552658943", "prom_XYZ")
        urodzony_przed_1960 = Konto("Kosma", "Kowalski", "03051419333", "prom_XYZ")
        urodzony_w_1960 = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")

        self.assertEqual(poprawny_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(zly_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(za_dlugi_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(za_krotki_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(kod_rabatowy_male_litery.saldo, 0, testmsg)
        self.assertEqual(urodzony_przed_1960.saldo, 0, testmsg)
        self.assertEqual(urodzony_w_1960.saldo, 0, testmsg)

    def test_przelewy(self):
        konto_z_50pln_z_kodu = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")
        konto_puste = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")

        #przelew wychodzący o kwocie 30 pln
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)

        self.assertEqual(konto_puste.saldo, 30, "Przelew nie dodał pieniędzy na konto docelowe")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 19, "Przelew nie odjął pieniędzy nadawcy przelewu")

        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)


        self.assertEqual(konto_z_50pln_z_kodu.historia_przelewow[1], "nieudana proba wykonania przelewu, powód: kwota wyższa od stanu konta")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 19, "Przelew odjął pieniądze z konta mimo niewystarczających środków")

    def test_przelew_firmowy(self):
        kfirmowe1 = KontoFirmowe('hello', "0234563452")
        firmowe = KontoFirmowe("wiesbud", "0443322210")
        kfirmowe1.przelew_firma(firmowe, '0443322210', 1000)
        self.assertEqual(kfirmowe1.saldo, -5, "Kwota nie została odjęta prawidłowo")
        self.assertEqual(firmowe.saldo, 2000, "Kwota nie została przesłana prawidłowo")
        self.assertEqual(kfirmowe1.historia_przelewow[0], 'przelew wychodzący do odbiorcy: wiesbud, kwota: 1000', "Niepoprawna wiadomosc zostala zapisana do historii przelewow")
        
        #próba przelewu kiedy saldo jest zbyt małe
        kfirmowe1.przelew_firma(firmowe, '0443322210', 1000)
        self.assertEqual(firmowe.saldo, 2000, "Kwota została przesłana mimo niewystarczających środków nadawcy")
        self.assertEqual(kfirmowe1.historia_przelewow[1], 'nieudana proba wykonania przelewu, powód: kwota wyższa od stanu konta', "Niepoprawna wiadomosc zostala zapisana do historii przelewow")
        
        

        
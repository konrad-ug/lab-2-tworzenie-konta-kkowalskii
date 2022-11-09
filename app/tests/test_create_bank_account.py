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
        poprawny_rok = Konto("Kosma", "Kowalski", "00602971412", "PROM_!?*")

        self.assertEqual(poprawny_litery.saldo, 50, testmsg)
        self.assertEqual(poprawny_cyfry.saldo, 50, testmsg)
        self.assertEqual(poprawny_znaki.saldo, 50, testmsg)
        self.assertEqual(poprawny_rok.saldo, 50, testmsg)

        #kody które nie powinny przyznać 50 złotych
        za_dlugi_pesel = Konto("Kosma", "Kowalski", "0552658943321")
        bez_kodu_rabatowego = Konto("Kosma", "Kowalski", "0552658943")
        poprawny_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ")
        zly_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM")
        za_dlugi_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XYZ1")
        za_krotki_kod_rabatowy = Konto("Kosma", "Kowalski", "0552658943", "PROM_XY")
        kod_rabatowy_male_litery = Konto("Kosma", "Kowalski", "0552658943", "prom_XYZ")
        urodzony_przed_1960 = Konto("Kosma", "Kowalski", "03051419333", "prom_XYZ")
        urodzony_w_1960 = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")


        self.assertEqual(za_dlugi_pesel.saldo, 0, testmsg)
        self.assertEqual(bez_kodu_rabatowego.saldo, 0, testmsg)
        self.assertEqual(poprawny_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(zly_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(za_dlugi_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(za_krotki_kod_rabatowy.saldo, 0, testmsg)
        self.assertEqual(kod_rabatowy_male_litery.saldo, 0, testmsg)
        self.assertEqual(urodzony_przed_1960.saldo, 0, testmsg)
        self.assertEqual(urodzony_w_1960.saldo, 0, testmsg)

    def test_konto_firmowe(self):
        kfirmowe1 = KontoFirmowe('hello', "0234563452")

        self.assertEqual(kfirmowe1.saldo, 1000, "Saldo konta firmowego nie zapisało się poprawnie")
        self.assertEqual(kfirmowe1.historia_przelewow, [], "Historia przelewow nie utworzyła się poprawnie")
        self.assertEqual(kfirmowe1.nazwa, "hello", "Nazwa firmy nie zapisała się poprawnie")
        self.assertEqual(kfirmowe1.NIP, "0234563452", "NIP nie zapisał się poprawnie")

    def test_NIP(self):

        za_krotki_NIP = KontoFirmowe("wiesbud", "044")
        za_dlugi_NIP = KontoFirmowe("wiesbud", "11223344556677")
        niepoprawny_NIP = KontoFirmowe("wiesbud", "01nieNIP05")

        self.assertEqual(za_krotki_NIP.NIP, "Niepoprawny NIP!", testmsg)
        self.assertEqual(za_dlugi_NIP.NIP, "Niepoprawny NIP!", testmsg)
        self.assertEqual(niepoprawny_NIP.NIP, "Niepoprawny NIP!", testmsg)



    def test_przelewy(self):
        konto_z_50pln_z_kodu = Konto("Kosma", "Kowalski", "80042971412", "PROM_!?*")
        konto_puste = Konto("Kosma", "Kowalski", "60101866617", "prom_XYZ")

        fakeKonto = {}
        fakeKonto['pesel'] = "1112223334"
        fakeKonto['imie'] = "fake"
        fakeKonto['nazwisko'] = "Konto"
        fakeKonto['historia_przelewow'] = []

        #proba przelewu na zly obiekt
        konto_z_50pln_z_kodu.przelew_wychodzacy(fakeKonto, 60101866617, 30)
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 50, "Przelew przeszedł mimo obiektu nienalezacego do klasy Konto")

        #przelew wychodzący o kwocie 30 pln
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)

        self.assertEqual(konto_puste.saldo, 30, "Przelew nie dodał pieniędzy na konto docelowe")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, 20, "Przelew nie odjął pieniędzy nadawcy przelewu")

        # przelew wychodzący (ekspresowy) o kwocie 10 pln
        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 20, True)
        self.assertEqual(konto_z_50pln_z_kodu.saldo, -1, "Przelew odjął niepoprawną wartość")

        konto_z_50pln_z_kodu.przelew_wychodzacy(konto_puste, 60101866617, 30)


        self.assertEqual(konto_z_50pln_z_kodu.historia_przelewow[1], -20, "historia przelewów nie zapisuje się prawidłowo")
        self.assertEqual(konto_z_50pln_z_kodu.saldo, -1, "Przelew odjął pieniądze z konta mimo niewystarczających środków")

    def test_przelew_firmowy(self):
        kfirmowe1 = KontoFirmowe('hello', "0234563452")
        firmowe = KontoFirmowe("wiesbud", "0443322210")

        # próba wykonania przelewu do obiektu nienależącego do klasy KontoFirmowe lub Konto

        fakeKonto = {}
        fakeKonto['NIP'] = "1112223334"
        fakeKonto['nazwa'] = "fakeKonto"
        fakeKonto['historia_przelewow'] = []

        #przelew na błędny obiekt
        kfirmowe1.przelew_firma(fakeKonto, '0443322210', 200, True)
        self.assertEqual(kfirmowe1.saldo, 1000, "Kwota została odjęta mimo złego odbiorcy")


        kfirmowe1.przelew_firma(firmowe, '0443322210', 500)
        self.assertEqual(kfirmowe1.saldo, 500, "Kwota nie została odjęta prawidłowo")


        kfirmowe1.przelew_firma(firmowe, '0443322210', 500, True)
        self.assertEqual(kfirmowe1.saldo, -5, "Kwota nie została odjęta prawidłowo")
        self.assertEqual(firmowe.saldo, 2000, "Kwota nie została przesłana prawidłowo")
        self.assertEqual(firmowe.historia_przelewow[0], 500, "Historia przelewu nie została zapisana prawidłowo")
        self.assertEqual(kfirmowe1.historia_przelewow[0], -500, "Niepoprawna wiadomosc zostala zapisana do historii przelewow")

        #próba przelewu kiedy saldo jest zbyt małe
        kfirmowe1.przelew_firma(firmowe, '0443322210', 1000)
        self.assertEqual(kfirmowe1.saldo, -5, "Saldo nadawcy zostało zmienione mimo niewystarczających środków do wykonania przelwu")
        self.assertEqual(firmowe.saldo, 2000, "Saldo odbiorcy zostało zmienione mimo niewystarczających środków nadawcy")




""""
        elif odbiorca.NIP != str(NIP):
            print("nieudana proba wykonania przelewu, powód: podany NIP był nieprawidłowy")
        elif not isinstance(odbiorca, KontoFirmowe):
            print("nieudana proba wykonania przelewu, powód: podane konto nie istnieje")
        else:
            print("nieudana proba wykonania przelewu, powód: nieznany")


"""
        
        

        
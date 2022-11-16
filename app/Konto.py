import re

def between_two_numbers(min, max, number):
    if number >= min and number <= max:
        return True
    else:
        return False


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.kod_rabatowy = kod_rabatowy
        self.historia_przelewow = []

        #mechanizm sprawdzania poprawnosci numeru pesel
        if pesel.isdigit() == True and len(pesel) == 11:
            self.pesel = pesel
        elif len(pesel) < 11:
            self.pesel = "Niepoprawny pesel!"
        elif len(pesel) > 11:
            self.pesel = "Niepoprawny pesel!"
        elif pesel.isdigit() == False:
            self.pesel = "Niepoprawny pesel!"
        
        #mechanizm odpowiedzialny za sprawdzanie kodu rabatowego i ewentualne przydzielanie określonej kwoty
        if (self.kod_rabatowy) and (len(self.pesel) == 11):
            if (bool(re.search('^PROM_...$', kod_rabatowy))) == True:
                    #people born after 1960
                if between_two_numbers(13, 80, int(self.pesel[2:4])) or (int(self.pesel[0:2]) >= 61 and between_two_numbers(1, 12, int(self.pesel[2:4]))):
                    self.saldo = 50



                    #print('z kodu rabatowego mogą korzystać tylko osoby urodzone po 1960 roku!')


    def przelew_wychodzacy(self, odbiorca, pesel, kwota, ekspresowy: bool = False):

        if isinstance(odbiorca, Konto):
            if self.saldo >= kwota and odbiorca.pesel == str(pesel):
                odbiorca.saldo += kwota

                if ekspresowy == True:
                    self.saldo -= (kwota + 1)
                elif ekspresowy == False:
                    self.saldo -= kwota

                dohistorii = -kwota
                self.historia_przelewow.append(dohistorii)
                odbiorca.historia_przelewow.append(kwota)
            else:
                return

        else:
            return
    def zaciagnij_kredyt(self, kwota):
        if len(self.historia_przelewow) < 3:
            return False
        if self.historia_przelewow[-3] > 0 and self.historia_przelewow[-2] > 0 and self.historia_przelewow[-1] > 0:
            self.saldo += kwota
            return True



class KontoFirmowe:
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        self.saldo = 1000
        self.historia_przelewow = []

        if len(NIP) == 10 and NIP.isdigit():
            self.NIP = NIP
        else:
            self.NIP = "Niepoprawny NIP!"


    def przelew_firma(self, odbiorca, NIP, kwota, ekspresowy: bool = False):

        if isinstance(odbiorca, KontoFirmowe):
            if self.saldo >= kwota and odbiorca.NIP == NIP:
                odbiorca.saldo += kwota

                if ekspresowy == True:
                    self.saldo -= (kwota + 5)
                elif ekspresowy == False:
                    self.saldo -= kwota
                dohistorii = -kwota
                self.historia_przelewow.append(dohistorii)
                odbiorca.historia_przelewow.append(kwota)
            else: return
        else:
            return





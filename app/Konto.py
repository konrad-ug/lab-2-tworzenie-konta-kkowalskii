import re
from datetime import date

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
        if pesel.isdigit() and len(pesel) == 11:
            self.pesel = pesel
        elif len(pesel) < 11:
            self.pesel = "Niepoprawny pesel!"
        elif len(pesel) > 11:
            self.pesel = "Niepoprawny pesel!"
        elif pesel.isdigit() == False:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = "Niepoprawny pesel!"
        
        #mechanizm odpowiedzialny za sprawdzanie kodu rabatowego i ewentualne przydzielanie określonej kwoty
        if (self.kod_rabatowy) and (len(self.pesel) == 11):
            if (bool(re.search('^PROM_...$', kod_rabatowy))) == True:
                    #people born after 1960 
                if between_two_numbers(13, 80, int(self.pesel[2:4])) or (int(self.pesel[0:2]) >= 61 and between_two_numbers(1, 12, int(self.pesel[2:4]))):
                    self.saldo = 50
                    
                    #people born between 1900 and 1960
                elif between_two_numbers(1, 12, int(self.pesel[2:4])) and between_two_numbers(1, 60, int(self.pesel[0:2])):
                    self.saldo = 0
                    #print('z kodu rabatowego mogą korzystać tylko osoby urodzone po 1960 roku!')   
        else:
            self.saldo = 0

    def przelew_wychodzacy(self, odbiorca, pesel, kwota):
        if self.saldo >= kwota and odbiorca.pesel == str(pesel) and isinstance(odbiorca, Konto):
            odbiorca.saldo += kwota
            self.saldo -= (kwota + 1)
            
            self.historia_przelewow.append("przelew wychodzący do odbiorcy: " + odbiorca.imie + " " + odbiorca.nazwisko + ", kwota: " + str(kwota))
            odbiorca.historia_przelewow.append("przelew przychodzący od: " + self.imie + " " + self.nazwisko + ", kwota: " + str(kwota))
        elif self.saldo < kwota:
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: kwota wyższa od stanu konta")
            return
        elif odbiorca.pesel != str(pesel):
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: podany pesel był nieprawidłowy")
        elif not isinstance(odbiorca, Konto):
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: podane konto nie istnieje")
        else:
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: nieznany")

class KontoFirmowe:
    def __init__(self, nazwa, NIP):
        self.nazwa = nazwa
        if len(NIP) == 10 and NIP.isdigit():
            self.NIP = NIP
        else:
            self.NIP = "Niepoprawny NIP!"
        self.saldo = 1000
        self.historia_przelewow = []

    def przelew_firma(self, odbiorca, NIP, kwota):
        if self.saldo >= kwota and odbiorca.NIP == NIP and isinstance(odbiorca, KontoFirmowe):
            odbiorca.saldo += kwota
            self.saldo -= (kwota + 5)
            self.historia_przelewow.append("przelew wychodzący do odbiorcy: " + odbiorca.nazwa + ", kwota: " + str(kwota))
            odbiorca.historia_przelewow.append("przelew przychodzący od: " + self.nazwa + ", kwota: " + str(kwota))

        elif self.saldo < kwota:
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: kwota wyższa od stanu konta")
            return

        elif odbiorca.NIP != str(NIP):
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: podany NIP był nieprawidłowy")
        elif not isinstance(odbiorca, KontoFirmowe):
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: podane konto nie istnieje")
        else:
            self.historia_przelewow.append("nieudana proba wykonania przelewu, powód: nieznany")



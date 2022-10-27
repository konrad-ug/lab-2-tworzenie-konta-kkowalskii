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
        self.pesel = pesel
        self.kod_rabatowy = kod_rabatowy
        if (self.kod_rabatowy) and (self.pesel):
            if (bool(re.search('^PROM_...$', kod_rabatowy))) == True:
                if between_two_numbers(13, 80, int(self.pesel[2:4])) or (int(self.pesel[0:2]) >= 61 and between_two_numbers(1, 12, int(self.pesel[2:4]))):
                    self.saldo = 50
                elif between_two_numbers(1, 12, int(self.pesel[2:4]))


            
                self.saldo = 50
        

        (((int(pierwsze_konto.pesel[2:4]) > 12 and int(pierwsze_konto.pesel[2:4]) < 81)

                        or (int(pierwsze_konto.pesel[0:2]) >= 61 and int(pierwsze_konto.pesel[2:4]) <= 12 ### wlasnie tutaj skonczylem
                            and int(pierwsze_konto.pesel[2:4]) > 0)) and (pierwsze_konto.saldo == 50) or not ((int(pierwsze_konto.pesel[2:4]) > 12 and int(pierwsze_konto.pesel[2:4]) < 81)

                        or (int(pierwsze_konto.pesel[0:2]) >= 61 and int(pierwsze_konto.pesel[2:4]) <= 12
                            and int(pierwsze_konto.pesel[2:4]) > 0)) and (pierwsze_konto.saldo == 0), True, "Rok urodzenia musi być większy niż 1960!")
        


class Dieta:
    def __init__(self, liczba_kalorii, liczba_posilkow, cena, wege):
        self._liczba_kalorii = liczba_kalorii
        self._liczba_posilkow = liczba_posilkow
        self._cena = cena
        self._wege = wege

    def get_liczba_kalorii(self):
        return self._liczba_kalorii

    def get_liczba_posilkow(self):
        return self._liczba_posilkow

    def get_cena(self):
        return self._cena

    def get_wege(self):
        return self._wege

class Osoba:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self._nazwisko = nazwisko

    def get_imie(self):
        return self._imie

    def get_nazwisko(self):
        return self._nazwisko

class Pacjent(Osoba):
    def __init__(self, imie, nazwisko, waga, wzrost, wiek):
        super().__init__(imie, nazwisko)
        self._waga = waga
        self._wzrost = wzrost
        self._wiek = wiek

    def get_waga(self):
        return self._waga

    def get_wzrost(self):
        return self._wzrost

    def get_wiek(self):
        return self._wiek

class Dietetyk(Osoba):
    def __init__(self, imie, nazwisko, nr_gabinetu, lata_doswiadczenia):
        super().__init__(imie, nazwisko)
        self._nr_gabinetu = nr_gabinetu
        self._lata_doswiadczenia = lata_doswiadczenia

    def get_nr_gabinetu(self):
        return self._nr_gabinetu

    def get_lata_doswiadczenia(self):
        return self._lata_doswiadczenia


class Zamowienie:
    def __init__(self):
        self._imie = 'fname'
        self._nazwisko = 'lname'
        self._diety = []
        self._cena = 0

    def get_diety(self):
        return self._diety

    def get_imie(self):
        return self._imie

    def get_nazwisko(self):
        return self._nazwisko

    def set_diety(self, diety):
        self._diety = diety

    def set_imie(self, imie):
        self._imie = imie

    def set_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    diety = property(get_diety, set_diety)
    imie = property(get_imie, set_imie)
    nazwisko = property(get_nazwisko, set_nazwisko)

    def wylicz_kalorie(self):
        liczba_kalorii = 0
        for dieta in self.diety:
            liczba_kalorii += dieta._liczba_kalorii
        return  liczba_kalorii

    def wylicz_cene(self):
        cena = 0
        for dieta in self.diety:
            cena += dieta._cena
        return round(cena, 2)

zamowienie = Zamowienie()
pacjent = Pacjent('Agnieszka', 'Zarzecka', 55, 175, 23)
dieta1 = Dieta(1200, 3, 300, False)
dieta2 = Dieta(3000, 5, 700, True)
zamowienie.set_imie(pacjent.get_imie())
zamowienie.set_nazwisko(pacjent.get_nazwisko())
zamowienie.set_diety([dieta1, dieta2])

print(zamowienie.__dict__)
print('Liczba kalorii: ' + str(zamowienie.wylicz_kalorie()))
print('Cena: ' + str(zamowienie.wylicz_cene()))

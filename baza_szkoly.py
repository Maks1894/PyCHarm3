class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
    def __repr__(self):
        return f"Uczen {self.imie} {self.nazwisko} klasa: {self.klasa}"
class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy
    def __repr__(self):
        return (f" Nauczyciel {self.imie} {self.nazwisko} - przedmiot: {self.przedmiot}, klasy:{self.klasy} ")
class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
    def __repr__(self):
        return f"Wychowawca {self.imie} {self.nazwisko} klasa: {self.klasa}"
uczniowie = [
    Uczen(imie="Lera", nazwisko= "Petrova", klasa="10B"),
    Uczen(imie="Maks", nazwisko= "Pychtin", klasa="10B"),
    Uczen(imie="Dina", nazwisko= "Komowa", klasa="9B"),
    Uczen(imie="Gosza", nazwisko= "Molin", klasa="9B")
]
nauczyciele = [
    Nauczyciel(imie="Marta", nazwisko= "Petrovna",przedmiot= "chemia", klasy=["10B", "9B", "1A", "9B"]),
    Nauczyciel(imie="Vika", nazwisko="Loma", przedmiot= "historia", klasy=["9B", "7B", "3D"])
]
wychowawce = [
    Wychowawca(imie="Agata", nazwisko= "Bedina", klasa="10B"),
    Wychowawca(imie="Anzela", nazwisko= "Volina", klasa="9B"),
]
def wczytaj_ucznia():
    imie = input("Podaj imie: ").capitalize()
    nazwisko = input("Podaj nazwisko: ").capitalize()
    klasa = input("Podaj klase: ").upper()

    nowy_u = Uczen(imie, nazwisko, klasa)
    return nowy_u

def wczytaj_nauczycielia():
    imie = input("Podaj imie: ").capitalize()
    nazwisko = input("Podaj nazwisko: ").capitalize()
    przedmiot = input("Podaj przedmiot: ").lower()
    klasy = []
    print ('Podaj klasy(pusta linia konczy)')
    while True:
        klasa =  input().upper()
        if klasa == "":
            break
        klasy.append(klasa)
    nowy_n = Nauczyciel(imie, nazwisko, przedmiot, klasy)
    return nowy_n
def wczytaj_wychowawca():
    imie = input("Podaj imie: ").capitalize()
    nazwisko = input("Podaj nazwisko: ").capitalize()
    klasa = input("Podaj klase: ").upper()

    nowy_w = Wychowawca(imie, nazwisko, klasa)
    return nowy_w
while True:
    akcja = input("Co chcesz zrobic?[utworz, zarzadzaj, kociec]: ").lower()
    if akcja == "koniec":
        print("Wpisales \"koniec\" ")
        break
    elif akcja == "utworz" :

        while True:
            opcja = input("Podaj opcje ktora chcesz wybrac [uczen, nauczyciel, wychowawca, koniec.]: ").lower()
            if opcja == "koniec":
                print("Wpisales \"koniec\" ")
                break

            elif opcja == "uczen":
                print("Dodaj ucznia")
                nowy_pracownik = wczytaj_ucznia()
                uczniowie.append(nowy_pracownik)
            elif opcja == "nauczyciel":
                print("Dodaj nauczycilia")
                nowy_nauczyciel = wczytaj_nauczycielia()
                nauczyciele.append(nowy_nauczyciel)
            elif opcja == "wychowawca":
                print("Dodaj wychowawca")
                nowy_wychoiwawca = wczytaj_wychowawca()
                wychowawce.append(nowy_wychoiwawca)
            else:
                print(f"Nie istnieje opcji {opcja}, wpisz poprawna [klasa, uczen, nauczyciel, wychowawca, koniec.]")

    elif akcja == "zarzadzaj":
        while True :
            opcja = input("Podaj opcje ktora chcesz wybrac [klasa, uczen, nauczyciel, wychowawca, koniec.]: ").lower()
            if opcja == "koniec":
                print("Wpisales \"koniec\" ")
                break
            elif opcja == "klasa":
                klasa= input("Wpisz klase ktora chcesz wyswietlic: ").upper()
                print(f"Klasa {klasa}:")
                for uczen in  uczniowie  :
                    if uczen.klasa == klasa :
                        print(uczen.imie, uczen.nazwisko)
                for wychowawca in wychowawce:
                    if wychowawca.klasa == klasa:
                        print(f"Wychowawca: {wychowawca.imie}, {wychowawca.nazwisko}")
            elif opcja == "uczen":
                imie_ucznia = input( "Podaj imie ucznia ").capitalize()
                nazwisko_ucznia = input("Podaj  nazwisko ucznia ").capitalize()
                for uczen in uczniowie:
                    if uczen.imie == imie_ucznia and uczen.nazwisko == nazwisko_ucznia:
                        print(f'Uczen {imie_ucznia} {nazwisko_ucznia}:')
                        for nauczyciel in nauczyciele:
                            if uczen.klasa in nauczyciel.klasy:
                                print(f" przedmiot: {nauczyciel.przedmiot}, nauczyciel: {nauczyciel.imie} {nauczyciel.nazwisko}")
            elif opcja == "nauczyciel":
                imie_nauczyciela = input( "Podaj imie nauczyciela ").capitalize()
                nazwisko_nauczyciela = input("Podaj  nazwisko nauczyciela ").capitalize()
                for nauczyciel in nauczyciele:
                    if nauczyciel.imie == imie_nauczyciela and nauczyciel.nazwisko == nazwisko_nauczyciela:
                        print(f'Nauczyciel: {imie_nauczyciela} {nazwisko_nauczyciela} klasy: {nauczyciel.klasy} ')
            elif opcja == "wychowawca":
                imie_wychowawcy = input( "Podaj imie wychowawcy ").capitalize()
                nazwisko_wychowawcy = input("Podaj  nazwisko wychowawcy ").capitalize()
                for wychowawca in wychowawce:
                    if wychowawca.imie == imie_wychowawcy and wychowawca.nazwisko == nazwisko_wychowawcy:
                        print(wychowawca)
                        for uczen in uczniowie:
                            if uczen.klasa == wychowawca.klasa:
                                print(f'uczen : {uczen.imie} {uczen.nazwisko} ')
        print("Wpisales nie poprawna komede, wpisz [utworz, zarzadzaj, koniec]")
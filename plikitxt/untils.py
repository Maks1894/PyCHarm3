


def wczytaj_magazyn ():
    # magazyn = {
    #     "Adidas": [10, 500],
    #     "Nike": [7, 600],
    #     "New balance": [9, 400],
    #     "Reebok": [15, 300],
    # return magazyn, licba
    magazyn ={}
    with open("buty.txt") as f:
        for line in f:
            tytul, liczba, cena= line.strip().split(',')
            magazyn[tytul] = [int(liczba), int(cena)]
    aktualizuj_baze_magazyna(magazyn)
    return magazyn
def wyswietl_powitania():
    print("Witam w programie  naszego sklepu butow sportowych")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
""")
def wprowadz_nazwe(magazyn, konto):
    tytul = input("Podaj nazwe butow: ").capitalize()
    liczba = int(input("Podaj ilos par butow: "))

    if tytul in magazyn and liczba > 0:
        magazyn[tytul][0] += liczba
        cena = magazyn[tytul][1]
        koszt = cena * liczba
        if konto > koszt:
            konto -= koszt
            print(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')

        else:
            print("Brakuje srodkow na koncie")

    else:
        if liczba <= 0:
            print("Wpisz poprawna ilos par butow")
        else:
            cena = int(input("Podaj cene butow: "))
            if cena > 0:
                magazyn[tytul] = [liczba, cena]
                konto -= cena * liczba
                print(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')
            else:
                print("Cena musi byc wiecej od 0")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania. 
""")
    aktualizuj_baze_magazyna(magazyn)
    return magazyn, konto
def sprzedaj (magazyn, konto):
        tytul = input("Podaj nazwe butow: ").capitalize()
        if tytul not in magazyn:
            print(f"Brak butow '{tytul}' w sklepie ")

        elif tytul in magazyn:
            liczba = int(input(f"Podaj ilos par butow '{tytul}' ktore chcesz sprzedac: "))
            if magazyn[tytul][0] >= liczba and liczba > 0:
                magazyn[tytul][0] -= liczba
                konto += liczba * magazyn[tytul][1]
                print(f"Sprzedales {liczba} par butow '{tytul}' ")
                if magazyn[tytul][0] == 0:
                    del magazyn[tytul]

            elif liczba == 0:
                print('Ilosz parz sprzedawanych butow musi byc wieksza od 0')
            else:
                print(f" Brak wystarczajacej ilosci par butow '{tytul}' ")
        print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
        """)
        aktualizuj_baze_magazyna(magazyn)
        return magazyn, konto
def stan(konto):
    print(f"Aktualnu stan konta sklepu {konto} zl.")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
                """)
def balans(konto) :
    kwota = int(input("Wprowadz kwote ktora chcesz dodac(wartos dodatnia) lub odjac(wartosc ujemna) z konta firmy zl. : "))
    if kwota < 0:
        if -kwota > konto:
            print("Nie mozna zdjac wiecej niz jest na koncie")
        else:
            konto += kwota
            print(f' Zdjeles z konta firmy {kwota} zl.')
    else:
        konto += kwota
        print(f'Dodales na konto firmy {kwota} zl.')
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
              """)
    return konto
def wyswietl_magazyn (magazyn) :
    tytul = input("Podaj nazwe butow: ").capitalize()
    if tytul in magazyn:
        print(
            f"Buty {tytul} sa dotepne, cena: {magazyn.get(tytul)[1]}, ilosc na magazynie : {magazyn.get(tytul)[0]} szt")
    else:
        print(f"Buty {tytul} nie sa dostepne")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
    """)
def wyswietl_dostepnosc (magazyn) :
    if magazyn:
        print("Dotepne buty sportowe:")
        for tytul, (liczba_sztuk, cena) in magazyn.items():
            print(f"buty: {tytul}, ilosc:{liczba_sztuk} par, cena: {cena} zl.")
    else:
        print("Brak butow na magazynie")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
                """)
def nie_istnieje ():
    print("Nie ma takiej komendy,wpisz komende z listy")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
            """)

def aktualizuj_baze_magazyna(magazyn):
    with open("buty.txt", "w") as f:
        for tytul, (liczba, cena) in  magazyn.items():
            f.write(f"{tytul}, {liczba}, {cena}\n")
def wyswietl_historie(historia) :
    od = int(input("Podaj przedzial OD: "))
    do = int(input("Podaj przedzial DO: "))
    if od >= 0 and do <= len(historia):
        print("Historia operacj:")
        for i in historia[od:do]:
            print(f"- {i}")
    else:
        print("Niepoprawny przedzial, wysweitlam cala historie")
        print("Historia operacj:")
        for i in historia:
            print(f"- {i}")
    print("""
Lista dotepnych komend:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
            """)
def aktualizuj_historie(historia):
    with open("historia.txt", "a") as f:
        for ts, komenda in  historia:
            f.write(f"{ts}- {komenda}\n")
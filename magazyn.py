# Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.
# Program po uruchomieniu wyświetla informację o dostępnych komendach:
# saldo
# sprzedaż
# zakup
# konto
# lista
# magazyn
# przegląd
# koniec
# Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:
# saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
# sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia
# respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu
# produktu "rower" oraz dodanie do konta kwoty 100).
# zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było.
# Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
# konto - Program wyświetla stan konta.
# lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
# magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
# przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane
# pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd
# od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i
# wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
# koniec - Aplikacja kończy działanie.
#
# Dodatkowe wymagania:
#
# Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
# Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
# Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi
# o wprowadzenie jednej z nich.
# Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu
# podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać).
# Zadbaj też o prawidłowe typy danych.
print("Witam w programie  naszego sklepu butow sportowych")
print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
""")
konto = 0
magazyn = {
    "Adidas": [ 10, 500],
    "Nike": [7, 600],
    "New balance": [9, 400],
    "Rebok": [15, 300],
}
historia = []
while True :
    komenda = input("Wpisz komende (wpisz \"koniec\" gdy chcesz skonczyc): ").lower()
    print(f"Wpisales komede {komenda}")
    if komenda == "koniec" :
        print("Koniec progarmu")
        historia.append(komenda)
        break
    elif  komenda == "saldo":
        kwota = int(input("Wprowadz kwote ktora chcesz dodac(wartos dodatnia) lub odjac(wartosc ujemna) z konta firmy: "))
        if kwota <0 :
            if -kwota> konto:
                print("Nie mozna zdjac wiecej niz jest na koncie")
                historia.append("Nie mozna zdjac wiecej niz jest na koncie")
            else:
                konto += kwota
                print(f' Zdjeles z konta firmy {kwota} zl.')
                historia.append(f' Zdjeles z konta firmy {kwota} zl.')
        else:
            konto += kwota
            print(f'Dodales na konto firmy {kwota} zl.')
            historia.append(f'Dodales na konto firmy {kwota} zl.')
    elif komenda == "sprzedaz":
        tytul = input("Podaj nazwe butow: ").capitalize()
        if tytul not in  magazyn :
            print(f"Brak butow '{tytul}' w sklepie ")
            historia.append(f"Brak butow '{tytul}' w sklepie ")
        elif tytul in magazyn:
            liczba = int(input(f"Podaj ilos par butow '{tytul}' ktore chcesz sprzedac: "))
            if magazyn[tytul][0] >= liczba  and liczba > 0:
                magazyn[tytul][0] -= liczba
                if magazyn[tytul][0] == 0:
                    del magazyn[tytul]
                konto += liczba*magazyn[tytul][1]
                print(f"Sprzedales {liczba} par butow '{tytul}' ")
                historia.append(f"Sprzedales {liczba} par butow '{tytul}' ")
            elif liczba == 0:
                print('Ilosz parz sprzedawanych butow musi byc wieksza od 0')
            else :
                print(f" Brak wystarczajacej ilosci par butow '{tytul}' ")
                historia.append(f" Brak wystarczajacej ilosci par butow '{tytul}' ")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
        """)
    elif komenda == "zakup":
        tytul = input("Podaj nazwe butow: ").capitalize()
        liczba = int(input("Podaj ilos par butow: "))
        if tytul in magazyn and liczba > 0:
            magazyn[tytul][0] += liczba
            cena = magazyn[tytul][1]
            konto -= cena * liczba
            print(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')
            historia.append(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')
        else:
            if liczba <=0:
                print("Wpisz poprawna ilos par butow")
            else :
                cena = int(input("Podaj cene butow: "))
                if cena > 0:
                    magazyn[tytul]=[liczba,cena]
                    konto -= cena * liczba
                    print(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')
                    historia.append(f'Zakupiles do sklepu buty: {tytul}, ilosc par: {liczba}, cena jednostki: {cena}')
                else: print("Cena musi byc wiecej od 0")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
        """)
    elif komenda == "konto":
        print(f"Aktualnu stan konta sklepu {konto} zl.")
        historia.append(f"Aktualnu stan konta sklepu {konto} zl.")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
            """)
    elif komenda == "lista":
        if magazyn:
            print("Dotepny buty sportowe:")
            for tytul, (liczba_sztuk, cena) in magazyn.items():
                print(f"buty: {tytul}, ilosc:{liczba_sztuk} par, cena: {cena} zl.")
        else:
            print("Brak butow na magazynie")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
            """)
    elif komenda == "magazyn":
        tytul = input("Podaj nazwe butow: ").capitalize()
        if tytul in magazyn:
            print(f"Buty {tytul} sa dotepne, cena: {magazyn.get(tytul)[1]}, ilosc na magazynie : {magazyn.get(tytul)[0]} szt")
        else:
            print(f"Buty {tytul} nie sa dostepne")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
""")
    elif komenda == "przeglad":
        od = int(input("Podaj przedzial OD: "))
        do = int(input("Podaj przedzial DO: "))
        if od >= 0 and do <= len(historia) :
            print("Historia operacj:")
            for i in historia[od:do]:
                print(f"- {i}")
        else:
            print("Niepoprawny przedzial, wysweitlam cala historie")
            print("Historia operacj:")
            for i in historia:
                print(f"- {i}")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
        """)
    else:
        print("Nie ma takiek komendy,wpisz komende z listy")
        print("""
Lista dotepnych komed:
saldo - Wprowadz kwote ktora chcesz dodac lub odjac z konta firmy.
sprzedaz - podaj nazwe cene i ilos produkta ktory chcesz spzedac
zakup - podaj nazwe cene i ilos produkta ktory chcesz kupic
konto - aktualny stan konta firmy
lista - pokazuje nazwy, ceny o ilosc  wszystkich produktow na magazynie
magazyn - podaj nazwe aktualnego produktu zeby wyswietlic go stan na magazynie
przeglad - podaz zakres czasy od - do zeby wyswetlic historie wukonanych operacji  w tym zakresie
koniec - koniec dzialania.
        """)

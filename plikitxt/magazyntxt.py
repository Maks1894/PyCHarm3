
from untils import wczytaj_magazyn, wyswietl_powitania, wprowadz_nazwe, sprzedaj, stan, balans, wyswietl_magazyn, nie_istnieje, wyswietl_dostepnosc, aktualizuj_baze_magazyna, wyswietl_historie, aktualizuj_historie
from _datetime import datetime
konto = 0
magazyn = wczytaj_magazyn()
wyswietl_powitania()
historia = []
while True :
    komenda = input("Wpisz komende (wpisz \"koniec\" gdy chcesz skonczyc): ").lower()
    print(f"Wpisales komende {komenda}")
    ts = str(datetime.now())
    historia.append((komenda, ts))
    if komenda == "koniec" :
        print("Koniec progarmu")

        break
    elif  komenda == "saldo":
        konto = balans(konto)
    elif komenda == "sprzedaz":
        magazyn, konto = sprzedaj(magazyn, konto)
    elif komenda == "zakup":
        magazyn, konto = wprowadz_nazwe(magazyn,konto)

    elif komenda == "konto":
        stan(konto)
    elif komenda == "lista":
        wyswietl_dostepnosc(magazyn)
    elif komenda == "magazyn":
        wyswietl_magazyn(magazyn)
    elif komenda == "przeglad":
        wyswietl_historie(historia)
    else:
        nie_istnieje()
aktualizuj_historie(historia)

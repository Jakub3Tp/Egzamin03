import random


def rzut_koscmi(ile_koscy):
    wyniki = [random.randint(1, 6) for _ in range(ile_koscy)]
    return wyniki

def punkty(wyniki):
    punkty = 0
    for punkt in set(wyniki):
        ile_razy = wyniki.count(punkt)
        if ile_razy >= 2:
            punkty += punkt * ile_razy
    return punkty

def gra():
    while True:
        liczba_kosci = int(input("Podaj liczbę kostek do rzucenia (3-10): \n"))
        if 3 <= liczba_kosci <= 10:
            break
    while True:
        wyniki = rzut_koscmi(liczba_kosci)
        for i, wynik in enumerate(wyniki, start=1):
            print(f"Kostka {i}, {wynik}")
        punkciki = punkty(wyniki)
        print(f"Uzyskano: {punkciki} punktów. \n")
        while True:
            jeszcze_raz = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
            if jeszcze_raz in ("t", "n"):
                break
        if jeszcze_raz == "n":
            break


if __name__ == '__main__':
    gra()

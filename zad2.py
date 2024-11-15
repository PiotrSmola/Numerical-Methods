def horner(tablica, x, rzad):
    wynik = []
    for i in range(rzad):
        wartosc = tablica[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)
    return wynik


def wypiszWiel(tablica):
    wielomian = ""
    stopienWielomianu = len(tablica) - 1
    for i, wspolczynnik in enumerate(tablica):
        if wspolczynnik != 0 & wspolczynnik != len(tablica) - 1:
            if i == 0:
                wielomian += "("
            if stopienWielomianu - i > 1:
                wielomian += f"{wspolczynnik}x^{stopienWielomianu - i}"
            elif stopienWielomianu - i == 1:
                wielomian += f"{wspolczynnik}x"
            else:
                wielomian += f"{wspolczynnik}"
            if i < len(tablica) - 1:
                wielomian += " + "

    wielomian += ")\t(x - " + f"{tablica[len(tablica) - 1]})"
    return wielomian


rzad = int(input("Podaj rząd wielomianu: "))
tab = []
print("Podaj współczynniki wielomianu. Zacznij od współczynnika przy najwyższej potędze:")
for i in range(rzad + 1):
    y = int(input())
    tab.append(y)

x = int(input("Proszę podać liczbę przez, którą chcesz dzielić: "))

wynik = horner(tab, x, rzad)
wielomian = wypiszWiel(wynik)
print("\nWynik dzielenia wielomianu przez x:", wielomian)

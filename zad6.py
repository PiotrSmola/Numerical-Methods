from math import cos


# Definicja funkcji
def f(x):
    return 3 * x - cos(x) - 1


# Wartość bezwzględna funkcji
def abs(x):
    if (x >= 0):
        return x
    else:
        return -x


# Funkcja obliczająca pierwiastek
def falsi(a, b, e):
    # Sprawdzenie założenia metody falsi
    if (f(a) * f(b) >= 0):
        raise ValueError("Założenia nie zostały spełnione - f(a) i f(b) muszą posiadać różne znaki.")

    # Zmienna do przechowywania liczby iteracji
    iteracja = 0

    while (True):
        # Obliczanie nowej wartości x0 zgodnie z metodą regula falsi
        x0 = a - (((b - a) * f(a)) / (f(b) - f(a)))

        iteracja = iteracja + 1

        # Sprawdzanie zbieżności
        if (abs(f(x0)) < e):
            print("Ilość iteracji:", iteracja)
            return x0  # Zwrócenie przybliżonej wartość pierwiastka f(x)
        else:
            # Jako nowy przedział [a,b] przyjmujemy tę połówkę [a,x0], [x0,b], w której funkcja zmienia znak
            if (f(x0) * f(a) < 0):
                b = x0
            else:
                a = x0


try:
    print("Metoda falsi")
    wynik = falsi(0.25, 0.75, 0.00001)
    print("Pierwiastek funkcji:", wynik)
except ValueError as e:
    print("Błąd:", e)

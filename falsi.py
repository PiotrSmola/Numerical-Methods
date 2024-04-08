from sympy import symbols, cos

x = symbols('x')
f = 3 * x - cos(x) - 1  # Wzór funkcji f(x)

blad = 0.00001  # Dokładność E
a = 0.25  # Początek przedziału
b = 0.75  # Koniec przedziału

# Sprawdzenie, czy w danym przedziale istnieje pierwiastek
if f.subs(x, a) * f.subs(x, b) >= 0:
    print("\nRównanie f(x) nie posiada pierwiastka w podanym przedziale.")
else:
    print("\nRównanie f(x) posiada pierwiastek w podanym przedziale.")

    ilosc_iteracji = 0
    while True:
        f_a = f.subs(x, a)
        f_b = f.subs(x, b)
        # Obliczanie nowego przybliżenia
        x_n = a - (f_a * (b - a)) / (f_b - f_a)
        wartosc_f_x_n = f.subs(x, x_n)

        # Sprawdzenie, czy osiągnięto zadaną dokładność
        if abs(wartosc_f_x_n) < blad:
            break

        # Zmiana przedziału
        if f_a * wartosc_f_x_n > 0:
            a = x_n
        else:
            b = x_n

        ilosc_iteracji += 1

    # Wyniki
    print(f"Ilość iteracji: {ilosc_iteracji}")
    print(f"Przybliżone rozwiązanie równania wynosi: {x_n.evalf()}")

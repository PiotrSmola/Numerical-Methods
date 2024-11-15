import sympy
from sympy import symbols, solve

x = symbols('x')
f = x ** 3 + x ** 2 - 3 * x - 3 # deklaracja funkcji

blad = 0.0001  # Dokładność E
a = 1  # Początek przedziału
b = 2  # Koniec przedziału

# Sprawdzenie, czy funkcja spełnia warunek na obecność pierwiastka w przedziale
if f.subs(x, a) * f.subs(x, b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastek w podanym przedziale.")
else:
    print("\nRównanie f(x) zawiera pierwiastek w podanym przedziale.")
    # Przypisanie wartości początkowych

    d1 = sympy.diff(f,x)
    d2 = sympy.diff(f,x,2)
    if((d1.subs(x,a)*d2.subs(x,a))>0):
        x_n = a
        x_n1 = b
    else:
        x_n = b
        x_n1 = a

    ilosc_iteracji = 1
    while True:
        # Obliczanie kolejnych przybliżeń metodą siecznych
        f_x_n = f.subs(x, x_n)
        f_x_n1 = f.subs(x, x_n1)
        x_next = x_n1 - (f_x_n1 * (x_n1 - x_n)) / (f_x_n1 - f_x_n)

        # Koniec iteracji
        if abs(x_next - x_n1) < blad:
            break

        # Przygotowanie do kolejnej iteracji
        x_n = x_n1
        x_n1 = x_next
        ilosc_iteracji += 1

    # Wyników
    print("Ilość iteracji: ", ilosc_iteracji)
    print("Przybliżone rozwiązanie równania wynosi: ", x_n1.evalf())
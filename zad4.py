from sympy import symbols, sin, pi, diff

x = symbols('x')

# Wzór funkcji
f = sin(x) - 1 / 2 * x

# Pochodna funkcji
d1 = diff(f, x)

# Początek i koniec przedziału
a = pi / 2
b = pi

# Sprawdzenie warunku Bolzano-Cauchy'ego
if f.subs(x, a) * f.subs(x, b) > 0:
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spełnione")
    print(f"W przedziale [{a}, {b}] najpewniej nie ma miejsca zerowego")
else:
    epsilon = 0.01  # Dana dokładność
    #Ustalenie początkowego x0 z warunku f(x0)*f''(x0)>=0
    d2 = diff(f,x,2)
    if ((f.subs(x,a)*d2.subs(x,a))>=0):
        x0 = a
    else:
        x0 = b

    # Metoda stycznych
    iteracje = 0
    while abs(f.subs(x, x0)) > epsilon:
        x0 = x0 - f.subs(x, x0) / d1.subs(x, x0)
        iteracje += 1

    print(f"\nFunkcja f(x) = {f}")
    print(f"ma miejsce zerowe w x = {x0.evalf()}")
    print(f"Zostało znalezione w {iteracje} próbach")
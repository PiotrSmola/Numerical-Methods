from sympy import sympify

prompt = input("Należy używać odpowiednich oznaczeń:\n\t* jako mnozenie\n\t** jako potegowanie\nPodaj wzor funkcji: ")
f = sympify(prompt)

a = float(input("Podaj poczatek przedziału: "))
b = float(input("Podaj koniec przedziału: "))
min = min(a, b)
max = max(a, b)

# Bolzano-Cauchy
if f.subs("x", min) * f.subs("x", max) > 0:
    print("\nTwierdzenie Bolzano-Cauchy'ego nie jest spełnione")
    print(f"W przedziale [{min}, {max}] najprawdopodobniej nie ma miejsca zerowego")
    exit(1)

epsilon = float(input("Wybierz dokladność(epsilon): "))

temp_min = min
temp_max = max
x = (temp_min + temp_max) / 2
count = 1
while abs(f.subs("x", x)) > epsilon:
    x = (temp_min + temp_max) / 2

    count += 1

    if f.subs("x", x) * f.subs("x", temp_min) <= 0:
        temp_max = x
    else:
        temp_min = x

print(f"\nFunkcja f(x) = {f}")
print(f"ma miejsce zerowe w x = {x}")
print(f"znaleziona w {count} probach")
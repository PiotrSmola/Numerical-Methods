from sympy import symbols, expand

# Zestaw węzłów P1(1,5), P2(2,7), P3(3,6).

# Wzór interpolacyjny Lagrange'a:
# Wzór L_n(x) = E k=0/n | lambda_k(x) * y_k
# Gdzie y_k = f(x_k), lambda_k(x) = TT i=0,i!=k/n | (x - x_i)/(x_k - x_i), k = 0, 1, ..., n

x = symbols('x')
wezly = [(1, 5), (2, 7), (3, 6)]  # Definiowanie węzłów
n = len(wezly)  # Liczba węzłów


# Obliczanie bazowych wielomianów Lagrange'a dla danego indeksu
def wielomianBazowy(k):
    x_k = wezly[k][0]  # k-ty węzeł
    # Lista czynników wielomianu bazowego, pomijając k-ty węzeł
    czynnikiWielomianu = [(x - wezly[i][0]) / (x_k - wezly[i][0]) for i in range(n) if i != k]
    wielomian_bazowy = 1  # Wielomian bazowy
    for czynnik in czynnikiWielomianu:
        wielomian_bazowy *= czynnik  # Mnożenie czynników wielomianu bazowego
    return wielomian_bazowy


# Sumowanie iloczynów wartości y_k oraz odpowiednich wielomianów bazowych
LagrangeWielomian = sum(wezly[k][1] * wielomianBazowy(k) for k in range(n))

# Wypisanie wyniku
print("Wielomian interpolacyjny Lagrange'a jest postaci:", expand(LagrangeWielomian).evalf())

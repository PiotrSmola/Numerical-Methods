import numpy as np

# Definicja macierzy A i wektora b jako float
A = np.array([
    [3, 0, 6],  # Definicja macierzy A
    [1, 2, 8],
    [4, 5, -2]
], dtype=float)
B = np.array([-12, -12, 39], dtype=float)  # Definicja wektora b


# Funkcja wykonująca eliminację Gaussa z wyborem elementu głównego
def eliminacjaGaussa(A, B):
    n = len(B)  # Liczba równań/rozmiar macierzy
    # Macierz rozszerzona powstała poprzez dołączenie wektora b jako nowej kolumny
    AB = np.hstack([A, B.reshape(-1, 1)])

    for i in range(n):

        # Sprawdzamy założenia do metody eliminacji Gaussa
        wyznacznikMacierzy = np.linalg.det(A)
        assert wyznacznikMacierzy != 0, "Wyznacznik macierzy nie jest różny od zera, zatem macierz jest osobliwa i nie można jej rozwiązać."
        # Wybór elementu głównego w kolumnie i
        max_row = np.argmax(np.abs(AB[i:, i])) + i  # Znajdujemy indeks maksymalnego elementu
        # Zamiana wierszy, aby maksymalny element był na pozycji głównej
        AB[[i, max_row]] = AB[[max_row, i]]

        # Upewniamy się, że element główny nie jest zerowy
        assert AB[i, i] != 0, "Macierz jest osobliwa i nie można jej rozwiązać."

        # Eliminacja Gaussa
        for j in range(i + 1, n):
            factor = AB[j, i] / AB[i, i]  # Współczynnik do eliminacji
            AB[j, i:] -= factor * AB[i, i:]  # Eliminacja wiersza

    x = np.zeros(n)  # Wektor rozwiązania
    for i in range(n - 1, -1, -1):  # Iteracja od ostatniego wiersza do pierwszego
        # Obliczenie i-tej współrzędnej wektora rozwiązania
        x[i] = (AB[i, -1] - np.dot(AB[i, i + 1:n], x[i + 1:n])) / AB[i, i]

    return x


# Rozwiązanie układu równań Ax = b
x = eliminacjaGaussa(A, B)
print("Rozwiązanie x:", x)

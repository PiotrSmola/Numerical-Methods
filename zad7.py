import math

#Definicja funkcji do całkowania
def funkcja(x):
    return math.sqrt(1 + x)

#Metoda trapezów do obliczenia całki
def metoda_trapezow(a, b, n):
    h = (b - a) / n  #Szerokość każdego trapezu
    przyblizona_calka = (funkcja(a) + funkcja(b)) / 2.0  #Pierwsza i ostatnia wartość funkcji
    for i in range(1, n):
        przyblizona_calka += funkcja(a + i * h)  #Sumowanie wartości funkcji wewnątrz przedziału
    przyblizona_calka *= h  #Mnożenie sumy przez szerokość trapezów
    return przyblizona_calka  #Zwrócenie przybliżonej wartości całki

#Określenie parametrów
dolne_ograniczenie = 0  #Dolne ograniczenie całkowania
gorne_ograniczenie = 1  #Górne ograniczenie całkowania
n = 3  #Liczba podziałów/trapezów

#Obliczenie aproksymacji
przyblizenie = metoda_trapezow(dolne_ograniczenie, gorne_ograniczenie, n)

#Wypisanie wyników
print("Aproksymacja metodą trapezów:", przyblizenie)

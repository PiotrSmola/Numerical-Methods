stopienWiel = int(input("Podaj stopień wielomianu: "))

lista = []
lista.append([])
lista.append([])
lista.append([])

licznik = int(0)
while licznik != stopienWiel + 1:
    lista[0].append(int(input("Podaj współczynnik przy x^" + str(stopienWiel - licznik) + ": ")))
    licznik += 1

punkt = int(input("Podaj punkt: "))

licznik = int(0)
for n in lista[0]:
    if licznik == 0:
        lista[1].append(n)
        lista[2].append(n)
    else:
        lista[1].append(punkt * lista[2][licznik - 1])
        lista[2].append(lista[1][licznik] + n)
    licznik += 1

licznik = int(0)
for n in lista[0]:
    if stopienWiel - licznik == 0:
        print("(" + str(n) + ")")
    else:
        print("(" + str(n) + ")x^" + str(stopienWiel - licznik) + " + ", end="")
    licznik += 1

print("Wartość tego wielomianu w punkcie " + str(punkt) + ": " + str(lista[2][stopienWiel]))

print("Iloczyn w(x)/(x-(" + str(punkt) + ")):")
licznik = int(0)
for n in lista[2]:
    if stopienWiel - licznik == 0:
        print(str(n) + "/(x-(" + str(punkt) + "))")
    else:
        print("(" + str(n) + ")x^" + str(stopienWiel - licznik - 1) + " + ", end="")
    licznik += 1

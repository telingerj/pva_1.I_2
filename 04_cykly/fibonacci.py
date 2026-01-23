cislo = int(input("Cislo: "))

# prvních n čísel fibonacciho posloupnosti
# každé další číslo je součet dvou předchozích
# 0 1 1 2 3 5 8

predposledni = 0
posledni = 1
print("0 1", end=" ")
for i in range(cislo - 2):
    soucet = predposledni + posledni
    print(soucet, end=" ")
    predposledni = posledni
    posledni = soucet

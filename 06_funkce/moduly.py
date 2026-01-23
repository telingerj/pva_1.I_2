import random

"""
pocet = 0
padlo = 0
vsechnyPokusy = []
while padlo != 6:
    padlo = random.randint(1, 6)
    vsechnyPokusy.append(padlo)
    pocet += 1

print(vsechnyPokusy)
"""

# spočítat kolikrát za 10 hodů padla 3
"""
pocet = 0
for i in range(10):
    padlo = random.randint(1, 6)
    if padlo == 3:
        pocet += 1

print(pocet)
"""

# házet tak dlouho dokud nepadne 5x za sebou 6
"""
pocetSestek = 0
cisla = []
while pocetSestek < 5:
    padlo = random.randint(1, 6)
    cisla.append(padlo)
    if padlo == 6:
        pocetSestek += 1
    else:
        pocetSestek = 0

print(cisla)
print(len(cisla))
"""

pocetHodu = 10000000
cisla = [0, 0, 0, 0, 0, 0]
for i in range(pocetHodu):
    hod = random.randint(1, 6)
    cisla[hod - 1] += 1


#  procentuální zastoupení každého z čísel 1-6
# 1: ?%
# 2: ?%
# ...

for i in range(len(cisla)):
    procenta = cisla[i] / pocetHodu
    print(i + 1, ":", procenta * 100, "%")
"""
seznam = ["Petr", "Jakub", "Jan", "Linda", "Eliška"]
for i in seznam:
    print("jmenuji se", i)
"""
# zjistit pomocí for součet čísel v seznamu
seznam2 = [4, 5, 7, 1, 2, 9]
"""
soucet = 0
for i in seznam2:
    soucet += i
print(soucet)
"""
# zjistí na které pozici je zadané číslo
cislo = int(input())
for i in range(len(seznam2)):
    if cislo == seznam2[i]:
        print("našli jsme naše číslo na pozici", i)
        break
    elif i == len(seznam2) - 1:
        print("nenašel jsem")
        
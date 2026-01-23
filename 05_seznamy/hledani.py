seznam2 = [4, 5, 7, 1, 2, 9]

cislo = int(input())
nasel = False
for i in range(len(seznam2)):
    if cislo == seznam2[i]:
        nasel = True
        print("našli jsme naše číslo na pozici", i)
        break

if not nasel:
    print("nenašli jsme")
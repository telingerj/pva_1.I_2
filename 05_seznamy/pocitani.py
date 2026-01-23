l = [4, 1, 2, 1, 4, 2, 1, 4, 3, 3, 2, 1, 2, 3]

# rozšíření: spočítat, kolikrát jsou v seznamu
# všechna čísla od 1 do 10
for cislo in range(11):
    # spočítat, kolikrát je v seznamu cislo
    pocet = 0
    for i in l:
        if cislo == i:
            pocet += 1
    print("číslo", cislo, "je v seznamu", pocet, "krát")

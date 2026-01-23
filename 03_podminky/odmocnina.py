cislo = int(input("zadej číslo: "))
if cislo < 0:
    print("ze záporného čísla nejde spočítat odmocninu")
else:
    print("odmocnina:", cislo ** 0.5)
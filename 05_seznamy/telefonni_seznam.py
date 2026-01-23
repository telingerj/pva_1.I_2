slovnik = {}

while True:
    jmeno = input("zadej jmeno: ")
    if jmeno == "":
        break
    cislo = int(input("zadej tel. cislo: "))
    slovnik[jmeno] = cislo

# jaké telefonní číslo má pepa?
if "pepa" in slovnik:
    print(slovnik["pepa"])
else:
    print("pepa tam není")

# kdo má telefonní číslo 123?
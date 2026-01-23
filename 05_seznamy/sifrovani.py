zprava = input("zadej zprávu: ") # znaky z anglické abecedy
posun = int(input("zadej posun: "))
zasifrovanaZprava = ""

for i in zprava:
    if i == " ":
        zasifrovanaZprava += i
    else:
        kod = ord(i)
        kod += posun
        if kod > ord("z"):
            kod -= 26
        elif kod < ord("a"):
            kod += 26
        zasifrovanyZnak = chr(kod)
        zasifrovanaZprava += zasifrovanyZnak

print(zasifrovanaZprava)
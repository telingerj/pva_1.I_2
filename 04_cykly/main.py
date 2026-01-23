"""
i = 0

while i <= 10:
    print(i, end=" ")
    i += 1

print()
"""
# vypsat sudá čísla od 0 do 10 (včetně)
"""
i = 2

while i <= 10:
    print(i, end=" ")
    i += 2
print()
"""
# vypsat lichá čísla od 0 do 10 (včetně)
"""
i = 1

while i <= 10:
    print(i, end=" ")
    i += 2

print()
"""

# čísla od 10 do 0 (pozpátku)
"""
i = 10
while i > 0:
    print(i, end=" ")
    i -= 1
"""

# stokrát vypsat "ahoj"
"""
i = 0
while i < 100:
    print("ahoj")
    i += 1
"""

# vypsat čísla od 0 do 10 kromě 7
"""
i = 0
while i < 10:
    if i != 7:
        print(i, end=" ")
    i += 1
"""
"""
i = 0
while i < 10:
    i += 1
    if i == 7:
        continue
    print(i, end=" ")
"""
"""
while True:
    vstup = input("zadej vstup: ")
    if vstup == "konec":
        break
"""

pocetMocnin = int(input())
# prvních "pocetMocnin" mocnin 2

i = 0
mocnina = 1
while i < pocetMocnin:
    print(mocnina, end=" ")
    mocnina *= 2
    i += 1

print()

i = 0
while i < pocetMocnin:
    print(2 ** i, end=" ")
    i += 1
penize = int(input())

tydny = 0
while penize >= 500:
    penize -= 150
    tydny += 1

while penize >= 110:
    penize -= 110
    tydny += 1

print(tydny)
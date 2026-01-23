for i in range(5):
    print("*" * 5)

for i in range(1, 6):
    print("*" * i)

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * i)

print("*" * 5)
for i in range(3):
    print("*", end="")
    print(" " * 3, end="")
    print("*")
print("*" * 5)
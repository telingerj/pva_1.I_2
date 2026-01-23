text = "ahoj jak se máš"

pocet1 = 0
pocet2 = 0
for znak in text:
    if znak == "a":
        pocet1 += 1
    elif znak == "e":
        pocet2 += 1

if pocet1 > pocet2:
    print("v textu je víc písmen a")
elif pocet2 > pocet1:
    print("v textu je víc písmen e")
else:
    print("v textu je stejně písmen a i písmen e")

# zjistit jestli je v textu víc a nebo e

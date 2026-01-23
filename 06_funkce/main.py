def pozdrav():
    print("ahoj")
    print("jak se máš")


def pozdrav_jmeno(jmeno):
    print("ahoj", jmeno)


def pozdrav_dva_lidi(jmeno1, jmeno2):
    print("ahoj", jmeno1, "a", jmeno2)


def prvni_pismeno(jmeno):
    return jmeno[0]


def druha_mocnina(cislo):
    return cislo ** 2

def absolutni_hodnota(cislo):
    if cislo >= 0:
        return cislo
    else:
        return cislo * -1


print(absolutni_hodnota(2))
print(absolutni_hodnota(-1))
print(absolutni_hodnota(3))
print(absolutni_hodnota(-2))

# vytvořit funkci, která vrací druhou mocninu čísla

# vytvořit funkci, která vrací absolutní hodnotu čísla

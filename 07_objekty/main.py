class Clovek:
    def __init__(self, jmeno, rokNarozeni):
        self.jmeno = jmeno
        self.rokNarozeni = rokNarozeni
        self.auta = []
        print("právě vzniknul nový člověk")

    def pozdrav(self):
        print("ahoj, já jsem", self.jmeno)

    def vypisRokNarozeni(self):
        print("narodil jsem se v roce", self.rokNarozeni)

    def jeStarsi(self, human):
        if self.rokNarozeni < human.rokNarozeni:
            return True
        return False

    def vratVek(self):
        return 2025 - self.rokNarozeni

    def pridejAuto(self, auto):
        self.auta.append(auto)
        auto.pridejMajitele(self)

    def vratPocetAut(self):
        return len(self.auta)
        # TODO: vrátí počet aut, která patří danému člověku

    def vlastniZnacku(self, znacka):
        for auto in self.auta:
            if auto.znacka == znacka:
                return True
        return False
        # TODO: vypsat, jestli má alespoň jedno auto dané značky

    def prepisAuto(self, auto, clovek2):
        vlastni = False
        for a in self.auta:
            if a == auto:
                vlastni = True
                self.auta.remove(auto)

        if not vlastni:
            return
        clovek2.pridejAuto(auto)


        # TODO: když člověku patří auto, změní se jeho majitel
        # TODO: na clovek2


class Auto:
    def __init__(self, znacka, barva, rokVyroby, vykon):
        self.znacka = znacka
        self.barva = barva
        self.rokVyroby = rokVyroby
        self.vykon = vykon
        self.majitel = None
        print("právě vzniklo nové auto")

    def vratStari(self):
        return 2025 - self.rokVyroby

    def pridejMajitele(self, human):
        self.majitel = human

h = Clovek("Pepa", 1998)
h2 = Clovek("Franta", 2001)

print(h2.jeStarsi(h2))

"""
a = Auto("Škoda", "černá", 2005, 70)
a2 = Auto("Volkswagen", "červená", 2013, 78)
h.pridejAuto(a)
h.pridejAuto(a2)
print(h.vlastniZnacku("Škoda"))
print(h.vlastniZnacku("Volkswagen"))
print(h.vlastniZnacku("Ferrari"))
h.prepisAuto(a, h2)
print(h.auta[0].znacka)
print(h2.auta[0].znacka)
"""
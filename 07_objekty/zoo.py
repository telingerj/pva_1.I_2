class Zoo:
    def __init__(self, jmeno, lokace, rokZalozeni, rozloha):
        self.jmeno = jmeno
        self.lokace = lokace
        self.rokZalozeni = rokZalozeni
        self.rozloha = rozloha
        self.vybehy = []


    def predstaveni(self):
        print("Zoologická zahrada",self.jmeno, "v místě", self.lokace, "byla založena", self.rokZalozeni, "a má rozlohu", self.rozloha,"ha")


    def vzniklaVTomtoStoleti(self):
        if self.rokZalozeni >= 2000:
            return True
        return False


    def pridejVybeh(self, vybeh):
        if self.rozlohaVsechVybehu() + vybeh.rozloha > self.rozloha:
            return False
        self.vybehy.append(vybeh)
        vybeh.pridejZoo(self)
        return True


    def rozlohaVsechVybehu(self):
        soucet = 0
        for v in self.vybehy:
            soucet += v.rozloha
        return soucet


    def pocetZvirat(self):
        soucet = 0
        for vybeh in self.vybehy:
            soucet += len(vybeh.zvirata)
        return soucet


    def hmotnostZvirat(self):
        soucet = 0
        for vybeh in self.vybehy:
            for zvire in vybeh.zvirata:
                soucet += zvire.hmotnost
        return soucet


    def maZvireSeJmenem(self, jmeno):
        for vybeh in self.vybehy:
            for zvire in vybeh.zvirata:
                if jmeno == zvire.jmeno:
                    return True
        return False


    def pocetZemi(self):
        zeme = []
        for vybeh in self.vybehy:
            for zvire in vybeh.zvirata:
                if zvire.puvod not in zeme:
                    zeme.append(zvire.puvod)
        return len(zeme)


class Vybeh:
    def __init__(self, jmeno, rozloha):
        self.jmeno = jmeno
        self.rozloha = rozloha
        self.zvirata = []
        self.zoo = None


    def pridejZoo(self, zoo):
        self.zoo = zoo


    def pridejZvire(self, zvire):
        if len(self.zvirata) > 0 and self.zvirata[0].druh != zvire.druh:
            return False
        self.zvirata.append(zvire)
        zvire.pridejVybeh(self)
        return True


    def odeberZvire(self, zvire):
        self.zvirata.remove(zvire)
        zvire.vybeh = None


class Zvire:
    def __init__(self, druh, jmeno, hmotnost, vyska, rokNarozeni, puvod):
        self.druh = druh
        self.jmeno = jmeno
        self.hmotnost = hmotnost
        self.vyska = vyska
        self.rokNarozeni = rokNarozeni
        self.puvod = puvod
        self.vybeh = None


    def pridejVybeh(self, vybeh):
        self.vybeh = vybeh


def zadejZoo():
    z = []
    print("zadej údaje o zoo, pro ukončení stiskni enter")
    while True:
        jmeno = input("jméno: ")
        if jmeno == "":
            break
        lokace = input("lokace: ")
        rokZalozeni = int(input("rok zalozeni: "))
        rozloha = int(input("rozloha: "))
        z.append(Zoo(jmeno, lokace, rokZalozeni, rozloha))
    return z

def vypisZoo(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)


def vypisVybehy(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)
        for j in range(len(z[i].vybehy)):
            print("   ", j, ":", z[i].vybehy[j].jmeno)


def vypisZvirata(z):
    for i in range(len(z)):
        print(i, ":", z[i].jmeno)
        for j in range(len(z[i].vybehy)):
            print("   ", j, ":", z[i].vybehy[j].jmeno)
            for k in range(len(z[i].vybehy[j].zvirata)):
                print("     ", k, ":", z[i].vybehy[j].zvirata[k].jmeno)


def zadejVybeh(z):
    print("zadej údaje o výběhu, pro ukončení stiskni enter")
    vypisZoo(z)
    while True:
        jmeno = input("jméno: ")
        if jmeno == "":
            break
        rozloha = int(input("rozloha: "))
        cisloZoo = int(input("číslo zoo: "))
        v = Vybeh(jmeno, rozloha)
        z[cisloZoo].pridejVybeh(v)


def zadejZvire(z):
    print("zadej údaje o zvířeti, pro ukončení stiskni enter")
    vypisVybehy(z)
    while True:
        jmeno = input("jmeno: ")
        if jmeno == "":
            break
        druh = input("druh: ")
        hmotnost = int(input("hmotnost: "))
        vyska = int(input("vyska: "))
        rokNarozeni = int(input("rok narozeni: "))
        puvod = input("puvod: ")
        cisloZoo = int(input("číslo zoo: "))
        cisloVybehu = int(input("číslo výběhu: "))
        zvire = Zvire(druh, jmeno, hmotnost, vyska, rokNarozeni, puvod)
        z[cisloZoo].vybehy[cisloVybehu].pridejZvire(zvire)


z = zadejZoo()
zadejVybeh(z)
zadejZvire(z)
vypisZvirata(z)

"""
z1 = Zoo("Zoo Praha", "Troja", 1954, 60)
z2 = Zoo("Zoo Plzeň", "Plzeň", 1962, 50)
z3 = Zoo("fiktivní zoo", "pohádkový les", 2010, 35)

v1 = Vybeh("sloni", 3)
v2 = Vybeh("zirafy", 4)
v3 = Vybeh("surikaty", 1)
v4 = Vybeh("ptaci", 1)

z1.pridejVybeh(v1)
z1.pridejVybeh(v2)
z1.pridejVybeh(v3)
z1.pridejVybeh(v4)

zvire1 = Zvire("slon", "Karel", 7000, 398, 2010, "Indie")
zvire2 = Zvire("slon", "Pepa", 6000, 387, 2011, "Indie")
zvire3 = Zvire("papoušek", "Franta", 1, 51, 2020, "Madagaskar")


v1.pridejZvire(zvire1)
v1.pridejZvire(zvire2)
v4.pridejZvire(zvire3)

print(z1.pocetZemi())
"""
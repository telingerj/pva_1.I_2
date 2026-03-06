#  hra, ve které proti sobě bojují dvě armády
import random

from unicodedata import ucd_3_2_0


class Armada:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva
        self.postavy = []


    def pridej_postavu(self, postava):
        if not isinstance(postava, Postava):
            raise TypeError("postava musí být typu Postava")
        self.postavy.append(postava)
        postava.pridej_armadu(self)



class Postava:
    def __init__(self, jmeno, zivoty):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.armada = None


    def pridej_armadu(self, armada):
        self.armada = armada


    def uber_zivoty(self, zivoty):
        self.zivoty -= zivoty


    def pridej_zivoty(self, zivoty):
        self.zivoty += zivoty


    def mrtvy(self):
        return self.zivoty <= 0


class Bojovnik(Postava):
    def __init__(self, jmeno, zivoty, poskozeni):
        super().__init__(jmeno, zivoty)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass



class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivoty, poskozeni, pocet_sipu):
        super().__init__(jmeno, zivoty, poskozeni)
        self.pocet_sipu = pocet_sipu


    def utok(self, postava):
        if self.mrtvy():
            return
        if not isinstance(postava, Postava):
            raise TypeError("postava musí být typu Postava")
        if self.pocet_sipu <= 0:
            return
        self.pocet_sipu -= 1
        postava.uber_zivoty(self.poskozeni)


    def dopln_sipy(self, pocet_sipu):
        self.pocet_sipu += pocet_sipu



class Sermir(Bojovnik):
    def __init__(self, jmeno, zivoty, poskozeni, ucinnost_stitu):
        super().__init__(jmeno, zivoty, poskozeni)
        self.ucinnost_stitu = ucinnost_stitu


    def utok(self, postava):
        if self.mrtvy():
            return
        if not isinstance(postava, Postava):
            raise TypeError("postava musí být typu Postava")
        postava.uber_zivoty(self.poskozeni)


    def uber_zivoty(self, zivoty):
        if random.randint(1, 100) <= self.ucinnost_stitu:
            self.ucinnost_stitu *= 0.95
            return
        self.zivoty -= zivoty


class Kouzelnik(Postava):
    def __init__(self, jmeno, zivoty, vyleceni):
        super().__init__(jmeno, zivoty)
        self.vyleceni = vyleceni


    def lecba(self, postava):
        if not isinstance(postava, Postava):
            raise TypeError("postava musí být typu Postava")
        if self.mrtvy() or postava.mrtvy():
            return
        postava.pridej_zivoty(self.vyleceni)



armada1 = Armada("hodni", "modra")
armada2 = Armada("zli", "cervena")

p1 = Postava("Pepa", 100)
p2 = Postava("Franta", 80)

armada1.pridej_postavu(p1)
armada2.pridej_postavu(p2)

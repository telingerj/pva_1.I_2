#  hra, ve které proti sobě bojují dvě armády
import random
import pygame

pygame.init()

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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.armada = None
        self.pozice = pozice
        self.textura_leva = textura_leva
        self.textura_prava = textura_prava
        self.otoceni = True


    def pridej_armadu(self, armada):
        self.armada = armada


    def uber_zivoty(self, zivoty):
        self.zivoty -= zivoty


    def pridej_zivoty(self, zivoty):
        self.zivoty += zivoty


    def mrtvy(self):
        return self.zivoty <= 0


    def vykresli(self, screen):
        if self.otoceni:
            screen.blit(self.textura_prava, self.pozice)
        else:
            screen.blit(self.textura_leva, self.pozice)


class Bojovnik(Postava):
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass



class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, pocet_sipu):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni)
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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, ucinnost_stitu):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni)
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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, vyleceni):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava)
        self.vyleceni = vyleceni


    def lecba(self, postava):
        if not isinstance(postava, Postava):
            raise TypeError("postava musí být typu Postava")
        if self.mrtvy() or postava.mrtvy():
            return
        postava.pridej_zivoty(self.vyleceni)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.textury = []
        self.nacti_textury()
        self.vytvor_postavy()


    def nacti_textury(self):
        for postava in ["archer", "magician", "swordsman"]:
            for otoceni in ["left", "right"]:
                image = pygame.image.load("images/" + postava + "_" + otoceni + ".png")
                self.textury.append(image)


    def vytvor_postavy(self):
        self.armada1 = Armada("hodni", (0, 0, 255))
        self.armada2 = Armada("zli", (255, 0, 0))

        self.s1 = Sermir("Pepa", 100, (100, 100), self.textury[4], self.textury[5], 10, 5)
        self.s2 = Sermir("Franta", 100, (600, 100), self.textury[4], self.textury[5], 10, 5)

        self.armada1.pridej_postavu(self.s1)
        self.armada2.pridej_postavu(self.s2)



    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.clock.tick(60)
            self.s1.vykresli(self.screen)
            self.s2.vykresli(self.screen)
            pygame.display.flip()

game = Game()
game.loop()

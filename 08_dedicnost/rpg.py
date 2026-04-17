#  hra, ve které proti sobě bojují dvě armády
import random
import pygame

pygame.init()
pygame.font.init()

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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, font):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.max_zivoty = zivoty
        self.armada = None
        self.pozice = pozice
        self.textura_leva = textura_leva
        self.textura_prava = textura_prava
        self.otoceni = True
        self.jmeno_textura = font.render(self.jmeno, True, (0, 150, 0))


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

        pomer_zivotu = self.zivoty / self.max_zivoty
        pygame.draw.rect(screen, (100, 100, 100),
                         (self.pozice[0] - 10, self.pozice[1] - 15, 35, 5))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.pozice[0] - 10, self.pozice[1] - 15, 35 * pomer_zivotu, 5))

        screen.blit(self.jmeno_textura, (self.pozice[0] - 10, self.pozice[1] - 30))


    def pohyb(self):
        if self.otoceni:
            self.pozice = (self.pozice[0] + 1, self.pozice[1])
        else:
            self.pozice = (self.pozice[0] - 1, self.pozice[1])

        if self.pozice[0] <= 0 and not self.otoceni:
            self.otoc()
        elif self.pozice[0] >= 800 - self.textura_leva.get_size()[0] and self.otoceni:
            self.otoc()


    def otoc(self):
        self.otoceni = not self.otoceni



class Bojovnik(Postava):
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, font):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, font)
        self.poskozeni = poskozeni


    def utok(self, postava):
        pass



class Lucistnik(Bojovnik):
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, pocet_sipu, font):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, font)
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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, ucinnost_stitu, font):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, poskozeni, font)
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
    def __init__(self, jmeno, zivoty, pozice, textura_leva, textura_prava, vyleceni, font):
        super().__init__(jmeno, zivoty, pozice, textura_leva, textura_prava, font)
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
        self.jmeno_postavy_font = pygame.font.SysFont("Calibri", 15)
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

        s1 = Sermir("Pepa", 100, (100, 100), self.textury[4], self.textury[5], 10, 5, self.jmeno_postavy_font)
        l1 = Lucistnik("Honza", 80, (80, 250), self.textury[0], self.textury[1], 5, 10, self.jmeno_postavy_font)
        k1 = Kouzelnik("Merlin", 50, (100, 500), self.textury[2], self.textury[3], 10, self.jmeno_postavy_font)


        s2 = Sermir("Franta", 100, (600, 100), self.textury[4], self.textury[5], 10, 5, self.jmeno_postavy_font)
        l2 = Lucistnik("Kuba", 80, (580, 250), self.textury[0], self.textury[1], 5, 10, self.jmeno_postavy_font)
        k2 = Kouzelnik("David", 50, (600, 500), self.textury[2], self.textury[3], 10, self.jmeno_postavy_font)

        self.armada1.pridej_postavu(s1)
        self.armada1.pridej_postavu(l1)
        self.armada1.pridej_postavu(k1)

        self.armada2.pridej_postavu(s2)
        self.armada2.pridej_postavu(l2)
        self.armada2.pridej_postavu(k2)

        for postava in self.armada2.postavy:
            postava.otoc()


    def vykresli(self):
        for armada in [self.armada1, self.armada2]:
            for postava in armada.postavy:
                postava.vykresli(self.screen)
                postava.pohyb()


    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.vykresli()
            self.clock.tick(60)
            pygame.display.flip()

game = Game()
game.loop()

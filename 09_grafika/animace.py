import pygame

class AnimatedObject:
    def __init__(self, x, y, sizeX, sizeY, color):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.odraz_x = 1
        self.odraz_y = 1


    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.sizeX, self.sizeY))
        self.check(screen)


    def move(self, moveX, moveY):
        self.x += moveX * self.odraz_x
        self.y += moveY * self.odraz_y


    def check(self, screen):
        if self.x >= screen.get_size()[0] - self.sizeX:
            self.odraz_x = -1
        elif self.x <= 0:
            self.odraz_x = 1

        if self.y >= screen.get_size()[1] - self.sizeY:
            self.odraz_y = -1
        elif self.y <= 0:
            self.odraz_y = 1


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

"""
def draw(posX):
    pygame.draw.rect(screen, (255, 0, 0), (posX, 300, 100, 100))
"""

ctverec1 = AnimatedObject(200, 100, 100, 100, (255, 0, 0))
ctverec2 = AnimatedObject(100, 200, 50, 50, (0, 255, 0))
ctverec3 = AnimatedObject(300, 100, 200, 200, (0, 0, 255))
ctverec4 = AnimatedObject(400, 200, 10, 10, (255, 255, 0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    clock.tick(60)
    ctverec1.draw(screen)
    ctverec2.draw(screen)
    ctverec3.draw(screen)
    ctverec4.draw(screen)
    ctverec1.move(10, 0)
    ctverec2.move(10, 10)
    ctverec3.move(20, 5)
    ctverec4.move(10, 10)
    pygame.display.flip()

pygame.quit()

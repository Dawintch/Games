import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))

class Actor(pygame.sprite.Sprite):
    def __init__(self, group, color, layer, pos):
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, group)

group = pygame.sprite.LayeredUpdates()
Actor(group, (255, 255, 255), 0, (100, 100))
Actor(group, (255, 0, 255),   1, (110, 110))
Actor(group, (0, 255, 255),   0, (120, 120))
Actor(group, (255, 255, 0),   3, (130, 130))
Actor(group, (0, 0, 255),     2, (140, 140))

run = True
while run:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    group.update()
    group.draw(screen)
    pygame.display.flip()
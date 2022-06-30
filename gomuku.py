import pygame

from pygame.locals import(
    MOUSEBUTTONUP
)
#variables

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
Yello = (208,176,144)
PLAYER = False

#grid
WIDTH = 20
MARGIN = 1
PADDING = 20
DOT = 4
BOARD = (WIDTH + MARGIN) * 14 + MARGIN
GAME_WIDTH = BOARD + PADDING *2
GAME_HIGHT = GAME_WIDTH + 100

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, length):
        super().__init__()
        self.length = int(length)
        self.image = pygame.Surface([length,length])
       
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,color, pygame.Rect(0,0,length,length))

        self.rect = self.image.get_rect()
        self.data = 0
        #clicked
    def drawClickedBlack(self):
        pygame.draw.circle(self.image, BLACK, (self.length/2,self.length/2),self.length/2-1,20)
        self.data = 1
    def drawClickedWhite(self):
        pygame.draw.circle(self.image, BLACK, (self.length/2,self.length/2),19,2)
        pygame.draw.circle(self.image, WHITE, (self.length/2,self.length/2),18,18)
        self.data =2
        
def drawline(n):
    for i in range(n):
        pygame.draw.line(screen, BLACK, (50, i * 40+50), (610, i * 40+50), 5)
        pygame.draw.line(screen, BLACK, (i * 40+50, 50), (i * 40+50, 610), 5)

pygame.init()


def checkwin(row,tempGroup):
    
    CrossWin = 0
    CircleWin = 0
    for block in tempGroup:
        if block.data ==1:
            CrossWin+=1
        if block.data ==2:
            CircleWin +=1
        if CrossWin ==3:
            print("Cross Wins")
        if CircleWin ==3 :
            print("Circle Wins")



# Set up the drawing window
screen = pygame.display.set_mode([650, 650])
pygame.display.set_caption("Testing")
screen.fill((255,255,255))
game_surf = pygame.surface.Surface([700, 700])


group = pygame.sprite.Group()

for i in range(15):
    for j in range(15):
        block = Sprite(WHITE, 40)
        block.rect.x = i*40
        block.rect.y = j*40
        group.add(block)



clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
check = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for block in group:
                if block.rect.collidepoint(pos):
                    
                    if block.data == 0:
                        if check == 0:
                            block.drawClickedBlack()
                            check = 1
                        else :
                            block.drawClickedWhite()
                            check = 0
                    print(block.data)
            
            #checkwin(3,group)
    group.update()
    screen.fill(WHITE)
    group.draw(screen)
    drawline(15)





    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
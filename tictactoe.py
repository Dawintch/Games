import pygame

from pygame.locals import(
    MOUSEBUTTONUP
)
#variables

linecolor = (0,0,0)
SURFACE_COLOR = (255,255,255)
RED = (255,0,0)
COLOR = (255,100,98)

class TicTacToe:
    def __init__(self):
        self.grid = [[0 for x in range(3)] for y in range(3)]
        pygame.init()
        pygame.display.set_caption("TicTacToe")

        self.running = True
        self._win = False
        
        
        self.group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.Player = 1
        self.last_move = [2,2]

    


    def check_event(self,event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == MOUSEBUTTONUP:
            for block in self.group:
                if block.rect.collidepoint(pos):
                    r = (pos[0])//200
                    c = (pos[1])//200
                    self.last_move = [r,c]
                    #print(self.last_move)
                    if block.data == 0:
                        if self.Player == 1:
                            block.drawClickedCross()
                            self.grid[c][r] = 1
                            self.Player = 2
                        else :
                            block.drawClickedCircle()
                            self.Player = 1
                            self.grid[c][r] = -1
                                #print(block.data)
                        #print(self.grid)
            self.checkwin()


    def run_game(self):
        print("running")
        self.render_board()
        while(self.running):
            for event in pygame.event.get():
                self.check_event(event)
            self.update_board()
        self.endGame()

    def update_board(self):
            self.group.update()
            self.screen.fill(SURFACE_COLOR)
            self.group.draw(self.screen)
            self.drawline(4)
            pygame.display.flip()
            self.clock.tick(60)


    def render_board(self):
        # Set up the drawing window
        self.screen = pygame.display.set_mode([600, 600])
        pygame.display.set_caption("Testing")
        self.screen.fill((255,255,255))
        
        for i in range(3):
            for j in range(3):
                block = Sprite(SURFACE_COLOR, 200, 200)
                block.rect.x = i*200
                block.rect.y = j*200
                self.group.add(block)


    def drawline(self,n):
        for i in range(n):
            pygame.draw.line(self.screen, linecolor, (0, i * 200), (600, i * 200), 5)
            pygame.draw.line(self.screen, linecolor, (i * 200, 0), (i * 200, 600), 5)
                 
    
    def endGame(self):
        pygame.quit()

    def checkwin(self):
        r = self.last_move[1]
        c = self.last_move[0]
        
        #checkrow
        if sum(self.grid[r]) == 3:
            print("Cross Win")
        if sum(self.grid[r]) == -3:
            print("circle win")
        #checkColumn
        vertSum = 0
        for i in range (3):
            vertSum += self.grid[i][c]
        if vertSum == 3:
            print("Cross WIn")
        if vertSum == -3:
            print("Circle Win")
        #checkDiagnoal
        if self.grid[0][0]+self.grid[1][1]+self.grid[2][2] == 3:
            print("Cross win")
        if self.grid[0][0]+self.grid[1][1]+self.grid[2][2] == -3:     
            print("Circle Win")
        if self.grid[0][2]+self.grid[1][1]+self.grid[2][0] == 3:   
             print("Cross win")
        if self.grid[0][2]+self.grid[1][1]+self.grid[2][0] == -3:   
             print("Circle win")



#custmized sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width,height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,color, pygame.Rect(0,0,width,height))

        self.rect = self.image.get_rect()
        self.data = 0
        #clicked
    def drawClickedCross(self):
        pygame.draw.line(self.image, linecolor, (20, 20), (self.width - 20, self.height - 20), 20)
        pygame.draw.line(self.image, linecolor, (self.width - 20, 20), (20, self.height - 20), 20)
        self.data = 1
    def drawClickedCircle(self):
        pygame.draw.ellipse(self.image, linecolor, [10, 10,self.height-20, self.width-20], 10)
        self.data =2
        


# Done! Time to quit.



if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.run_game()
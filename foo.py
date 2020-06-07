'''
pygamegame.py
FRAMEWORK CREATED BY: Lukas Peraza
'''
import pygame, webbrowser, os


class PygameGame(object):

    def init(self):
        print(pygame.image.get_extended())
        self.background = pygame.image.load("capitalOne.png")
        self.title = "Tartan Hacks" #TITLE
        self.names = "Made by Denzel Hardy, Roshan Nair, Mihir Paralkar, and Mayur Paralkar"
        self.namesFont = pygame.font.Font(None, 40)
        self.titleScreen = False
        self.menuSelection = None
        self.clicked = None
        self.selections = ['Branch Performance', 'ATM', 'Accounts'] #EDIT NAMES HERE
        self.cellHeight = self.height // 10
        self.cellWidth = self.width //2
        self.font = pygame.font.Font(None, 70)
        self.spaceBetween = self.cellHeight // 2

    def mousePressed(self, x, y):
        self.clicked = self.menuSelection

    def mouseReleased(self, x, y):
    	#EDIT URLS HERE
        if self.clicked == 0: 
        	webbrowser.open("https://plot.ly/dashboard/temp18%3A6/")
        elif self.clicked == 1:
        	webbrowser.open("bing.com")
        elif self.clicked == 2:
        	webbrowser.open("youtube.com")
        self.clicked = None


    def mouseMotion(self, x, y):
        if x < 3*self.width/4 and x > self.width/4:
        	if y < 2*self.cellHeight + self.spaceBetween and y > self.cellHeight + self.spaceBetween:
        		self.menuSelection = 0
        	elif y < 3 * self.cellHeight + 2*self.spaceBetween and y > 2 * self.cellHeight + 2*self.spaceBetween:
        		self.menuSelection = 1
        	elif y < 4 * self.cellHeight + 3 * self.spaceBetween and y > 3 * self.cellHeight + 3 * self.spaceBetween:
        		self.menuSelection = 2
        	else:
        		self.menuSelection = None
        else:
        	self.menuSelection = None
  

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        screen.blit(self.background, (self.width // 2 - self.background.get_size()[0] / 2, 3*self.height // 5 ))
        for selection in range(len(self.selections)):
            if self.clicked == selection: 
                color = (0,0, 255)
            elif self.menuSelection == selection: 
                color = (127, 127, 127)
            else:
                color = (0,0,0)
            self.image = pygame.Surface((self.cellWidth, self.cellHeight))
            self.image.fill(color)
            text = self.font.render(self.selections[selection], True, (255,255,255))
            self.image.blit(text, (self.cellWidth//2 - text.get_size()[0]/2,0))
            
            screen.blit(self.image, (self.width//4, self.cellHeight * (selection + 1) + self.spaceBetween * (selection + 1)))

        title = self.font.render(self.title, True, (0,0,0))
        size = title.get_size()
        screen.blit(title, (self.width//2 - size[0] // 2, (len(self.selections) + 2)*(self.cellHeight + self.spaceBetween + 4)))

        names = self.namesFont.render(self.names, True, (0,0,0))
        namesSize = names.get_size()
        screen.blit(names, (self.width//2 - namesSize[0] // 2, (len(self.selections) + 3)*(self.cellHeight + self.spaceBetween)))

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1200, height=800, fps=50, title="Tartan Hacks"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

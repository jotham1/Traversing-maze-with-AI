import random
import pygame
pygame.init()
import sys

#SEE LINE167 TO FIX THE looping ISSUE for the episodes
clock = pygame.time.Clock()
# global variables
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)

class Grid:
    def __init__(self):
        #The grid will be 5x5
        self.dimensions = 5
        #agent can only move 1 square at a time
        self.moveDistance = 100
        #Dimensions for the whole page
        self.canvasHeight = 1000
        self.canvasWidth = 1000
        #width of a single square in the grid 
        self.singleGridWidth = 100
        #starting position for the agent is in the top left corner of the grid
        self.startX = 200
        self.startY = 300
        #The end location is in the bottom right corner of the grid
        self.endX = 600
        self.endY = 700
        #obstacle 1 location
        self.obs1x = 300
        self.obs1y = 500
        #obstacle 2 location
        self.obs2x = 500
        self.obs2y = 400

        self.screen = pygame.display.set_mode((self.canvasWidth, self.canvasHeight))
        pygame.display.set_caption('Grid World')
        self.screen.fill(BLACK)

    def drawGrid(self):
        # Main grid
        pygame.draw.rect(self.screen,WHITE,(self.startX, self.startY, 500, 500))
        #end zone
        pygame.draw.rect(self.screen, BLUE, pygame.Rect(self.endX,self.endY,self.singleGridWidth,self.singleGridWidth))
        # Drawing the obstacles at 300,500(which is 2,3) and 500,400(which is 4,1)
        pygame.draw.rect(self.screen, GREEN,(self.obs1x,self.obs1y,self.singleGridWidth,self.singleGridWidth))
        pygame.draw.rect(self.screen, GREEN, (self.obs2x,self.obs2y,self.singleGridWidth,self.singleGridWidth))
        for i in range(4):
            pygame.draw.line(self.screen,BLACK,((i+3)*100,300),((i+3)*100,800))
        for j in range(4):
            pygame.draw.line(self.screen,BLACK,(200,(j+4)*100),(700,(j+4)*100))
        dim = 5
        grid = [[(x,y) for x in range(dim)] for y in range(dim)]
    
    def redrawLines(self):
        for i in range(4):
            pygame.draw.line(self.screen,BLACK,((i+3)*100,300),((i+3)*100,800))
        for j in range(4):
            pygame.draw.line(self.screen,BLACK,(200,(j+4)*100),(700,(j+4)*100))

    def findAgent(self):
        checkX = 200
        checkY = 300
        
        found = False
        for i in range(5):
            for j in range(5):
                coord = (checkX+50+(j*100),checkY+50+(i*100))    
                colour = self.screen.get_at(coord)[:3]  # (R, G, B)   
                if(colour == RED ):
                    print(f"Agent location at {i},{j}")
                    output = (i,j)
                    found = True
                    break
            if(found == True):
                return output
                break

class Agent:
    def __init__(self,canvas,startX,startY,width):
        self.episodeStepLimit = 10
        self.canvas = canvas
        self.startX = startX
        self.startY = startY
        self.width = width
        self.currentX = self.startX
        self.currentY = self.startY
        self.agent = pygame.draw.rect(self.canvas, RED, (self.startX, self.startY,self.width,self.width))
    
    
    

    def move(self,grid,direction):

        pygame.draw.rect(self.canvas, WHITE, (self.currentX, self.currentY,self.width,self.width))
        if(direction == "left"):
            self.currentX -= 100
        elif(direction == "right"):
            self.currentX += 100
        elif(direction == "up"):
            self.currentY -= 100
        elif(direction == "down"):
            self.currentY += 100

        self.agent = pygame.draw.rect(self.canvas, RED, (self.currentX, self.currentY,self.width,self.width))
        grid.redrawLines()
        pygame.display.flip()


    def resetGrid(self,grid):
        grid.drawGrid()
        self.agent = pygame.draw.rect(self.canvas, RED, (self.startX, self.startY,self.width,self.width)) 


    def randomMove(self,grid):
        playing = True
        valid = False
        pygame.draw.rect(self.canvas, WHITE, (self.currentX, self.currentY,self.width,self.width))
        while(valid == False):
            num = random.randint(1,4)
            if(num ==1):
                self.currentX -= 100
                print("left")
            elif(num ==2):
                self.currentX += 100
                print("right")
            elif(num == 3):
                self.currentY -= 100
                print("up")
            elif(num ==4):
                self.currentY += 100
                print("down")
            if(self.currentX >=self.startX and self.currentX <= 600 and self.currentY >= self.startY and self.currentY <=700):
                #fix the program so it doesnt crash into green
                if (not((self.currentX == grid.obs1x and self.currentY == grid.obs1y) or (self.currentX == grid.obs2x and self.currentY ==grid.obs2y))):
                    valid = True
            
            else:
                
                if(num ==1):
                    self.currentX += 100
                    print("left")
                elif(num ==2):
                    self.currentX -= 100
                    print("right")
                elif(num == 3):
                    self.currentY += 100
                    print("up")
                elif(num ==4):
                    self.currentY -= 100
                    print("down")


        self.agent = pygame.draw.rect(self.canvas, RED, (self.currentX, self.currentY,self.width,self.width))
        grid.redrawLines()
        pygame.display.flip()
    #trialling episodes
    #Facing big issues with: 
        #resetting after each episode
        #Movement is not working properly
        #       
    def run(self,grid,agent):
        noSteps = 0
        minSteps = 0
        # There ill be 1000 trials in total
        for episode in range(self.episodeStepLimit):
            #The maximum number of steps allowed(for efficiency) is 100 
            noSteps = 0
            for steps in range(100):              
                if(grid.findAgent() == (4,4)):   
                    self.resetGrid(grid)
                    pygame.draw.rect(grid.screen, BLUE, pygame.Rect(grid.endX,grid.endY,grid.singleGridWidth,grid.singleGridWidth))

                    if(minSteps>=noSteps): 
                        print(f"The episode with the shortest number of steps so far is step {episode}")
                        print(f"The smallest number of steps so far is {noSteps} ")
                        minSteps = noSteps
                        break
                agent.randomMove(grid)
                noSteps = noSteps+1
                pygame.time.delay(500)
            
        

def main():
    
    playing = True
    grid1 = Grid()
    grid1.drawGrid()
    myAgent = Agent(grid1.screen,grid1.startX,grid1.startY,grid1.singleGridWidth)
    pygame.display.flip()
    #Failed implementation 
    #myAgent.run(grid1,myAgent)
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        myAgent.randomMove(grid1)
        
        
        if(grid1.findAgent() == (4,4)):
            playing = False
            break
        clock.tick(60)
        

    


    
if __name__ == "__main__":    
    main()

pygame.quit()
sys.exit()

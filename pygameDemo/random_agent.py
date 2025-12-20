import random
import pygame
import time
pygame.init()
import sys

import my_globals as gl

clock = pygame.time.Clock()

class RandomAgent:
    def __init__(self,canvas,startX,startY,width):
        self.episodeStepLimit = 10
        self.canvas = canvas
        self.startX = startX
        self.startY = startY
        self.width = width
        self.currentX = self.startX
        self.currentY = self.startY
        self.agent = pygame.draw.rect(self.canvas, gl.RED, (self.startX, self.startY,self.width,self.width))
    
    
    

    def move(self,grid,direction):

        pygame.draw.rect(self.canvas, gl.WHITE, (self.currentX, self.currentY,self.width,self.width))
        if(direction == "left"):
            self.currentX -= 100
        elif(direction == "right"):
            self.currentX += 100
        elif(direction == "up"):
            self.currentY -= 100
        elif(direction == "down"):
            self.currentY += 100

        self.agent = pygame.draw.rect(self.canvas, gl.RED, (self.currentX, self.currentY,self.width,self.width))
        grid.redrawLines()
        pygame.display.flip()


    def resetGrid(self,grid):
        grid.drawGrid()
        self.agent = pygame.draw.rect(self.canvas, gl.RED, (self.startX, self.startY,self.width,self.width)) 
        self.currentX = self.startX
        self.currentY = self.startY

    def randomMove(self,grid):
        playing = True
        valid = False
        direction = ""
        pygame.draw.rect(self.canvas, gl.WHITE, (self.currentX, self.currentY,self.width,self.width))
        while(valid == False):
            num = random.randint(1,4)
            if(num ==1):
                self.currentX -= 100
                direction = "left"
            elif(num ==2):
                self.currentX += 100
                direction = "right"
            elif(num == 3):
                self.currentY -= 100
                direction = "up"
            elif(num ==4):
                self.currentY += 100
                direction = "down"
            if(self.currentX >=self.startX and self.currentX <= 600 and self.currentY >= self.startY and self.currentY <=700):
                
                if (not((self.currentX == grid.obs1x and self.currentY == grid.obs1y) or (self.currentX == grid.obs2x and self.currentY ==grid.obs2y))):
                    valid = True
                    print(direction)
            
            else:
                
                if(num ==1):
                    self.currentX += 100
                    
                elif(num ==2):
                    self.currentX -= 100
                    
                elif(num == 3):
                    self.currentY += 100
                    
                elif(num ==4):
                    self.currentY -= 100
                    


        self.agent = pygame.draw.rect(self.canvas, gl.RED, (self.currentX, self.currentY,self.width,self.width))
        grid.redrawLines()
        pygame.display.flip()
    #trialling episodes
   
        
            
    def run(self,grid,agent):
        noSteps = 0
        minSteps = 10**6
        # There ill be 1000 trials in total
        for episode in range(self.episodeStepLimit):
            #The maximum number of steps allowed(for efficiency) is 100 
            noSteps = 0
            for steps in range(100):   
                if steps == 0:
                    pygame.time.delay(50)          
                agent.randomMove(grid)
                noSteps = noSteps+1
                pygame.time.delay(50)
                if(grid.findAgent() == (4,4)):                     
                    self.resetGrid(grid)
                    pygame.draw.rect(grid.screen, gl.BLUE, pygame.Rect(grid.endX,grid.endY,grid.singleGridWidth,grid.singleGridWidth))
                    pygame.display.flip()
                    time.sleep(3)
                    if(minSteps>=noSteps): 
                        print(f"The episode with the shortest number of steps so far is step {episode}")
                        print(f"The smallest number of steps so far is {noSteps} ")
                        minSteps = noSteps
                        break
            
            pygame.time.delay(50)
            clock.tick(120)
            
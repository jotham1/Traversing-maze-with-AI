import random
import pygame
pygame.init()
import sys

import my_globals as gl

clock = pygame.time.Clock()

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
        self.screen.fill(gl.BLACK)

    def drawGrid(self):
        # Main grid
        pygame.draw.rect(self.screen,gl.WHITE,(self.startX, self.startY, 500, 500))
        #end zone
        pygame.draw.rect(self.screen, gl.BLUE, pygame.Rect(self.endX,self.endY,self.singleGridWidth,self.singleGridWidth))
        # Drawing the obstacles at 300,500(which is 2,3) and 500,400(which is 4,1)
        pygame.draw.rect(self.screen, gl.GREEN,(self.obs1x,self.obs1y,self.singleGridWidth,self.singleGridWidth))
        pygame.draw.rect(self.screen, gl.GREEN, (self.obs2x,self.obs2y,self.singleGridWidth,self.singleGridWidth))
        for i in range(4):
            pygame.draw.line(self.screen,gl.BLACK,((i+3)*100,300),((i+3)*100,800))
        for j in range(4):
            pygame.draw.line(self.screen,gl.BLACK,(200,(j+4)*100),(700,(j+4)*100))
        dim = 5
        grid = [[(x,y) for x in range(dim)] for y in range(dim)]
    
    def redrawLines(self):
        for i in range(4):
            pygame.draw.line(self.screen,gl.BLACK,((i+3)*100,300),((i+3)*100,800))
        for j in range(4):
            pygame.draw.line(self.screen,gl.BLACK,(200,(j+4)*100),(700,(j+4)*100))

    def findAgent(self):
        checkX = 200
        checkY = 300
        
        found = False
        for i in range(5):
            for j in range(5):
                coord = (checkX+50+(j*100),checkY+50+(i*100))    
                colour = self.screen.get_at(coord)[:3]  # (R, G, B)   
                if(colour == gl.RED ):
                    print(f"Agent location at {i},{j}")
                    output = (i,j)
                    found = True
                    break
            if(found == True):
                return output
                break

import pygame
pygame.init()
import sys
clock = pygame.time.Clock()
dimensions = 5
moveDistance = 100
canvasHeight = 1000
canvasWidth = 1000
singleGridWidth = 100
# color
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((canvasWidth, canvasHeight))
pygame.display.set_caption('Grid World')
# setup timer



startX = 200
startY = 300
endX = 600
endY = 700
#When you create a rectangle it uses the top leftof the rect to map coordinates
#This means that for the object to appear in bottom left, the x has to be 0
# the y has to be the max dist - the width to show up or else it will be just under
#      

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.fill(BLACK)

# Draw a agent in the left bottom, a target on the top right
    pygame.draw.rect(screen,WHITE,(startX, startY, 500, 500))
    agent = pygame.draw.rect(screen, RED, (startX, startY, singleGridWidth, singleGridWidth))
    
    pygame.draw.rect(screen, BLUE, pygame.Rect(endX,endY, singleGridWidth,singleGridWidth))
# Adds all shapes that are drawn to the surface
    for i in range(4):
        pygame.draw.line(screen,BLACK,((i+3)*100,300),((i+3)*100,800))
    for j in range(4):
        pygame.draw.line(screen,BLACK,(200,(j+4)*100),(700,(j+4)*100))
    dim = 5
    grid = [[(x,y) for x in range(dim)] for y in range(dim)]
    checkX = 200
    checkY = 300
    for i in range(5):
        for j in range(5):
            coord = (checkX+50+(j*100),checkY+50+(i*100))    
            colour = screen.get_at(coord)[:3]  # (R, G, B)   
            if(colour == RED ):
                print(f"Agent location at {i},{j}")
                found = True
                break
        if(found == True):
            break

            
    



    pygame.display.flip()
pygame.quit()


    
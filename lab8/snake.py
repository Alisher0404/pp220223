import pygame
import random
import math
pygame.init()

black=(0,0,0)
red=(220,20,60)
white=(255,255,255)
vanila=(255,250,226)
pink=(255,204,255)

display_width=400
display_height=400

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Snake")

clock=pygame.time.Clock()

block_size=10

font=pygame.font.SysFont(None,25)

def score(score):
    text=font.render("Score:"+str(score),True,red)
    gameDisplay.blit(text,[0,0])

def level(score):
    text=font.render("Level:"+str(score),True,red)
    gameDisplay.blit(text,[0,15])



def snake(block_size,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay,red,[XnY[0],XnY[1],block_size,block_size])

gameDisplay.fill(red)
pygame.display.update()


def gameLoop():
    gameExit=False

    lead_x=display_width/2
    lead_y=display_height/2

    lead_x_change=0
    lead_y_change=0

    snakeList=[]
    snakeLength=1

    foodX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
    foodY=round(random.randrange(0,display_height-block_size)/10.0)*10.0

    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_LEFT:
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()

        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            pygame.quit()
            quit()

        lead_x+=lead_x_change
        lead_y+=lead_y_change

        gameDisplay.fill(pink)
        pygame.draw.rect(gameDisplay,black,[foodX,foodY,block_size,block_size])

        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameExit = True

        snake(block_size,snakeList)

        score(snakeLength-1)

        if len(snakeList)>=11 and len(snakeList)<21:
            level(1)
        elif len(snakeList)<11:
            level(0)
        elif len(snakeList)>=21 and len(snakeList)<31:
            level(2)
        elif len(snakeList)>=31 and len(snakeList)<math.inf:
            level(3)

        pygame.display.update()

        if lead_x==foodX and lead_y==foodY:
            
            foodX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
            foodY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakeLength+=1

        if len(snakeList)>=11 and len(snakeList)<21:
            clock.tick(15)
        elif len(snakeList)<11:
            clock.tick(10)
        elif len(snakeList)>=21 and len(snakeList)<31:
            clock.tick(20)
        elif len(snakeList)>=31 and len(snakeList)<math.inf:
            clock.tick(25)

    pygame.quit()
    quit()

gameLoop()
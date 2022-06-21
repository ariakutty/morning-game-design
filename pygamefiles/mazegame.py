#aria kutty
#final game
#maze

import sys
import pygame, time,os,random, math, datetime 
pygame.init()#initialize the pygame package
date=datetime.datetime.now() 
pygame.init() 
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255), "green": (50,200,10) , "blue":(0,0,255), "limeGreen":(153,255,51)}
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT))  

while True:
    Bx=WIDTH//3
    wall= pygame.Rect(Bx, 150, WIDTH//4, 20)
    bg=pygame.image.load('pygamefiles\images\\background.png')
    screen.blit(bg, (0, 0))
    dog=pygame.image.load('pygamefiles\images\\dog.png.jpg')
    dog=pygame.transform.scale(dog, (40,40))
    screen.blit(dog, (WIDTH//2.5, HEIGHT//2.5))
    pygame.draw.rect(screen, colors.get("green"), wall)
    pygame.display.update()
    pygame.time.delay(1000)




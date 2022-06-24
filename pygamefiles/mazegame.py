#aria kutty
#final game
#maze

import pygame, time,os,random, math, datetime, sys
from pygame.locals import*
pygame.init()#initialize the pygame package
date=datetime.datetime.now() 
pygame.init() 
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255), "green": (50,200,10) , "blue":(0,0,255), "limeGreen":(153,255,51)}
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT))  

dog=pygame.image.load('pygamefiles\images\\dog.png.jpg')
bg=pygame.image.load('pygamefiles\images\\background.png')
dogbone=pygame.image.load('pygamefiles\images\\dogbone.png')
youwin=pygame.image.load('pygamefiles\images\\youwin.jpg')
x_dog = 30
y_dog = 0
score=0

wall1= pygame.Rect(80, 120, 80, 20)
wall2= pygame.Rect(0,0, 20, 700)
wall3= pygame.Rect(80, 0, 20, 120)
wall4= pygame.Rect(0, 215, 200, 20)
wall5= pygame.Rect(80, 120,200, 20)
wall6= pygame.Rect(270, 120, 20, 200)
wall7= pygame.Rect(180, 224, 20, 200)
wall8= pygame.Rect(185, 404, 280, 20)
wall9= pygame.Rect(368, 53, 20, 300)
wall10= pygame.Rect(370, 333, 200, 20)
wall11= pygame.Rect(88, 266, 20, 150)
wall12= pygame.Rect(550, 345, 20, 184)
wall13= pygame.Rect(351, 509, 200, 20)
wall14= pygame.Rect(368, 54, 220, 20)
wall15= pygame.Rect(350, 510, 20, 100)
wall15= pygame.Rect(680, 54, 20, 560)
wall16= pygame.Rect(447, 127, 240, 20)
wall17= pygame.Rect(368, 200, 240, 20)
wall18= pygame.Rect(447,267 , 240, 20)
wall19= pygame.Rect(351, 405 , 20, 110)
wall20= pygame.Rect(290, 594 , 435, 20)
wall21= pygame.Rect(270, 514 , 20, 100)
wall22= pygame.Rect(89, 508 , 201, 20)
dog=pygame.transform.scale(dog, (40,40))
dogRect = dog.get_rect()
dogbone=pygame.transform.scale(dogbone, (50, 40))
boneRect = dogbone.get_rect()

wallList=[wall1, wall2, wall3, wall4,wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14,wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22]
#will go under the main game 1 function
#game two will have the same walls set up, but will have powerups throughout the middle
while True:
    mousePos = pygame.mouse.get_pos()
    mx = mousePos[0]
    my = mousePos[1]
    Bx=WIDTH//3

    screen.blit(bg, (0, 0))
    
    screen.blit(dog, dogRect)
    
    screen.blit(dogbone, (620, 625))
    pygame.draw.rect(screen, colors.get("green"), wall1)
    pygame.draw.rect(screen, colors.get("green"), wall2)
    pygame.draw.rect(screen, colors.get("green"), wall3)
    pygame.draw.rect(screen, colors.get("green"), wall4)
    pygame.draw.rect(screen, colors.get("green"), wall5)
    pygame.draw.rect(screen, colors.get("green"), wall6)
    pygame.draw.rect(screen, colors.get("green"), wall7)
    pygame.draw.rect(screen, colors.get("green"), wall8)
    pygame.draw.rect(screen, colors.get("green"), wall9)
    pygame.draw.rect(screen, colors.get("green"), wall10)
    pygame.draw.rect(screen, colors.get("green"), wall11)
    pygame.draw.rect(screen, colors.get("green"), wall12)
    pygame.draw.rect(screen, colors.get("green"), wall13)
    pygame.draw.rect(screen, colors.get("green"), wall14)
    pygame.draw.rect(screen, colors.get("green"), wall15)
    pygame.draw.rect(screen, colors.get("green"), wall16)
    pygame.draw.rect(screen, colors.get("green"), wall17)
    pygame.draw.rect(screen, colors.get("green"), wall18)
    pygame.draw.rect(screen, colors.get("green"), wall19)
    pygame.draw.rect(screen, colors.get("green"), wall20)
    pygame.draw.rect(screen, colors.get("green"), wall21)
    pygame.draw.rect(screen, colors.get("green"), wall22)
    
    pygame.display.update()

    keyPressed= pygame.key.get_pressed()
    speed= 4
    if keyPressed[K_LEFT]: 
        dogRect.x -= speed
    elif keyPressed[K_RIGHT]:
        dogRect.x+= speed
    elif keyPressed[K_UP]:
        dogRect.y -= speed
    elif keyPressed[K_DOWN]:
        dogRect.y += speed

    for walls in wallList:
        if dogRect.colliderect(walls): 
            dogRect.x=30
            dogRect.y=0
    print(int(mx), int(my))

    if dogRect.collidepoint(620,625):
        score+=10 
        print(score)
        screen.fill('pink')
        pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()





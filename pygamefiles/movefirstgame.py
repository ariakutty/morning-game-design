#aria kutty
#learning about pygame
#learning how to move the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
# K_INSERT              insert

import pygame, time,os, random, math 
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255), "limeGreen":(153,255,51), "tan":(255,211,155), "orange":(255,127,36)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
#square variables
hb=50
wb=50
xb=100
yb=300
speed=2
cx=350
cy=350
rad=25
ibox = rad*math.sqrt(2) 
xig = cx-(ibox/2)
yig = cy-(ibox/2)
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
#create variable to move
bg=pygame.image.load('pygamefiles\images\\bgSmaller.jpg')
screen.blit(bg, (0, 0))
pygame.display.update()
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    keys= pygame.key.get_pressed() #this is a list
    if keys[pygame.K_RIGHT] and square.x < WIDTH-(wb):
        square.x += speed
    if keys[pygame.K_LEFT] and square.x > speed:
         square.x -= speed 
    if keys[pygame.K_UP] and square.y > speed:
        square.y-= speed 
    if keys[pygame.K_DOWN] and square.y < HEIGHT-(hb):
        square.y += speed
    if keys[pygame.K_d] and cx < WIDTH-(rad):
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_a] and cx > (speed+rad):
         cx -= speed 
         insSquare.x -= speed
    if keys[pygame.K_w] and cy > (speed+rad):
        cy-= speed 
        insSquare.y += speed
    if keys[pygame.K_s] and cy < HEIGHT-(rad):
        cy += speed
        insSquare.y += speed
    if square.colliderect(insSquare):
        print("boooooom")
        rad+=1 
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        ibox = rad*math.sqrt(2) 
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    screen.blit(char, (10,10))
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.draw.rect(screen, squareClr, insSquare, )
    pygame.display.update()
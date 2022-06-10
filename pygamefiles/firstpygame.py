#aria kutty
#learning about pygame



import pygame, time,os
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255)}
clr=colors.get("white")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
greenClr=(0,255,0)
# screen.fill(greenClr)
# pygame.display.update()
# pygame.time.delay(2000)
redClr=(255,0,0)
purpleClr=(125,0,125)
# screen.fill(redClr)
# pygame.display.update()
# pygame.time.delay(2000)
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb)# create the object to draw
#keep running create a lp
backgrnd=clr
run = True
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, redClr,square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, purpleClr, (350,350), 25)
    pygame.display.update()
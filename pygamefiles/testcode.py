# Fernando Gupta
# making the full menu
from pickle import TRUE
import pygame, os, time, random, math
pygame.init()
#screen dimentions
WIDTH = 700
HEIGHT = 700


TITLE_FONT = pygame.font.SysFont('comicsans', 20)
MENU_FONT = pygame.font.SysFont('comicsans', 25)

os.system('cls')

#buttons ofr menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx,150,WIDTH//4,40)
Button_instruct=pygame.Rect(Bx,150,WIDTH//4,40)
Button_settings=pygame.Rect(Bx,200,WIDTH//4,40)
Button_Game1=pygame.Rect(Bx,250,WIDTH//4,40)
Button_Game2=pygame.Rect(Bx,300,WIDTH//4,40)
Button_score=pygame.Rect(Bx,350,WIDTH//4,40)
Button_exit=pygame.Rect(Bx,400,WIDTH//4,40)
Button_color=pygame.Rect(Bx,150,WIDTH//4,40)
Button_size=pygame.Rect(Bx,200,WIDTH//4,40)
Button_sound=pygame.Rect(Bx,250,WIDTH//4,40)

#colors
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
messageMenu=['instructions','settings','game 1','game 2','scoreboard','exit']
messageSettings=["Background Color","Screen Size","sound on/off"]
titleMain="circle eat square menu"
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window
#images
bg = pygame.image.load("pygamefiles\images\\bgSmaller.jpg")
char = pygame.image.load("pygamefiles\images\PixelArtTutorial.png")
char = pygame.transform.scale(char, (50,50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#circle var
cx = 350
cy = 350
rad = 25

#square var
hb = 50
wb = 50
xb = 325
yb = 325
square = pygame.Rect(xb,yb,wb,hb) #create the object to draw

#char var
charx = xb
chary = yb

#inscribed square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

#bounce
mountainSquare = pygame.Rect(250, 320, 180, 250)
insSquare=pygame.Rect(xig,yig,ibox,ibox)




run= True
Game = False  
speed = 2  
def Menu(Title,message,MENU):
    
    textTitle = TITLE_FONT.render(Title,1,colors.get("blue"))
    screen.fill(colors.get("white"))
    xd = WIDTH//2 - (textTitle.get_width()//2)
    screen.blit(textTitle,(xd,50))
    yMenu=150
    clslist=list(colors.keys())
    for item in message:
        colorRand=random.choice(clslist)
        if colorRand=="blue":
            colorRand=random.choice(clslist)
    
    Button_menu=pygame.Rect(Bx,yMenu,WIDTH//3,40)
    text=MENU_FONT.render(item,1, colors.get("blue"))
    pygame.draw.rect(screen,colors.get(colorRand),Button_menu)
    screen.blit(text,(Bx,yMenu))
    pygame.display.update()
    pygame.time.delay(50)
    yMenu+=50 

    while MENU:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos
                mx = mousePos[0]
                my = mousePos[1]
                print(mx,my)
                if Button_instruct.collidepoint((mx,my)):
                    instruction("instructions","instructions.txt")
                if Button_settings.collidepoint((mx,my)):
                    settings()
                if Button_Game1.collidepoint((mx,my)):
                    Game_1()
                if Button_Game2.collidepoint((mx,my)):
                    Game_1()
                if Button_score.collidepoint((mx,my)):
                    score("ScoreBoard","cesscore.txt")
                if Button_exit.collidepoint((mx,my)):
                    textTitle = TITLE_FONT.render("Bye-Bye",1, colors.get("blue"))

def instruction():
    #title font
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("pygamefiles\instructions.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40

def score():
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("ScoreBoard", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("pygamefiles\cesscore.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
 
def settings(Settings,messageSettings):

    textTitle = TITLE_FONT.render(Settings,1,colors.get("blue"))
    screen.fill(colors.get("white"))
    xd = WIDTH//2 - (textTitle.get_width()//2)
    screen.blit(textTitle,(xd,50))
    yMenu=150
    clslist=list(colors.keys())
    for item in messageSettings:
        colorRand=random.choice(clslist)
        if colorRand=="blue":
            colorRand=random.choice(clslist)
    
    Button_menu=pygame.Rect(Bx,yMenu,WIDTH//3,40)
    text=MENU_FONT.render(item,1, colors.get("blue"))
    pygame.draw.rect(screen,colors.get(colorRand),Button_menu)
    screen.blit(text,(Bx,yMenu))
    pygame.display.update()
    pygame.time.delay(50)
    yMenu+=50 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos
            mx = mousePos[0]
            my = mousePos[1]
            print(mx,my)
            if Button_color.collidepoint((mx,my)):
                print("y")
            if Button_size.collidepoint((mx,my)):
                WIDTH = 1500
                HEIGHT = 1500
                pygame.display.update()
            if Button_sound.collidepoint((mx,my)):
                print("c")

def Game_1():
    while run:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("you quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            # print(mousePos)
    keys = pygame.key.get_pressed() #allow us to see what key was pressed

    

    #square movement
    if keys[pygame.K_d] and square.x < WIDTH-wb:
        square.x += speed
        charx += speed
    if keys[pygame.K_a] and square.x > 0:
        square.x -= speed
        charx -= speed
    if keys[pygame.K_s] and square.y < HEIGHT-hb:
        square.y += speed
        chary += speed
    if keys[pygame.K_w] and square.y > 0:
        square.y -= speed
        chary -= speed

    #circle and inscribed square movement
    if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_LEFT] and cx > 0+rad:
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
        cy += speed
        insSquare.y += speed
    if keys[pygame.K_UP] and cy > 0+rad:
        cy -= speed
        insSquare.y -= speed
    
    #circle square collide
    if square.colliderect(insSquare): 
        print("BOOM")
        cx = random.randint(rad, WIDTH-rad)
        cy = random.randint(rad, HEIGHT-rad)
        rad += 5
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    
    #mountain collide square
    if square.colliderect(mountainSquare):
        square.x = 10
        square.y = 10
        charx = 10
        chary = 10
    
    #mountain collide circle
    if insSquare.colliderect(mountainSquare):
        cx = rad + 10
        cy = rad + 10
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)

    #rect(surface, color, object)
    pygame.draw.rect(screen, colors.get("blue"), square)
    pygame.draw.rect(screen, colors.get("blue"), insSquare)
    screen.blit(char, (charx, chary))

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
    
    pygame.display.update()
    pygame.time.delay(5)


                
  

    
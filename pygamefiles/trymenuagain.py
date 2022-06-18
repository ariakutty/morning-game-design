#aria kutty
#this is me trying the circle menu again


import sys
import pygame, time,os,random, math, datetime 
pygame.init()#initialize the pygame package
date=datetime.datetime.now() 
pygame.init() 
# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=800 #like constant
HEIGHT=800
colors={"white":(255,255,255),"pink":(244,194,194),"blue":(137, 207, 240),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0),  "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr=colors.get("limeGreen")
print(list(colors.values()))
backgroundcolor=random.choice(list(colors.values()))
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Color","Screen Size","sound on/off"]
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
clock=pygame.time.Clock()
#boxes for menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH//4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH//4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH//4, 40)
#images
bg=pygame.image.load('PygameFiles\images\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\images\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#mouse varuables
mx = 0
my = 0

def enterName():
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Get Name")
    screen.fill(backgroundcolor)
    run=True #to run the while loop
    user_name=''
    nameClr=(0,105,105) #for the text of the name
    boxClr= (200,200,200) #for the text box
    TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
    MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
    title=TITLE_FONT.render("Enter Name",1,boxClr)
    screen.blit(title,(200,50)) 
    input_rect = pygame.Rect((WIDTH//3, HEIGHT//3), (140, 40))

    #make box
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:  
                    print("hello, "+ user_name)
                    #run main menu
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_BACKSPACE:
                    user_name=user_name[:-1]
                else:
                    user_name+=event.unicode
            pygame.draw.rect(screen, boxClr, input_rect)
            
            text_surface = MENU_FONT.render(user_name, True, nameClr)
            #use your x,y
            screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

            pygame.display.flip()

def mainMenu():
    global yMenu 
    pygame.draw.rect(screen, colors.get('pink'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(backgroundcolor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(Bx, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('pink'), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50

    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print("You quit")
                pygame.display.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game1()
                if Button_Game2.collidepoint((mx, my)):
                    Game2()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
    
def Instructions():
 
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
  
    screen.fill(backgroundcolor)

    Button_1 = pygame.Rect(WIDTH//17, 629, WIDTH//3.5, 40) 
    pygame.draw.rect(screen, colors.get("blue"), Button_1)
  
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("white"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                pygame.display.quit()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 

def settings():
    global content, screen, WIDTH, HEIGHT 
    

    while True:
        global backgroundcolor
        title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
        text=MENU_FONT.render('Return to Menu', 1, colors.get('white'))
        textSizing=MENU_FONT.render('shrink screen size', 1, colors.get('white'))
        textColor=MENU_FONT.render('change colors', 1, colors.get('white'))
        textSizing2=MENU_FONT.render('expand screen size', 1, colors.get('white'))
        screen.fill(backgroundcolor)
        myFile = open("PygameFiles\settings.txt", "r")
        content = myFile.readlines()
        Button_2 = pygame.Rect(WIDTH//17, 629, WIDTH//3.5, 40) 
        pygame.draw.rect(screen, colors.get("blue"), Button_2)
        Button_3= pygame.Rect(Bx, 150, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("blue"), Button_3)
        Button_4= pygame.Rect(Bx, 200, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("blue"), Button_4)
        Button_5= pygame.Rect(Bx, 250, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("blue"), Button_5)
        screen.blit(title, (WIDTH//3,HEIGHT//10))
        screen.blit(text, (WIDTH//17, 629,))
        screen.blit(textSizing, (Bx, 150,))
        screen.blit(textColor, (Bx, 200))
        screen.blit(textSizing2,(Bx, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_2.collidepoint((mx, my)):
                    mainMenu()
                if Button_3.collidepoint((mx,my)):
                    WIDTH*=.5
                    HEIGHT*=.5
                    pygame.display.update()
                    screen=pygame.display.set_mode((int(WIDTH),int(HEIGHT)))
                if Button_4.collidepoint((mx,my)):
                    backgroundcolor=random.choice(list(colors.values()))
                if Button_5.collidepoint((mx,my)):
                    WIDTH*=2
                    HEIGHT*=2
                    pygame.display.update()
                    screen=pygame.display.set_mode((int(WIDTH),int(HEIGHT)))

        pygame.display.update()
                    
def scoreboard():
   screen.fill(backgroundcolor)
   myFile=open("pygamefiles/cesscore.txt", 'r')
   score_txt = myFile.readlines()
   for i in score_txt:
       txt = MENU_FONT.render(i, 1, colors.get('white'))
       screen.blit(txt, (0,0))
 
   text3 = MENU_FONT.render("Return to Menu", 1, colors.get("white"))
  
   xd = WIDTH//2 - (title.get_width()//2)
   Button_3 = pygame.Rect(WIDTH//17, 629, WIDTH//3.5, 40)
   pygame.draw.rect(screen, colors.get("blue"), Button_3)
  

   screen.blit(text3, (WIDTH//17, 629,))
   pygame.display.update()
 
   scoreboard=True
   while scoreboard:
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.display.quit()
               print("You quit")
           if event.type==pygame.MOUSEBUTTONDOWN:
               mousePos=pygame.mouse.get_pos()
               mx=mousePos[0]
               my=mousePos[1]
               if Button_3.collidepoint((mx, my)):
                   mainMenu()
 
   import os, datetime
   os.system('cls')
   name= ('player')
 
   date=datetime.datetime.now() #todays date and time
 
   screLine=str(score) + "\t"+name+"\t"+date.strftime("%m/%d/%Y")
 
   myFile=open("pygamefiles/cesscore.txt", 'a')
   myFile.write(screLine)
   myFile.close()

def exit():
    global title
    global Game
    title = TITLE_FONT.render("bye-bye!", 1, colors.get("blue"))
    screen.fill(backgroundcolor)
    screen.blit(title, (WIDTH/2.5, HEIGHT//2.5))
    pygame.display.update()
    Game= False         

def Game1():
    #square Var
    hb=50
    wb=50
    xb=100
    yb=300
    global score
    score=0 
    high=0

    charx = xb
    chary = yb

    cx=350
    cy=350
    rad=25
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)
    square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    squareClr=colors.get("pink")
    #keep running create a lp
    mountainSquare=pygame.Rect(250,320,180,250)
    circleClr=colors.get("blue")
    backgrnd=colors.get("limeGreen")
    run = True
    global mx
    global my
    run=True 
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            score +=1 
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)       
        #if square.colliderect(mountainSquare):
            #square.x=10
            #square.y=10
            #charx=10
            #chary=10
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)

        #pygame.draw.rect(screen, colors.get('white'), mountainSquare,)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainMenu()
        clock.tick(60)

def Game2():
    #square Var
    hb=50
    wb=50
    xb=100
    yb=300
    global score
    score=0 
    high=0

    charx = xb
    chary = yb

    cx=350
    cy=350
    rad=25
    speed=2
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)
    square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    squareClr=colors.get("limeGreen")
    #keep running create a lp
    mountainSquare=pygame.Rect(250,320,180,250)
    circleClr=colors.get("white")
    backgrnd=colors.get("limeGreen")
    run = True
    global mx
    global my
    run=True 
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            score +1 
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
            
        #if square.colliderect(mountainSquare):
            #square.x=10
            #square.y=10
            #charx=10
            #chary=10
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)

        #pygame.draw.rect(screen, colors.get('white'), mountainSquare,)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainMenu()

enterName()
mainMenu()
Instructions()

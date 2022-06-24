#aria kutty
#this is me trying the circle menu again
#i need help with getting the scoreboard to run
#i need help with getting my tic tac toe to not quit the game
#why does the yes i want to play again button not work in tic tac toe

import sys
import pygame, time,os,random, math, datetime 
from pygame.locals import*
pygame.init()#initialize the pygame package
date=datetime.datetime.now() 
pygame.init() 
# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(244,194,194),"green": (0,255,0) , "blue":(137, 207, 240),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0),  "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
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
    screen.blit(title,(WIDTH//2.8, HEIGHT//11)) 
    input_rect = pygame.Rect((WIDTH//2.5, HEIGHT//2.5), (140, 40))

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
                    mainMenu()
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
    Title = TITLE_FONT.render("Maze Game", 1, colors.get("blue"))
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
                # if Button_score.collidepoint((mx, my)):
                #     scoreboard()
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

def exit():
    global title
    global Game
    title = TITLE_FONT.render("bye-bye!", 1, colors.get("blue"))
    screen.fill(backgroundcolor)
    screen.blit(title, (WIDTH/2.5, HEIGHT//2.5))
    pygame.display.update()
    Game= False         

def Game1():
    #aria kutty
    #final game
    #maze
    pygame.init()#initialize the pygame package
    date=datetime.datetime.now() 
    pygame.init() 
    WIDTH=700 #like constant
    HEIGHT=700
    colors={"white":(255,255,255),"pink":(255,0,255), "green": (50,200,10) , "blue":(0,0,255), "limeGreen":(153,255,51)}
    #create dispay wind with any name y like
    screen=pygame.display.set_mode((WIDTH,HEIGHT))  

    #download images

    dog=pygame.image.load('pygamefiles\images\\dognobg.png')
    bg=pygame.image.load('pygamefiles\images\\background.png')
    dogbone=pygame.image.load('pygamefiles\images\\dogbonenobg.png')
    youwin=pygame.image.load('pygamefiles\images\\youwin.jpg')
    score=0
    #create all the walls 
    wall1= pygame.Rect(80, 120, 80, 20)
    wall2= pygame.Rect(0,50, 20, 700)
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
    dog=pygame.transform.scale(dog, (35,35))
    dogRect = dog.get_rect()
    dogbone=pygame.transform.scale(dogbone, (50, 40))
    boneRect = dogbone.get_rect()
    youwin=pygame.transform.scale(youwin, (700,700))
    #list for the walls so I don't need to collide point every single wall
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
        #draw the walls
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

        #make dog move
        keyPressed= pygame.key.get_pressed()
        speed= 3
        if keyPressed[K_LEFT]: 
            dogRect.x -= speed
        elif keyPressed[K_RIGHT]:
            dogRect.x+= speed
        elif keyPressed[K_UP]:
            dogRect.y -= speed
        elif keyPressed[K_DOWN]:
            dogRect.y += speed

        #when the dog hits the wall, it goes back to the start 
        for walls in wallList:
            if dogRect.colliderect(walls): 
                dogRect.x=30
                dogRect.y=0
        #when the dog hits the bone, it gets 5 points
        if dogRect.collidepoint(620,625):
            score+=10 
            print(score)
            screen.blit(youwin, (0,0))
            score_text = MENU_FONT.render('Your score is: ' + str(score), True, colors.get('pink'))
            screen.blit(score_text, (WIDTH//2-50, HEIGHT//2+100))
            pygame.display.update()
            pygame.time.delay(3000)
            mainMenu()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                mainMenu()

def Game2():
    #aria kutty
    #final game
    #maze
    pygame.init()#initialize the pygame package
    date=datetime.datetime.now() 
    pygame.init() 
    WIDTH=700 #like constant
    HEIGHT=700
    colors={"white":(255,255,255),"pink":(255,0,255), "green": (50,200,10) , "blue":(0,0,255), "limeGreen":(153,255,51)}
    #create dispay wind with any name y like
    screen=pygame.display.set_mode((WIDTH,HEIGHT))  

    dog=pygame.image.load('pygamefiles\images\\dognobg.png')
    bg=pygame.image.load('pygamefiles\images\\background.png')
    dogbone=pygame.image.load('pygamefiles\images\\dogbonenobg.png')
    youwin=pygame.image.load('pygamefiles\images\\youwin.jpg')
    coin1=pygame.image.load('pygamefiles\images\\goldcoin.png')
    slime=pygame.image.load('pygamefiles\images\\slimenobg.png')
    score=0


    wall1= pygame.Rect(80, 120, 80, 15)
    wall2= pygame.Rect(0,50, 15, 700)
    wall3= pygame.Rect(80, 0, 15, 120)
    wall4= pygame.Rect(0, 215, 200, 15)
    wall5= pygame.Rect(80, 120,200, 15)
    wall6= pygame.Rect(270, 120, 15, 200)
    wall7= pygame.Rect(180, 224, 15, 200)
    wall8= pygame.Rect(185, 404, 280, 15)
    wall9= pygame.Rect(368, 53, 15, 300)
    wall10= pygame.Rect(370, 333, 200, 15)
    wall11= pygame.Rect(88, 266, 15, 150)
    wall12= pygame.Rect(550, 345, 15, 184)
    wall13= pygame.Rect(351, 509, 200, 15)
    wall14= pygame.Rect(368, 54, 220, 15)
    wall15= pygame.Rect(350, 510, 15, 100)
    wall15= pygame.Rect(680, 54, 15, 560)
    wall16= pygame.Rect(447, 127, 240, 15)
    wall17= pygame.Rect(368, 200, 240, 15)
    wall18= pygame.Rect(447,267 , 240, 15)
    wall19= pygame.Rect(351, 405 , 15, 110)
    wall20= pygame.Rect(290, 594 , 435, 15)
    wall21= pygame.Rect(270, 514 , 15, 100)
    wall22= pygame.Rect(89, 508 , 201, 15)
    dog=pygame.transform.scale(dog, (35,35))
    dogRect = dog.get_rect()
    dogbone=pygame.transform.scale(dogbone, (50, 40))
    boneRect = dogbone.get_rect()
    coin=pygame.transform.scale(coin1, (40,30))
    coinRect = coin.get_rect()
    youwin=pygame.transform.scale(youwin, (700,700))
    slime=pygame.transform.scale(slime, (40, 40))
    

    wallList=[wall1, wall2, wall3, wall4,wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14,wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22]
    #will go under the main game 1 function
    #game two will have the same walls set up, but will have powerups throughout the middle
    while True:
        mousePos = pygame.mouse.get_pos()
        mx = mousePos[0]
        my = mousePos[1]
        Bx=WIDTH//3

        screen.blit(bg, (0, 0))

        screen.blit(coin, (136, 261))
        
        screen.blit(dog, dogRect)
        
        screen.blit(dogbone, (620, 625))

        screen.blit(slime, (404,453))

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

        # for walls in wallList:
        #     if dogRect.colliderect(walls): 
        #         dogRect.x=30
        #         dogRect.y=0

        if dogRect.collidepoint(620,625):
            score+=10 
            print(score)
            screen.blit(youwin, (0,0))
            score_text = MENU_FONT.render('Your score is: ' + str(score), True, colors.get('pink'))
            screen.blit(score_text, (WIDTH//2-50, HEIGHT//2+100))
            pygame.display.update()
            pygame.time.delay(3000)
            mainMenu()
        
        if dogRect.collidepoint(136, 261):
            dogRect.y+=15
            coin=pygame.transform.scale(coin1, (1,1))
            score+=5
            print(score)

        if dogRect.collidepoint(405, 455):
            dogRect.x+=15
            slime=pygame.transform.scale(slime, (1,1))
            score-=2
            print(score)
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                mainMenu()


def exit():
    global title
    global Game
    title = TITLE_FONT.render("bye-bye!", 1, colors.get("blue"))
    screen.fill(backgroundcolor)
    screen.blit(title, (WIDTH/2.5, HEIGHT//2.5))
    pygame.display.update()
    Game= False     
   
gameOver=False  #check if game is over
enterName()
mainMenu()
Instructions()
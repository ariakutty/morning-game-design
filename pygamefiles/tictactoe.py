#aria kutty
#tic tac toe game

#functions: 
#draw_grid(), 
#zero_grid()
#draw_markers
#check_winner()
#game_end
import sys
import pygame, time,os,random, math, datetime

pygame.init()
os.system('cls')
WIDTH=800 #like constant
HEIGHT=800
colors={"white":(255,255,255),"pink":(244,194,194),"blue":(137, 207, 240),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0),  "pink2":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
size=3
markers=[]
MxMy=(0,0)
linewidth=10
cellx=0
celly=0
player=1

circlecolor=colors.get("blue")
xcolor=colors.get("purple")
def zero_grid():
    for x in range(3):
        row=[0]*size #this will create lists
        markers.append(row)
        
# zero_grid()
# print(markers)
# markers[1][1]=-1 #first index is row second index is column
# print(markers)
# print(markers[1][1])
def draw_grid():
    global linecolor
    linecolor=colors.get("white")
    
    for x in range(1,3):
        pygame.draw.line(screen, linecolor,(0, HEIGHT//size*x),(HEIGHT, HEIGHT//size*x), linewidth)
        pygame.draw.line(screen, linecolor,(WIDTH//size*x,0),(WIDTH//size*x, HEIGHT), linewidth)
        pygame.display.update()
        pygame.time.delay(100)
draw_grid()
def draw_markers():
    xvalue=0
    for x in markers: #give me each row of list
        yvalue=0
        for y in x: #give each element
            if y==1:
                # draw x
                pygame.draw.line(screen, xcolor, (xvalue*WIDTH//size+15, yvalue*HEIGHT//size+15), (xvalue*WIDTH//size+WIDTH//size-15, yvalue*HEIGHT//size+HEIGHT//size-15), linewidth)
                pygame.draw.line(screen, xcolor, (xvalue*WIDTH//size+WIDTH//size-15, yvalue*HEIGHT//size+15), (xvalue*WIDTH//size+15, yvalue*HEIGHT//size+HEIGHT//size-15), linewidth)
            if y==-1:
                #draw o
                pygame.draw.circle(screen, circlecolor, (xvalue*WIDTH//size+WIDTH//(2*size)+5, yvalue*HEIGHT//size+HEIGHT//(2*size)+5), WIDTH//(2*size)-linewidth-10, linewidth)
            yvalue+=1
        xvalue+=1
    pygame.display.update()

def vert_0():
    pygame.draw.line(screen, linecolor, (WIDTH//(2*size), 15), (WIDTH//(2*size), HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def vert_1():
    pygame.draw.line(screen, linecolor, (WIDTH//2, 15), (WIDTH//2, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def vert_2():
    pygame.draw.line(screen, linecolor, ((2*size-1)*WIDTH//(2*size), 15), ((2*size-1)*WIDTH//(2*size), HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_0():
    pygame.draw.line(screen, linecolor, (15, HEIGHT//(2*size)), (WIDTH-15, HEIGHT//(2*size)), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_1():
    pygame.draw.line(screen, linecolor, (15, HEIGHT//2), (WIDTH-15, HEIGHT//2), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def hori_2():
    pygame.draw.line(screen, linecolor, (15, (2*size-1)*HEIGHT//(2*size)), (WIDTH-15, (2*size-1)*HEIGHT//(2*size)), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def diag_1():
    pygame.draw.line(screen, linecolor, (15, 15), (WIDTH-15, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)
def diag_2():
    pygame.draw.line(screen, linecolor, (WIDTH-15, 15), (15, HEIGHT-15), lineWidth)
    pygame.display.update()
    pygame.time.delay(1000)

def check_winner():
    global Game
    if markers[0][0] + markers[0][1] + markers[0][2] == 3:#vertical
        vert_0()
        x_win()
    elif markers[0][0] + markers[0][1] + markers[0][2] == -3:
        vert_0()
        O_win()
    elif markers[1][0] + markers[1][1] + markers[1][2] == 3:#vertical
        vert_1()
        x_win()
    elif markers[1][0] + markers[1][1] + markers[1][2] == -3:
        vert_1()
        O_win()
    elif markers[2][0] + markers[2][1] + markers[2][2] == 3:#vertical
        vert_2()
        x_win()
    elif markers[2][0] + markers[2][1] + markers[2][2] == -3:
        vert_2()
        O_win()
    elif markers[0][0] + markers[1][0] + markers[2][0] == 3:#horizontal
        hori_0()
        x_win()
    elif markers[0][0] + markers[1][0] + markers[2][0] == -3:
        hori_0()
        O_win()
    elif markers[0][1] + markers[1][1] + markers[2][1] == 3:#horizontal
        hori_1()
        x_win()
    elif markers[0][1] + markers[1][1] + markers[2][1] == -3:
        hori_1()
        O_win()
    elif markers[0][2] + markers[1][2] + markers[2][2] == 3:#horizontal
        hori_2()
        x_win()
    elif markers[0][2] + markers[1][2] + markers[2][2] == -3:
        hori_2()
        O_win()
    elif markers[0][0] + markers[1][1] + markers[2][2] == 3:#diagonal
        diag_1()
        x_win()
    elif markers[0][0] + markers[1][1] + markers[2][2] == -3:#diagonal
        diag_1()
        O_win()
    elif markers[2][0] + markers[1][1] + markers[0][2] == 3:#diagonal
        diag_2()
        x_win()
    elif markers[2][0] + markers[1][1] + markers[0][2] == -3:#diagonal
        diag_2()
        O_win()
    else:
        Game = True

zero_grid()
Game=True
while Game:
    screen.fill(bgcolor)
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit() 

            if event.type == pygame.MOUSEBUTTONDOWN:
                MxMy = pygame.mouse.get_pos()
                cellx=MxMy[0]//(WIDTH//size)
                celly=MxMy[1]//(HEIGHT//size)
                print(cellx, celly)
                print(markers)
                if markers[cellx][celly]==0:
                    markers[cellx][celly]=player 
                    player *=-1
    pygame.time.delay(50)
    pygame.display.update()


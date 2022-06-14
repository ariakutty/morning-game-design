#Aria Kutty
#Number guessing game


import random
import os, datetime
date=datetime.datetime.now()

os.system('cls')
        
Game=True
cnt=0
high=0
cscore=0
check=False
name=input("what is your name? ")
def Menu(choice):
    global check  
    if choice ==1:
        print("welcome to the instruction page," + name + "!")
        print("there are three levels to choose from")
        print("level 1 is guessing a number from 1-25")
        print("level 2 is guessing a number from 1-50")
        print("level 3 is guessing a number from 1-100")
        print("you have 5 guesses")
        print("good luck!")
        input("press enter to return to menu") 
        check=False
    global num
  
    if choice ==2:
        num = random.randint(1,25)+1
        check=True
    if choice ==3:
        num = random.randint(1,50)+1 
        check=True
    if choice ==4:
        num = random.randint(1,100)+1
        check=True
    if choice ==5:
        File=open("scre.txt",'r') 
        print()
        for line in File.readlines(): 
            print(line)
            File.close() 
        check=False
    if choice ==6:
        print("thanks for playing")
        input("press enter to play again") 
        with open("cscore.txt",'r+') as f:
            f.truncate(0)
        

high=0

while Game:
    print("welcome to the magic number guessing game!")
    print("you have six options to select from to start your journey in the magic number guessing game :)")
    print("1. instructions! ")
    print("2. level 1")
    print("3. level 2")
    print("4. level 3")
    print("5. check score")
    print("6. exit game")


    print(name, end=", ")
    choice= input("what option do you want to select? imput number here: ")
    choice=int(choice)
    choice = Menu(choice)
    
    while check and cnt <5:
        guess=input("please put your guess here: ")
        print() 
        guess=int(guess)
        if guess > num: 
            print("sorry, you guessed too high!")
            print()
        if guess < num:
            print("sorry, you guessed too low!")
            print()
        if guess == num:
            print("congrats, you got it")
            print("here is your trophy!")
            print(" |      |")
            print("[|      |]")
            print(" \      /")
            print("   \  /")
            print("    ||")
            print("    --")
            input("press enter when done")
            print()
            check=False
            cnt=0
        cnt+=1   
        if cnt ==5:
            print()
            print("sorry! that's the max guesses")            
    cscore=10000-cnt*100
    input("press enter")
    
File=open("cscores.txt",'a') 
File.write (str(cscore)) 
File.close()
with open("cscores.txt") as f:
    score=cscore 
    if score > high:
            high=score  
File.write(str(score)+"\t"+name+"\t"+ date.strftime("%m/%d/%Y"))
File.close() 

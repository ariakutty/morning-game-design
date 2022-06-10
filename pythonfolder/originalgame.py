#Aria Kutty
#Guess the singer

#start
#input: a title
#input: instructions
#input: 10 singers into list
#descision: computer picks a random singer
#process: give hint for the chosen singer
#input: take a guess
#descision: if guess is correct, tell user "congrats! you guessed the singer!"
#descision: if guess in incorrect, tell user "wrong! try again!"
#input: take another guess if needed
#descision: if new guess is correct, tell user "congrats! you guessed the singer!"
#descision: if new guess in incorrect, tell user "wrong! try again!"
#input: take another guess if needed
#descision: if new guess is correct, tell user "congrats! you guessed the singer!"
#descision: if new guess in incorrect, tell user "wrong! try again!"
#end




import random
import os 
os.system('cls')

for i in range (75): #this is for title screen
    print("*", end="")
print("     ")
print()
print("hello! welcome to guess the singer!")
print("rules:")
print("you will receive a hint about a singer.")
print("after this, you will have three guesses to figure out who it is!")
print("good luck!")
print("     ")

thislist= ["ariana grande", "taylor swift", "harry styles", "lorde", "dua lipa", "olivia rodrigo", "billie eilish", "ed sheeran", "katy perry", "doja cat" ]
word = random.choice(thislist) #this lets the computer choose the magic word

for i in range (75): 
    print("*", end="")
print()
print("  ")

if word == "ariana grande": #these are the hints dependeing on the selected singer
    print("hint! she used to be on nickelodeon")
if word== "taylor swift":
    print("hint! she is currently re-recording her masters")
if word== "harry styles":
    print("hint! he was in one direction")
if word== "lorde":
    print("hint! she has an album called melodrama")
if word== "dua lipa":
    print("hint! she is known for reviving 'disco pop'")
if word== "olivia rodrigo":
    print("hint! she starred in disney's 'high school musical: the musical: the series")
if word== "billie eilish":
    print("hint! she once had green hair")
if word== "ed sheeran":
    print("hint! he is a ginger")
if word== "katy perry":
    print("hint! she entered her superbowl halftime show on a massive lion")
if word== "doja cat":
    print("hint! she rose to fame during quarantine when her hit song blew up on tiktok")


guess = input("input a singer: ") #lets user take the first guess
if guess==word:
    print("congrats! you guessed the singer on your first try! here is your trophy!")    #winning screen with trophy
    print(" |      |")
    print("[|      |]")
    print(" \      /")
    print("   \  /")
    print("    ||")
    print("    --")
else:
    print("wrong. try again!")
    guess= input("input a singer: ") #lets user take another guess
    if guess==word:
        print("congrats, you guessed the singer!")
    else:
        print("wrong. try again!")
        guess= input("input a singer: ")  #lets user take their last guess
        if guess==word: 
            print("congrats! you guessed the singer!")
        else:
            print("sorry, you are out of guesses! better luck next time :(") #losing screen
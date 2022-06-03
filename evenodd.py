#Aria Kutty
#Write a code that finds an input number to be even or odd


import os
os .system('cls')

variable= input('enter a number') #let person choose number
variable=int(variable) #makes sure number is integer
num= (variable % 2) #mod, sets the outcome to a variable
print(num) #prints the 1 or 0
if num == 0: #if statement 
    print("you are even") #if the mod outcome is 0 the number has to be even
else:
    print("you are odd") #if the mod outcome is 1 the number has to be odd
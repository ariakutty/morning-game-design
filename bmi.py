#Aria Kutty
# How to Calculate someone's BMI

import os
os .system('cls')

weight= float(input("your weight in pounds")) #the number that the person enters their weight as in the terminal
a=weight*703
height= float(input("your height in inches: ")) #the number the person enters as their height in the terminal
b=height*height 
x=a/b 
print (x) #the BMI in terminal

if (x < 18.5):
    print ("you are underweight")

if (x > 25):
    print ("you are overweight")

if (x > 18.6 and x < 24.9): #how do you do greater than or equal to? like what happns if they are exactly 18.6
    print ("you are healthy")
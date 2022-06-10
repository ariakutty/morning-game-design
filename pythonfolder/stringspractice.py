#Aria Kutty
#we are going to learn about strings  ' ' or " "
import os
os.system('cls')
print('Hi')
print("hi, let's go to the park")
message=("you are awesome") #a string is an array. all arrays begin in 0
print(message)
print(message[5])
print(message[0:5]) #zero is included, five is not (wil print 4 characters)
if message.isdigit():  #since it is a method u have to use it w a dot
    sum=message +3
else:
    print(message+" I say so") #concatenation 
print(message.upper()) #changes it temporarily
print(message)
if message.isupper():
        print(message)
else:
    print("i am in false") #use only for debugging
    message=message.upper() #changes it permanently 
    print(message)
print(type(message))
print(dir(message))  #list of all methods in string

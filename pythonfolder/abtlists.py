#Aria Kutty
#We are going to learn about lists, functions to lists
#We are going to learn about for loop 
import random
import os 
os.system('cls')

thislist = ["apple", "banana", "cherry", "mango", "strawberry", "pineapple", "melon"]
print(thislist[1]) #second item
print(thislist[-1]) #very last item
print(thislist[-3]) #starts from the end and goes towards the start
print(thislist[1:4]) #print a range
print(thislist[:3]) #print everything up to index 3
print(thislist[-4:-1]) #print everything between not including -1
print(thislist[-4:])

if "apple" in thislist:
    print("yes, the apple is in the list")

for num in range(11): #prints number 0-11
    print(num)

for element in thislist: #element = thislist[times it runs through the loop]
    print(element)
print()

thislist.append("papaya")
print(thislist[0:])

#for num in range(1):
    #thislist.append(input("input a food"))
#print(thislist[0:]) 

thislist.insert(0, "tangerine")
print(thislist[0:])

for i in range(len(thislist)):
    print(thislist[i], end = " / ")
print()

list_num = [1, 2, 3, 4]
list_num.extend(thislist) #adds the two lists together
print(list_num)
list_num.append(thislist) #puts a list in a list
print(list_num)

word = random.choice(thislist)
print(word)

guess = input("input a food")
if guess.lower() in word.lower():
    print("congrats you guessed the food!")
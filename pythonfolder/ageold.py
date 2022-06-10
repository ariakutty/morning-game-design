#Aria Kutty
#Calculate Age
#Get user year and current year
import os
os.system ('cls')
by=2006 #assign this value as a number 
#by = input('year you were born, ') give us a string
by = int(input ('year you were born, ')) #typecast
currentYear=2022 #also number
age=currentYear-by
print('your age is', age)
#selection
if age >50:
    print('you are old')
#Aria Kutty
#String Worksheet 

import os
os.system('cls')

#Create a string made of the first, middle, and last character 
# Given str1= "James"; expected output Jms

message=("James")
print(message[0], end= "")
print(message[2], end= "")
print(message[4])

#Create a string made of the middle three characters 
# Given case 1 str1= "JhonDipPeta"; output Dip

message2=("JhonDipPeta")
print(message2[4:7])

# Given case 2 str2= "JaSonAy"; output Son

message3=("JaSonAy")
print(message3[2:5])

#Append new string in the middle of a given string
# given S1= Ault and s2= Kelly; output AuKellylt

message4=("Ault")
message5=("Kelly")
print(message4[0:2] + message5 + message4[2:4])

#Create a new string made of the first, middle, and last characters of each input string
# Given s1= "America" and s2= "Japan"; output AJrpan

message6=("America")
message7=("Japan")
print(message6[0] + message7[0] + message6[3] + message7[2] + message6[6] + message7[4])

#arrange string characters such that lowercase letters should come first
# Given s1= PyNaTive

message8=("PyNaTive")
print(message8[1] + message8[3] + message8[5:8] + message8[0] + message8[2] + message8[4])
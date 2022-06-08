#Aria Kutty
#Files
# r read
# w write
# a append
#
#open files make sure you close 

import os, datetime
os.system('cls')
name="aria"
score=120
date=datetime.datetime.now() #todays date and time
print(date.strftime("%m/%d/%Y"))
print(date.strftime("%Y/%m/%d?"))
screLine=str(score) + "\t"+name+"\t"+date.strftime("%m/%d/%Y")
print(screLine)
#to open a file we must create an object
myFile=open("scre.txt", 'w') #open a file to write. if you want to keep the stuff, use 'a'
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'a') #open a file to write. if you want to keep the stuff, use 'a'
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'r')# open a file to read
#lines=myFile.readline()
lines=myFile.readlines()
print(lines) 
for line in myFile.readlines: #if you say readline() singular, it prints everything on seperate lines
    print(line)
myFile.close()
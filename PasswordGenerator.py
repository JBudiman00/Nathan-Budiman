#Create a program that creates strong, random passwords

import random

def randGen(letterPref, length):
    #length
    if length == -1:
        length = random.randint(10, 20)

    pw = ""

    for x in range(length):
        c = random.randint(1,9)
        if c >= letterPref:
            a = random.randint(0,9)
            a = str(a)
        else:
            a = random.randint(97, 122)
            a = chr(a)
            a = str(a)
        pw+=a
    return pw


def main():
    print("Your password system has been updated; We can now handle prefernces toward random passwords")
    letterPref = input("On a scale of 1-10 (1 being all numbers, 10 being all letters), choose your lettertype prefernce.\n")
    letterPref = int(letterPref)
    lenChoice = input("Choose one of the following options: \n1. Set length for your password \n2. Random length (Between 10-20)\n")
        
    if lenChoice == "1":
        length = input("Enter a specific length between 8 and 20\n")
        while (True):
            length = int(length)
            if length > 7 and length < 21:
                break
            length = input("Requested length is either too long or too short, Enter a specific length between 8 and 20\n ")
    else:
        #-1 indicates that length will be random
        length = -1
    
    input("Press enter to generate a new random password")
    print(randGen(letterPref, length))
main()

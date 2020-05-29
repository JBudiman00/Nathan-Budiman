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

    #WIP
def keyWord(keyWordList, pw):     #Method that adds in keywords at random points within the random method
    count = 0
    holdB = 21
    holdE = -1

    while (True):   #Goes through each keyWord elment
        while (True):   #Ensures keyword is placed into password
            start = random.randint(1, len(pw))
            if start + len(keyWordList[count]) <= len(pw):      #Added words will start at position [start]
                for b in range(len(keyWordList[count])):
                    if start+b <= holdE and start+b >= holdB:
                        break
                else:
                    c = 0
                    element = keyWordList[count]
                    for x in range(start, start+len(keyWordList[count])):    #Range goes from Start (Inclusive) to start+len(keyWordList[count[]) (Exclusive)
                        pw = pw[:x] + element[c] + pw[x+1:]
                        c+=1
                    holdB = start
                    holdE = start+len(keyWordList[count])
                    break
        count += 1
        if count == len(keyWordList):
            break
    return pw



def chooseKeyWord(length):
    count = 0
    if length == -1:
        length = 20
    addWord = input("Would you like to add a key word to be included in your random password?\n1. Yes\n2. No\nKeep in mind adding a keyword may mess with your number/letter ratio preference\n")
    if addWord == "1":
        while (True):
            keyWordstr = input("Enter the words you would like to have included in your password, add a space between each word\nThe word limit is two\n")
            keyWordList = keyWordstr.split()
            for x in keyWordList:
                count += len(x)
            if count <= length:
                break
            print("Your chosen keywords are longer than the given password length, choose less keywords")
            count = 0
        return keyWordstr.split()
    return -1
        
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

    #keyWordList will be -1 if no keywords are chosen
    keyWordList = chooseKeyWord(length)

    input("Press enter to generate a new random password")
    pw = randGen(letterPref, length)

    #System adds keywords after generating random password
    if keyWordList != -1:
        pw = keyWord(keyWordList, pw)

    print(pw)
main()
